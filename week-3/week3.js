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
    
}
getdata()

