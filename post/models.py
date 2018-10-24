from django.db import models


from user.models import *
# Create your models here.

class Post(models.Model):
    # 自动创建一个id列，id为主键，自增长

    # 帖子标题文字
    ptitle=models.CharField(max_length=32,)

    #帖子标题图片
    ptitleimg=models.CharField(max_length=200,null=True)

    # 帖子详细内容
    pdetailcont=models.CharField(max_length=9000)

    #帖子简略内容(存储文字)
    pbriefcont=models.CharField(max_length=900)

    #帖子创建时间[存储时间戳]
    p_createtime=models.IntegerField()

    #帖子状态()
    p_status=models.SmallIntegerField(choices=((0,"不显示"),(1,"显示")) ,default=1)

    # 帖子创建者 ForeignKey :userinfo
    p_userid=models.ForeignKey(to=UserInfo,to_field='id',on_delete=models.CASCADE,default=1)

class PostReply(models.Model):
    # 自动创建一个id列，id为主键，自增长

    # 回复内容
    pReply_con=models.CharField(max_length=120)

    # 回复另一条评论的根评论
    pReply_reply=models.IntegerField(null=True)

    # 回复时间
    pReply_time=models.IntegerField()

    #回复帖子id ForeignKey :Post
    pReply_pid=models.ForeignKey(to='Post',to_field='id',on_delete=models.CASCADE)

    #回复帖子者 ForeignKey :userinfo
    pReply_uid=models.ForeignKey(to=UserInfo,to_field='id',on_delete=models.CASCADE,default=1)

    # 帖子收藏表
class PostCollect(models.Model):
    # 自动创建一个id列，id为主键，自增长

    # ForeignKey :post
    post_id=models.ForeignKey(to='Post',to_field='id',on_delete=models.CASCADE)

    # ForeignKey :UserInfo
    userinfo = models.ForeignKey(to=UserInfo, to_field='id', on_delete=models.CASCADE, default=1)

    # 礼物点赞表 GiftsThumb表
class PostThumb(models.Model):
    # ForeignKey :Gifts
    post_id = models.ForeignKey(to='Post', to_field='id', on_delete=models.CASCADE)

    # ForeignKey :UserInfo
    userinfo = models.ForeignKey(to=UserInfo, to_field='id', on_delete=models.CASCADE, default=1)

    # thumb_status_choices = ((0, "未点赞"),
    #                         (1, "点赞")
    #                         )
    #
    # # 点赞状态
    # thumb_status = models.SmallIntegerField(choices=thumb_status_choices)

# 举报类型
class PostReportType(models.Model):
# 自动创建一个id列，id为主键，自增长

# 类型名
    prTName=models.CharField(max_length=30)

# 类型描述
    prTContent=models.CharField(max_length=150)


class PostReport(models.Model):
# 自动创建一个id列，id为主键，自增长

# 举报描述
    PRContent=models.CharField(max_length=150)

# 举报状态


# 举报类型 ForeignKey :PostReportType
    PRType=models.ForeignKey(to='PostReportType',to_field='id', on_delete=models.CASCADE)

# 举报帖子的id ForeignKey :Post
    post=models.ForeignKey(to='Post',to_field='id', on_delete=models.CASCADE)

# 举报用户id  ForeignKey :UserInfo
    userinfo = models.ForeignKey(to=UserInfo, to_field='id', on_delete=models.CASCADE, default=1)
