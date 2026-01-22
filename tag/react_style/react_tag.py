# 리액트 스타일대로 커스텀 태그를 만들어보기
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

def react_tag(tag_name, *children, **props):
    # props 키와 키값을 받을 배열 초기화
    props_arr = []
    
    # props 딕셔너리를 분해
    # items메소드를 통해 value까지 나타내기
    for key, value in props.items():
        # key, value를 문자열로 묶어서 표현
        key_value = f" {key}={value}"
        # key_value를 props_arr에 담음
        # append 방식으로 담아보기
        props_arr.append(key_value)
    
    # props_arr 다 담았다면 join을 통해 묶음
    props_value = "".join(props_arr)
    # children도 다 담았다면 join을 통해 묶음
    # 기본 값들끼리 묶기
    children_value = "".join(children)
    
    # 한번에 묶기(f-string)
    # result
    result = f"<{tag_name}{props_value}>{children_value}</{tag_name}>"
    
    # result 반환
    return result