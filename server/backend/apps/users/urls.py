from django.urls import path

from apps.users import views

urlpatterns = [
    path('simple/', views.simple_view),
    path('login/', views.UsersView.login),
    path('register/', views.UsersView.register),
    path('userinfo/', views.UsersView.userinfo),
    path('userProfile/', views.UsersView.userProfile),
    path('upload/avatar/', views.UsersView.upload_avatar),
    path('upload/face/', views.UsersView.upload_face),
    path('gethub/', views.UsersView.fetch_github_repos),
]