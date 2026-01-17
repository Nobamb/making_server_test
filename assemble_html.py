# 태그 관련 함수들 가져옴
from tag.tag import tag
from tag.open_tag import open_tag
from tag.open_close_tag import open_close_tag


# http.server에서 basehttp, httpserver import
from http.server import BaseHTTPRequestHandler, HTTPServer


# baseHTTPRequestHandler 오버라이딩
# AssembleHtmlServer 클래스 생성
class AssembleHtmlServer(BaseHTTPRequestHandler):
    # do_GET 메서드 재정의
    def do_GET(self):
        # 응답코드 200 전달
        self.send_response(200)
        # 헤더 전달
        # content-type
        # text/html; charset = utf-8
        self.send_header("content-type", "text/html; charset = utf-8")

        # 헤더 전달 종료
        self.end_headers()
        # 테스트
        print("서버 동작 성공")

        # DOCTYPE
        # open_tag
        # 속성 html
        doctype = open_tag("!DOCTYPE", types=["html"])

        # h1
        # open_close_tag
        # 내용은 제목
        h1 = open_close_tag("h1",childrens=["제목"])

        # p
        # open_close_tag
        # 내용은 내용
        p = open_close_tag("p",childrens=["내용"])

        # body
        # open_close_tag
        # children 받음
        body = open_close_tag("body",childrens=[h1, p])

        # meta데이터
        # open_tag
        # meta charset
        # 속성 charset
        # 속성값 UTF-8
        meta_charset = open_tag("meta", types=["charset"], values=["UTF-8"])
        # open_tag
        # meta name content
        # 속성 name content
        # 속성값 viewport width=device-width, initial-scale=1.0
        meta_name_content = open_tag("meta", types=["name","content"], values=["viewport", "width=device-width, initial-scale=1.0"])

        # open_close_Tag
        # title
        # 제목
        # 제목은 html 서버 조립 테스트
        title = open_close_tag("title",childrens=["html 서버 조립 테스트"])

        # head
        # open_close_tag
        # children받음
        # meta_charset, meta_name_content, title
        head = open_close_tag("head",childrens=[meta_charset, meta_name_content, title])

        # html 전달
        # open_close_tag
        # 속성 lang
        # 속성값 ko
        # children : head, body
        html = open_close_tag(
            "html", types=["lang"], values=["ko"], childrens=[head, body]
        )

        # 값을 더함
        result = doctype + html

        # 더한 값을 쓰도록 함(인코딩하여 utf-8로 변경)
        self.wfile.write(result.encode("utf-8"))


# 포트 번호 지정
# 8000번
port = 8000

# HTTPServer 클래스 생성
# ip 모두 허용 및 8000번대
# AssembleHtmlServer 클래스 받아옴
# serve_forever 실행시
# AssembleHtmlServer 클래스 내의 do_GET 메소드 사용 목적
server = HTTPServer(("", port), AssembleHtmlServer)

# serve_forever 메소드 실행
server.serve_forever()
