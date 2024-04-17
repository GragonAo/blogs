import os

from rest_framework import status


class FileVerificatory:
    @staticmethod
    def get_valid_extension(filename,ALLOWED_EXTENSIONS):
        base, ext = os.path.splitext(filename)
        # 确保扩展名不为空，且只包含一个点号
        if ext and '.' in ext and len(ext.split('.')) == 2:
            # 提取真正的扩展名部分（去掉点号）
            ext = ext.split('.')[1]
            # 转换为小写
            ext = ext.lower()
            # 检查扩展名是否在允许的列表中
            if ext in ALLOWED_EXTENSIONS:
                return ext
        return None  # 如果没有有效的扩展名，返回None
    @staticmethod
    def verify_file(base_path,path,ALLOWED_EXTENSIONS):
        paths = path.split('/')
        if len(paths) < 3:
            return (False,"无效的路径")
        # 假设第二个部分是子目录名称，最后一个部分是文件名
        subdir = paths[-2]
        filename = paths[-1]
        ext = FileVerificatory.get_valid_extension(filename,ALLOWED_EXTENSIONS)
        if ext is None:
            return (False,"不支持的文件类型或扩展名格式不正确")
        child_path = os.path.join(subdir,filename)
        # 根据子目录和文件名构造完整路径
        full_path = os.path.join(base_path, child_path)
        # 防止目录遍历攻击：确保路径在基础路径下
        if not os.path.abspath(full_path).startswith(os.path.abspath(base_path)):
            return(False,"无效的文件路径")
            # 检查文件是否存在
        if not os.path.isfile(full_path):
            return (False,"文件不存在")
        return (True,{'full_path':full_path,'ext':ext})