from django.db import models

from user.models import *

# Create your models here.

# 礼物表 Gifts表
class Gifts(models.Model):
    # 礼物名
    gift_name=models.CharField(max_length=100,null=True)

    # 礼物描述
    descr=models.CharField(max_length=200,null=True)

    # 原价格
    price=models.FloatField(default=0,null=True)

    # 现价格
    new_price=models.FloatField(default=0)


    # 库存
    store=models.SmallIntegerField(default=1,null=True)

    # 浏览量
    clicknum=models.IntegerField(default=0,null=True)

    # 上架时间
    grounding=models.FloatField(null=True)



    # 备注
    remark=models.CharField(max_length=64,null=True)

    giftId=models.CharField(max_length=64,null=True)
    giftImg=models.CharField(max_length=100,null=True)

    # 礼物小提示
    gift_tip=models.CharField(max_length=64,null=True)

    # 包装
    gift_package=models.CharField(max_length=100,null=True)


    #  ForeignKey :GiftsType
    type_id=models.ForeignKey(to='GiftsType',to_field='id',on_delete=models.CASCADE,default=1)
    day_id=models.ForeignKey(to='GiftsFestival',to_field='id',on_delete=models.CASCADE,default=1)


# 礼物类型表 GiftsType表
class GiftsType(models.Model):
    # 类型名
    typename=models.CharField(max_length=16,unique=True)



# 礼物节日表
class GiftsFestival(models.Model):
    dayname=models.CharField(max_length=64,null=True)




# 礼物购买记录表 GiftsRecord表
class GiftsRecord(models.Model):
    # 购买数量
    record_num=models.SmallIntegerField(default=1)

    # 订单完成时间
    record_date=models.FloatField()

    # ForeignKey :UserInfo
    userinfo=models.ForeignKey(to=UserInfo,to_field='id',on_delete=models.CASCADE,default=1)

    # ForeignKey :Gifts
    gifts=models.ForeignKey(to='Gifts',to_field='id',on_delete=models.CASCADE,default=1)



# 礼物订单表 GiftsOrder表
class GiftsOrder(models.Model):
    # 订单数量
    order_num=models.SmallIntegerField(default=1)

    # 下单时间
    ordertime=models.FloatField()

    # 地址id
    address_id = models.SmallIntegerField(null=True)


    # 礼物备注
    note=models.CharField(max_length=200,null=True)

    field01=models.CharField(max_length=64,null=True)

    

    # ForeignKey :UserInfo
    userinfo=models.ForeignKey(to=UserInfo,to_field='id',on_delete=models.CASCADE,default=1)

    # ForeignKey :Gifts
    gifts=models.ForeignKey(to='Gifts',to_field='id',on_delete=models.CASCADE,default=1)

    # ForeignKey :OrderStatus
    status=models.ForeignKey(to='OrderStatus',to_field='id',on_delete=models.CASCADE,default=1)






# 订单状态表 OrderStatus表
class OrderStatus(models.Model):
    # 状态
    ststus_name=models.CharField(max_length=16,unique=True)


# 购物车 GiftsCart表
class GiftsCart(models.Model):
    # 购物车数量
    cart_num=models.SmallIntegerField(default=1)

    # ForeignKey :UserInfo
    userinfo=models.ForeignKey(to=UserInfo,to_field='id',on_delete=models.CASCADE,default=1)

    # ForeignKey :Gifts
    gifts=models.ForeignKey(to='Gifts',to_field='id',on_delete=models.CASCADE,default=1)


# 礼物图片表 GiftsPic表
class GiftsPic(models.Model):
    pic_url=models.CharField(max_length=100,null=True)

    # ForeignKey :Gifts
    gifts=models.ForeignKey(to='Gifts',to_field='id',on_delete=models.CASCADE,default=1)


# 礼物收藏表 GiftsCollect表
class GiftsCollect(models.Model):
    # ForeignKey :Gifts
    gifts = models.ForeignKey(to='Gifts', to_field='id', on_delete=models.CASCADE, default=1)

    # ForeignKey :UserInfo
    userinfo = models.ForeignKey(to=UserInfo, to_field='id', on_delete=models.CASCADE, default=1)



# 礼物点赞表 GiftsThumb表
class GiftsThumb(models.Model):
    # ForeignKey :Gifts
    gifts = models.ForeignKey(to='Gifts', to_field='id', on_delete=models.CASCADE, default=1)

    # ForeignKey :UserInfo
    userinfo = models.ForeignKey(to=UserInfo, to_field='id', on_delete=models.CASCADE, default=1)

    thumb_status_choices=((0,"未点赞"),
                          (1,"点赞")
                          )

    # 点赞状态
    thumb_status=models.SmallIntegerField(choices=thumb_status_choices)


# 礼物评论表
class GiftsComment(models.Model):
    # ForeignKey :Gifts
    gifts = models.ForeignKey(to='Gifts', to_field='id', on_delete=models.CASCADE, default=1)
    # ForeignKey :UserInfo
    userinfo = models.ForeignKey(to=UserInfo, to_field='id', on_delete=models.CASCADE, default=1)
    # 评论内容
    comment=models.CharField(max_length=200,null=True)
    # 评分
    credit=models.SmallIntegerField(default=1)
    # 评论时间
    comment_time=models.FloatField(null=True)










