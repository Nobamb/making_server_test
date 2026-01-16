# server가져오기(baseHTTPRequestHandler, HTTPServer)

from http.server import BaseHTTPRequestHandler, HTTPServer

# 서버 생성
# BaseHTTPRequestHandler 오버라이드
# GetServerRequestResponse

class GetServerRequestResponse(BaseHTTPRequestHandler):
    # GET요청을 받았을 때의 메소드
    # do_GET 메소드
    def do_GET(self):
        # 응답코드 전송
        # 200 코드
        self.send_response(200)
        # header를 전송
        # content-type
        # text/html; charset = utf-8
        self.send_header("content-type", "text/html; charset = utf-8")
        # header 종료
        self.end_headers()
        
        # 요청 받아오기
        print(self.request)
        # 응답 받아오기
        print(self.responses)
        # 서버 실행 완료 출력
        print("서버 실행 완료")
        
        
