import os
import base64
from deepface import DeepFace

class FaceTool:
    @staticmethod
    def baseEncode(file_name):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, file_name)
        with open(file_path, "rb") as file:
            file_content = file.read()
            base64_encoded = base64.b64encode(file_content).decode('utf-8')
        print("Base64 Encoded:", base64_encoded)
        return base64_encoded

    @staticmethod
    def save_base64_image(encoded_str, file_name):
        decoded_file_path = os.path.join('/tmp', file_name)
        with open(decoded_file_path, 'wb') as f:
            f.write(base64.b64decode(encoded_str))
        print(f"Image saved to {decoded_file_path}")
        return decoded_file_path

    @staticmethod
    def verifyFace(encoded_str, original_file_path):
        decoded_file_path = ""
        try:
            # 保存 base64 编码的图像到临时文件
            decoded_file_path = FaceTool.save_base64_image(encoded_str, 'temp_image.png')
            # 进行人脸验证
            result = DeepFace.verify(
                img1_path=original_file_path,
                img2_path=decoded_file_path,
                model_name='VGG-Face',
                enforce_detection=False,
                align=True,
                threshold=0.5
            )
            print(f"Face Verification result: {result}")
            return result.get('verified')
        except Exception as e:
            print(f"Verification failed: {e}")
            return 0
        finally:
            # 删除临时文件
            if decoded_file_path and os.path.exists(decoded_file_path):
                os.remove(decoded_file_path)
                print(f"Deleted temporary file: {decoded_file_path}")