# 클래스 기반으로 태그 생성
# 리액트의 느낌을 따라해보기
class ReactTag:
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

    # get_tag(한번에 열고 닫는 태그 만들어줌)
    def get_tag(self):

        # props를 담을 배열 초기화
        props_value_arr = []

        # props 객체를 가져옴
        # key, value를 동시에 가져옴
        # props는 item()으로 키와 키값 분해
        for key, value in self.__props.items():
            # value가 빈문자열일 때
            if key == "":
                # key 값을 문자열화
                props_value = f" {key}"
            # 빈 문자열이 아니면
            else:
                # key, value 값을 문자열화
                props_value = f" {key}={value}"
            # props_value_arr에 추가
            props_value_arr.append(props_value)

        # props_value_arr의 값들 묶기
        props_result = "".join(props_value_arr)

        # 열고 닫는 태그의 형태로 전달
        result = f"<{self.__tag_name}{props_result}/>"

        # result 반환
        return result

    # get_open_tag(열기만 하는 태그 만들어줌)
    def get_open_tag(self):

        # props를 담을 배열 초기화
        props_value_arr = []

        # props 객체를 가져옴
        # key, value를 동시에 가져옴
        # props는 item()으로 키와 키값 분해
        for key, value in self.__props.items():
            # value가 빈문자열일 때
            if key == "":
                # key 값을 문자열화
                props_value = f" {key}"
            # 빈 문자열이 아니면
            else:
                # key, value 값을 문자열화
                props_value = f" {key}={value}"
            # props_value_arr에 추가
            props_value_arr.append(props_value)

        # props_value_arr의 값들 묶기
        props_result = "".join(props_value_arr)

        # 열고 닫는 태그의 형태로 전달
        result = f"<{self.__tag_name}{props_result}>"
        # result 반환
        return result

    # get_open_tag(열고 닫으면서 children 추가하는 태그 만들어줌)
    def get_open_close_tag(self):
        # get_open_tag가져옴
        tag_open = self.get_open_tag(self)
        # 튜플 값 children join으로 묶기
        children_value = "".join(self.__children)
        # 닫는 태그 가져오기
        tag_close = f"</{self.__tag_name}>"
        # 값 모두 더하기
        result = tag_open + children_value + tag_close
        # result 반환
        return result



