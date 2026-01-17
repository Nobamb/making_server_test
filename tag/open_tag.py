# open_tag 함수(여는 태그만. !DOCTYPE에서 사용)
# tag_name : 태그명
# types : 타입명들(배열)
# values : 타입값들(배열)

def open_tag(tag_name, types=[],values=[]):
    # 태그 시작
    result = f"<{tag_name}"
    
    # 클로저 함수
    # 속성 값들 더함
    def type_plus(types, values):
        # result 불러오기
        nonlocal result
        # types 순회하기(type_name으로)
        # 인덱스를 같이 가져옴
        for index, type_name in enumerate(types):
            # 만약에 values가 list면서 빈배열이 아니면
            if type(values) == list and values != []:
                # type_name에 values값(index)가져옴
                result += f" {type_name}={values[index]}"
            # values가 list면서 빈배열이면
            if type(values) == list and values == []:
                # type_name만 추가
                result += f" {type_name}"
                
        # result 마무리
        result += ">"
        
        # result 리턴
        return result
    
    # type_plus 실행
    type_plus(types, values)
    
    # result 리턴하기
    return result


# 테스트
doctype = open_tag("!DOCTYPE",["html"])
# 출력
print(doctype)