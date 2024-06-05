import os
import shutil

import jwt
from bs4 import BeautifulSoup
from django.core.cache import cache
from django.forms import model_to_dict
import requests
from apps.users.models import User, PersonalData
from apps.users.serializes import UserSerializer
from backend import settings
from utils.FileTools import fileVerify
from utils.utils import get, json_response, post, jwt_authentication, create_jwt, put


def simple_view(request, *args, **kwargs):
    # 尝试从缓存中获取一个键
    value = cache.get('my_key')

    if value is None:
        # 如果键不存在，将其设置为一个新值
        cache.set('my_key', 'Hello, Redis!', timeout=60)  # 60秒超时
        value = cache.get('my_key')
    return json_response({'value': value})
class UsersView():
    @post
    def login(request, *args, **kwargs):
        serializer = UserSerializer.login_validate(request.data)
        if isinstance(serializer, dict):
            user = serializer['user']
            access_token = create_jwt(user, expiration_minutes=15)
            refresh_token = create_jwt(user, expiration_days=7, refresh=True)
            return json_response(message='登录成功', code=200, data={'token':access_token, 'refresh_token':refresh_token,'user_id':user.id})
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
    @put
    @jwt_authentication
    def updateUserProfile(request, *args, **kwargs):
        try:
            data = request.data;
            user = request.user
            personal_data = PersonalData.objects.get(user=user)
            UserSerializer.update_validate(personal_data,data);
            personal_data.save()
            return json_response(code=200, data=data,message='修改成功')
        except PersonalData.DoesNotExist:
            return json_response(code=404, message= '用户资料不存在')
        except Exception as e:
            return json_response(code= 500, message= f'服务器内部错误: {str(e)}')
    @get
    @jwt_authentication
    def fetch_github_repos(request, *args, **kwargs):
        user = request.user
        userInfo = PersonalData.objects.get(id=user.id)
        username = None
        if userInfo:
            url = userInfo.github
            if url:
                username = url.split('/')[-1]

        if username:
            api_url = f"https://api.github.com/users/{username}/repos"
            response = requests.get(api_url)
            if response.status_code == 200:
                repos_data = response.json()
                formatted_repos_data = []
                for repo in repos_data:
                    repo_info = {
                        "name": repo["name"],
                        "description": repo["description"] or "No description",
                        "html_url": repo["html_url"],
                        "language": repo["language"] or "N/A"
                    }
                    formatted_repos_data.append(repo_info)
                return json_response(formatted_repos_data, 200, "查询成功")
            else:
                return json_response({}, 400, "查询失败")
        return json_response({}, 400, "查询失败")
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