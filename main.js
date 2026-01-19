// 테스트
console.log("서버와 자바스크립트와 연결 성공")

// body의 4번째 요소에 접근시(div)
// ul의 특정 순서의 li에 접근을 하였다면
// (1,2번째 ul 다 상관없음)
// (1번째만 하면 2번째 등장하자마자 off될수있기에)
// 두번째 ul의 class를 on으로 변경
// on으로 변경하면서 콜백함수를 통해 바로 
// 특정 li의 opacity를 0에서 1로 변경
// opacity0 => opacity100



// body를 먼저 가져옴
const body = document.body

// body에서 div를 찾음
// div_in_ul(ul들이 존재하는 div)
const divInUl = body.children[3]



// ul_triangle
const ulTriangle = divInUl.children[0]

// ul_text
const ulText = divInUl.children[1]


// triangle 내부의 li의 인덱스
// 기본값 undifined
let triangleIndex = undefined;



// div_in_ul에 마우스를 올렸을 때
divInUl.addEventListener("mouseenter",(e)=> {
    


    // 올려놓은 li(ul_triangle)의 요소를 저장
    const triangleLi = e.target.querySelector("ul:nth-child(1)>li")


    
    // 인덱스 값 찾음
    // foreach
    triangleIndex = ulTriangle.map((element,index) => {
        
        // 만약에 element와 triangleLi가 같다면
        if (element === triangleLi){
            // 인덱스 반환
            return index

        }


    });



    // triangleIndex 테스트
    console.log(triangleIndex)


    // ul_text의 class를 off=> on으로 변경
    ulText.classList.remove("off")
    ulText.classList.add("on")

    // (콜백, ul_text의 li)
    // 그 index의 값에 맞추어 ul_text의 
    // index에 해당하는 li의 class를 
    // opacity0 => opacity100으로 변경





})


// div_in_ul에 마우스를 뗏을 때
divInUl.addEventListener("mouseleave",()=>{

    // 테스트(마우스가 나갔다고 확인)
    console.log("마우스뗌")

})
