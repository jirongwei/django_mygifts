from django.http import JsonResponse,HttpResponse
from . import models
import json
import time
from datetime import datetime

# tribune首页
def tribunes(request,page):
    if request.method=='GET':
        try:
            glmes=[
                {
                    "glid": '001',
                    "glimg": 'https://img01.hua.com/uploadpic/newpic/1073038.jpg',
                    "gltitle": '仙女的美貌会发光！绝美高光盘了解一下',
                    "glcontent": '刚开始学化妆的时候，不敢用高光，怕下手重了会不好看。但是自从尝试着用过一次以后，小礼君就成了彻彻底底的“追光者”！高光用得好，不仅能修饰面部细节，让整个妆面看起来更加饱满透亮，而且整张脸看起来都有一种“zanzanzan”的元气感。',
                    "glclicknum": 100,
                    "glreplynum": 200
                },
                {
                    "glid": '001',
                    "glimg": 'https://img01.hua.com/uploadpic/newpic/1073038.jpg',
                    "gltitle": '仙女的美貌会发光！绝美高光盘了解一下',
                    "glcontent": '刚开始学化妆的时候，不敢用高光，怕下手重了会不好看。但是自从尝试着用过一次以后，小礼君就成了彻彻底底的“追光者”！高光用得好，不仅能修饰面部细节，让整个妆面看起来更加饱满透亮，而且整张脸看起来都有一种“zanzanzan”的元气感。',
                    "glclicknum": 100,
                    "glreplynum": 200
                },
                {
                    "glid": '001',
                    "glimg": 'https://img01.hua.com/uploadpic/newpic/1073038.jpg',
                    "gltitle": '仙女的美貌会发光！绝美高光盘了解一下',
                    "glcontent": '刚开始学化妆的时候，不敢用高光，怕下手重了会不好看。但是自从尝试着用过一次以后，小礼君就成了彻彻底底的“追光者”！高光用得好，不仅能修饰面部细节，让整个妆面看起来更加饱满透亮，而且整张脸看起来都有一种“zanzanzan”的元气感。',
                    "glclicknum": 100,
                    "glreplynum": 200
                },
                {
                    "glid": '001',
                    "glimg": 'https://img01.hua.com/uploadpic/newpic/1073038.jpg',
                    "gltitle": '仙女的美貌会发光！绝美高光盘了解一下',
                    "glcontent": '刚开始学化妆的时候，不敢用高光，怕下手重了会不好看。但是自从尝试着用过一次以后，小礼君就成了彻彻底底的“追光者”！高光用得好，不仅能修饰面部细节，让整个妆面看起来更加饱满透亮，而且整张脸看起来都有一种“zanzanzan”的元气感。',
                    "glclicknum": 100,
                    "glreplynum": 200
                },
                {
                    "glid": '001',
                    "glimg": 'https://img01.hua.com/uploadpic/newpic/1073038.jpg',
                    "gltitle": '仙女的美貌会发光！绝美高光盘了解一下',
                    "glcontent": '刚开始学化妆的时候，不敢用高光，怕下手重了会不好看。但是自从尝试着用过一次以后，小礼君就成了彻彻底底的“追光者”！高光用得好，不仅能修饰面部细节，让整个妆面看起来更加饱满透亮，而且整张脸看起来都有一种“zanzanzan”的元气感。',
                    "glclicknum": 100,
                    "glreplynum": 200
                },
                {
                    "glid": '001',
                    "glimg": 'https://img01.hua.com/uploadpic/newpic/1073038.jpg',
                    "gltitle": '仙女的美貌会发光！绝美高光盘了解一下',
                    "glcontent": '刚开始学化妆的时候，不敢用高光，怕下手重了会不好看。但是自从尝试着用过一次以后，小礼君就成了彻彻底底的“追光者”！高光用得好，不仅能修饰面部细节，让整个妆面看起来更加饱满透亮，而且整张脸看起来都有一种“zanzanzan”的元气感。',
                    "glclicknum": 100,
                    "glreplynum": 200
                }

            ]

            # glmes=models.
            return JsonResponse(glmes,safe=False,json_dumps_params={"ensure_ascii":False})
        except Exception as e:
            print(e)
            return HttpResponse({"code":"701"})

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


# 关注
def concernPublisher(request):
    pass

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