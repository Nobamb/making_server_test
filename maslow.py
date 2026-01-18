# 서버 생성
# http.server에서
# basehttp, httpserver 가져오기
from http.server import BaseHTTPRequestHandler, HTTPServer
# basic_tag_complete 함수 가져오기
from tag.basic_tag_complete import basic_tag_complete
# tag들 가져오기
from tag.open_tag import open_tag
from tag.open_close_tag import open_close_tag


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
        
        
        # h1 태그
        # open_close_tag
        # 내용 : 매슬로우의 욕구이론
        h1 = open_close_tag("h1",childrens=["매슬로우의 욕구 이론"])
        
        # p 태그
        # open_close_tag
        # 내용 : 매슬로우의 욕구이론 테스트
        p = open_close_tag("p",childrens=["매슬로우의 욕구이론 테스트"])
        
        
        # basic_tag_complete 함수 사용해보기
        # 제목 매슬로우
        result = basic_tag_complete(title_name="매슬로우", add_body_tags=[h1, p])
        
        # 서버에 출력
        # encode utf-8
        self.wfile.write(result.encode("utf-8"))
        
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