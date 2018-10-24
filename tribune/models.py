from django.db import models

# Create your models here.

from user.models import *

class Tribune(models.Model):
    # 自动创建一个id列，id为主键，自增长

    # 攻略标题信息
    ttitle = models.CharField(max_length=32)

    # 攻略标题图片
    ttitleimg = models.CharField(max_length=200, null=True)

    # 攻略详细内容
    tdetailcont = models.CharField(max_length=9000)

    # 功略内容(存储文字)
    tbriefcont=models.CharField(max_length=900)

    # 攻略创建时间[存储时间戳]
    t_createtime=models.IntegerField()

    # 攻略创建者 ForeignKey :userinfo
    t_userid = models.ForeignKey(to=UserInfo, to_field='id', on_delete=models.CASCADE, default=1)

class TribuneReply(models.Model):
    # 自动创建一个id列，id为主键，自增长

    # 回复内容
    tReply_con = models.CharField(max_length=120)

    # 回复时间
    tReply_time=models.IntegerField()

    # 回复攻略id ForeignKey :Tribune
    tReply_pid = models.ForeignKey(to='Tribune', to_field='id', on_delete=models.CASCADE)

    # 回复攻略者 ForeignKey :userinfo
    tReply_uid=models.ForeignKey(to=UserInfo,to_field='id',on_delete=models.CASCADE,default=1)

    # 攻略收藏表
class TribuneCollect(models.Model):
    # 自动创建一个id列，id为主键，自增长

    # ForeignKey :tribune
    tribune_id = models.ForeignKey(to='Tribune', to_field='id', on_delete=models.CASCADE)

    # ForeignKey :UserInfo
    userinfo = models.ForeignKey(to=UserInfo, to_field='id', on_delete=models.CASCADE, default=1)

class TribuneThumb(models.Model):
    # ForeignKey :Tribune
    tribune_id = models.ForeignKey(to='Tribune', to_field='id', on_delete=models.CASCADE)

    # ForeignKey :UserInfo
    userinfo = models.ForeignKey(to=UserInfo, to_field='id', on_delete=models.CASCADE, default=1)


