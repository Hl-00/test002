# from datetime import timezone

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    root = models.CharField(max_length=2)
    is_show = models.CharField(default='flase', max_length=10)

# class Electric_meter(models.Model):
#     start_numbering = models.CharField(max_length=32)
#     stop_numbering = models.CharField(max_length=32)
#     model = models.CharField(max_length=100)
#     factory = models.CharField(max_length=32)
#     date = models.DateTimeField(auto_now = True)
#     years = models.CharField(max_length=32)
#     cycle = models.CharField(max_length=32)
#     appraiser = models.CharField(max_length=32)
#     appraisal_date = models.DateTimeField(auto_now = True)


class meter(models.Model):
    start_numbering = models.CharField(max_length=32)
    stop_numbering = models.CharField(max_length=32)
    model = models.CharField(max_length=100)
    factory = models.CharField(max_length=32)
    date = models.DateTimeField(default = timezone.now)
    years = models.CharField(max_length=32)
    cycle = models.CharField(max_length=32)
    appraiser = models.CharField(max_length=32)
    appraisal_date = models.DateTimeField(default = timezone.now)
    is_show = models.CharField(default='flase',max_length=10)


class inventory(models.Model):
    inventory_number = models.CharField(max_length=32) #货物编号
    inventory_model = models.CharField(max_length=32) #货物型号
    number = models.CharField(max_length=10) #数量
    date = models.DateTimeField(default=timezone.now) #出库时间
    univalent = models.CharField(max_length=10) #单价
    order_number = models.CharField(max_length=32) #订单号
    amount = models.CharField(max_length=32) # 金额
    operating_user = models.CharField(max_length=32) #操作人


