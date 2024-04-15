from django.urls import path
from user import views
from user.views import Users, UserInfos

#配置路由规则
urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('users/',Users.as_view()),
    path('userinfos/',UserInfos.as_view()),
]
