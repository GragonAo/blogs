# utils.py
from datetime import datetime, timedelta
import json
import jwt
import pytz
from django.conf import settings
from apps.users.models import User
from functools import wraps
from django.http import JsonResponse

def create_jwt(user, expiration_minutes=15, expiration_days=0, refresh=False):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes=expiration_minutes, days=expiration_days),
        'iat': datetime.utcnow(),
        'refresh': refresh
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def json_response(data=None, code=401, message=None):
    return JsonResponse({
        'code': code,
        'message': message,
        'data': data
    }, status=code)

def jwt_authentication(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return json_response(code=401, message='Invalid token header')

        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return json_response(code=401, message='Token has expired')
        except jwt.InvalidTokenError:
            return json_response(code=401, message='Invalid token')

        try:
            user = User.objects.get(id=payload['user_id'])
        except User.DoesNotExist:
            return json_response(code=401, message='User not found')

        request.user = user
        return func(request, *args, **kwargs)

    return wrapper

def get(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.method != 'GET':
            return json_response(code=405, message='Method not allowed')
        return func(request, *args, **kwargs)
    return wrapper

def post(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.method != 'POST':
            return json_response(code=405, message='Method not allowed')

        # 检查是否是多部分表单数据
        if request.content_type.startswith('multipart/form-data'):
            request.data = request.FILES
        else:
            try:
                # 解析请求主体中的JSON数据
                data = json.loads(request.body.decode('utf-8'))
                request.data = data
            except json.JSONDecodeError:
                return json_response({'message': 'Invalid JSON'}, code=400)

        return func(request, *args, **kwargs)

    return wrapper

def put(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.method != 'PUT':
            return json_response(code=405, message='接口类型不一致')
        try:
            data = json.loads(request.body.decode('utf-8'))
            request.data = data
        except json.JSONDecodeError:
            return json_response({'message': 'Invalid JSON'}, code=400)
        return func(request, *args, **kwargs)
    return wrapper

def delete(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.method != 'DELETE':
            return json_response(code=405, message='Method not allowed')
        return func(request, *args, **kwargs)
    return wrapper

def shanghai_time():
    # 获取上海时区
    shanghai_tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.now(shanghai_tz)
    print(current_time)
    # 将当前时间转换为上海时间
    return current_time

