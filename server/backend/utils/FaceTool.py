import os
import base64
from deepface import DeepFace
import tensorflow as tf
from PIL import Image

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

        # 降低图像大小
        with Image.open(decoded_file_path) as img:
            img = img.resize((224, 224), Image.Resampling.LANCZOS)
            img.save(decoded_file_path)

        return decoded_file_path

    @staticmethod
    def verifyFace(encoded_str, original_file_path):
        decoded_file_path = ""
        try:
            # 保存 base64 编码的图像到临时文件
            decoded_file_path = FaceTool.save_base64_image(encoded_str, 'temp_image.png')
            # 打印调试信息
            print(f"Original file path: {original_file_path}")
            print(f"Decoded file path: {decoded_file_path}")

            # 配置 TensorFlow 以防止 OOM 错误
            gpus = tf.config.experimental.list_physical_devices('GPU')
            if gpus:
                try:
                    for gpu in gpus:
                        tf.config.experimental.set_memory_growth(gpu, True)
                except RuntimeError as e:
                    print(f"Memory growth setting error: {e}")

            # 手动指定模型权重文件路径
            model_weights_path = "/home/backend/models/facenet_weights.h5"

            # 进行人脸验证
            result = DeepFace.verify(
                img1_path=original_file_path,
                img2_path=decoded_file_path,
                model_name='Facenet',
                detector_backend='opencv',
                enforce_detection=False,
                align=True,
                normalization='base',
                distance_metric='cosine',
                model_weights_path=model_weights_path
            )
            print(f"Verification result: {result}")

            return result.get('verified', False)
        except Exception as e:
            print(f"Verification failed: {e}")
            return False
        finally:
            # 删除临时文件
            if decoded_file_path and os.path.exists(decoded_file_path):
                os.remove(decoded_file_path)
                print(f"Deleted temporary file: {decoded_file_path}")

# 调试信息
# encoded_image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAAAAAXNSR0IAr"  # 这是一个示例编码字符串
# print(FaceTool.verifyFace(encoded_image, 'original_image.png'))