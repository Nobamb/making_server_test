# 시스템(최상위 경로 추가 목적)
import sys
# 경로 가져오기
from pathlib import Path

# 최상위 경로 가져오기
# 절대 경로 지정 후(resolve())
# 현재 파일의 부모 : react_style
top_path = Path(__file__).resolve().parent.parent

# 시스템에 top_path 추가
sys.path.append(str(top_path))


# react_style 태그 가져오기
from react_style.react_tag import react_tag
from react_style.react_open_tag import react_open_tag
from react_style.react_open_close_tag import react_open_close_tag


def data_component_change(data):
    # data를 받게되면 
    # key에 따라 다른 데이터 형식으로 값을 가져옴
    # tag_name(단일 데이터)
    tag_name = data.get("tag_name")
    # tag_type(어떤 태그일지)
    tag_type = data.get("tag_type")
    # props(딕셔너리 데이터, 없으면 빈 딕셔너리 반환)
    # **kwarg를 통해 태그 함수에 값을 대입
    props = data.get("props",{})
    # children(배열 데이터, 없으면 빈 배열 반환)
    children = data.get("children",[])
    
    
    # children을 담을 배열
    # *args를 통해 값을 대입
    children_arr = []
    
    
    # 만약에 children이 배열이 아니라면
    if not isinstance(children, list):
        # children을 다시 배열화(children 순회해야 하기에)
        children = [children]
        
    # children을 순회
    for item in children:
        # 만약에 item이 딕셔너리이다(자식 태그가 있다는 뜻)
        if isinstance(item,dict):
            # 재귀 호출하면서
            child_item = data_component_change(item)
            # 배열에 추가(문자열화 하기, 숫자도 존재할 수 있기에)
            children_arr.append(str(child_item))
        # 딕셔너리가 아니라면
        else:
            # children_arr에 값 추가(문자열화 하기, 숫자도 존재할 수 있기에)
            children_arr.append(str(item))
            
    # tag_type의 값을 확인
    # 만약에 tag_type이 tag라면
    if tag_type == "tag":
        # result에 react_tag를 통해
        # tag_name, **props를 투입
        # 가변 인자 문법은 파라미터로써도 들어갈 수 있음
        result = react_tag(tag_name,**props)
    # 만약에 tag_type이 open_tag라면
    if tag_type == "open_tag":
        # result에 react_open_tag를 통해
        # tag_name, **props를 투입
        # 가변 인자 문법은 파라미터로써도 들어갈 수 있음
        result = react_open_tag(tag_name,**props)
    # 만약에 tag_type이 open_close_tag라면
    if tag_type == "open_close_tag":
        # result에 react_open_close_tag를 통해
        # tag_name, *children_arr,**props를 투입
        # 가변 인자 문법은 파라미터로써도 들어갈 수 있음
        result = react_open_close_tag(tag_name,*children_arr,**props)
        
    # result 반환
    return result