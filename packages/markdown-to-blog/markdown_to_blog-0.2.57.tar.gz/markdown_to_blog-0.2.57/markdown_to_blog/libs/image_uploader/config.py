from dataclasses import dataclass
from .exceptions import ImageUploadError

@dataclass
class UploadConfig:
    """업로드 설정을 위한 데이터 클래스
    이 데이터 클래스는 이미지 업로드에 필요한 설정을 저장합니다.

    Attributes:
        max_retries (int): 최대 재시도 횟수
        timeout_connect (int): 연결 타임아웃 시간
        timeout_read (int): 읽기 타임아웃 시간
        min_file_size (int): 최소 파일 크기
        user_agent (str): 사용자 에이전트 문자열
        
    Raises:
        ImageUploadError: 설정 값이 유효하지 않을 경우
    """
    max_retries: int = 3
    timeout_connect: int = 30
    timeout_read: int = 60
    min_file_size: int = 100
    user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

    def __post_init__(self):
        """설정 값 유효성 검사"""
        if self.max_retries < 1:
            raise ImageUploadError("최대 재시도 횟수는 1 이상이어야 합니다.")
        if self.timeout_connect < 1:
            raise ImageUploadError("연결 타임아웃은 1초 이상이어야 합니다.")
        if self.timeout_read < 1:
            raise ImageUploadError("읽기 타임아웃은 1초 이상이어야 합니다.")
        if self.min_file_size < 1:
            raise ImageUploadError("최소 파일 크기는 1바이트 이상이어야 합니다.")
        if not self.user_agent:
            raise ImageUploadError("사용자 에이전트는 비어있을 수 없습니다.") 
