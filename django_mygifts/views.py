from django.http import JsonResponse,HttpResponse
import post.models
# 网站首页
def index(request):
    return HttpResponse('i am website Home')


# 循环轮播图
def som(request):
    if request.method == 'GET':
        try:
            postimgs=[]
            postmes = list(post.models.Post.objects.all()[0:4].values("id","ptitle","pbriefcont","p_userid__nickname","p_userid__user_id","p_userid__icon"))
            for i in postmes:
                pomes={}
                pomes["userTelephone"]=i["p_userid__user_id"]
                pomes["userImg"]=i["p_userid__icon"]
                pomes["userName"]=i["p_userid__nickname"]
                pomes["postId"]=i["id"]
                pomes["postTitle"]=i["ptitle"]
                pomes["postContent"]=i["pbriefcont"]
                postimgs.append(pomes)
            return JsonResponse(postimgs, safe=False, json_dumps_params={"ensure_ascii": False})
        except Exception as e:
            print(e)
            return HttpResponse({"code": "701"})

    elif request.method == 'POST':
        return HttpResponse({"code": "801"})

    else:
        return HttpResponse({"code": "901"})








