var div_comments=document.getElementById("div_comments")
var reputation_id=document.getElementById("rep_id").value;

setInterval(() => {    
    fetch_comments();
}, 500);
async function fetch_comments(){
    const action = "/truetube/fetch_comments/"+reputation_id;
    const options = {
        method: 'GET'
    };

    fetch(action, options).then(function (data) {
        return data.json(); // 読み込むデータをJSONに設定
      }).then(function (json){
        while(div_comments.children.length>0){
            div_comments.removeChild(div_comments.firstChild)
        }
        const comments=json.comments;
        const foot_div=document.createElement("div");
        div_comments.appendChild(foot_div)
        comments.forEach(element => {
            var namestr="";
            if(element.name==""){namestr="名無し";}
            else{namestr=element.name;}
            const text_name=document.createTextNode("名前："+namestr)
            var p_name=document.createElement("p");
            p_name.style.color="#00ff7f";
            p_name.style.lineHeight="5px";
            p_name.appendChild(text_name);

            const div_content=document.createElement("div");
            const content_header_text=document.createTextNode("内容：");
            const content_header_p=document.createElement("p");
            content_header_p.lineHeight="5px";
            content_header_p.appendChild(content_header_text);
            div_content.appendChild(content_header_p);

            element.content.split("\n").forEach(
                line=>{
                    const p_line=document.createElement("p");
                    p_line.style.lineHeight="5px";
                    p_line.appendChild(document.createTextNode(line));
                    div_content.appendChild(p_line);
                }
            )

            const text_time=document.createTextNode(element.time)
            const p_time=document.createElement("p");
            p_time.style.lineHeight="5px"
            p_time.appendChild(text_time);

            const div_entry=document.createElement("div");
            div_entry.appendChild(p_name);
            div_entry.appendChild(div_content);
            div_entry.appendChild(p_time);
            div_entry.style.border="solid";
            div_entry.style.borderWidth="1px"

            foot_div.after(div_entry)
        });
      });
}