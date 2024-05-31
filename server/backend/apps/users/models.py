from django.db import models

from utils.db import BaseModel


# Create your models here.
class User(BaseModel):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=11, unique=True)
    avatar = models.ImageField(upload_to='static/avatar/', blank=True, null=True,default='static/avatar/default.jpg')
    face = models.CharField(max_length=100,verbose_name="人脸")
    class Meta:
        db_table = 'users'
        verbose_name = '用户表'

class PersonalData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="所属用户")
    school = models.CharField(max_length=100, verbose_name="学校", blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name="地址", blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name="城市", blank=True, null=True)
    state = models.CharField(max_length=50, verbose_name="省份", blank=True, null=True)
    zip = models.CharField(max_length=10, verbose_name="邮编", blank=True, null=True)
    age = models.IntegerField(verbose_name="年龄", blank=True, null=True)
    hobbies = models.CharField(max_length=100, verbose_name="爱好", blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    github = models.URLField(blank=True, null=True, verbose_name="GitHub")
    degree = models.CharField(max_length=50, verbose_name="学位", blank=True, null=True)
    major = models.CharField(max_length=50, verbose_name="专业", blank=True, null=True)
    graduation_year = models.IntegerField(verbose_name="毕业年份", blank=True, null=True)
    company_name = models.CharField(max_length=100, verbose_name="公司名称", blank=True, null=True)
    job_title = models.CharField(max_length=100, verbose_name="职位", blank=True, null=True)
    job_description = models.TextField(verbose_name="工作描述", blank=True, null=True)
    skills = models.CharField(max_length=200, verbose_name="技能", blank=True, null=True)
    certificates = models.CharField(max_length=200, blank=True, null=True, verbose_name="证书")
    languages = models.CharField(max_length=100, verbose_name="语言能力", blank=True, null=True)

    class Meta:
        db_table = 'personal_data'
        verbose_name = '个人资料'
        verbose_name_plural = '个人资料'

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name="发送者")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', verbose_name="接收者")
    content = models.TextField(verbose_name="内容")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="发送时间")
    read = models.BooleanField(default=False, verbose_name="已读")

    class Meta:
        db_table = 'messages'
        verbose_name = '消息'
        verbose_name_plural = '消息'