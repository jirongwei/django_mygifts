from django.db import models

# Create your models here.

# User表
class User(models.Model):
    # 自动创建一个id列，id为主键，自增长

    # 电话号码
    telephone = models.CharField(max_length=64,unique=True)

    # 邮箱
    email = models.CharField(max_length=64,unique=True,null=True)

    # 密码
    password = models.CharField(max_length=200)

    # User注册时间[存储时间戳]
    pub_time = models.FloatField(null=True)

    # ForeignKey :Role
    role_id=models.ForeignKey(to='Role',to_field='id',on_delete=models.CASCADE,default=1)


# 存放短信验证码
class Register(models.Model):
    telephone = models.CharField(max_length=11)
    time = models.DateTimeField()
    message_code = models.CharField(max_length=8)


# User :Role表
class Role(models.Model):
    # 角色类型名
    rolename=models.CharField(max_length=16,unique=True)


# User :Gender表
class Gender(models.Model):
    # 性别类型名
    sexname=models.CharField(max_length=16,unique=True,null=True)


# User详情表
class UserInfo(models.Model):
    # 昵称
    nickname=models.CharField(max_length=64,null=True,blank=True)

    # 生日
    birthday=models.IntegerField(null=True)

    # 个性签名
    signature=models.CharField(max_length=200,null=True,blank=True)

    # 居住地
    location=models.CharField(max_length=32,null=True,blank=True)

    # 真实姓名
    username=models.CharField(max_length=32,null=True,blank=True)

    # qq
    qq=models.CharField(max_length=32,null=True,unique=True,blank=True)

    # 头像
    icon=models.CharField(max_length=200,null=True,blank=True)


    # ForeignKey :User
    user=models.ForeignKey(to='User',to_field='id',on_delete=models.CASCADE,default=1)

    # ForeignKey :Gender
    gender=models.ForeignKey(to='Gender',to_field='id',on_delete=models.CASCADE,default=1)



# User 积分表
class Integral(models.Model):
    # 积分数
    integral_num=models.SmallIntegerField(null=True,default=0)

    # ForeignKey :UserInfo
    userinfo_id=models.ForeignKey(to='UserInfo',to_field='id',on_delete=models.CASCADE,default=1)


# User 地址表
class Address(models.Model):
    # 收件人
    receiver=models.CharField(max_length=16)

    # 省
    province=models.CharField(max_length=16)

    # 市
    city=models.CharField(max_length=16)

    # 区
    area=models.CharField(max_length=16,null=True,blank=True)

    # 详细地址
    detailLocation=models.CharField(max_length=200)

    # 手机号码
    phone=models.CharField(max_length=32)

    # 邮编
    postcode=models.CharField(max_length=16,null=True,blank=True)

    # 状态
    status=models.SmallIntegerField(default=1)

    # ForeignKey :UserInfo
    user_address = models.ForeignKey(to='UserInfo', to_field='id', on_delete=models.CASCADE,default=1)