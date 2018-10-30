from django.http import JsonResponse,HttpResponse
from . import models
import json
import time,math
from datetime import datetime
from utils.Tools.tools import *

# tribune首页
def tribunes(request,page):
    pagesize=6
    page=int(page)
    if request.method=='GET':
        # try:
            gls=[]
            glmes=list(models.Tribune.objects.all()[(page-1)*pagesize:page*pagesize].values("id","ttitleimg","ttitle","tbriefcont"))
            for i in glmes:
                gl={}
                gl["glid"]=i["id"]
                gl["glimg"]=i["ttitleimg"]
                gl["gltitle"]=i["ttitle"]
                gl["glcontent"]=i["tbriefcont"]
                gl["glclicknum"]=models.TribuneThumb.objects.filter(userinfo_id=gl["glid"]).count()
                gl["clickstatus"]=False
                gl["colnum"]=models.TribuneCollect.objects.filter(userinfo_id=gl["glid"]).count()
                gl["praisestatus"]=False
                gl["glreplynum"]=models.TribuneReply.objects.filter(tReply_uid_id=gl["glid"]).count()
                gls.append(gl)

            return JsonResponse(gls,safe=False,json_dumps_params={"ensure_ascii":False})
        # except Exception as e:
        #     print(e)
        #     return HttpResponse({"code":"701"})

    elif request.method=='POST':
        return HttpResponse({"code":"801"})

    else:
        return HttpResponse({"code": "901"})


# 攻略点赞
def thumbUpPost(request):
    if request.method=="POST":
        try:
            userid = json.loads(request.body)["userid"]
            postid = json.loads(request.body)["postid"]
            dianzanstatus = json.loads(request.body)["dianzanstatus"]
            if dianzanstatus:
                obj = models.TribuneThumb(userinfo_id=userid, post_id_id=postid)
                obj.save()
            else:
                models.TribuneThumb.objects.filter(userinfo_id=userid, post_id_id=postid).delete()
            return JsonResponse({"code": 200})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": 500})





# 发表攻略
def publishPost(request):
    pass

# 攻略收藏
def collectStrategy(request):
    if request.method=="POST":
        try:
            userid = json.loads(request.body)["userid"]
            postid = json.loads(request.body)["postid"]
            collectstatus = json.loads(request.body)["collectstatus"]
            if collectstatus:
                obj = models.TribuneCollect(userinfo_id=userid, post_id_id=postid)
                obj.save()
            else:
                models.TribuneCollect.objects.filter(userinfo_id=userid, post_id_id=postid).delete()
            return JsonResponse({"code":200})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":500})


# 攻略详情页面
def concernPublisher(request):
    # 从前台接受到的攻略id
    tid=request.GET.get('tid')
    if request.method=='GET':
        tribune=models.Tribune.objects.filter(id=tid).values('id','ttitle','t_userid__icon','ttitleimg','tdetailcont','t_createtime','t_userid__nickname')
        print(tribune)
        tribunes=[]
        for t in tribune:
            t['t_createtime']=str(datetime.fromtimestamp(t['t_createtime'])).split('.')[0]
            tribunes.append(t)
        return HttpResponse(json.dumps(list(tribunes),ensure_ascii=False))

# 热门攻略
def hottribune(request):
    htsmes=[]
    hts=list(models.Tribune.objects.all().values("id","ttitle")[0:1])
    for i in range(len(hts)):
        ht={}
        ht["glid"]=hts[i]["id"]
        ht["gltitle"]=hts[i]["ttitle"]
        ht["gllovenum"]=models.TribuneThumb.objects.filter(tribune_id=ht["glid"]).count()
        ht["glcomptentnum"]=models.TribuneReply.objects.filter(tReply_pid=ht["glid"]).count()
        htsmes.append(ht)
    return JsonResponse(htsmes,safe=False, json_dumps_params={"ensure_ascii": False})

# 向数据库中添加评论
def zmAddComment(request):
    if request.method == 'POST':
        res=json.loads(request.body)
        # user_id = res['tReply_uid_id']
        # tokencon = getToken('')

        res['tReply_time']=time.time()
        models.TribuneReply.objects.create(**res)
        return HttpResponse('{"code":"202"}')


# 攻略评论
def commentPost(request):
    if request.method == 'GET':
        # 获取所有评论
        # comments = list(models.TribuneReply.objects.all().values('id', 'tReply_con', 'tReply_time', 'tReply_pid','tReply_pid__t_userid__nickname','tReply_pid__t_userid__icon','tReply_uid'))
        comments = list(models.TribuneReply.objects.all().values('id', 'tReply_con', 'tReply_time', 'tReply_pid','tReply_uid__nickname','tReply_uid__icon','tReply_uid'))
        aa=[]
        for co in comments:
            co['tReply_time']=str(datetime.fromtimestamp(co['tReply_time'])).split('.')[0]
            aa.append(co)
        aa = sorted(aa,key=lambda co: co['tReply_time'], reverse=True)
        return HttpResponse(json.dumps(aa,ensure_ascii=False))


# 我的攻略收藏
def collectStrategis(request):
    if request.method=='GET':
        uid=request.GET.get('u_id')
        strate=models.TribuneCollect.objects.filter(userinfo_id=uid).values('id','tribune_id__ttitle','tribune_id__ttitleimg','tribune_id__tdetailcont','tribune_id__id')
        print(strate)
        return HttpResponse(json.dumps(list(strate),ensure_ascii=False))



# 对gl进行条件查询
def getsearchgl(request):
    pagesize = 8
    if request.method=='POST':
        try:
            tiaojian = json.loads(request.body)["tiaojian"]
            if tiaojian:
                page = json.loads(request.body)["page"]
                glmes1=list(models.Tribune.objects.filter(ttitle__regex=tiaojian).values("id", "ttitle", "ttitleimg", "tbriefcont", "t_createtime"))
                glmes2 = list(models.Tribune.objects.filter(tbriefcont__regex=tiaojian).values("id", "ttitle", "ttitleimg", "tbriefcont",
                                                                                      "t_createtime"))
                glmes=glmes1
                for i in range(len(glmes2)):
                    flog=True
                    for j in range(len(glmes)):
                        if glmes2[i]["id"]==glmes[j]["id"]:
                            flog=False
                            break
                    if flog:
                        glmes.append(glmes2[i])
                glmes = sorted(glmes, key=lambda ll: ll["t_createtime"], reverse=True)[(page - 1) * pagesize:page * pagesize]
                for i in range(len(glmes)):
                    glmes[i]["clicknum"]=models.TribuneThumb.objects.filter(tribune_id=glmes[i]["id"]).count()
                    glmes[i]["replynum"]=models.TribuneReply.objects.filter(tReply_pid=glmes[i]["id"]).count()
                return HttpResponse(json.dumps(glmes, ensure_ascii=False))
            else:
                page = int(json.loads(request.body)["page"])
                lens = models.Tribune.objects.all().values("id", "ttitle", "ttitleimg", "tbriefcont", "t_createtime")
                lens = sorted(lens, key=lambda ll: ll["t_createtime"], reverse=True)[
                       (page - 1) * pagesize:page * pagesize]
                for i in range(len(lens)):
                    lens[i]["clicknum"]=models.TribuneThumb.objects.filter(tribune_id=lens[i]["id"]).count()
                    lens[i]["replynum"]=models.TribuneReply.objects.filter(tReply_pid=lens[i]["id"]).count()
                return HttpResponse(json.dumps(list(lens), ensure_ascii=False))
        except Exception as es:
            print(es)
            return JsonResponse({"code": "001"})

# 查询攻略的页数
def getsearchglpages(request):
    pagesize = 8
    if request.method=='POST':
        try:
            tiaojian = json.loads(request.body)["tiaojian"]
            if tiaojian:
                glmes1 = list(models.Tribune.objects.filter(ttitle__regex=tiaojian).values("id"))
                glmes2 = list(
                    models.Tribune.objects.filter(tbriefcont__regex=tiaojian).values("id"))
                glmes = glmes1
                for i in range(len(glmes2)):
                    flog = True
                    for j in range(len(glmes)):
                        if glmes2[i]["id"] == glmes[j]["id"]:
                            flog = False
                            break
                    if flog:
                        glmes.append(glmes2[i])
                pages=math.ceil(len(glmes)/pagesize)
                return HttpResponse(pages)
            else:
                lens = models.Tribune.objects.all().count()
                return HttpResponse(math.ceil(lens/pagesize))
        except Exception as es:
            print(es)
            return JsonResponse({"code": "001"})

