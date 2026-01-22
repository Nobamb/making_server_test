# 리액트 스타일대로 커스텀 태그를 만들어보기
# (한번에 열고 닫는 태그)
# 태그명, children, props를 받음
# props는 객체의 형태로 받도록
# key:value느낌의 데이터를 key = value의 형식으로 단순하게 표현
# props의 데이터들을 묶어서 딕셔너리 형식으로 만들기
# => **kwargs의 형태로 만들기(**props)
# props를 items()로 분해하여 key, value로 나누기
# f-string을 통해 문자열들 한번에 정리한 후 반환

def react_tag(tag_name,**props):
    # props 키와 키값을 받을 배열 초기화
    props_arr = []
    
    # props 딕셔너리를 분해
    # items메소드를 통해 value까지 나타내기
    for key, value in props.items():
        
        # 만약에 key가 className이면
        # class로 변경
        if key == "className":
            key = "class"
        # value가 빈문자열이면
        if value == "":
            # key만 전달
            key_value = f" {key}" 
        # 아니라면
        else:
            # key, value를 문자열로 묶어서 표현
            key_value = f' {key}="{value}"'
        # key_value를 props_arr에 담음
        # append 방식으로 담아보기
        props_arr.append(key_value)
    
    # props_arr 다 담았다면 join을 통해 묶음
    props_value = "".join(props_arr)
    
    # 한번에 묶기(f-string)
    # result
    result = f"<{tag_name}{props_value}/>"
    
    # result 반환
    return result


# 테스트
div = react_tag("div",className = "")
# 출력
print(div)