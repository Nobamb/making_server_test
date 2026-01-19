// 테스트
console.log("서버와 자바스크립트와 연결 성공");

// body의 4번째 요소에 접근시(div)
// ul의 특정 순서의 li에 접근을 하였다면
// (1,2번째 ul 다 상관없음)
// (1번째만 하면 2번째 등장하자마자 off될수있기에)
// 두번째 ul의 class를 on으로 변경
// on으로 변경하면서 콜백함수를 통해 바로
// 특정 li의 opacity를 0에서 1로 변경
// opacity0 => opacity100

// body를 먼저 가져옴
const body = document.body;

// body에서 div를 찾음
// div_in_ul(ul들이 존재하는 div)
const divInUl = body.children[3];

// ul_triangle
const ulTriangle = divInUl.children[0];

// ul_text
const ulText = divInUl.children[1];

// triangle 내부의 li의 인덱스
// 기본값 undifined
let triangleIndex = undefined;

// ulTriangle에 있는 리스트
let triangleLi = undefined;

// 유사배열인 ulTriangle의 요소들 배열화
const ulTriangleArr = Array.from(ulTriangle.children);

// ulTriangle에 마우스를 올렸을 때
ulTriangle.addEventListener("mouseover", (e) => {
  // 올려놓은 li(ul_triangle)의 요소를 저장
  triangleLi = e.target.closest("li");

  // 만약에 triangleLi가 존재하면서
  // ulTriangle에 포함되어있다면
  if (triangleLi && ulTriangle.contains(triangleLi)) {
    // ulTriangleArr에서 triangleLi의 인덱스 찾기
    // 찾은 인덱스를 triangleIndex에 추가
    triangleIndex = ulTriangleArr.indexOf(triangleLi);
  }

  // ul_text의 class를 off=> on으로 변경
  ulText.classList.remove("off");
  ulText.classList.add("on");

  // (콜백, ul_text의 li)
  // 그 index의 값에 맞추어 ul_text의
  // index에 해당하는 li의 class를
  // opacity0 => opacity100으로 변경
  // 가져온 인덱스를 토대로 opacity0=>100 진행

  ulText.children[triangleIndex].classList.remove("opacity0");
  ulText.children[triangleIndex].classList.add("opacity100");
});

// div_in_ul에 마우스를 뗏을 때
divInUl.addEventListener("mouseleave", () => {
  // 초기화
  // 기본값 undifined
  triangleIndex = undefined;

  // ulTriangle에 있는 리스트
  triangleLi = undefined;

  //   ulText 배열화
  const ulTextArr = Array.from(ulText);

  //   모두 opacity100=>0
  ulTextArr.forEach((element) => {
    element.classList.remove("opacity100");
    element.classList.add("opacity0");
  });

  // ul_text의 class를 on=> off로 변경
  ulText.classList.remove("on");
  ulText.classList.add("off");
});
