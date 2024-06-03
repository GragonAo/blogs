from django.urls import path
from apps.articles import views

urlpatterns = [
    path('list/', views.ArticlesView.list),
    path('<int:articleId>/', views.ArticlesView.getArticle),
    path('create/', views.ArticlesView.create),
    path('userArticles/', views.ArticlesView.userArticles),
    path('update/<int:articleId>/', views.ArticlesView.update),
    path('delete/<int:articleId>/', views.ArticlesView.delete),
]