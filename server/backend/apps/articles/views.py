from datetime import datetime

import pytz
from django.forms import model_to_dict
from django.utils import timezone
from django.utils.timezone import make_aware

from apps.articles.models import Article
from apps.articles.serializes import ArticleSerializer
from utils.utils import get, json_response, post, jwt_authentication, put, delete, shanghai_time


class ArticlesView():
    @get
    def list(request, *args, **kwargs):
        articles = Article.objects.all().order_by('-update_time')
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
    @jwt_authentication
    def userArticles(request, *args, **kwargs):
        try:
            user = request.user
            articles = Article.objects.filter(user_id=user.id).order_by('-update_time')
            user_profile_data = [model_to_dict(article) for article in articles]
            return json_response(data=user_profile_data,code=200,message="获取成功")
        except Exception as e:
            return json_response(message=str(e), code=400)
    @get
    def getArticle(request, *args, **kwargs):
        try:
            articleId = kwargs.get('articleId')
            article = Article.objects.get(id=articleId)
            article_data = model_to_dict(article)
            article_data['create_time'] = article.create_time
            article_data['update_time'] = article.update_time
            return json_response(data=article_data,code=200,message="获取成功")
        except Exception as e:
            return json_response(message="获取失败\n"+str(e), code=400)
    @put
    @jwt_authentication
    def update(request, *args, **kwargs):
        user = request.user
        articleId = kwargs.get('articleId')
        serializer = ArticleSerializer.create_validate(request.data)
        if isinstance(serializer, dict):
            try:
                article = Article.objects.get(id=articleId)
                if article.user_id != user.id:
                    return json_response(message="该用户没有权限修改", code=400)
                article.title = serializer['title']
                article.content = serializer['content']
                article.save()
                return json_response( message='文章修改成功', code=200)
            except Exception as e:
                return json_response(message= '文章修改错误:'+str(e), code=404)
        else:
            return json_response(message=serializer, code=400)
    @delete
    @jwt_authentication
    def delete(request, *args, **kwargs):
        user = request.user
        try:
            articleId = kwargs.get('articleId')
            article = Article.objects.get(id=articleId)
            if(user.id != article.user_id):
                return json_response(message="该用户没有权限删除", code=400)
            article.delete()
            return json_response(message="删除成功",code=200)
        except Exception as e:
            return json_response(message=str(e), code=400)
