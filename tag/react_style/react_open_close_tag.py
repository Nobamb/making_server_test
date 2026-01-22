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
# react_open_tag를 가져와서 사용하려 했으나
# react_open_close_tag에서 props를 딕셔너리로 변환한 채
# react_open_tag에 props에 넣는 문제 발생
# react_open_tag는 key="value" 형태를 받기에
# 별도로 만들어야겠음


def react_open_close_tag(tag_name, *children, **props):
    
    # props를 받을 배열(props_arr) 초기화
    props_arr = []
    
    # props의 key, value를 나눔
    # props를 items()의 형태로 변환하여
    # key와 value를 가져옴
    for key, value in props.items():
        # 만약에 key가 className일 때
        if key == "className":
            # class로 변경
            key = "class"
            
        # 만약에 value가 빈문자열이면
        # key만 전달하기
        if value == "":
            key_value = f" {key}"
        # 아니라면
        else:    
            # key,value를 한번에 문자열(f-string)로 묶은
            # key_value 지정
            key_value = f' {key}="{value}"'
        # props_arr에 추가
        props_arr.append(key_value)
    
    
    # props_arr를 따로 join 메서드를 통해 한 문자열로 묶기
    props_value = "".join(props_arr)
    
    # children을 따로 join메서드를 통해 한 문자열로 묶기
    # \n을 통해 문자열을 들여쓰기로 나눔
    children_value = "\n".join(children)
    
    # children_value를 open_tag와 합쳐서 문자열의 형태로 만들기
    result = f"<{tag_name}{props_value}>\n{children_value}\n</{tag_name}>"
    
    # result 반환
    return result

