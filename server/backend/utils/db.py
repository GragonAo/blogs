from datetime import datetime

import pytz
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    is_delete = models.BooleanField(default=False,verbose_name='删除标记') #逻辑删除

    def save(self, *args, **kwargs):
        shanghai_tz = pytz.timezone('Asia/Shanghai')
        if not self.id:
            self.create_time = datetime.now(shanghai_tz)
        self.update_time = datetime.now(shanghai_tz)
        super(BaseModel, self).save(*args, **kwargs)
    class Meta:
        abstract = True #声明这是一个抽象的模型，在执行牵引文件的时候不会在数据中生成表
        verbose_name_plural = '公共字段表'
        db_table = 'BaseTable'