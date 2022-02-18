function getVal() {
    let val = document.getElementById('getUsername').value;
    let myname=val;
    let url=`http://127.0.0.1:3000/api/members?username=${myname}`;
    async function getdata(){
        let data= await fetch(url);
        let dataJson= await data.json();
        if (dataJson.data !== null){
            let output=dataJson.data["name"];
            let outputUser= dataJson.data["username"];
            var result = document.getElementById("searchUser");
            result.innerHTML = output+"("+outputUser+")";    
        }
        else{
            var result = document.getElementById("searchUser");
            result.innerHTML = "無此會員";    
        }
        // console.log(dataJson)
        // let output=dataJson.data["name"]
        // console.log(output)
        // let outputUser= dataJson.data["username"]
        // // var paragraph=document.createElement("p");
        // // var newContent = document.createTextNode(output);
        // // document.body.appendChild(paragraph);
        // // paragraph.appendChild(newContent);
        // var result = document.getElementById("searchUser");
        // result.innerHTML = output+"("+outputUser+")";      

        }
getdata()
}