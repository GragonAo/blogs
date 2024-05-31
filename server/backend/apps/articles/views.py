from django.core.serializers import serialize
from django.shortcuts import render

from apps.articles.models import Article
from apps.articles.serializes import ArticleSerializer
from utils.smart_search import search
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
        query_list = request.GET.getlist('query')
        # 过滤掉空字符串
        query_list = [q for q in query_list if q]

        if not query_list:
            return json_response(code=400,message= '查询参数不能为空')
        # 组合所有查询字符串，假设使用 OR 操作符组合查询条件
        query_str = " OR ".join(query_list)
        articles = search(query_str)
        articles_json = []
        if len(articles) > 0:
            articles_json = list(articles.values())
        return json_response(data=articles_json,code=200,message='查询成功')
