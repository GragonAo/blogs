from django.db import models
from django.contrib.auth.models import AbstractUser
from common.db import BaseModel


# Create your models here.

class User(AbstractUser,BaseModel):
    mobile = models.CharField(max_length=11, unique=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True,default='static/avatar/default.jpg')
    class Meta:
        db_table = 'users'
        verbose_name = '用户表'
class VerifyCode(BaseModel):
    mobile = models.CharField(max_length=11, unique=True,verbose_name="手机号")
    code = models.CharField(max_length=11, unique=True,verbose_name="验证码")
    class Meta:
        db_table = 'verify_codes'
        verbose_name="手机验证码表"