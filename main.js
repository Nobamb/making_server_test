// 테스트
console.log("서버와 자바스크립트와 연결 성공")

// body의 4번째 요소에 접근시(div)
// ul의 특정 순서의 li에 접근을 하였다면
// (1,2번째 ul 다 상관없음)
// (1번째만 하면 2번째 등장하자마자 off될수있기에)
// 두번째 ul의 class를 on으로 변경
// on으로 변경하면서 콜백함수를 통해 바로 opacity를 0에서 1로 변경


// body를 먼저 가져옴
const body = document.body

// body에 마우스를 올렸을 때
body.addEventListener("mouseenter",()=> {
    // 알람이 뜨도록 함
    alert("body 동작 테스트 성공")

})

