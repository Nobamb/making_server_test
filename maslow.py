# 서버 생성
# http.server에서
# basehttp, httpserver 가져오기
from http.server import BaseHTTPRequestHandler, HTTPServer

# basic_tag_complete 함수 가져오기
from tag.basic_tag_complete import basic_tag_complete

# react_basic_tag_complete 함수 가져오기
from tag.react_style.react_basic_tag_complete import react_basic_tag_complete


# maslow_data 가져오기
from data.maslow_data import maslow_data
# head_data 가져오기
from data.head_data import head_data

# maslow_data의 각 데이터를 태그로 변환하기
from tag.react_style.data_component_change import data_component_change


# react_style의 tag들 가져오기
from tag.react_style.react_tag import react_tag
from tag.react_style.react_open_tag import react_open_tag
from tag.react_style.react_open_close_tag import react_open_close_tag


# basehttp 클래스 오버라이드
# maslow_server
class MaslowServer(BaseHTTPRequestHandler):
    # post 메소드 받음
    # 테스트
    def do_POST(self):
        # 200 코드 전달
        self.send_response(200)
        # 전송할 header 지정
        # content-type
        # text/html
        self.send_header("content-type", "text/html; charset=utf-8")
        # header 전송 완료
        self.end_headers()

        # 전송 완료 테스트
        # 내가 직접 작성한 react_style의 태그 함수들 가져오기

        # p
        # react_open_close_tag
        # 내용 : POST 요청에 성공했습니다.
        p = react_open_close_tag("p", "POST 요청에 성공했습니다.")

        # h1
        # react_open_close_tag
        # 내용 : 전송 성공
        h1 = react_open_close_tag("h1", "전송 성공")

        # body
        # h1 받음
        # p 받음
        # react_open_close_tag
        body = react_open_close_tag("body", h1, p)

        # meta name viewport content width=device-width, initial-scale=1.0
        # react_open_tag
        meta_name_viewport = react_open_tag(
            "meta", name="content", viewport="width=device-width, initial-scale=1.0"
        )

        # meta charset UTF-8
        # react_open_tag
        meta_charset = react_open_tag("meta", charset="UTF-8")

        # title 문서
        # react_open_close_tag
        title = react_open_close_tag("title", "문서")

        # head
        # meta charset UTF-8
        # meta name viewport content width=device-width, initial-scale=1.0
        # title 문서
        # react_open_close_tag
        head = react_open_close_tag("head", meta_charset, meta_name_viewport, title)

        # html
        # head, body를 받음
        # lang타입 ko
        # react_open_close_tag
        html = react_open_close_tag("html", head, body, lang="ko")

        # DOCTYPE
        # html 타입(값 x)
        # react_open_tag
        doctype = react_open_tag("!DOCTYPE", html="")

        # result
        # doctype + html
        result = doctype + html
        # result 작성(encode(utf-8))
        self.wfile.write(result.encode("utf-8"))

    # get메소드 받음
    def do_GET(self):
        # 만약에 메인 경로일때(""또는 "/")
        if self.path == "" or self.path == "/":

            # 응답코드 출력 200
            self.send_response(200)

            # 응답 헤더 전송
            # content-type
            # text/html; charset = utf-8
            self.send_header("content-type", "text/html; charset = utf-8")

            # 헤더 전송 종료
            self.end_headers()

            # 배열 초기화(body에 들어갈 내용)
            maslow_data_html_body_arr = []

            # 배열 초기화(head에 들어갈 내용)
            maslow_data_html_head_arr = []

            # maslow_data의 각 배열을 순회
            for data in maslow_data:
                # 각 data를 data_component_change로 변환
                maslow_data_html_body = data_component_change(data)
                # maslow_data_html_body을 maslow_data_html_body_arr에 추가
                maslow_data_html_body_arr.append(maslow_data_html_body)

            # head_data의 각 배열을 순회
            for data in head_data:
                # 각 data를 data_component_change로 변환
                maslow_data_html_head = data_component_change(data)
                # maslow_data_html_head를  maslow_data_html_head_arr에 추가
                maslow_data_html_head_arr.append(maslow_data_html_head)

            # maslow_data_html_body_arr에 있는 값들을
            # join을 통해 묶어놓기
            body_result = "\n".join(maslow_data_html_body_arr)

            # maslow_data_html_head_arr에 있는 값들을
            # join을 통해 묶어놓기
            head_result = "\n".join(maslow_data_html_head_arr)


            # 값을 가져옴
            # react_basic_tag_complete 사용
            result = react_basic_tag_complete(
                title_value="매슬로우", body_value=body_result,
                head_value=head_result
            )

            # 서버에 출력
            # encode utf-8
            self.wfile.write(result.encode("utf-8"))

            # 연결 테스트
            print("서버 접속 성공")

        # 만약에 경로가 /style.css일 때
        # 브라우저에서 style.css를 인식하였을 때
        elif self.path == "/style.css":
            # style.css 읽어오기
            with open("style.css", "r", encoding="utf-8") as f:
                # 읽어온 값을 저장
                style_css = f.read()

            # 응답코드 전달(200)
            self.send_response(200)
            # header 전달
            # content-type text/css(css 내용을 가져와야하기에); charset = utf-8
            self.send_header("content-type", "text/css; charset = utf-8")
            # header 종료
            self.end_headers()
            # 읽어온 css 값 전달
            # encode utf-8 적용
            self.wfile.write(style_css.encode("utf-8"))

        # 만약에 경로가 /main.js일 때
        # 브라우저에서 main.js를 인식하였을 때
        elif self.path == "/main.js":
            # 200코드 전달
            self.send_response(200)
            # header 전달
            # content-type text/javascript; charset = utf-8
            self.send_header("content-type", "text/javascript; charset = utf-8")
            # header 종료
            self.end_headers()
            # 파일 읽기(main.js 내용에 대한 읽기)
            with open("main.js", "r", encoding="utf-8") as f:
                js_content = f.read()

            # js_content에 대해 값을 쓰기
            # encode utf-8
            self.wfile.write(js_content.encode("utf-8"))

        # 그 외의 경로라면
        else:
            # 에러 발생
            self.send_error(404)
            # 경로를 찾을 수 없다며 print
            print("경로를 찾을 수 없습니다.", self.path)


# 포트번호 8000
port = 8000


# httpserver 생성
# "" : 아이피 모두 허용
# port : 8000번의 포트번호 지정
# MaslowServer : MaslowServer의 do_GET 메소드 사용(serve_forever()사용시)
server = HTTPServer(("", port), MaslowServer)

# 서버 실행
server.serve_forever()
