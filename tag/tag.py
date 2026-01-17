# 한번에 열고 닫는 태그
# tagname : 태그명
# types : 타입들(배열)
# values : 타입값들(배열)
def tag(tagname, types=[],values=[]):
    # 태그 시작
    # 태그명을 붙여줌
    result = f"<{tagname}"
    
    # 클로저 함수
    # 타입명을 추가
    def type_plus(types, values):
        # result 가져오기
        nonlocal result
        
        # types를 for 문을 통해 분해
        # index도 같이(해당하는 values의 인덱스값 추출)
        for index,type_name in enumerate(types):
            # 만약에 values가 배열이고, 빈 배열이 아닐 때
            if type(values) == list and values != []:
                # types에 비슷한 인덱스에 해당하는
                # 값들을 result에 지정
                result += f" {type_name} = {values[index]}"
            # 만약에 values가 배열이고, 빈 배열이면
            if type(values) == list and values == []:
                # type_name만 지정
                result += f" {type_name}"
                
        # 태그 닫기
        result += " />"
        
    
    # type_plus 함수 실행
    type_plus(types, values)
    
    # result 리턴
    return result



# # 테스트
# img = tag("img", ["src"], ["https://fastly.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U"])

# # 출력
# print(img)