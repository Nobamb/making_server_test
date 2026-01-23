# data_component_change 함수 가져오기
from tag.react_style.data_component_change import data_component_change
# maslow_data 가져오기
from data.maslow_data import maslow_data


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
                
        
        # maslow_data로 변환한 태그 데이터 배열 받기
        maslow_data_to_html_arr = []
        
        
        # maslow_data 가져오기
        for data in maslow_data:
            # data_component_change를 변환한 값 추가
            # data를 파라미터값으로 줌
            maslow_data_to_html = data_component_change(data)
            # maslow_data_to_html_arr에 추가
            maslow_data_to_html_arr.append(maslow_data_to_html)
            
        # maslow_data_to_html_arr의 배열 값들을 join
        # \n으로 값들을 묶음
        # body_result로 저장
        body_result = "\n".join(maslow_data_to_html_arr)
        
        # react_basic_tag_complete 실행값 저장
        result = react_basic_tag_complete(body_value=body_result)
        # 값을 서버에 띄우도록 내용 전달
        self.wfile.write(result.encode("utf-8"))
        
        
        
        
# 포트 작성
port = 8000

# 서버 생성
server = HTTPServer(("",port),TestBasicServer)


# 서버 실행
server.serve_forever()