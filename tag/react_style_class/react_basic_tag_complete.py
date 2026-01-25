# copy를 가져옴(반복되는 객체 참조 접근이 이어지면 원본값이 훼손)
import copy

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
    if isinstance(data["children"], list) and data["children"] != []:
        for child_data in data["children"]:
            find_name_change_children(child_data, find_name, change_children)

    # 못찾았으면 그대로 종료
    return


# # 재귀함수
# # 값을 찾도록 도와줌
# # data(객체)를 받고
def find_name_plus_children(data, find_name, change_children):

    # 만약에 tag_name 값이 find_name와 동일하면
    if data["tag_name"] == find_name:

        # print(f"찾음, {find_name}")

        # children이 배열이면
        if isinstance(data["children"], list):
            # 해당 값의 children값을 배열 형태로 추가
            data["children"].extend(change_children)
        # 아니라면
        else:
            # 해당 값의 children값을 기본 데이터 형태로 추가
            data["children"] += change_children
        # 종료
        return

    # key값중에 children이 배열이고 배열이 없는것이 아니라면
    # children의 각 배열 값에 대해 재귀실행
    if isinstance(data["children"], list) and data["children"] != []:
        for child_data in data["children"]:
            find_name_plus_children(child_data, find_name, change_children)

    # 못찾았으면 그대로 종료
    return


# ReactTag를 기반으로
# 기본 구조를 작성
# title 타이틀 값
# body 웹 브라우저에 보여줄 값
# head 추가할 head 설정값
def react_basic_tag_complete(
    title="document",
    head=[],
    body="<h1>테스트</h1>",
):

    # 데이터 복사
    basic_copy_data = copy.deepcopy(basic_data)

    # basic 순회
    for data in basic_copy_data:
        # 데이터를 변경
        # 객체 참조에 의한 호출은 원본 값이 그대로 바뀜
        find_name_change_children(data, "title", title)
        find_name_change_children(data, "body", body)
        # 만약에 head가 list이면서 비어있지 않을 때
        if isinstance(head, list) and head != []:
            # head를 찾아서 값을 추가
            find_name_plus_children(data, "head", head)

    # basic_data를 담을 배열 초기화
    basic_data_arr = []

    # basic_data를 순회
    for data in basic_copy_data:
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

# test head
head = [
    {
        # <link rel="stylesheet" href="style.css">
        "tag_type": "open_tag",
        "tag_name": "link",
        "children": [],
        "props": {"rel": "stylesheet", "href": "style.css"},
    }
]

# title, body, head 넣어보기
print(react_basic_tag_complete(title="테스트", head=head, body="<p>1</p>"))
