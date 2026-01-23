# react_style의 태그들 가져옴
from react_tag import react_tag
from react_open_tag import react_open_tag
from react_open_close_tag import react_open_close_tag

# data 가져오기
from data.maslow_basic_data import maslow_basic_data

# 기본 형식의 html 구조 생성
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
    
# </body>
# </html>

# 함수명 react_basic_tag_complete
# head에 들어갈 값
# body에 들어갈 값 지정
# title 지정
def react_basic_tag_complete(title_value, head, body):
    # maslow_basic_data의 값들 가져와서 for문 돌려보기
    for data in maslow_basic_data:
        # 어떤 타입의 태그를 사용할 지 결정
        # 초기값 none
        how_to_tag = None
        # 딕셔너리 형식의 데이터를 분해(key,value)
        for key, value in data.items():
            # 만약에 key가 tag_type일 때
            if key == "tag_type":
                # value가 tag면
                if value == "tag":
                    # react_tag 사용
                    pass
                # value가 open_tag면
                if value == "open_tag":
                    # react_open_tag 사용
                    pass
                # value가 open_close_tag면
                if value == "open_close_tag":
                    # react_open_tag 사용
                    pass
        