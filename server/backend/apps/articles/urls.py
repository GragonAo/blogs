from django.urls import path

from apps.articles import views

urlpatterns = [
    path('list/', views.ArticlesView.list),
    # path('<int:pk>/', views.ArticlesView.),
    path('create/', views.ArticlesView.create),
    path('search/', views.ArticlesView.search),
    # path('update/', views.UsersView.userinfo),
    # path('delete/<int:pk>/', views.UsersView.userinfo),
]