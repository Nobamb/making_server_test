# 시스템(최상위 경로 추가 목적)
import sys
# 경로 가져오기
from pathlib import Path

# 최상위 경로 가져오기
# 절대 경로 지정 후(resolve())
# 현재 파일의 부모 : react_style => tag => making_server_test 순(3번 접근)
top_path = Path(__file__).resolve().parent.parent.parent

# 시스템에 top_path 추가
sys.path.append(str(top_path))

# data/maslow_data 데이터를 가져옴
from data.maslow_data import maslow_data



# data_component_change 함수 생성
def data_component_change():
    pass