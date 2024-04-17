from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.articles.views import ArticleViewSet  # 确保这里导入了正确的 ArticleViewSet

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='article')

urlpatterns = [
    # ... 其他 URL 配置 ...
    path('', include(router.urls)),
]