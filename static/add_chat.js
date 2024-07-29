var chat_form = document.forms["send_chat"];
var chat_name = document.getElementById("chat_name");
var chat_content = document.getElementById("chat_content");
var chat_submit = document.getElementById("chat_button");
var reputation_id=document.getElementById("rep_id").value;
var video_time=document.getElementById("vid_t");
chat_submit.onclick=add_chat
function add_chat(){
    const formData = new FormData(chat_form);
    formData.append("sec",video_time.value);
    const action = "/truetube/add_chat/"+reputation_id;
    const options = {
        method: 'POST',
        body: formData,
    };
    fetch(action, options).then((e) => {
        chat_content.value="";
    });
}

var is_enter_pressed=false;
var is_shift_pressed=false;
//chat_content.addEventListener("keydown", enter_event);
//chat_content.addEventListener("keydown", shift_event_down);
//chat_content.addEventListener("keyup", shift_event_up);
function enter_event(e) {
    if (e.key == "Enter" && is_shift_pressed==false){
        add_chat();
        chat_content.value="";
    }else{

    }
    return false;
}
function shift_event_down(e) {
    if (e.key == "Shift"){
        //console.log("Shifted")
        is_shift_pressed=true;
    }
    return false;
}
function shift_event_up(e) {
    if (e.key == "Shift"){
        //console.log("Shifted_up")
        is_shift_pressed=false;
    }
    return false;
}