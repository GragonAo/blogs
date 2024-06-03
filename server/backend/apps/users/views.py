import os
import shutil

import jwt
from django.forms import model_to_dict

from apps.users.models import User, PersonalData
from apps.users.serializes import UserSerializer
from backend import settings
from utils.FileTools import fileVerify
from utils.utils import get, json_response, post, jwt_authentication, create_jwt


@post
def simple_view(request, *args, **kwargs):
    return json_response({'message': 'Hello, world!'})
class UsersView():
    @post
    def login(request, *args, **kwargs):
        serializer = UserSerializer.login_validate(request.data)
        if isinstance(serializer, dict):
            user = serializer['user']
            access_token = create_jwt(user, expiration_minutes=15)
            refresh_token = create_jwt(user, expiration_days=7, refresh=True)
            return json_response(message='登录成功', code=200, data={'token':access_token, 'refresh_token':refresh_token})
        else:
            return json_response(message=serializer, code=400)

    @post
    def register(request, *args, **kwargs):
        serializer = UserSerializer.register_validate(request.data)
        if isinstance(serializer, dict):
            user = User(
                username=serializer['username'],
                email=serializer['email'],
                password=serializer['password'],
                mobile=serializer['mobile'])
            user.save()
            PersonalData.objects.create(user=user)
            return json_response(message='注册成功', code=200)
        else:
            return json_response(message=serializer, code=400)

    @get
    @jwt_authentication
    def userinfo( request, *args, **kwargs):
        user = request.user
        user_data = {
            'username': user.username,
            'email': user.email,
            'mobile': user.mobile,
            'avatar': user.avatar.url if user.avatar else None,
        }
        return json_response(message='用户信息获取成功', code=200, data=user_data)
    @get
    @jwt_authentication
    def userProfile(request, *args, **kwargs):
        user = request.user
        userProfile = PersonalData.objects.get(id=user.id)
        user_profile_data = model_to_dict(userProfile, exclude=['user', 'id'])
        return json_response(message='用户信息获取成功', code=200, data=user_profile_data)
    @post
    def refresh_token(request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')
        try:
            payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
            if payload.get('refresh'):
                user_id = payload['user_id']
                user = User.objects.get(id=user_id)
                access_token = create_jwt(user, expiration_minutes=15)
                return json_response(message='Token刷新成功', code=200, access_token=access_token)
            else:
                return json_response(message='无效的刷新令牌', code=400)
        except jwt.ExpiredSignatureError:
            return json_response(message='刷新令牌已过期', code=400)
        except jwt.InvalidTokenError:
            return json_response(message='无效的刷新令牌', code=400)

    @post
    @jwt_authentication
    def upload_avatar( request, *args, **kwargs):
        user =request.user
        upload_dir = 'static/avatar'  # 替换为实际的上传目录
        res = fileVerify ('avatar', upload_dir,file_data=request.data['avatar'], max_size=1024 * 2000, compress=True, quality=75)
        if (res['code'] == 200):
            data = res['data']
            User.objects.update_or_create(id=user.id, defaults={'avatar': data['avatar']});
        print(data)
        return json_response(data=res['data'], code=res['code'],message=res['message'])

    @post
    @jwt_authentication
    def upload_face( request, *args, **kwargs):
        user = request.user
        upload_dir = os.path.join('file/face/',str(user.id)) # 替换为实际的上传目录
        if os.path.exists(upload_dir):
            shutil.rmtree(upload_dir)
        if 'faces' not in request.FILES:
            return json_response(message='No face files provided', code=400)
        for face in request.FILES.getlist('faces'):
            res = fileVerify('face', upload_dir, file_data=face, max_size=1024 * 1000)
            if (res['code'] == 200):
                data = res['data']
                User.objects.update_or_create(id=user.id, defaults={'face': data['face']})
        return json_response(message=res['message'], data=res['data'], code=res['code'])