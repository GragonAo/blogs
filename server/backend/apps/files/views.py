# Create your views here.
import os
from django.conf import settings
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from common.FileVerificatory import FileVerificatory


class ImageFileView(APIView):
    def get(self, request, path):
        # 定义允许访问的图片文件后缀
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
            # 定义基础路径
        base_path = os.path.join(settings.MEDIA_ROOT, 'image')
        is_valid,data = FileVerificatory.verify_file(base_path,request.path,ALLOWED_EXTENSIONS)
        if(is_valid == False):
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
        full_path = data['full_path']
        ext = data['ext']
        try:
            return FileResponse(open(full_path, 'rb'), content_type='image/{}'.format(ext[1:]))
        except Exception as e:
            return Response(f"无法读取文件: {e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
