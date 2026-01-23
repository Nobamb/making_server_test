# react_basic_tag_complete가 되는지 테스트
from tag.react_style.react_basic_tag_complete import react_basic_tag_complete

# 서버 가져오기
from http.server import BaseHTTPRequestHandler, HTTPServer

# 서버 구조 작성
# TestBasicServer
class TestBasicServer(BaseHTTPRequestHandler):
    # do_GET 메서드 생성
    def do_GET(self):
        # 200코드 전달
        self.send_response(200)
        # header 전달
        # content-type text/html
        self.send_header("content-type","text/html; charset = utf-8")
        # header 전달 완료
        self.end_headers()
        # react_basic_tag_complete 실행값 저장
        result = react_basic_tag_complete()
        # 값을 서버에 띄우도록 내용 전달
        self.wfile.write(result.encode("utf-8"))
        
        
        
        
# 포트 작성
port = 8000

# 서버 생성
server = HTTPServer(("",port),TestBasicServer)


# 서버 실행
server.serve_forever()