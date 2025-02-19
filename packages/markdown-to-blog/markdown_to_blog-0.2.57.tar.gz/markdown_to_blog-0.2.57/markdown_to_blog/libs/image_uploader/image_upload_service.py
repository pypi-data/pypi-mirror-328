import os
import subprocess
from typing import Protocol, List, Optional
import random
from loguru import logger
from .utils import log_operation
from .url_handler import URLHandler
from .exceptions import ImageUploadError
import time

# 로깅 포맷 상수
LOG_FORMAT = {
    'SERVICE': 15,    # 서비스 이름 최대 길이
    'STATUS': 10,     # 상태 표시 최대 길이
    'ATTEMPT': 8,     # 시도 횟수 표시 최대 길이
    'PROGRESS': 10,   # 진행 상황 표시 최대 길이
    'MESSAGE': 50     # 메시지 최대 길이
}

def format_log_message(service: str, status: str, attempt: Optional[int] = None, 
                      progress: Optional[tuple[int, int]] = None, message: str = "") -> str:
    """로그 메시지를 일관된 형식으로 포맷팅
    
    Args:
        service: 서비스 이름
        status: 상태 (SUCCESS, FAIL, INFO 등)
        attempt: 시도 횟수 (선택적)
        progress: (현재 진행, 전체) 튜플 (선택적)
        message: 추가 메시지
    
    Returns:
        포맷팅된 로그 메시지
    """
    service_part = f"[{service:<{LOG_FORMAT['SERVICE']}s}]"
    status_part = f"[{status:<{LOG_FORMAT['STATUS']}s}]"
    attempt_part = f"[{f'{attempt}/{3}' if attempt is not None else 'N/A':<{LOG_FORMAT['ATTEMPT']}s}]"
    
    if progress:
        current, total = progress
        progress_part = f"[{current}/{total}]".ljust(LOG_FORMAT['PROGRESS'] + 2)
    else:
        progress_part = " " * (LOG_FORMAT['PROGRESS'] + 2)
    
    message_part = message[:LOG_FORMAT['MESSAGE']] + ('...' if len(message) > LOG_FORMAT['MESSAGE'] else '')
    
    return f"{service_part} {status_part} {attempt_part} {progress_part} {message_part}"

class ImageUploadService(Protocol):
    """이미지 업로드 서비스 인터페이스
    이 인터페이스는 이미지 업로드 기능을 정의합니다.
    """
    def upload(self, file_path: str) -> str:
        """이미지 업로드 구현
        
        Args:
            file_path (str): 업로드할 이미지 파일의 경로
            
        Returns:
            str: 업로드된 이미지의 URL
            
        Raises:
            ImageUploadError: 업로드 실패 시
        """
        pass

class DefaultImageUploader(ImageUploadService):
    """기본 이미지 업로드 구현
    이 클래스는 기본적인 이미지 업로드 기능을 제공합니다.
    """
    
    def __init__(self, service: Optional[str] = None):
        """DefaultImageUploader 클래스의 생성자
        
        Args:
            service (Optional[str]): 사용할 특정 업로드 서비스. None이면 랜덤 선택
        """
        self.service = service
        self.max_retries = 3
        self.retry_delay = 5
        self._used_services = set()
        self._progress_count = 0
        self._total_progress = 0

    def _reset_progress(self):
        """진행 상황 카운터 초기화"""
        self._progress_count = 0
        self._total_progress = 0

    @log_operation
    def upload(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise ImageUploadError(f"파일이 존재하지 않습니다: {file_path}")

        last_error = None
        self._used_services.clear()
        self._reset_progress()

        for attempt in range(self.max_retries):
            process = None
            try:
                service = self._select_next_service()
                logger.info(format_log_message(
                    service=service,
                    status="START",
                    attempt=attempt + 1,
                    message="업로드 시작"
                ))
                
                cmd = ["poetry", "run", "images-upload-cli", "-h", service, file_path]
                cmd_str = " ".join(cmd)
                
                process = subprocess.Popen(
                    cmd_str,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True,
                    text=True,
                    universal_newlines=True,
                    env=os.environ.copy(),
                )

                try:
                    result = self._handle_upload_process(process, service, attempt + 1)
                    logger.info(format_log_message(
                        service=service,
                        status="SUCCESS",
                        attempt=attempt + 1,
                        progress=(self._total_progress, self._total_progress),
                        message=f"업로드 완료: {result}"
                    ))
                    return result
                except ImageUploadError as e:
                    last_error = e
                    logger.warning(format_log_message(
                        service=service,
                        status="FAIL",
                        attempt=attempt + 1,
                        progress=(self._progress_count, self._total_progress),
                        message=str(e)
                    ))
                    if attempt < self.max_retries - 1:
                        wait_time = self.retry_delay * (attempt + 1)
                        logger.info(format_log_message(
                            service=service,
                            status="WAIT",
                            attempt=attempt + 1,
                            progress=(self._progress_count, self._total_progress),
                            message=f"{wait_time}초 후 재시도"
                        ))
                        time.sleep(wait_time)
                    continue

            except Exception as e:
                last_error = e
                logger.warning(format_log_message(
                    service=service,
                    status="ERROR",
                    attempt=attempt + 1,
                    progress=(self._progress_count, self._total_progress),
                    message=str(e)
                ))
                if attempt < self.max_retries - 1:
                    wait_time = self.retry_delay * (attempt + 1)
                    logger.info(format_log_message(
                        service=service,
                        status="WAIT",
                        attempt=attempt + 1,
                        progress=(self._progress_count, self._total_progress),
                        message=f"{wait_time}초 후 재시도"
                    ))
                    time.sleep(wait_time)
                continue
            finally:
                if process:
                    try:
                        process.kill()
                    except:
                        pass

        error_msg = f"모든 재시도 실패. 시도한 서비스: {', '.join(self._used_services)}"
        if last_error:
            error_msg += f"\n마지막 에러: {str(last_error)}"
        raise ImageUploadError(error_msg)

    def _select_next_service(self) -> str:
        """다음 업로드 서비스 선택
        
        이미 시도한 서비스를 제외하고 새로운 서비스를 선택합니다.
        모든 서비스를 시도했다면 다시 처음부터 시작합니다.
        
        Returns:
            str: 선택된 업로드 서비스
        """
        from .services import get_available_services
        available_services = get_available_services()
        
        if not available_services:
            raise ImageUploadError("사용 가능한 업로드 서비스가 없습니다")
            
        if self.service:
            if self.service not in available_services:
                raise ImageUploadError(f"지정된 서비스({self.service})는 사용할 수 없습니다")
            return self.service
            
        unused_services = [s for s in available_services if s not in self._used_services]
        if not unused_services:
            self._used_services.clear()
            unused_services = available_services
            
        selected_service = random.choice(unused_services)
        self._used_services.add(selected_service)
        return selected_service

    def _handle_upload_process(self, process: subprocess.Popen[str], service: str, attempt: int) -> str:
        stdout_lines = []
        stderr_lines = []
        max_wait_time = 300  # 5분 타임아웃
        start_time = time.time()

        try:
            while True:
                if time.time() - start_time > max_wait_time:
                    raise ImageUploadError("5분 타임아웃 초과")

                output = process.stdout.readline()
                error = process.stderr.readline()
                
                if error:
                    error_msg = error.strip()
                    stderr_lines.append(error_msg)
                    logger.warning(format_log_message(
                        service=service,
                        status="ERROR",
                        attempt=attempt,
                        progress=(self._progress_count, self._total_progress),
                        message=error_msg
                    ))
                    
                if output:
                    line = output.strip()
                    stdout_lines.append(line)
                    
                    # 진행 상황 업데이트
                    if "Progress:" in line or "Uploading:" in line:
                        self._progress_count += 1
                        if self._total_progress == 0:
                            # 첫 번째 진행 상황 메시지에서 전체 크기 추정
                            self._total_progress = 100
                    
                    logger.info(format_log_message(
                        service=service,
                        status="PROGRESS",
                        attempt=attempt,
                        progress=(self._progress_count, self._total_progress),
                        message=line
                    ))
                
                if output == "" and error == "" and process.poll() is not None:
                    break

            return_code = process.wait()
            
            if return_code != 0:
                error_msg = "\n".join(stderr_lines) if stderr_lines else "알 수 없는 오류"
                raise ImageUploadError(f"업로드 실패 (코드 {return_code}): {error_msg}")

            if not stdout_lines:
                raise ImageUploadError("업로드는 성공했으나 URL을 받지 못했습니다")

            try:
                url = stdout_lines[-1]
                return URLHandler.normalize_url(url)
            except Exception as e:
                raise ImageUploadError(f"잘못된 URL 형식: {str(e)}")
                
        finally:
            try:
                process.kill()
            except:
                pass 