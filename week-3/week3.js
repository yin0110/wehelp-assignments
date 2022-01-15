var p=[];
var pic=[];
async function getdata(){
    let data= await fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
    let dataj= await data.json();
    // console.log(dataj)
    let x=dataj.result.results
    for(b in x){
        let n=x[b].file.split("https:")[1]
        m="https:"+n;
        pic.push(m);
    }//pic是我抓取的圖片網址
    for(a in x){
        let place=x[a].stitle;
        p.push(place);
    }
    var divB= document.createElement("div");
    document.body.appendChild(divB);
    divB.className="container3";
    for(let z=0; z<4; z++){
        var output=p[z];
        var div= document.createElement("div");
        div.className="boxa";
        var div2= document.createElement("div");
        var div3= document.createElement("div");
        var newImage=document.createElement("img");
        var paragraph=document.createElement("p");
        var newContent = document.createTextNode(output);
        // var div=document.createElementById("pho");
        newImage.src=pic[z];
        divB.appendChild(div);
        div.appendChild(div2);
        div2.appendChild(newImage);
        div.appendChild(div3);
        div3.appendChild(paragraph);
        paragraph.appendChild(newContent);
        div2.className="pho";
        div3.className="text";
    }
    var divC= document.createElement("div");
    document.body.appendChild(divC);
    divC.className="container3";
    for(let z=4; z<8; z++){
        var output=p[z];
        var div= document.createElement("div");
        div.className="boxa";
        var div2= document.createElement("div");
        var div3= document.createElement("div");
        var newImage=document.createElement("img");
        var paragraph=document.createElement("p");
        var newContent = document.createTextNode(output);
        // var div=document.createElementById("pho");
        newImage.src=pic[z];
        divC.appendChild(div);
        div.appendChild(div2);
        div2.appendChild(newImage);
        div.appendChild(div3);
        div3.appendChild(paragraph);
        paragraph.appendChild(newContent);
        div2.className="pho";
        div3.className="text";
    }
    

    // for(q in p){
    //     var newp=document.createElement("p");
    //     var newcontent=document.createTextNode(p[0])
    //     document.getElementById("name").appendChild(newcontent);
    // }
}
getdata()

// let imgg= new Image();
// imgg.onload=function(){
//     imgg.src=pic[z];
// }
// document.getElementById("imgc").appendChild(imgg);
// window.onload=function(){//網頁載入就開始跑
//     for(file in pic){
//     let imgg= new Image();
//         imgg.src= pic[file];
// console.log(imgg);
//         // document.getElementById("imgc").appendChild(imgg);
// }
// window.onload=function(){//網頁載入就開始跑
//     let img1=document.createElement("img");//點了之後插入img
//     src="https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000848.jpg";//載入圖片
//     img1.src=src;//我的img的scr要放入我設定的src
//     document.getElementById("imgc").appendChild(img1);//在body裡插入img
// }

// let pic= document.querySelectorAll('.pho');//抓到要的標籤id
// let a= document.createElement('a');//創建標籤
// create.appendChild(a);//你要把這個新的東西方在creat 裡

// document.getElementById("btn").onclick= function()//取得第一個按鈕的id
// {
//     let val= document.getElementById("imagename").value;//拿取第一個要放入的資訊id
//     src="https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000848.jpg";//載入圖片
//     img=document.createElement("img");//點了之後插入img
//     img.src=src;//我的img的scr要放入我設定的src
//     document.body.appendChild(img);//在body裡插入img
// }
// window.onload=function(){//網頁載入就開始跑
//     // document.getElementById("btn")//取得第一個按鈕的id
//     let val= document.getElementById("imagename");//拿取第一個要放入的資訊id
//     src="https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000848.jpg";//載入圖片
//     img=document.createElement("img");//點了之後插入img
//     img.src=src;//我的img的scr要放入我設定的src
//     document.body.appendChild(img);//在body裡插入img
// }
// var p=[];
// async function getplace(){
//     let data= await fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
//     let dataj= await data.json();
//     // console.log(dataj)
//     let x=dataj.result.results
//     // console.log(x);
//     for(a in x){
//         let place=x[a].stitle;
//         p.push(place);
//     }
//     window.onload=function(){//網頁載入就開始跑
//     let url=p;//讓url會等於我們跑出來的地點
//     let site=url.map(function(u){
//         let sites= u;
//     document.getElementById("name").appendChild(sites);
// })
// }
// }
// getplace();
// let img1=document.createElement("img");//點了之後插入img
// src="https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000848.jpg";//載入圖片
// img1.src=src;//我的img的scr要放入我設定的src
// document.getElementById("imgc").appendChild(img1);//在body裡插入img

// let url=p;
// let imgs= p
// .map(function(u){
//     let imgg= new Image();
//     imgg.src= u;
//     document.body.appendChild(imgg);
//     return imgg;
// })
// }
// getplace()

// window.onload=function(){//網頁載入就開始跑
//     let img1=document.createElement("img");//點了之後插入img
//     src="https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000848.jpg";//載入圖片
//     img1.src=src;//我的img的scr要放入我設定的src
//     document.getElementById("imgc").appendChild(img1);//在body裡插入img