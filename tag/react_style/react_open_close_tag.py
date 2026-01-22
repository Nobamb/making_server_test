# react_open_tag가져오기
from react_open_tag import react_open_tag

# 리액트 스타일대로 커스텀 태그를 만들어보기
# (열고 닫으면서 children 추가)
# 태그명, children, props를 받음
# children은 튜플의 형태로 받도록
# 단일 데이터를 children으로 받아서 내부에서 합치기
# => *args의 형태로 만들기(*children)
# props는 객체의 형태로 받도록
# key:value느낌의 데이터를 key = value의 형식으로 단순하게 표현
# props의 데이터들을 묶어서 딕셔너리 형식으로 만들기
# => **kwargs의 형태로 만들기(**props)
# props를 items()로 분해하여 key, value로 나누기
# children은 join을 통해 묶기
# f-string을 통해 문자열들 한번에 정리한 후 반환
# react_open_tag를 가져와서 사용


def react_open_close_tag(tag_name, *children, **props):
    # react_open_tag 가져오기
    # children, props 가져오기
    open_tag = react_open_tag(tag_name,props)
    # children을 따로 join메서드를 통해 한 문자열로 묶기
    # \n을 통해 문자열을 들여쓰기로 나눔
    children_value = "\n".join(children)
    
    # children_value를 open_tag와 합쳐서 문자열의 형태로 만들기
    result = f"{open_tag}{children_value}</{open_tag}>"
    
    # result 반환
    return result