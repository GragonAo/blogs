from rest_framework import serializers

from apps.articles.models import Article
from apps.users.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        read_only_fields = ('user',)  # 只读字段
        exclude = ('is_delete',)