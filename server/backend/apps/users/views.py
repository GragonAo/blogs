from urllib.request import Request

from rest_framework import status, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.models import User
from apps.users.serializes import UserSerializer
from common.Result import Result
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.authenticate import UserPermissions


# Create your views here.
class LoginView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        ser = self.get_serializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors['non_field_errors'][0], status=status.HTTP_400_BAD_REQUEST)
        data = ser.validated_data
        data['token'] = ser.validated_data.pop('access')
        data['id'] = ser.user.id;
        return Response(data, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, request):
        ser = UserSerializer(data=request.data)
        if request.data['password_confirm'] != request.data['password']:
            return Response("密码输入不一致", status=status.HTTP_400_BAD_REQUEST)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(username=ser.data['username'],password=request.data['password'],mobile=ser.data['mobile'],email=ser.data['email'])
        return Response(ser.data, status=status.HTTP_201_CREATED)

class UserView(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #设置用户认证才能访问
    permission_classes = [IsAuthenticated,UserPermissions]
    #用于处理 JSON Web Tokens (JWT) 的身份验证
    authentication_classes = [JWTAuthentication]

    def upload_avatar(self, request, *args, **kwargs):
        # 获取请求中的数据
        avatar_data = request.data.get('avatar')
        user = self.get_object()
        # 检查文件是否存在
        if not avatar_data:
            return Response("上传失败，请上传头像文件", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # 检查文件大小
        if avatar_data.size > 1024 * 500:
            return Response("上传失败，文件不允许大于300kb", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # 获取序列化器
        ser = self.get_serializer(user,data={"avatar":avatar_data}, partial=True)
        # 验证序列化器数据
        try:
            ser.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
            # 保存数据
        ser.save()
        # 返回上传后的头像URL
        return Response({'avatar': ser.data.get('avatar')}, status=status.HTTP_200_OK)
