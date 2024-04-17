
from django.urls import path
from apps.users import views
from common.authenticate import RefreshTokenView, VerifyTokenView

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('token/refresh/', RefreshTokenView.as_view()),
    path('token/verify/', VerifyTokenView.as_view()),
    path('<int:pk>/', views.UserView.as_view({'get':'retrieve'})),
    path('<int:pk>/avatar/upload/', views.UserView.as_view({'post': 'upload_avatar'}), name='avatar-upload')
]