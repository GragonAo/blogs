from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.articles.models import Article
from apps.articles.serializes import ArticleSerializer
from common.authenticate import UserPermissions
from django.contrib.auth import get_user_model

User = get_user_model()


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JWTAuthentication]
    def get_serializer_context(self):
        # 添加用户到序列化器上下文，以便在序列化时可以使用
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @permission_classes([IsAuthenticated, UserPermissions])
    def create(self, request, *args, **kwargs):
        try:
            ser = self.get_serializer(data=request.data)
            if(ser.is_valid()):
                # 获取当前登录用户
                user = request.user
                # 创建文章实例，并将用户关联到文章
                ser.save(user=user)
                headers = self.get_success_headers(ser.data)
                return Response(ser.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as e:
            print(e)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    @permission_classes([IsAuthenticated, UserPermissions])
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if getattr(instance, '_prefetched_objects_cache', None):
            # 如果实例有预取的对象缓存，则清除它，因为可能已经更改
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    @permission_classes([IsAuthenticated, UserPermissions])
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @permission_classes([IsAuthenticated, UserPermissions])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if(user.id != instance.user_id):
            return Response('没有权限操作',status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)