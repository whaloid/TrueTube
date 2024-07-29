import datetime
import json
import random
import os

class Comment:
    def __init__(self,name,content,time):
        self.name=name
        self.content=content
        self.time=time

class Chat:
    def __init__(self,name,content,sec):
        self.name=name
        self.content=content
        self.sec=sec

class Reputation:
    def __init__(self,id_,url,title,content):
        self.id_=id_
        self.url=url
        self.title=title
        self.content=content
        self.comments=[]
        self.chats=[]
    
    def add_comment(self,comment):
        self.comments.append(comment)
    
    def add_chat(self,chat:Chat):
        i=0
        for ct in self.chats:
            if ct.sec>=chat.sec:
                break
            i+=1
        self.chats.insert(i,chat)

def reputation2json(r:Reputation):
    dic={}
    dic["id"]=r.id_
    dic["url"]=r.url
    dic["title"]=r.title
    dic["content"]=r.content
    dic["comments"]=[]
    for i in range(len(r.comments)):
        dic["comments"].append(
            {"name":r.comments[i].name,
             "content":r.comments[i].content,
             "time":r.comments[i].time}
        )
    dic["chats"]=[]
    for i in range(len(r.chats)):
        dic["chats"].append(
            {"name":r.chats[i].name,
             "content":r.chats[i].content,
             "sec":r.chats[i].sec}
        )
    with open("tt_threads/"+r.id_+".json","w") as f:
        json.dump(dic,f,ensure_ascii=False,indent=4)

def json2reputation(filename):
    with open(filename,"r") as f:
        dic=json.load(f)
    reputation=Reputation(dic["id"],dic["url"],dic["title"],dic["content"])
    for i in range(len(dic["comments"])):
        dcom=dic["comments"][i]
        reputation.add_comment(Comment(dcom["name"],
                dcom["content"],dcom["time"]))
    for i in range(len(dic["chats"])):
        dcha=dic["chats"][i]
        reputation.add_chat(Chat(dcha["name"],dcha["content"],float(dcha["sec"])))
    return reputation

def gen_rand_id(n):
    s=""
    for i in range(n):
        s=s+str(random.randint(0,9))
    return s

def extract_video_id(yturl):
    yturl_=yturl.replace("https://www.youtube.com/watch?v=","")
    ret=""
    lsyturl=list(yturl_)
    for i in range(11):
        ret=ret+lsyturl[i]
    return ret

def is_youtube_video_format_url(url):
    pat="https://www.youtube.com/watch?v="
    pat=list(pat)
    url=list(url)
    if len(url)<len(pat):
        return False
    for i in range(len(pat)):
        if pat[i]!=url[i]:
            return False
    return True
