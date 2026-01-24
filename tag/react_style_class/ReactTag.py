# 클래스 기반으로 태그 생성
# 리액트의 느낌을 따라해보기
class ReactTag():
    # 생성자
    # tag명
    # children
    # props
    def __init__(self, tag_name, *children, **props):
        # tag_name을 받음
        # 값 보호
        self.__tag_name = tag_name
        # children을 받음
        # 값 보호
        self.__children = children
        # props받음
        # 값 보호
        self.__props = props
    
    