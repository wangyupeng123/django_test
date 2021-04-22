from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpup_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    """英雄人物类模型类"""
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别 布尔类型 default默认值
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    #  关系属性 hbook-建立图书类与英雄人物类之间一对多的关系
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)