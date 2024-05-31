import hashlib
import os
from django.db.models import Q
from django.conf import settings
from apps.users.models import User
from utils.FaceTool import FaceTool


class ArticleSerializer:
    @staticmethod
    def create_validate(article):
        title = article.get('title')
        content = article.get('content')
        if not title or not content:
            return "所有字段都是必填项"
        return {
            "title": title,
            "content": content,
        }