from django.urls import path

from apps.files import views

urlpatterns = [
    path('upload/img/', views.FileView.upload_image),
]