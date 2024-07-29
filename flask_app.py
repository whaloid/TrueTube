from flask import Flask, render_template,request,url_for,redirect,jsonify
import datetime
import os
import tt_util

app = Flask(__name__)

@app.route('/truetube')
def tthome():
    retidxs=[]
    repjs=os.listdir("tt_threads")
    for js in repjs:
        reputation=tt_util.json2reputation("tt_threads/"+js)
        retidxs.append({"id":reputation.id_,
                "title":reputation.title,"content":reputation.content})
    return render_template('tt_index.html',replis=retidxs)

@app.route('/truetube/reputation/<string:rid>',methods=["GET","POST"])
def reputation_page(rid):
    if request.method=="GET":
        reputation=tt_util.json2reputation("tt_threads/"+rid+".json")
        video_id=tt_util.extract_video_id(reputation.url)
        return render_template('tt_reputation.html',
                reputation=reputation,video_id=video_id)

@app.route('/truetube/add_comment/<string:rid>',methods=["POST"])
def add_comment(rid):
    if request.method=="POST" and len(list(request.values["content"]))>0\
        and len(list(request.values["content"]))<1000:
        new_comment=tt_util.Comment(request.values["name"],
                request.values["content"],str(datetime.datetime.now()))
        reputation=tt_util.json2reputation("tt_threads/"+rid+".json")
        reputation.add_comment(new_comment)
        tt_util.reputation2json(reputation)
        return redirect("/truetube/reputation/"+rid)

@app.route('/truetube/fetch_comments/<string:rid>',methods=["GET"])
def fetch_comments(rid):
    if rid+".json" in os.listdir("tt_threads"):
        reputation=tt_util.json2reputation("tt_threads/"+rid+".json")
        retarr=[]
        for comment in reputation.comments:
            retarr.append({"name":comment.name,"content":comment.content,
                           "time":str(comment.time)})
        return jsonify({"comments":retarr})
    else:
        return jsonify({"comments":[]})

@app.route('/truetube/fetch_chats/<string:rid>',methods=["GET"])
def fetch_chats(rid):
    if rid+".json" in os.listdir("tt_threads"):
        reputation=tt_util.json2reputation("tt_threads/"+rid+".json")
        retarr=[]
        i=0
        for chat in reputation.chats:
            if chat.sec>float(request.values["sec"]):
                i-=1
                break
            i+=1
        for j in range(int(request.values["num"])):
            if i-j-1<0:
                break
            else:
                added_chat=reputation.chats[i-j-1]
                retarr.insert(0,{"name":added_chat.name,
                    "content":added_chat.content,"sec":added_chat.sec})
        return jsonify({"chats":retarr})
    else:
        return jsonify({"chats":[]})

@app.route('/truetube/add_chat/<string:rid>',methods=["POST"])
def add_chat(rid):
    if len(list(request.values["content"]))>0 and len(list(request.values["content"]))<200:
        if rid+".json" in os.listdir("tt_threads"):
            reputation=tt_util.json2reputation("tt_threads/"+rid+".json")
            chat=tt_util.Chat(request.values["name"],
                    request.values["content"],float(request.values["sec"]))
            reputation.add_chat(chat)
            tt_util.reputation2json(reputation)
            return jsonify({"result":True})
        else:
            return jsonify({"result":False})
    else:
        return jsonify({"result":False})

@app.route('/truetube/register',methods=["GET","POST"])
def tt_createpage():
    if request.method=="POST":
        id_=tt_util.gen_rand_id(20)
        url=request.values["url"]
        title=request.values["title"]
        if tt_util.is_youtube_video_format_url(url)\
            and len(list(request.values["content"]))>0\
                and len(list(request.values["content"]))<1000\
            and len(list(title))>0 and len(list(title))<100:
            content=request.values["content"]
            reputation=tt_util.Reputation(id_,url,title,content)
            tt_util.reputation2json(reputation)
            return redirect("/truetube")
        else:
            return render_template("tt_register.html")
    elif request.method=="GET":
        return render_template("tt_register.html")
    
if __name__ == "__main__":
    app.run()