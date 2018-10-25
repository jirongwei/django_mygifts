from django.http import HttpResponse,JsonResponse
import json,time

from . import models

# gift首页
def gifts(request):
    if request.method=='GET':
        gifts=models.Gifts.objects.all().values('id','gift_name','price','clicknum','giftImg')
        print(gifts)




        return HttpResponse(json.dumps(list(gifts),ensure_ascii=False))



    # post = [
    #     {
    #         "goodid": '001',
    #         "goodimg": 'https://img01.hua.com/uploadpic/newpic/9012060.jpg',
    #         "goodtitle": '眷念--戴安娜粉玫瑰33枝，石竹梅围绕',
    #         "goodprice": 338,
    #         "goodclicknum": 56,
    #         "goodreplynum": 33
    #     }
    # ]


def Indexgifts(request,page):
    pagesize=3
    if request.method == 'GET':
        try:


            # # 数据库数据
            # def gifts(request, page):
            #     page=int(page)
            #     pagesize = 8;
            #     if request.method == 'GET':
            #         try:
            #             goodlist = []
            #             gomes = models.Gifts.objects.all()[pagesize*(page-1), pagesize*page].values("id", "gift_name", "price")
            #             print(gomes[0])
            #             goomes = list(gomes)
            #             for goo in goomes:
            #                 good = {
            #                     "goodid": "",
            #                     "goodimg": "",
            #                     "goodtitle": "",
            #                     "goodprice": "",
            #                     "goodclicknum": 0,
            #                     "goodreplynum": 0
            #                 }
            #                 good["goodid"] = goo["id"]
            #                 good["goodtitle"] = goo["gift_name"]
            #                 good["goodprice"] = goo["price"]
            #                 good["goodimg"] = models.GiftsPic.objects.filter(gifts_id=good["goodid"]).values('pic_url')
            #                 good["goodclicknum"] = models.GiftsThumb.objects.filter(
            #                     {"gifts_id": good["goodid"], "thumb_status": 1}).count()
            #                 good["goodreplynum"] = models.GiftsThumb.objects.filter(gifts_id=good["goodid"]).count()
            #                 goodlist.append(good)
            #
            #             return JsonResponse(goodlist, safe=False, json_dumps_params={"ensure_ascii": False})
            #         except Exception as e:
            #             print(e)
            #             return HttpResponse({"code": "701"})
            #
            #     elif request.method == 'POST':
            #         return HttpResponse({"code": "801"})
            #
            #     else:
            #         return HttpResponse({"code": "901"})

            gomes=models.Gifts.objects.all().values("id","gift_name","price")
            print(gomes)
            goodmes = [
                {
                    "goodid": '001',
                    "goodimg": 'https://img01.hua.com/uploadpic/newpic/9012060.jpg',
                    "goodtitle": '眷念--戴安娜粉玫瑰33枝，石竹梅围绕',
                    "goodprice": 338,
                    "goodclicknum": 56,
                    "goodreplynum": 33
                },
                {
                    "goodid": '001',
                    "goodimg": 'https://img01.hua.com/uploadpic/newpic/9012060.jpg',
                    "goodtitle": '眷念--戴安娜粉玫瑰33枝，石竹梅围绕',
                    "goodprice": 338,
                    "goodclicknum": 56,
                    "goodreplynum": 33
                },
                {
                    "goodid": '001',
                    "goodimg": 'https://img01.hua.com/uploadpic/newpic/9012060.jpg',
                    "goodtitle": '眷念--戴安娜粉玫瑰33枝，石竹梅围绕',
                    "goodprice": 338,
                    "goodclicknum": 56,
                    "goodreplynum": 33
                },
                {
                    "goodid": '001',
                    "goodimg": 'https://img01.hua.com/uploadpic/newpic/9012060.jpg',
                    "goodtitle": '眷念--戴安娜粉玫瑰33枝，石竹梅围绕',
                    "goodprice": 338,
                    "goodclicknum": 56,
                    "goodreplynum": 33
                },
                {
                    "goodid": '001',
                    "goodimg": 'https://img01.hua.com/uploadpic/newpic/9012060.jpg',
                    "goodtitle": '眷念--戴安娜粉玫瑰33枝，石竹梅围绕',
                    "goodprice": 338,
                    "goodclicknum": 56,
                    "goodreplynum": 33
                },
                {
                    "goodid": '001',
                    "goodimg": 'https://img01.hua.com/uploadpic/newpic/9012060.jpg',
                    "goodtitle": '眷念--戴安娜粉玫瑰33枝，石竹梅围绕',
                    "goodprice": 338,
                    "goodclicknum": 56,
                    "goodreplynum": 33
                },
                {
                    "goodid": '001',
                    "goodimg": 'https://img01.hua.com/uploadpic/newpic/9012060.jpg',
                    "goodtitle": '眷念--戴安娜粉玫瑰33枝，石竹梅围绕',
                    "goodprice": 338,
                    "goodclicknum": 56,
                    "goodreplynum": 33
                },
                {
                    "goodid": '001',
                    "goodimg": 'https://img01.hua.com/uploadpic/newpic/9012060.jpg',
                    "goodtitle": '眷念--戴安娜粉玫瑰33枝，石竹梅围绕',
                    "goodprice": 338,
                    "goodclicknum": 56,
                    "goodreplynum": 33
                }
            ]
            return JsonResponse(goodmes, safe=False, json_dumps_params={"ensure_ascii": False})
        except Exception as e:
            print(e)
            return HttpResponse({"code": "701"})

    elif request.method == 'POST':
        return HttpResponse({"code": "801"})

    else:
        return HttpResponse({"code": "901"})



# gift详情
def getGiftDetail(request,giftid):

    giftid = int(giftid)

    if request.method=='GET':
        try:

            # 查询礼物详情信息
            gift_detail=models.Gifts.objects.filter(id=giftid).values('id','gift_name','gift_tip',
                        'type_id__typename','descr','gift_package','remark','price','new_price')

            # 查询礼物image-->url
            gift_images=models.GiftsPic.objects.filter(gifts_id=giftid).all().values('id','pic_url')

            print(gift_images)

            return JsonResponse({"gift_detail":list(gift_detail),"gift_images":list(gift_images)},json_dumps_params={"ensure_ascii": False})

        except Exception as ex:

            return JsonResponse({"code":"408"})

# 获取礼物评论
def getGiftsComments(request,giftid,cindex):
    cindex = int(cindex)
    giftid = int(giftid)

    pagesize = 2
    start = pagesize*(cindex-1)
    end = pagesize*cindex

    if request.method=='GET':
        try:
            # 查询礼物评论
            comments=models.GiftsComment.objects.filter(gifts_id=giftid,userinfo__address__status=1).order_by('-comment_time').values('userinfo__nickname','userinfo__icon',
                      'comment_time','comment','credit','userinfo__address__detailLocation')[start:end]
            return JsonResponse({"comments":list(comments)},json_dumps_params={"ensure_ascii": False})
        except Exception as ex:
            return JsonResponse({"code":"408"})

# 加入购物车
def addCart(request):
    if request.method == 'POST':
        try:
            cart = json.loads(request.body)
            cart['gifts_id'] = int(cart['gifts_id'])
            # 判断购物车是否存在商品
            count = models.GiftsCart.objects.filter(gifts_id=cart['gifts_id']).count()
            if count:
                # 购物车已存在该商品
                return JsonResponse({"code":"202"})
            else:
                # 将用户选择购物礼物加入购物车
                res=models.GiftsCart.objects.create(**cart)
                if res:
                    return JsonResponse({"code":"808"})
                else:
                    return JsonResponse({"code": "809"})
        except Exception as ex:
            return JsonResponse({"code":"408"})


# 获取购物车信息
def getAllCarts(request):
    if request.method == 'POST':
        try:
            userid = json.loads(request.body)
            # 根据用户id获取用户所有的购物车信息
            carts = models.GiftsCart.objects.filter(userinfo_id=userid['userinfo_id']).all().values('gifts_id','gifts__gift_name',
                    'gifts__descr','cart_num','gifts__giftImg','gifts__price')
            return JsonResponse({"carts":list(carts)},json_dumps_params={"ensure_ascii":False})
        except Exception as ex:
            return JsonResponse({"code":"408"})

# 删除指定商品
def delSelectedGift(request):
    if request.method == 'POST':
        try:
            carts = json.loads(request.body)
            # 根据用户id删除用户商品
            res = models.GiftsCart.objects.filter(userinfo_id=carts['userinfo_id'],gifts_id=carts['gifts_id']).delete()
            if res:
                return JsonResponse({"code":"808"})
            else:
                return JsonResponse({"code":"809"})
        except Exception as ex:
            return JsonResponse({"code":"408"})

# 清空购物车
def clearCart(request):
    if request.method == 'POST':
        try:
            userid = json.loads(request.body)
            # 根据用户id清空购物车
            res = models.GiftsCart.objects.filter(userinfo_id=userid['userinfo_id']).all().delete()
            if res:
                return JsonResponse({"code":"808"})
            else:
                return JsonResponse({"code":"809"})
        except Exception as ex:
            return JsonResponse({"code":"408"})











# 加入收藏
def addCollectGift(request):
    pass







# 结算商品
def account(request):
    giftsmes = {}
    giftsmes["address_id"]=json.loads(request.body)["addressid"]
    giftsmes["userinfo_id"] = json.loads(request.body)["userid"]
    giftsmes["gifts_id"] = json.loads(request.body)["postid"]
    giftsmes["order_num"] = json.loads(request.body)["postnum"]
    maxnum=models.Gifts.objects.filter(id=giftsmes["gifts_id"]).values("store")[0]["store"]
    print(maxnum)
    if json.loads(request.body)["payStatus"]:
        if maxnum<giftsmes["order_num"]:
            return JsonResponse({"code":"111"})
        else:
            giftsmes["status_id"] = 2
    else:
        giftsmes["status_id"] = 1
    giftsmes["ordertime"] = int(time.time())
    order = models.GiftsOrder(**giftsmes)
    order.save()
    models.GiftsCart.objects.filter(gifts_id=giftsmes["gifts_id"],userinfo_id=giftsmes["userinfo_id"]).delete()
    print(order.id)
    return HttpResponse({"code": "200"})




# 礼物类型
def type(request):

    if request.method=='GET':
        try:

            # 获取所有礼物对象
            type_obj=models.GiftsType.objects.all().values('id','typename')
            # 获取所有礼物节日
            type_day=models.GiftsFestival.objects.all().values('id','dayname')

            return JsonResponse({"type_obj":list(type_obj),"type_day":list(type_day)},json_dumps_params={'ensure_ascii':False})

        except Exception as ex:
            return JsonResponse({"code":"408"})


# 按条件查询礼物
def getSelectGifts(request,dayid,objid,sortid,con,pindex):
    '''
    :param request:
    :param dayid: 节日分类
    :param objid: 礼物类型
    :param sortid: 排序
    :param con:   搜索条件
    :param pindex: 查询的课程页码
    :return: 返回符合要求的所有礼物信息
    '''

    dayid = int(dayid)
    objid = int(objid)
    sortid = int(sortid)
    pindex = int(pindex)

    pageSize = 4
    start = pageSize * (pindex - 1)
    end = pageSize * pindex
    all_con={}
    if dayid:
        all_con['day_id_id']=dayid
    if objid:
        all_con['type_id_id']=objid

    if con:
        all_con['gift_name__icontains'] = con

    result = sortRegular(sortid)

    try:
        gifts=models.Gifts.objects.filter(**all_con).order_by(result).values(
            'id','gift_name','giftImg','price','clicknum')[start:end]

        return JsonResponse({"gifts":list(gifts)},json_dumps_params={"ensure_ascii":False})
    except Exception as ex:
        return JsonResponse({"code":"408"})


# 判断排序规则
def sortRegular(sortid):
    if sortid==0:
        res='id'
    elif sortid==1:
        res='grounding'
    elif sortid==2:
        res='-grounding'
    elif sortid==3:
        res='price'
    else:
        res='-price'

    return res


# 多条件查询获取总页数
def getAllPages(request,dayid,objid,sortid,con,pindex):
    dayid = int(dayid)
    objid = int(objid)
    sortid = int(sortid)

    all_con = {}
    if dayid:
        all_con['day_id_id'] = dayid
    if objid:
        all_con['type_id_id'] = objid
    if sortid:
        pass
    if con:
        all_con['gift_name__icontains'] = con

    try:

        count = models.Gifts.objects.filter(**all_con).order_by('id').values(
            'id', 'gift_name', 'giftImg', 'price', 'clicknum').count()

        return JsonResponse({"count":count}, json_dumps_params={"ensure_ascii": False})
    except Exception as ex:
        return JsonResponse({"code":"408"})

def showOrder(request,userid,ordertype,page):
    page=int(page)
    pageSize=5
    if request.method=="GET":
        ordermes = list(
            models.GiftsOrder.objects.filter(userinfo_id=userid).values("gifts_id", "gifts__giftImg", "gifts__descr",
                                                                        "gifts__gift_name", "gifts__price", "order_num",
                                                                        "status__ststus_name", "ordertime"))
        ordlist = []
        if ordertype=="all":
            for ord in ordermes:
                ord['cart_num']=ord["order_num"]
                ord['order_status']=ord["status__ststus_name"]
                ordlist.append(ord)
        elif ordertype=="nopay":
            for ord in ordermes:
                if ord['status__ststus_name']=="待付款":
                    ord['cart_num']=ord["order_num"]
                    ord['order_status']=ord["status__ststus_name"]
                    ordlist.append(ord)
        elif ordertype=="history":
            for ord in ordermes:
                if ord["status__ststus_name"]=="已完成":
                    ord['cart_num']=ord["order_num"]
                    ord['order_status']=ord["status__ststus_name"]
                    ordlist.append(ord)
        elif ordertype=="nofinish":
            for ord in ordermes:
                if ord["status__ststus_name"]!="已完成":
                    ord['cart_num']=ord["order_num"]
                    ord['order_status']=ord["status__ststus_name"]
                    ordlist.append(ord)
        ordlist=sorted(ordlist,key=lambda order:order["ordertime"],reverse=True)
        return HttpResponse(json.dumps(ordlist[(page-1)*pageSize:page*pageSize],ensure_ascii=False))
    else:
        return HttpResponse(json.dumps({"code":"001"}))


