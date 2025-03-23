from common.db import BaseModel
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class Users(AbstractUser, BaseModel):
    mobile = models.CharField(max_length=11, default="")
    avatar = models.ImageField(verbose_name="用户头像", blank=True, null=True)
    class Meta:
        db_table = 'users'
        verbose_name = '用户表'



class Addr(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, default="")
    name = models.CharField(max_length=20, default="")
    province = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")
    country = models.CharField(max_length=20, default="")
    address = models.TextField(default="", max_length=100)
    is_default = models.BooleanField(default=False)

    class Meta:
        db_table = 'addr'
        verbose_name = "地址表"

class Area(models.Model):
    pid = models.ImageField(max_length=11, default=0)
    name = models.CharField(max_length=20, default="")
    level = models.CharField(verbose_name="区域等级",max_length=20)
    class Meta:
        db_table = 'area'
        verbose_name = "地区"


class VerifyCode(models.Model):
    mobile = models.CharField(max_length=11, default="")
    code = models.CharField(max_length=11, default="")
    class Meta:
        db_table = 'verifyCode'
        verbose_name = "验证码"


