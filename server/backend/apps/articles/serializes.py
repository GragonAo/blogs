from rest_framework import serializers

from apps.articles.models import Article
from apps.users.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('user','is_delete')