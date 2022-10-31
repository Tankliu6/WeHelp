// 資料庫[[地名, imgUrl]、[]、[]....[]]，是一個大陣列包小陣列
let placeData=[];
// 產生地名
function getPlace(place_number){
    //console.log(placeImg[place_number][0]);
    return placeData[place_number][0];
};
// 產生圖片網址
function getImgUrl(place_number){
    //console.log(placeImg[place_number][1]);
    return placeData[place_number][1];
};
function getData(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
    .then(function(response){
        return response.json(); // 讀取為 JSON 格式的資料
    }).then(function(data){
        let dataPool=data.result.results;
        for(let url_i=0; url_i < dataPool.length; url_i++){
            // 將每一筆資料的第一張圖片的 url 及 地區名稱放進一個陣列當中，方便資料調用!!
            data=[dataPool[url_i].stitle, `https:${dataPool[url_i].file.split("https:")[1]}`];
            placeData.push(data);
            // 大陣列(資料庫) placeData[0]=["新北投溫泉區", "https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000848.jpg"]
        };
        //console.log(placeImg);
        // 1200px 內容頁左上角
        let imgTag_1=document.createElement("img");
        imgTag_1.src=getImgUrl(0); imgTag_1.style.width="80px"; imgTag_1.style.height="50px"; 
        let htmlTag_1=document.querySelector(".up-content-left");
        htmlTag_1.appendChild(imgTag_1);
        let spanTag_1=document.createElement("span");
        let spanContent_1=document.createTextNode(getPlace(0));
        spanTag_1.appendChild(spanContent_1);
        htmlTag_1.appendChild(spanTag_1);
        // 1200px 內容頁右上角
        let imgTag_2=document.createElement("img");
        imgTag_2.src=getImgUrl(1); imgTag_2.style.width="80px"; imgTag_2.style.height="50px"; 
        let htmlTag_2=document.querySelector(".up-content-right");
        htmlTag_2.appendChild(imgTag_2);
        let spanTag_2=document.createElement("span");
        let spanContent_2=document.createTextNode(getPlace(1));
        spanTag_2.appendChild(spanContent_2);
        htmlTag_2.appendChild(spanTag_2);
        // 1200px 內容頁豆腐岩區
        function addContent(data_number){
            //console.log(placeData);
            //console.log(getPlace(data_number));
            //console.log(getImgUrl(data_number));
            document.querySelector(".picture-title-flex").insertAdjacentHTML("beforeend", 
            `<div class="picture-title">
                <div class="picture-title-img-div"><img class="picture-title-div-img" src=${getImgUrl(data_number)}></img></div>
                <div class="title-position">${getPlace(data_number)}</div>
            </div>`           
            );
        };
        for(let i=2; i < 10; i++){
            addContent(i);
        };
    });
};
// // quest 4 增加下方宮格
// let data_number=10, data_number_check=data_number+8
// function addContent(){
//     for(; data_number < data_number_check; data_number++){
//         document.querySelector(".picture-title-flex").insertAdjacentHTML("beforeend", 
//         `<div class="picture-title">
//             <div class="picture-title-img-div"><img class="picture-title-div-img" src=${getImgUrl(data_number)}></img></div>
//             <div class="title-position">${getPlace(data_number)}</div>
//         </div>`           
//         );
//     };
//     console.log([data_number, data_number_check])
//     data_number_check+=8;
// };
