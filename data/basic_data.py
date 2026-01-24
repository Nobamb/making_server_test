# 각 요소는 딕셔너리 형태,
# 요소를 배열 단위로 받음
# tag_name, tag_type, children(배열 또는 문자열), props(딕셔너리)
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

basic_data = [
    # doctype
    # 타입 : html
    {
        "tag_name": "!DOCTYPE",
        "tag_type": "open_close_tag",
        "children": "",
        "props": {"html": ""},
    },
    # html
    # 타입 lang
    # 타입값 ko
    {
        "tag_name": "html",
        "tag_type": "open_tag",
        "children": [
            # head
            {
                "tag_name": "head",
                "tag_type": "open_close_tag",
                "children": [
                    # meta
                    # 타입 name
                    # 타입값 charset
                    # 타입 UTF-8
                    {
                        "tag_name": "meta",
                        "tag_type": "open_tag",
                        "children": [],
                        "props": {
                            "charset":"UTF-8"
                        },
                    },
                    # meta
                    {
                        "tag_name": "meta",
                        "tag_type": "open_tag",
                        "children": [],
                        "props": {
                            "name": "viewport",
                            "content": "width=device-width, initial-scale=1.0",
                        },
                    },
                    # title
                    # 기본값 : document
                    {
                        "tag_name": "title",
                        "tag_type": "open_close_tag",
                        "children": "document",
                        "props": {},
                    },
                ],
                "props": {},
            }
            # body
            ,
            {
                "tag_name": "body",
                "tag_type": "open_close_tag",
                "children": "",
                "props": {},
            },
        ],
        "props": {"lang": "ko"},
    },
]
