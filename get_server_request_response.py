# server가져오기(baseHTTPRequestHandler, HTTPServer)

from http.server import BaseHTTPRequestHandler, HTTPServer

# 서버 생성
# BaseHTTPRequestHandler 오버라이드
# GetServerRequestResponse

class GetServerRequestResponse(BaseHTTPRequestHandler):
    # POST 메소드 테스트
    # do_POST 메소드
    # def do_POST(self):
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
        
        # # 요청 받아오기
        # print(f"서버 요청 {self.request}")
        # # 응답 받아오기
        # print(f"서버 응답 {self.responses}")
        
        # 메서드, 경로,헤더 출력
        # http 메서드 : command
        print(f"HTTP 메서드 {self.command}")
        # 경로 : path
        print(f"경로 {self.path}")
        # 헤더 : headers
        print(f"헤더 {self.headers}")
        
        
        # 서버 실행 완료 출력
        print("서버 실행 완료")
        
        
# 포트 지정 8000
port = 8000

# 서버 실행
# HTTPServer 생성자 생성
# ("",port) => 모든 ip를 받고 8000번 포트 받기
# GetServerRequestResponse 받아서
# serve_forever로 do_GET 메소드 실행

server = HTTPServer(("",port),GetServerRequestResponse)

# server에서 serve_forever 실행
server.serve_forever()
print("서버 종료전")
server.server_close()
print("서버 종료")
