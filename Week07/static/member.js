// 插入一行結果
function insertTextLine(text, tag){
    // 取得 html 標籤位置
    console.log(tag)
    let divTag = document.querySelector(tag);
    let div = document.createElement("div");
    divTag.appendChild(div);
    div.innerText = text; // 放入要傳到瀏覽器上的文字
    let count = divTag.getElementsByTagName('div').length; // 計算放入的查詢結果是否超過一行
    if ( count > 1){
        divTag.removeChild(divTag.firstChild); // 刪除最上方一行
    }
}

// 搜尋該會員的會員姓名
function find_name(){
    // 由瀏覽器抓取 input 內容
    username = document.querySelector("#find-member-name").value
    fetch(`/api/member?username=${username}`)
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        if (data.length == 1){ // 有搜尋到該會員才會有資料回傳
            insertTextLine(`${data[0][1]}(${data[0][2]})`, `.find-member-container`)
        }else{
            insertTextLine(`無此會員姓名或聯絡官方`, `.find-member-container`)
        }
    })
}


// 更新該會員的會員姓名
function change_name(){
    // 由瀏覽器抓取 input 內容
    let nameToChange = document.querySelector("#change-member-name").value
    let entry = {
        nameToChange : nameToChange
    };
    fetch(`/api/member`, {
        method: "PATCH",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
        if('ok' in data){
            insertTextLine(`更新成功!`, `.change-member-container`)
        }else{
            insertTextLine(`更新失敗!`, `.change-member-container`)
        }
    })
}
