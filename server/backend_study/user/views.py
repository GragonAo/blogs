# Create your views here.
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics

from user.models import User, UserInfo
from user.serializers import UserSerializer, UserInfoSerializer


@api_view(['POST'])
def login(request):
    # 从请求数据中获取用户名和密码
    username = request.data.get('username')
    password = request.data.get('password')
    # 使用Django的authenticate函数验证凭据
    user = authenticate(request, username=username, password=password)
    if user is not None:
        ser = UserSerializer(user)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        # 如果用户不存在或凭据不正确，返回错误响应
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def register(request):
    ser = UserSerializer(data=request.data)
    if(ser.is_valid()):
        user_obj = ser.save()
        UserInfo.objects.create(user=user_obj)
        return  Response(ser.data,status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class Users(GenericAPIView,mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def put(self, request,*args,**kwargs):
        return self.put(request,*args,**kwargs)

class UserInfos(generics.CreateAPIView,
                generics.ListAPIView,
                generics.RetrieveAPIView,
                generics.UpdateAPIView,):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer