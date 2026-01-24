# pathlib 가져옴
# 현재 파일 기준 최상위 경로 지정 목적
from pathlib import Path

# sys 가져옴
# 시스템에 경로 추가 목적
import sys

# 현재 경로를 기준으로 절대 경로 지정후 최상위경로를 불러옴
get_path = Path(__file__).resolve().parent.parent.parent

print(get_path)

# get_path를 시스템에 추가(문자열화)
sys.path.append(str(get_path))

# basic_data를 가져옴
from data.basic_data import basic_data

# data_component_change를 가져옴
from tag.react_style_class.data_component_change import data_component_change


# 재귀함수
# 특정 값을 찾도록 도와줌
# data(객체)를 받고
def find_name_change_children(data, find_name, change_children):

    # 만약에 tag_name 값이 find_name와 동일하면
    if data["tag_name"] == find_name:
        
        # 해당 값의 children값을 변경   
        data["children"] = change_children
        # 종료
        return
    
    # key값중에 children이 배열이고 배열이 없는것이 아니라면 
    # children의 각 배열 값에 대해 재귀실행
    if isinstance(data["children"],list) and data["children"] != []:
        for child_data in data["children"]:
            find_name_change_children(child_data, find_name, change_children)
            
    # 못찾았으면 그대로 종료
    return


# ReactTag를 기반으로
# 기본 구조를 작성
# title 타이틀 값
# body 웹 브라우저에 보여줄 값
# head 추가할 head 설정값
def react_basic_tag_complete(title="document", head="", body=""):

    
    
    
    # 데이터를 변경
    # 객체 참조에 의한 호출은 원본 값이 그대로 바뀜
    find_name_change_children(basic_data[1], "title", title)
    
    

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
# title, body, head 넣어보기
print(react_basic_tag_complete(title="테스트"))
