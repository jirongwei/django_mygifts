from django.http import JsonResponse,HttpResponse
import time,json
from . import models
import user.models

# personal首页
def personal(request):

    return HttpResponse('i am post')

# 根据id获取用户信息
def getUserInfo(request):
    pass

# update用户信息
def updateUserInfo(request):
    pass

# upload头像
def uploadIcon(request):
    pass

# 安全等级
def securityLevel(request):
    pass

# 修改密码
def updatePwd(request):
    pass

# 绑定手机
def bindPhone(request):
    pass

# 收藏-->展示
def getCollectList(request):
    if request.method=='GET':
        # 前端传来收藏的用户id
        uid=request.GET.get('u_id')
        # 这里定义一个空列表，将后面遍历出来的数据加进来
        all_result=[]
        # 通过id 查询
        colpost=models.PostCollect.objects.filter(userinfo_id=uid).values('post_id_id','id','post_id__ptitle','post_id__pbriefcont')
        print(colpost)
        # 将查询到的结果遍历出来
        for col in colpost:
            # 获取里面的收藏的文章的ID
            pe_id=col['post_id_id']
            # 根据文章id查找用户id
            collect=models.PostCollect.objects.filter(post_id_id=pe_id).values()
            # print(collect)
            # 将查出来的用户id通过.count计算出来个数
            col['coll_count']=collect.count()
            # 在插入到列表中
            all_result.append(col)
        return HttpResponse(json.dumps(list(all_result),ensure_ascii=False))


# 收藏-->详情
def getCollectDetail(request):
    pass

# 收藏-->删除
def delCollect(request):
    pass

# 订单展示
def getOrderList(request):
    pass

# 订单详情
def getOrderDetail(request):
    pass

# 地址管理
def getAddressList(request):
    pass

# 添加地址
def addAddress(request):
    pass

# 修改地址
def updateAddress(request):
    pass

# 插入帖子
def createPost(request):
   if request.method=="POST":
       try:
           post={}
           post["ptitle"]=json.loads(request.body)["ptitle"]
           post["ptitleimg"]=json.loads(request.body)["ptitleimg"]
           post["pdetailcont"]=json.loads(request.body)["pdetailcont"]
           post["pbriefcont"]=json.loads(request.body)["pbriefcont"]
           post["p_createtime"]=time.time()
           post["p_userid"]=json.loads(request.body)["p_userid"]
           post["p_status"]=1
           postsave=models.Post(**post)
           postsave.save()
           return HttpResponse({"code":postsave.id})
       except Exception as ex:
           print(ex)
           return HttpResponse({"code":"901"})

# 删除地址
def delAddress(request):
    pass

 #加载帖子（根据类型，页码）Post
def showPost(request):
    pageSize=5
    postlist=[]
    # 有时间时再次写
    searchtype=json.loads(request.body)["navtype"]
    page=int(json.loads(request.body)["pageindex"])
    userid=json.loads(request.body)["uid"]
    postmes=list(models.Post.objects.all()[(page-1)*pageSize:page*pageSize].values("id","ptitle","ptitleimg","pdetailcont","pbriefcont"))

    for i in range(len(postmes)):
        post={}
        post["easyshow"]=True
        post["postid"]=postmes[i]["id"]
        post["posttitle"]=postmes[i]["ptitle"]
        post["postImg"]=postmes[i]["ptitleimg"]
        post["postdetailcon"]=postmes[i]["pdetailcont"]
        post["posteasycon"]=postmes[i]["pbriefcont"]
        post["postreplynum"]=models.PostReply.objects.filter(pReply_pid_id=post["postid"]).count()
        post["postcollectnum"]=models.PostCollect.objects.filter(post_id_id=post["postid"]).count()
        postcollectionstatus=models.PostCollect.objects.filter(post_id_id=post["postid"],userinfo_id=userid).count()
        if postcollectionstatus:
            post["postcollectstatus"]=True
        else:
            post["postcollectstatus"]=False
        post["postdianzannum"] = models.PostThumb.objects.filter(post_id_id=post["postid"]).count()
        postdianzanstatus=models.PostThumb.objects.filter(post_id_id=post["postid"],userinfo_id=userid).count()
        if postdianzanstatus:
            post["postdianzanstatus"]=True
        else:
            post["postdianzanstatus"] = False
        postlist.append(post)
    print(postlist)
    return JsonResponse(postlist,safe=False,json_dumps_params={"ensure_ascii":False})


#收藏帖子
def collectpost(request):
    if request.method=="POST":
        try:
            userid = json.loads(request.body)["userid"]
            postid = json.loads(request.body)["postid"]
            collectstatus = json.loads(request.body)["collectstatus"]
            if collectstatus:
                obj = models.PostCollect(userinfo_id=userid, post_id_id=postid)
                obj.save()
            else:
                models.PostCollect.objects.filter(userinfo_id=userid, post_id_id=postid).delete()
            return JsonResponse({"code":200})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":500})


#点赞帖子
def  dianzanpost(request):
    if request.method=="POST":
        # try:
        userid = json.loads(request.body)["userid"]
        postid = json.loads(request.body)["postid"]
        dianzanstatus = json.loads(request.body)["dianzanstatus"]
        if dianzanstatus:
            obj = models.PostThumb(userinfo_id=userid, post_id_id=postid)
            obj.save()
        else:
            models.PostCollect.objects.filter(userinfo_id=userid, post_id_id=postid).delete()
        return JsonResponse({"code": 200})
        # except Exception as ex:
        #     print(ex)
        #     return JsonResponse({"code": 500})




