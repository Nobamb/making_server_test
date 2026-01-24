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
# data_component_change를 가져옴
from tag.react_style_class.data_component_change import data_component_change




# ReactTag를 기반으로
# 기본 구조를 작성
def react_basic_tag_complete():
    
    # basic_data를 담을 배열 초기화
    basic_data_arr = []
    
    
    # basic_data를 순회
    for data in basic_data:
        # 각 데이터에 대해 data_component_change 실행
        # 실행한 값을 배열에 저장
        basic_data_arr_value = data_component_change(data)
        # 저장한 값을 basicc_data_arr에 추가
        basic_data_arr.append(basic_data_arr_value)
    
    # basic_data_arr를 문자열로 묶어서 result로 저장
    result = "".join(basic_data_arr)

    # 결과 반환
    return result
    
    
# 실행 테스트
print(react_basic_tag_complete())