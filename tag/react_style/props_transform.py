# props_transform 함수
# props를 받을 배열 초기화 후
# props를 key, value로 분해(items화)
# key가 className일 때
# key를 class로 변경
# 분해한 key value 문자열화
# value가 빈 문자열일 때
# key만 전달하여 문자열화
# 문자열화한 값을 배열에 추가
# 배열에 추가 후 join을 통해 반환


# props_transform 함수 생성
def props_transform(props):
    # props를 담을 배열 초기화 선언
    props_arr = []
    # props를 분해
    # key, value를 나눔
    # items로 key, value를 가져오도록 함
    for key, value in props.items():
        # 만약에 key가 className이면
        if key == "className":
            # class로 변경
            key = "class"
        # 만약에 value가 빈문자열이면
        if value == "":
            # key만 전달
            key_value = f" {key}"
            # props_arr에 추가
            props_arr.append(key_value)
        # 빈문자가 아니라면
        else:
            # key, value 전달
            key_value = f" {key}={value}"
            # props_arr에 추가
            props_arr.append(key_value)
            
    # props를 join으로 묶음
    props_value = "".join(props_arr)

    # props_value 반환
    return props_value

# 테스트
props = {
    
    "class" : "hello",
    "type" : ""
}

props_value = props_transform(props)

print(props_value)