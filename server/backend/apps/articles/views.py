from django.core.serializers import serialize
from django.shortcuts import render

from apps.articles.models import Article
from apps.articles.serializes import ArticleSerializer
from utils.utils import get, json_response, post, jwt_authentication


# Create your views here.
class ArticlesView():
    @get
    def list(request, *args, **kwargs):
        articles = Article.objects.all()
        articles_json = list(articles.values())
        return json_response(data=articles_json, code=200,message='查询成功')

    @jwt_authentication
    @post
    def create(request, *args, **kwargs):
        user = request.user
        serializer = ArticleSerializer.create_validate(request.data)
        if isinstance(serializer, dict):
            Article(title=serializer['title'],content= serializer['content'],user_id=user.id).save()
        else: return json_response(message=serializer, code=400)
        return json_response(message='发布成功', code=200)

    @get
    def search(request, *args, **kwargs):
        # 获取查询字符串参数
        pass
