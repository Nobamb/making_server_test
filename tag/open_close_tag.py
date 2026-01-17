# open_close_tag(열고 닫는 태그)
# open_tag 가져옴(여는 태그에서 사용)
from open_tag import open_tag
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
        
    
    # result에 닫는 태그 추가
    result += f"</{tag_name}>"
    # result 리턴
    return result

