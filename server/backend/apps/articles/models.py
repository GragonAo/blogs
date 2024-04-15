from django.db import models

from apps.users.models import User
from common.db import BaseModel

# Create your models here.
class Article(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="所属用户")
    title = models.CharField(max_length=255,verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    class Meta:
        db_table = 'articles'
        verbose_name = '文章表'
