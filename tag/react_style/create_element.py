# 리액트 컴포넌트의 느낌으로 만들어보기
# 태그명, children(튜플(변경 불가한 배열) 형식), props(딕셔너리 형식)을 받음
# 각각의 형식은 *args(children), **kwargs(props)로 지정
# props를 받으면 " 키=값"의 형식으로 받음
# 만약에 key를 className을 받으면 
# className => class로 변형
# children을 join 문법을 통해 묶음
# f 스트링을 통해 tag_name, children, props값들을 모두 대입

# create_element 함수 생성
def create_element(tag_name, *children,**props):
    # 태그에 대한 props 문자열 초기값 지정
    tag_props = ""
    # props를 받아옴
    # key, value를 꺼내옴
    # value까지 꺼내오기 위해 items() 사용
    for key, value in props.items():
        # tag_props에 key, value 추가
        tag_props += f"{key}={value}"
        
    # children을 분해
    # ""을 기반으로
    children_value = "".join(children)
    
    
    # tag_name, tag_props, children_value를 통해
    # 하나의 태그 만들기
    result = f"<{tag_name} {tag_props}>{children_value}</{tag_name}>"
    
    # result 반환
    return result