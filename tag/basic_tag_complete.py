# tag들 가져오기
from .tag import tag
from .open_tag import open_tag
from .open_close_tag import open_close_tag


# 기본적인 html 기본 구조 완성시켜줌
# 파라미터로 body 안에 넣을 새로운 태그들어가게 함
# title_name : head 태그의 title 이름 지정(기본값 "문서")
# add_head_tags : head 태그 내에 추가할 태그(배열)
# add_body_tags : body 태그 내에 추가할 태그(배열)


def basic_tag_complete(title_name="문서", add_head_tags=[], add_body_tags=[]):
    # 기본 형태
    #     <!DOCTYPE html>
    # <html lang="ko">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>Document</title>
    # </head>
    # <body>

    # </body>
    # </html>
    # DOCTYPE html 가져오기
    # open_tag
    # 태그명 !DOCTYPE
    # 속성명 html
    doctype = open_tag("!DOCTYPE", types=["html"])

    # body 태그
    # open_close_tag
    # children = add_body_tags
    body = open_close_tag("body", childrens=add_body_tags)

    # head 태그

    # meta charset
    # open_tag
    # 태그명 meta
    # 속성 charset
    # 속성값 UTF-8

    meta_charset = open_tag("meta", types=["charset"], values=["UTF-8"])

    # meta name content
    # open_tag
    # 태그명 meta
    # 속성 name content
    # 속성값 viewport width=device-width, initial-scale=1.0

    meta_name_content = open_tag(
        "meta",
        types=["name", "content"],
        values=["viewport", "width=device-width, initial-scale=1.0"],
    )

    # title
    # open_close_tag
    # 태그명 title
    # 기본 내용 "문서"

    title = open_close_tag("title", childrens=[title_name])

    # head 태그
    # open_close_tag
    # 태그명 head
    # childrens = meta_charset, meta_name_content, title
    head = open_close_tag(
        "head", childrens=[meta_charset, meta_name_content, title] + add_head_tags
    )

    # html 태그
    # open_close_tag
    # 태그명 html
    # 속성명 lang
    # 속성값 ko
    # childrens = head, body
    html = open_close_tag("html", types=["lang"], values=["ko"], childrens=[head, body])

    # 표시될 값(doctype + html)
    result = doctype + html
    # 출력
    return result


# 실행 테스트

# test = basic_tag_complete()

test = basic_tag_complete(
    title_name="테스트",
    add_body_tags=[
        open_close_tag("h1", childrens=["안녕"]),
        open_close_tag("p", childrens=["반가워"]),
    ],
)

# 출력
print(test)