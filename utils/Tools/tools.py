from datetime import datetime,timedelta
import jwt
SECRET_KEY = 'leftheart.com'

# 生成token
def createToken(user_id):
    # 生成token
    datetimeInt = datetime.utcnow() + timedelta(hours=1)
    option = {
        'iss': 'jobapp.com',  # token 的签发者
        'exp': datetimeInt,  # 过期时间
        'aud': 'webkit',  # token的接受者
        'user_id': user_id  # 放入用户信息，唯一标识，解析后可以使用该消息
    }
    token = jwt.encode(option, SECRET_KEY, 'HS256').decode()
    return token


# 解析token
def getToken(token):
    decode_token = ''
    try:
        decode_token = jwt.decode(token,SECRET_KEY,audience='webkit', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        print('Error')
    except Exception as ex:
        print(ex)
    return decode_token

# 密码加密示例
# from werkzeug.security import check_password_hash,generate_password_hash
# 加密
# user_password = generate_password_hash(明文,method='pbkdf2:sha1:2000',salt_length=8)
# 检查
# check_password_hash(密文,明文):