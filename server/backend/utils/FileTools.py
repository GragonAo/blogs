import hashlib
import os
from io import BytesIO
from tkinter import Image

from django.core.files.uploadedfile import InMemoryUploadedFile

from utils.utils import json_response


def fileVerify(field_name, upload_dir, file_data, max_size=1024 * 800, compress=False, quality=75):
    # 检查文件是否存在
    if not file_data:
        return {'data':None, 'message': f"上传失败，请上传{field_name}文件", 'code':422}

    # 检查文件大小
    if file_data.size > max_size:
        return {'data':None,'message': f"上传失败，文件不允许大于{max_size // 1024}kb", 'code': 422}

    # 计算文件哈希值
    hash_md5 = hashlib.md5()
    for chunk in file_data.chunks():
        hash_md5.update(chunk)
    file_hash = hash_md5.hexdigest()
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    existing_files = [f for f in os.listdir(upload_dir) if os.path.isfile(os.path.join(upload_dir, f))]
    file_path = os.path.join(upload_dir, f"{file_hash}_{file_data.name}")
    if not any(file_hash in file for file in existing_files):
        # 如果需要压缩图片
        if compress:
            try:
                image = Image.open(file_data)
                image_io = BytesIO()
                image.save(image_io, format='JPEG', quality=quality)  # 调整压缩比例
                file_data = InMemoryUploadedFile(image_io, None, file_data.name, 'image/jpeg', image_io.tell(), None)
            except Exception as e:
                print( f"图片压缩失败: {str(e)}")

        # 保存文件
        with open(file_path, 'wb') as f:
            for chunk in file_data.chunks():
                f.write(chunk)
    # 返回上传后的文件URL
    return {'data':None,'message': '上传成功', 'code': 200,'data':{field_name: file_path}}