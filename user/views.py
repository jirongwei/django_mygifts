from django.http import JsonResponse,HttpResponse
import json
from datetime import datetime
import time

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
   pass

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
                                             'smsContent': "【苏州驰星】尊敬的用户，您的验证码为{0}".format(message),
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




