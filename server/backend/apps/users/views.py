from urllib.request import Request

from rest_framework import status, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import User
from apps.users.serializes import UserSerializer
from common.Result import Result


# Create your views here.
class LoginView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        ser = self.get_serializer(data=request.data)
        result = Result(code=status.HTTP_401_UNAUTHORIZED)
        if not ser.is_valid():
            result.message = ser.errors["non_field_errors"][0]
            return Response(result.to_dict(), status=status.HTTP_400_BAD_REQUEST)
        data = ser.validated_data
        data['token'] = ser.validated_data.pop('access')
        result.data = data
        result.code = status.HTTP_200_OK
        return Response(result.to_dict(), status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, request):
        ser = UserSerializer(data=request.data)
        result = Result(code=status.HTTP_400_BAD_REQUEST)
        if request.data['password_confirm'] != request.data['password']:
            result.message = "密码输入不一致"
            return Response(result.to_dict(), status=status.HTTP_400_BAD_REQUEST)
        if not ser.is_valid():
            result.message = ser.errors
            return Response(result.to_dict(), status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(username=ser.data['username'],password=ser.data['password'],mobile=ser.data['mobile'],email=ser.data['email'])
        result.data = ser.data
        result.code = status.HTTP_201_CREATED
        return Response(result.to_dict(), status=status.HTTP_201_CREATED)



class UserView(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer