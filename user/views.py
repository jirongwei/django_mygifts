from django.http import JsonResponse,HttpResponse
import json
from datetime import datetime
import time

from qiniu import Auth
import uuid

from . import models
from utils.Tools.tools import createToken,getToken

# 将QuerySet转化为dict
from django.forms.models import model_to_dict

# 密码加密解密
from django.contrib.auth.hashers import make_password, check_password

# user首页
def index(request):
    return HttpResponse('i am user_index')

# 用户登录
def login(request):
    if request.method=='POST':
        user = json.loads(request.body)

        print(user)
        print(user['telephone'])

        # 判断用户名密码，签发token
        # 根据电话号码获取用户密码
        # 匹配用户
        get_user = models.User.objects.filter(telephone=user['telephone']).values('id', 'telephone', 'password').first()
        if get_user:
            # 解析判断密码是否正确，解析正确返回True,错误返回False
            if check_password(user['password'],get_user['password']):
                # 匹配成功;将密码删除；根据用户id生成token
                del get_user['password']
                resp = JsonResponse(get_user, status=202, charset='utf-8', content_type='application/json')
                resp['token'] = createToken(get_user['id'])
                # 将token字段添加到请求头；在setting的CORS_ALLOW_HEADERS里添加token字段：将token字段设置为服务器允许暴露给客户端访问的字段
                resp["Access-Control-Expose-Headers"] = "token"
                return resp
            else:
                # 密码匹配失败
                return JsonResponse({'code': "409"})
        else:
            # 用户未注册
            return JsonResponse({'code': "403"})


# 用户注册
def regist(request):
    if request.method=='POST':
        # 接收前端用户名/密码
        user=json.loads(request.body)
        verification_code = user['message_code']

        try:

            # 判断用户名是否存在
            exist_id = models.User.objects.filter(telephone=user['telephone']).first()
            if exist_id:
                # 用户名存在
                return JsonResponse({"code":"401"},status=200,charset='utf-8',content_type='application/json')
            else:
                result = models.Register.objects.filter(telephone=user['telephone']).values('time', 'message_code').order_by('-time')[0]

                if result['message_code']:
                    message = result['message_code']
                    register_time = result['time']
                else:
                    return JsonResponse({"statuscode": "408"})

                if str(verification_code) == message and int(time.mktime(datetime.now().timetuple())) - int(time.mktime(register_time.timetuple())) < 60:
                    user['password'] = make_password(user['password'])  # 密码进行加密

                    res = models.User.objects.create(telephone=user['telephone'],password=user['password'],role_id_id=1)
                    if res:
                        # 注册成功
                        # 签发token
                        resp = JsonResponse({"code":"202","id":res.id},status=200,charset='utf-8',content_type='application/json')

                        resp['token'] = createToken(res.id)
                        resp['Access-Control-Expose-Headers'] = "token"
                        return resp
                    else:
                        # 注册失败
                        return JsonResponse({"code": "410"}, status=200, charset='utf-8', content_type='application/json')
                else:
                    return JsonResponse({"statuscode": "407"})


        except Exception as ex:
            # 服务异常
            return JsonResponse({"code": "410"}, status=200, charset='utf-8', content_type='application/json')


# 根据id判断用户是否存在
def getUserById(request,id):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')

        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    # 判断该用户是否存在
                    res = models.User.objects.filter(telephone=id).first()
                    if res:
                        return JsonResponse({"code": "808"})
                    else:
                        return JsonResponse({"code": "403"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})

# 获取短信验证码
def sendMessage(request,user_telephone):
    import random
    import http.client
    import urllib.parse,hashlib

    if request.method == "GET":
        # 匹配用户
        get_user = models.User.objects.filter(telephone=user_telephone)
        if len(get_user) == 0:
            # 定义账号和密码，开户之后可以从用户中心得到这两个值
            accountSid = '81cd0c133cde4617a5bdef1dd2850918'
            acctKey = '04a80c1ee4c9408bb4d1eb18d92a87b5'

            # 定义地址，端口等
            serverHost = "api.miaodiyun.com"
            serverPort = 443
            industryUrl = "/20150822/industrySMS/sendSMS"

            # 生成随机数
            message = random.randrange(1000, 9999)
            # 格式化时间戳，并计算签名
            timeStamp = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
            rawsig = accountSid + acctKey + timeStamp
            m = hashlib.md5()
            m.update(str(rawsig).encode('utf-8'))
            sig = m.hexdigest()
            params = urllib.parse.urlencode({'accountSid': accountSid,
                                             'smsContent': "【左心房】尊敬的用户，欢迎您注册左心房平台，您的验证码为{0}".format(message),
                                             'to': user_telephone,
                                             'timestamp': timeStamp,
                                             'sig': sig})
            # 定义header
            headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}

            # 与构建https连接
            conn = http.client.HTTPSConnection(serverHost, serverPort)

            # Post数据
            conn.request(method="POST", url=industryUrl, body=params, headers=headers)
            # 返回处理后的数据
            response = conn.getresponse()
            models.Register.objects.create(telephone=user_telephone, message_code=message, time=datetime.now())
            # 读取返回数据
            jsondata = response.read().decode('utf-8')
            # 解析json，获取特定的几个字段
            jsonObj = json.loads(jsondata)
            respCode = jsonObj['respCode']
            print("错误码:", respCode)
            respDesc = jsonObj['respDesc']
            print("错误描述:", respDesc)
            # 关闭连接
            conn.close()

            return JsonResponse({'code': "202"})
        else:
            return JsonResponse({'code': "408"})
    else:
        return JsonResponse({'code': "409"})


# 获取用户基本信息
def getUserInfo(request):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')
        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:

                    # 获取登录用户基本信息
                    userMsg = models.UserInfo.objects.filter(id=user_id).values('user__telephone', 'nickname',
                                                                                'user__email',
                                                                                'gender__id', 'location', 'username',
                                                                                'signature', 'qq')

                    return JsonResponse({"userMsg": list(userMsg)}, json_dumps_params={"ensure_ascii": False})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})
        else:
            return JsonResponse({"code": "409"})


# 修改用户基本信息
def updateMsg(request):
    if request.method == 'POST':
        update_msg = json.loads(request.body)
        user_token = request.META.get('HTTP_TOKEN')

        if user_token:
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                # 根据token解析用户id
                try:
                    # 获取用户email
                    res = models.User.objects.filter(id=user_id).update(email=update_msg['email'])
                    obj_info = models.UserInfo.objects.filter(user_id=user_id).update(nickname = update_msg['nickname'],gender_id = int(update_msg['gender_id']),
                                                                                      location = update_msg['location'],signature = update_msg['signature'],
                                                                                      username = update_msg['username'],qq = update_msg['qq'])
                    if obj_info:
                        return JsonResponse({"code":"808"})
                    else:
                        return JsonResponse({"code": "401"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})
        else:
            return JsonResponse({"code": "410"})


# 修改密码
def updatePassword(request):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')
        updateMsg =json.loads(request.body)

        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    # 获取当前用户密码
                    user_pwd = models.User.objects.get(id=user_id).password
                    if check_password(updateMsg['old_pwd'],user_pwd):
                        res = models.User.objects.filter(id=user_id).update(password=make_password(updateMsg['new_pwd']))
                        print(res)
                        if res:
                            return JsonResponse({"code": "808"})
                        else:
                            return JsonResponse({"code": "403"})
                    else:
                        return JsonResponse({"code": "401"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})
        else:
            return JsonResponse({"code": "410"})


# 绑定手机号
def bindPhone(request):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')
        bindMsg =json.loads(request.body)
        print(bindMsg)

        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    userPwd = models.User.objects.get(id=user_id).password
                    if check_password(bindMsg['old_pwd'],userPwd):

                        verification_code = bindMsg['phone_code']
                        result = models.Register.objects.filter(telephone=bindMsg['new_telephone']).values('time', 'message_code').order_by('-time')[0]

                        if result['message_code']:
                            message = result['message_code']
                            register_time = result['time']
                        else:
                            return JsonResponse({"statuscode": "408"})

                        if str(verification_code) == message and int(time.mktime(datetime.now().timetuple())) - int(
                                time.mktime(register_time.timetuple())) < 60:
                            # 修改当前绑定手机号
                            res = models.User.objects.filter(id=user_id).update(telephone=bindMsg['new_telephone'])
                            if res:
                                return JsonResponse({"statuscode": "808"})  # 修改成功
                            else:
                                return JsonResponse({"statuscode": "403"})  # 修改失败
                        else:
                            return JsonResponse({"statuscode": "802"})  # 短信验证码过期
                    else:
                        return JsonResponse({"statuscode": "801"})  # 密码错误
                except Exception as ex:
                    return JsonResponse({"code": "408"})    # 服务异常
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})



        if str(verification_code) == message and int(time.mktime(datetime.now().timetuple())) - int(
                time.mktime(register_time.timetuple())) < 60:
            user['password'] = make_password(user['password'])  # 密码进行加密

            res = models.User.objects.create(telephone=user['telephone'], password=user['password'], role_id_id=1)
            if res:
                # 注册成功
                # 签发token
                resp = JsonResponse({"code": "202", "id": res.id}, status=200, charset='utf-8',
                                    content_type='application/json')

                resp['token'] = createToken(res.id)
                resp['Access-Control-Expose-Headers'] = "token"
                return resp
            else:
                # 注册失败
                return JsonResponse({"code": "410"}, status=200, charset='utf-8', content_type='application/json')
        else:
            return JsonResponse({"statuscode": "407"})

# 获取用户所有地址
def getAllAddress(request):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')

        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    # 获取当前用户地址
                    user_address = models.Address.objects.filter(user_address_id=user_id).all().values()
                    if user_address:
                        return JsonResponse({"address":list(user_address)},json_dumps_params={"ensure_ascii":False})
                    else:
                        return JsonResponse({"code": "401"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})


# 用户添加地址
def addAddr(request):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')

        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                addMsg = json.loads(request.body)
                print(addMsg)
                try:
                    # 根据用户id添加地址
                    res = models.Address.objects.filter(user_address_id=user_id).create(**addMsg)
                    if res:
                        return JsonResponse({"code":"808"})
                    else:
                        return JsonResponse({"code": "403"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})


# 用户头像上传，通过图片名称，返回七牛token和图片名称
def sendToken(request):
    # import

    if request.method == 'GET':
        access_key = 'FWK-lVOxt6VsWtxTl75B8efU3_-OOc8f-bjDp8p9'
        secret_key = 'W0orBmFERBkbwTjsqAdhjoS-bhOuU9hfC7sSVK58'
        # 构建鉴权对象
        q = Auth(access_key, secret_key)
        # 要上传的空间
        bucket_name = 'giftsapp'
        # 上传到七牛后保存的文件名
        key = str(uuid.uuid4()) + '.' + str(request.GET.get('key')).split('.')[-1]
        # 生成上传 Token，可以指定过期时间等 一天
        token = q.upload_token(bucket_name, key, 3600)
        return JsonResponse({"token": token, "filename": key})


# 给你一个图片名，将图片名存到头像表中，并且把当前用户的头像id改为新头像id
def getIconUrl(request,url):

    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')

        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    # 将图片名存到头像表中
                    icon_url = {"iconurl":url}
                    res = models.myicon.objects.create(**icon_url)
                    if res:
                        icon_id = models.myicon.objects.get(iconurl=url).id
                        # 当前用户的头像id改为新头像id
                        result = models.UserInfo.objects.filter(id=user_id).update(icons_id=icon_id)
                        if result:
                            return JsonResponse({"code": "808"})
                        else:
                            return JsonResponse({"code": "403"})

                    else:
                        return JsonResponse({"code": "403"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})


# 获取当前用户头像
def getUserIcon(request):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')

        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    # 获取用户头像id
                    res = models.UserInfo.objects.get(id=user_id).icons_id
                    if res:
                        icons_url = models.myicon.objects.filter(id=res).values('iconurl')
                        if icons_url:
                            return JsonResponse({"icons_url":list(icons_url)},json_dumps_params={"ensure_ascii":False})
                        else:
                            return JsonResponse({"code": "403"})

                    else:
                        return JsonResponse({"code": "403"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})


 # 获取当前登录用户的头像，昵称，积分
def getLoginUser(request):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')

        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    # 获取用户头像、昵称、积分
                    login_user = models.UserInfo.objects.filter(id=user_id).values('icons__iconurl','nickname','integral__integral_num')
                    if login_user:

                        return JsonResponse({"login_user":list(login_user)},json_dumps_params={"ensure_ascii":False})
                    else:
                        return JsonResponse({"code": "403"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})


# 获取修改该地址的信息
def updateAddr(request,addrid):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')

        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    # 获取该地址信息
                    addrid = int(addrid)
                    update_addr = models.Address.objects.filter(id=addrid,user_address_id=user_id).values('receiver','province','city','area','detailLocation','phone','postcode')
                    if update_addr:
                        return JsonResponse({"update_addr":list(update_addr)},json_dumps_params={"ensure_ascii":False})
                    else:
                        return JsonResponse({"code": "403"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})


# 修改地址
def updateAddress(request,addrid):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')
        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    # 获取该地址信息
                    addrid = int(addrid)
                    updateMsg = json.loads(request.body)
                    update_addr = models.Address.objects.filter(id=addrid,user_address_id=user_id).update(receiver=updateMsg['receiver'],province=updateMsg['province'],
                                                                                                          city=updateMsg['city'],area=updateMsg['area'],detailLocation=updateMsg['detailLocation'],
                                                                                                          phone=updateMsg['phone'],postcode=updateMsg['postcode'])
                    if update_addr:
                        return JsonResponse({"code": "808"})
                    else:
                        return JsonResponse({"code": "403"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})

# 删除地址
def delAddr(request,addrid):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')
        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                try:
                    # 获取该地址信息
                    addrid = int(addrid)
                    res = models.Address.objects.filter(id=addrid,user_address_id=user_id).delete()
                    if res:
                        return JsonResponse({"code": "808"})
                    else:
                        return JsonResponse({"code": "403"})
                except Exception as ex:
                    return JsonResponse({"code": "408"})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})

# 顶部导航Cart
def cartAuth(request):
    if request.method == 'POST':
        user_token = request.META.get('HTTP_TOKEN')
        if user_token:
            # 根据token解析用户id
            my_token = getToken(user_token)
            if my_token:
                user_id = my_token['user_id']
                return JsonResponse({"user_id": user_id})
            else:
                return JsonResponse({"code": "410"})

        else:
            return JsonResponse({"code": "410"})




# 根据token获取id
def getUserbyToken(request):
    if request.method == 'POST':
        try:
            userid = json.loads(request.body)["token"]
            # result = models.User.objects.filter(telephone=id)  # 返回的是对象列表

            usermes=models.UserInfo.objects.filter(id=userid).values("id","nickname","icon")[0]
            usemes={
                "userid":usermes["id"],
                "usernickname":usermes["nickname"],
                "userimg":usermes["icon"]
            }
            print(usemes)
            return JsonResponse(usemes, safe=False, json_dumps_params={"ensure_ascii": False})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "408"})

    elif request.methd == 'GET':
        return JsonResponse({"code": "409"})


def getaddr(request):
    userid=json.loads(request.body)["userid"]
    addrmes=list(models.Address.objects.filter(user_address_id=userid).values("id","receiver","phone","province","city","area","detailLocation","status"))
    return JsonResponse(addrmes, safe=False, json_dumps_params={"ensure_ascii": False})


