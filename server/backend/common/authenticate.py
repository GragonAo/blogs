from tokenize import TokenError
from urllib.request import Request

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from apps.users.models import User
from common.Result import Result


class LoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username)|Q(mobile=username))
        except:
            raise serializers.ValidationError("未找到该用户")
        else:
            if user.check_password(password):
                return user
            else:
                raise serializers.ValidationError("密码错误")


class RefreshTokenView(TokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        result = Result(code=status.HTTP_401_UNAUTHORIZED)
        if not serializer.is_valid():
            result.message = serializer.errors
            return Response(result.to_dict(), status=status.HTTP_401_UNAUTHORIZED)
        result.code = status.HTTP_200_OK
        result.data = {"token": serializer.validated_data.pop('access')}
        return Response(result.to_dict(), status=status.HTTP_200_OK)


class VerifyTokenView(TokenVerifyView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        result = Result(code=status.HTTP_401_UNAUTHORIZED)
        if not serializer.is_valid():
            result.message = serializer.errors
            return Response(result.to_dict(), status=status.HTTP_401_UNAUTHORIZED)
        result.code = status.HTTP_200_OK
        result.data = {"token": request.data["token"]}
        return Response(result.to_dict(), status=status.HTTP_200_OK)
