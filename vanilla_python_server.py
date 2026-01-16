# http 서버 가져오기

from http.server import BaseHTTPRequestHandler, HTTPServer

# 서버 구조 생성
# BaseHTTPRequestHandler 오버라이딩
class ServerTest(BaseHTTPRequestHandler):
    # do_GET 메소드 생성
    # 동적 디스패치 때문에 무조건 do_GET이어야 함
    def do_GET(self):
        # 생성자로부터
        # 응답코드 반환
        # 200 코드
        self.send_response(200)
        # 헤더 전송
        # content-type
        # text/html 형식이고, 
        # charset = utf-8
        self.send_header('content-type',"text/html; charset = utf-8")
        # 헤더 종료
        self.end_headers()
        # 서버가 실행되었다고 표시
        print("서버가 실행되었습니다.")
        

# 포트 번호 지정
# 8000 포트
port = 8000
        
        
# HttpServer 클래스를 통해 값을 받아 서버 설정
# 8000포트 실행(port), 어떤 ip에서건 볼 수 있도록("")
# => 첫번째 파라미터로 묶음(튜플)
# 튜플은 고정된 값을 묶기 위해
# ServerTest를 두번째 파라미터
# httpserver에서 forever_serve 메소드 실행 시
# ServerTest 클래스 내부에서 오버라이드한
# do_GET 메소드를 찾아서 사용하기 위해 ServerTest를 받음(동적 디스패치)
HTTPServer(("",port), ServerTest)

# forever_serve 메소드 실행
HTTPServer.serve_forever()