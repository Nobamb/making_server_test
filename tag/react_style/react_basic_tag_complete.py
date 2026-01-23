# react_style의 태그들 가져옴
from react_tag import react_tag
from react_open_tag import react_open_tag
from react_open_close_tag import react_open_close_tag

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
# head에 들어갈 값(기본값 "")
# body에 들어갈 값(기본값 "")
# title 지정(기본값 document)
def react_basic_tag_complete(title_value="document", head_value="", body_value=""):
    # 각각의 데이터들을 지정
    # doctype
    # react_open_tag
    # html 타입
    doctype = react_open_tag("!DOCTYPE","html")
    # <meta charset="UTF-8">
    # react_open_tag사용
    # 태그명 meta
    # 타입명 charset
    # 타입값 UTF-8
    meta_charset = react_open_tag("meta",charset="UTF-8")
    # <meta name="viewport" content="width=device-width, initial-scale=1.0">
    # react_open_tag사용
    # 태그명 meta
    # 타입명 name content
    # 타입값 viewport width=device-width, initial-scale=1.0
    meta_name_content = react_open_tag("meta",name = "viewport",content ="width=device-width, initial-scale=1.0")
    
    # title태그
    # react_open_close_tag
    # 태그명 title
    # 값은 title_value
    title = react_open_close_tag("title",title_value)
    
    # head 태그
    # react_open_close_tag
    # 태그명 head
    # 값은 meta_charset, meta_name_content, title, head_value
    head = react_open_close_tag("head",meta_charset, meta_name_content, title,head_value)
    
    
    
    # body 태그 
    # react_open_close_tag
    # 태그명 body
    # 값은 body_value
    body = react_open_close_tag("body",body_value)
    
    # html 태그
    # react_open_close_tag
    # 태그명 html
    # 속성 lang="ko"
    # 값은 head, body
    html = react_open_close_tag("html",head, body)
    
    # 태그들의 합
    result = doctype + html
    
    # 출력
    return result



# 테스트 
result = react_basic_tag_complete()
# 출력
print(result)