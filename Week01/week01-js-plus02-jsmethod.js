// function openFun() {
//     var hamburger=document.querySelector(".hamburger"); // 要注意class前要"."，id前要"#"
//     hamburger.classList.remove("close") // 將display:none 移除
//     hamburger.classList.add("open"); // 顯示title1~4
// }

// function closeFun() {
//     var hamburger=document.querySelector(".hamburger"); // 要注意class前要"."，id前要"#"
//     if(hamburger.style.display=="block"){
//         hamburger.style.display="none";
//     }else{
//         hamburger.style.display="none";
//     };
// }

function openFun(elem) {
    var hamburger=document.querySelector(".hamburger");
    var checkpoint=elem.classList.contains("up-right-flex-600px"); // 檢查是否為漢堡按鈕 classList.contains!!
    var checkpoint02=elem.classList.contains("hamburger"); // 開啟漢堡表單後不會按表單就關閉
    if(checkpoint || checkpoint02){
        hamburger.classList.remove("close") // 將display:none 移除
        hamburger.classList.add("open"); // 顯示title1~4
        document.querySelector("#a").classList.add("coverlayer"); // 打開表單同時打開可以觸發關閉表單的透明div
    }
}

function closeFun() {
    /* 關閉表單的程式碼 */ 
    var hamburger=document.querySelector(".hamburger"); // 要注意class前要"."，id前要"#"
    hamburger.classList.remove("open");
    hamburger.classList.add("close");
    /* 最後將透明div關閉，才能再次點擊右上角漢堡打開表單 */ 
    document.querySelector("#a").classList.remove("coverlayer");
}

