# pathlib 가져옴
# 현재 파일 기준 최상위 경로 지정 목적
from pathlib import Path

# sys 가져옴
# 시스템에 경로 추가 목적
import sys

# 현재 경로를 기준으로 절대 경로 지정후 최상위경로를 불러옴
get_path = Path(__file__).resolve().parent.parent.parent

# get_path를 시스템에 추가(문자열화)
sys.path.append(str(get_path))



# basic_data를 가져옴
from data.basic_data import basic_data


# ReactTag를 기반으로
# 기본 구조를 작성
def react_basic_tag_complete():
    pass