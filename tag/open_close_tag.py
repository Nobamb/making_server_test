# open_close_tag(열고 닫는 태그)
# open_tag 가져옴(여는 태그에서 사용)
from .open_tag import open_tag
# tag_name : 태그 이름
# types : 타입명(배열)
# values : 타입값(배열)
# childrens : 하위 내용(배열)
def open_close_tag(tag_name, types=[],values=[],childrens=[]):
    # open_tag 가져옴
    result = open_tag(tag_name, types, values)
    # 클로저 함수 children_plus
    # children 값을 더함
    def children_plus(childrens):
        # result 가져옴
        nonlocal result
        # chidlrens를 하나씩 가져옴
        for children in childrens:
            # result에 더함
            result += children
        
    
    # children_plus 실행
    children_plus(childrens)
    # result에 닫는 태그 추가
    result += f"</{tag_name}>"
    # result 리턴
    return result

# # 테스트
# # html
# # 태그명만
# html = open_close_tag("html")
# # div
# # 태그명과 속성과 속성값
# div = open_close_tag("div",types=["class"],values=["wid100"])
# # p
# # 태그명과 내용
# p = open_close_tag("p",childrens=["내용"])
# # span
# # 태그명과 속성과 속성값, 그리고 내용
# span = open_close_tag("span",types=["class"],values=["colorRed"],childrens=["span"])

# # 출력
# print(html)
# print(div)
# print(p)
# print(span)