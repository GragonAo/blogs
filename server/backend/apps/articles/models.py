from django.db import models
from apps.users.models import User
from utils.db import BaseModel
import spacy

# 加载spaCy模型
nlp = spacy.load('zh_core_web_sm')

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="分类名称")

    class Meta:
        db_table = 'categories'
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="标签名称")

    class Meta:
        db_table = 'tags'
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Article(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所属用户")
    title = models.CharField(max_length=255, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    likes = models.PositiveIntegerField(default=0, verbose_name="点赞数")
    views = models.PositiveIntegerField(default=0, verbose_name="访问数")
    comments_count = models.PositiveIntegerField(default=0, verbose_name="评论数")
    shares = models.PositiveIntegerField(default=0, verbose_name="分享数")
    categories = models.ManyToManyField(Category, related_name="articles", verbose_name="分类")
    tags = models.ManyToManyField(Tag, related_name="articles", verbose_name="标签")

    class Meta:
        db_table = 'articles'
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def generate_tags(self):
        doc = nlp(self.content)
        tags = set(ent.text for ent in doc.ents)
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            self.tags.add(tag)


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments", verbose_name="文章")
    content = models.TextField(verbose_name="评论内容")
    likes = models.PositiveIntegerField(default=0, verbose_name="点赞数")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies', verbose_name="父评论")

    class Meta:
        db_table = 'comments'
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __str__(self):
        return f"Comment by {self.user.username} on {self.article.title}"