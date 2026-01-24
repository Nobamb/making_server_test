# data를 파라미터로 받음
# 데이터를 받게 되면 ReactTag클래스로 넘기기
def data_component_change(data):
    # data를 받으면 data의 키값을 출력
    # 각각의 데이터 타입에 맞게 값을 받기
    # children은 배열
    # props는 딕셔너리
    # tag_type, tag_name은 단일 데이터
    tag_type = data.get("tag_type")
    tag_name = data.get("tag_name")
    children = data.get("children",[])
    props = data.get("props",{})
    
    
    # 만약에 children이 배열이 아니라면
    # 배열의 형식으로 변형
    if not isinstance(children, list):
        children = [children]
        
    # children의 값을 담을 배열 초기화
    children_arr = []
        
    # children을 순회
    for item in children:
        # 만약에 객체타입이면
        # 즉, 자식 태그가 존재하면
        if isinstance(item, dict):
            # 재귀 함수 실행
            child_data = data_component_change(item)
            # 배열에 추가
            children_arr.append(child_data)
        # 아니라면
        else:
            # 그대로 배열에 추가
            children_arr.append(item)
        
    # children_arr의 값들을 모두 묶음
    children_value = "".join(children_arr)