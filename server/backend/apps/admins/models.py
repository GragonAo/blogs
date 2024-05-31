from django.db import models

from apps.articles.models import Article
from apps.users.models import User


# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    content = models.TextField(verbose_name="反馈内容")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")

    class Meta:
        db_table = 'feedback'
        verbose_name = '反馈'
        verbose_name_plural = '反馈'

    def __str__(self):
        return f"Feedback by {self.user.username}"

class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews', verbose_name="文章")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="审核人")
    review_time = models.DateTimeField(auto_now_add=True, verbose_name="审核时间")
    approved = models.BooleanField(default=False, verbose_name="是否通过")

    class Meta:
        db_table = 'reviews'
        verbose_name = '审核'
        verbose_name_plural = '审核'

    def __str__(self):
        return f"{self.article.title} reviewed by {self.reviewer.username}"