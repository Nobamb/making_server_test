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
        self.send_header("content-type","text/html; charset = utf-8")
        
        # 헤더 전달 종료
        self.end_headers()
        # 테스트
        print("서버 동작 성공")
        
        # html 전달
        
        
        
# 포트 번호 지정
# 8000번
port = 8000

# HTTPServer 클래스 생성
# ip 모두 허용 및 8000번대
# AssembleHtmlServer 클래스 받아옴
# serve_forever 실행시
# AssembleHtmlServer 클래스 내의 do_GET 메소드 사용 목적
server = HTTPServer(("",port),AssembleHtmlServer)

# serve_forever 메소드 실행
server.serve_forever()