var div_chats=document.getElementById("chat_log");
var reputation_id=document.getElementById("rep_id").value;
var video_time=document.getElementById("vid_t");

setInterval(() => {    
    fetch_chats();
    const sch= div_chats.scrollHeight;
}, 500);

setInterval(() => {    
    fetch_chats();
    const sch= div_chats.scrollHeight;
    if (div_chats.scrollTop>=sch-750){
        div_chats.scrollTop=sch
    }
}, 100);

async function fetch_chats(){
    const action = "/truetube/fetch_chats/"+reputation_id;
    const param = new URLSearchParams({"sec":video_time.value,"num":20})
    const options = {
        method: 'GET'
    };

    fetch(action+"?"+param, options).then(function (data) {
        return data.json(); // 読み込むデータをJSONに設定
      }).then(function (json){
        while(div_chats.children.length>0){
            div_chats.removeChild(div_chats.firstChild)
        }
        const chats=json.chats;
        chats.forEach(element => {
            var namestr="";
            if (element.name==""){
                namestr="名無し"
            }else{
                namestr=element.name
            }
            const text_name=document.createTextNode("名前："+namestr)
            const p_name=document.createElement("p");
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

            const div_entry=document.createElement("div");
            div_entry.appendChild(p_name);
            div_entry.appendChild(div_content);
            div_entry.style.border="solid";
            div_entry.style.borderWidth="1px"

            div_chats.appendChild(div_entry);
        });
      });
}