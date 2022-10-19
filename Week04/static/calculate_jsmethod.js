function square(){
    number=document.querySelector("#calculate").value;
    // 轉跳動態路由時要注意不用打成<${number}>
    // 原因在於動態路由外面的<>只是語法，並非網址上的東西
    window.location.assign(`/square/${number}`); 
}



// action="{{url_for('square', number=144)}}"