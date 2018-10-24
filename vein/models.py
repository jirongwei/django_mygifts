from django.db import models

# Create your models here.


# vein 申请表
class Apply(models.Model):
    # 申请人
    inviter=models.SmallIntegerField()

    # 被申请人
    binviter=models.SmallIntegerField()

    # 申请日期
    apply_time=models.IntegerField()

    # 回复日期
    replay=models.IntegerField(null=True)

    field01=models.CharField(max_length=64,null=True)
    field02=models.CharField(max_length=64,null=True)
    field03=models.CharField(max_length=64,null=True)

    # ForeignKey :TagStatus
    status_id=models.ForeignKey(to='TagStatus',to_field='id',on_delete=models.CASCADE,default=1)

    # ForeignKey :TagRelation
    relation_id=models.ForeignKey(to='TagRelation',to_field='id',on_delete=models.CASCADE,default=1)



# vein TagStatus表
class TagStatus(models.Model):
    # 申请状态
    status=models.CharField(max_length=16,unique=True)


# vein TagRelation表
class TagRelation(models.Model):
    # 关系类型
    relation=models.CharField(max_length=16,unique=True)

