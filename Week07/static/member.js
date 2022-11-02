// 插入會員姓名
function insertMemberName(text){
    // 取得 html 標籤位置
    let nameTag = document.querySelector(".find-member-container");
    let name = document.createElement("div");
    nameTag.appendChild(name);
    name.innerText = text; // 放入要傳到瀏覽器上的文字
    nameTag.removeChild(nameTag.firstChild); // 刪除最上方的姓名查詢
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
        if (data.length == 1){
            insertMemberName(`${data[0][1]}(${data[0][2]})`)
        }else{
            insertMemberName(`無此會員姓名`)
        }
    })
}
