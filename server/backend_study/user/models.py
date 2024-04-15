from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True,null=False,blank=False,max_length=40,verbose_name="邮箱")
    avatar = models.ImageField(upload_to='avatars/',blank=True,null=True,default='avatars/default.png',verbose_name="头像")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        db_table='user'
        verbose_name = '用户登录信息表'

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="用户名")
    birthday = models.DateField(null=True,verbose_name="生日")
    signature = models.TextField(default="这个家伙很懒，什么都没留下！",verbose_name="个性签名")
    biography = models.TextField(default="这个家伙很懒，什么都没留下！",verbose_name="个人简介")
    school = models.CharField(max_length=50,verbose_name="所在学校")
    articles = models.IntegerField(default=0,verbose_name="写的文章数")
    last_login_Date = models.DateTimeField(auto_now_add=True,verbose_name="最后登录时间")
    class Meta:
        db_table='userinfo'
        verbose_name = '用户详细信息表'