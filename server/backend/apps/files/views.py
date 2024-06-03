from django.shortcuts import render

from utils.FileTools import fileVerify
from utils.utils import post, jwt_authentication, json_response
class FileView():
    @post
    @jwt_authentication
    def upload_image(request, *args, **kwargs):
        upload_dir = 'static/imgs'  # 替换为实际的上传目录
        res = fileVerify ('imgs', upload_dir,file_data=request.data['imgs'], max_size=1024 * 2000, compress=True, quality=75)
        return json_response(data=res['data'], code=res['code'],message=res['message'])
