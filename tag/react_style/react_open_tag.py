# props_transform 가져오기
from .props_transform import props_transform




# 리액트 스타일대로 커스텀 태그를 만들어보기
# 여는 태그만 지정
# 태그명, props를 받음
# props는 객체의 형태로 받도록
# key:value느낌의 데이터를 key = value의 형식으로 단순하게 표현
# props의 데이터들을 묶어서 딕셔너리 형식으로 만들기
# => **kwargs의 형태로 만들기(**props)
# props를 items()로 분해하여 key, value로 나누기
# f-string을 통해 문자열들 한번에 정리한 후 반환


# react_open_tag 지정
def react_open_tag(tag_name, **props):
    
    # props_transform 가져오기
    # props를 받음
    props_value = props_transform(props)    
    
    
    
    # # props를 받을 배열값 초기화
    # props_arr = []
    # # props의 key, value를 for문을 통해 순회
    # # items()를 사용하여 value까지 꺼내오기 편하게 지정
    # for key, value in props.items():
    #     # 만약에 key가 className이면
    #     # class로 변경
    #     if key == "className":
    #         key = "class"
    #     # 만약에 value의 값이 없으면
    #     if value == "":
    #         key_value = f" {key}"
    #     # value의 값이 존재한다면
    #     else:            
    #         # props_arr에 추가할 문자열 지정
    #         # key = value의 형태
    #         key_value = f' {key}="{value}"'
    #     # props_arr에 추가
    #     props_arr.append(key_value)
    # # 추가가 완료되면 join으로 묶기
    # props_value = "".join(props_arr)

    # tag_name, props_value를 통해 open_tag 작성
    # result의 형태로 지정
    result = f"<{tag_name}{props_value}>"
    # result 반환
    return result


# # 테스트
# div = react_open_tag("div",className = "hello")
# print(div)