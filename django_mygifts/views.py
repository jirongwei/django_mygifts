from django.http import JsonResponse,HttpResponse

# 网站首页
def index(request):
    return HttpResponse('i am website Home')


# 循环轮播图
def som(request):
    if request.method == 'GET':
        try:
            postimgs = [
                {
                    "userTelephone": "15776554502",
                    "userImg": 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2474915043,820939899&fm=26&gp=0.jpg',
                    "userName": "ff",
                    "postId": "000",
                    "postTitle": "疯流涕淌",
                    "postContent": "qqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
                },
                {
                    "userTelephone": "15776554502",
                    "userImg": 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2474915043,820939899&fm=26&gp=0.jpg',
                    "userName": "ff",
                    "postId": "000",
                    "postTitle": "ww",
                    "postContent": "qqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
                },
                {
                    "userTelephone": "15776554502",
                    "userImg": 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2474915043,820939899&fm=26&gp=0.jpg',
                    "userName": "ff",
                    "postId": "000",
                    "postTitle": "ww",
                    "postContent": "qqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
                },
                {
                    "userTelephone": "15776554502",
                    "userImg": 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2474915043,820939899&fm=26&gp=0.jpg',
                    "userName": "ff",
                    "postId": "000",
                    "postTitle": "ww",
                    "postContent": "qqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
                },
            ]
            # postimgs=models.
            return JsonResponse(postimgs, safe=False, json_dumps_params={"ensure_ascii": False})
        except Exception as e:
            print(e)
            return HttpResponse({"code": "701"})

    elif request.method == 'POST':
        return HttpResponse({"code": "801"})

    else:
        return HttpResponse({"code": "901"})








