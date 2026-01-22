# 리액트 스타일대로 커스텀 태그를 만들어보기
# (한번에 열고 닫는 태그)
# 태그명, children, props를 받음
# children은 튜플의 형태로 받도록
# 단일 데이터를 children으로 받아서 내부에서 합치기
# => *args의 형태로 만들기(*children)
# props는 객체의 형태로 받도록
# key:value느낌의 데이터를 key = value의 형식으로 단순하게 표현
# props의 데이터들을 묶어서 딕셔너리 형식으로 만들기
# => **kwargs의 형태로 만들기(**props)
# props를 items()로 분해하여 key, value로 나누기
# children은 join을 통해 묶기
# f-string을 통해 문자열들 한번에 정리한 후 반환
# react_open_tag를 가져와서 사용
