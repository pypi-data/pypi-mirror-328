import codecs
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import cycle
from typing import Dict, List, Tuple
import os
import random
import time

from loguru import logger
from markdown2 import Markdown

from .image_uploader import ImageUploader, UploadConfig, get_available_services, ImageUploadError
from .md_converter.base import MarkdownConverter


def convert_markdown(converter: MarkdownConverter, text: str):
    return converter.convert(text)


def convert(input_fn, output_fn, is_temp=False):
    with codecs.open(input_fn, "r", "utf_8") as fp:
        markdowner = Markdown(extras=["highlightjs-lang", "fenced-code-blocks"])
        html = markdowner.convert(fp.read())
        with codecs.open(output_fn, "w", "utf_8") as fwp:
            fwp.write(html)


def read_first_header_from_md(file_path):
    """
    마크다운 파일로부터 첫 번째 헤더를 읽어 반환하는 함수.
    :param file_path: 마크다운 파일의 경로
    :return: 첫 번째 헤더 (문자열), 헤더가 없으면 None 반환
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # 마크다운 헤더는 '#'으로 시작함
            if line.startswith("#"):
                return line.strip()  # 헤더 반환 전 앞뒤 공백 제거
    return None  # 파일에 헤더가 없는 경우


def _extract_images_from_markdown(file_path: str) -> List[Tuple[int, str]]:
    """마크다운 파일에서 이미지 링크를 추출하는 함수
    
    Args:
        file_path (str): 마크다운 파일 경로
        
    Returns:
        List[Tuple[int, str]]: (라인 번호, 이미지 링크) 튜플의 리스트
        
    Raises:
        FileNotFoundError: 파일을 찾을 수 없는 경우
        IOError: 파일 읽기 오류 발생 시
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Markdown file not found: {file_path}")
        
    images = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for i, line in enumerate(file.readlines()):
                if line.startswith("![") and "]" in line:
                    try:
                        image_link = line.split("(")[1].split(")")[0].strip()
                        if image_link:  # 빈 링크 제외
                            images.append((i, image_link))
                    except IndexError:
                        logger.warning(f"잘못된 이미지 링크 형식 (라인 {i+1}): {line.strip()}")
    except IOError as e:
        logger.error(f"Error reading markdown file: {e}")
        raise
        
    return images


def _upload_image_with_retry(image_link: str, services: List[str], config: UploadConfig, max_retries: int = 3) -> Tuple[str, str]:
    """이미지를 여러 서비스로 재시도하며 업로드하는 함수
    
    Args:
        image_link (str): 업로드할 이미지 링크
        services (List[str]): 사용 가능한 서비스 목록
        config (UploadConfig): 업로드 설정
        max_retries (int): 최대 재시도 횟수
        
    Returns:
        Tuple[str, str]: (원본 링크, 업로드된 URL) 튜플
        
    Raises:
        ImageUploadError: 모든 서비스로 업로드 실패 시
    """
    if not services:
        raise ValueError("No available services provided")
        
    errors = []
    services_tried = set()
    retry_count = 0
    
    while retry_count < max_retries:
        # 아직 시도하지 않은 서비스 선택
        available_services = [s for s in services if s not in services_tried]
        if not available_services:
            # 모든 서비스를 시도했다면 다시 전체 서비스 사용
            services_tried.clear()
            available_services = services
            
        # 랜덤하게 서비스 선택
        service = random.choice(available_services)
        services_tried.add(service)
        
        try:
            uploader = ImageUploader(config=config, service=service)
            uploaded_url = uploader.upload(image_link)
            logger.info(f"Successfully uploaded image {image_link} to {uploaded_url} using {service}")
            return image_link, uploaded_url
        except Exception as e:
            error_msg = f"Failed to upload image using {service}: {str(e)}"
            logger.warning(error_msg)
            errors.append(error_msg)
            
            # 재시도 전 대기 시간 추가 (재시도 횟수에 따라 증가)
            retry_count += 1
            if retry_count < max_retries:
                wait_time = min(2 ** retry_count, 30)  # 최대 30초까지 대기
                logger.info(f"Waiting {wait_time} seconds before next retry...")
                time.sleep(wait_time)
            continue
            
    # 모든 재시도 실패
    error_summary = "\n".join(errors)
    raise ImageUploadError(
        f"Failed to upload image after {max_retries} retries with different services.\n"
        f"Services tried: {', '.join(services_tried)}\n"
        f"Errors:\n{error_summary}"
    )


def upload_markdown_images(file_path: str, service: str = None, max_retries: int = 3) -> bool:
    """
    마크다운 파일에 포함된 이미지들을 병렬로 업로드하고, 마크다운의 이미지 링크를 교체하는 함수.
    실패한 업로드는 다른 서비스로 재시도됩니다.
    
    Args:
        file_path (str): 마크다운 파일의 경로
        service (str, optional): 사용할 이미지 업로드 서비스. None이면 사용 가능한 서비스를 로테이션합니다.
        max_retries (int, optional): 이미지당 최대 재시도 횟수. 기본값은 3입니다.
        
    Returns:
        bool: 이미지 업로드 성공 여부
        
    Raises:
        FileNotFoundError: 마크다운 파일을 찾을 수 없는 경우
        IOError: 파일 읽기/쓰기 오류 발생 시
        ImageUploadError: 모든 서비스로 업로드 실패 시
        ValueError: 파일 경로가 비어있거나 사용 가능한 서비스가 없는 경우
    """
    if not file_path:
        raise ValueError("File path must not be empty")
        
    logger.info(f"Uploading images from markdown file: {file_path}")
    
    try:
        # 이미지 링크 추출
        images = _extract_images_from_markdown(file_path)
        if not images:
            logger.info("No images found in the markdown file")
            return True
        
        total_images = len(images)
        logger.info(f"Found {total_images} images to upload")
        
        # 서비스 목록 설정
        services = [service] if service else get_available_services()
        if not services:
            raise ValueError("No available upload services")
            
        logger.info(f"Available services: {', '.join(services)}")
        
        # 설정 초기화
        config = UploadConfig()
        
        # 이미지 병렬 업로드
        upload_results: Dict[str, str] = {}
        completed_uploads = 0
        failed_uploads = 0
        
        with ThreadPoolExecutor(max_workers=min(len(images), 5)) as executor:
            future_to_image = {
                executor.submit(_upload_image_with_retry, image_link, services, config, max_retries): image_link
                for _, image_link in images
            }
            
            for future in as_completed(future_to_image):
                try:
                    original_link, uploaded_url = future.result()
                    upload_results[original_link] = uploaded_url
                    completed_uploads += 1
                    logger.info(f"Progress: {completed_uploads}/{total_images} images uploaded")
                except Exception as e:
                    failed_uploads += 1
                    logger.error(f"Image upload failed after all retries: {e}")
                    continue
        
        # 업로드 결과 요약
        success_rate = (len(upload_results) / total_images) * 100
        logger.info(
            f"Upload summary: {len(upload_results)}/{total_images} images uploaded successfully "
            f"({success_rate:.1f}%), {failed_uploads} failed"
        )
        
        # 모든 업로드가 실패한 경우
        if not upload_results:
            logger.error("All image uploads failed")
            return False
        
        # 파일 내용 읽기 및 수정
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # 링크 교체
            replacements = 0
            backup_content = content  # 원본 내용 백업
            
            for original_link, uploaded_url in upload_results.items():
                new_content = content.replace(original_link, uploaded_url)
                if new_content != content:
                    replacements += 1
                    content = new_content
            
            # 변경사항이 있을 때만 파일 저장
            if replacements > 0:
                try:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(content)
                except Exception as e:
                    # 저장 실패 시 원본 내용 복구 시도
                    logger.error(f"Error saving changes, attempting to restore original content: {e}")
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(backup_content)
                    raise
            
            logger.info(f"Successfully replaced {replacements} image links in the markdown file")
            return True
            
        except IOError as e:
            logger.error(f"Error updating markdown file: {e}")
            raise
            
    except Exception as e:
        logger.error(f"Error processing markdown file: {e}")
        raise
