var comment_form = document.forms["comment_form"];
var comment_name = document.getElementById("comment_name");
var comment_content = document.getElementById("comment_content");
var comment_submit = document.getElementById("submit_comment");
var reputation_id=document.getElementById("rep_id").value;
comment_submit.onclick=add_comment
function add_comment(){
    const formData = new FormData(comment_form);
    const action = "/truetube/add_comment/"+reputation_id;
    const options = {
        method: 'POST',
        body: formData,
    };
    fetch(action, options).then((e) => {
        comment_name.value="";
        comment_content.value="";
    });
}