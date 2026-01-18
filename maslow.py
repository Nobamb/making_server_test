# 서버 생성
# http.server에서
# basehttp, httpserver 가져오기
from http.server import BaseHTTPRequestHandler, HTTPServer


# basehttp 클래스 오버라이드
# maslow_server
class MaslowServer(BaseHTTPRequestHandler):
    # get메소드 받음
    def do_GET(self):
        # 응답코드 출력 200
        self.send_response(200)
        
        # 응답 헤더 전송
        # content-type
        # text/html; charset = utf-8
        self.send_header("content-type","text/html; charset = utf-8")
        
        # 헤더 전송 종료
        self.end_headers()
        
        # 연결 테스트
        print("서버 접속 성공")


# 포트번호 8000
port = 8000

        
# httpserver 생성
# "" : 아이피 모두 허용
# port : 8000번의 포트번호 지정
# MaslowServer : MaslowServer의 do_GET 메소드 사용(serve_forever()사용시)
server = HTTPServer(("",port),MaslowServer)

# 서버 실행
server.serve_forever()