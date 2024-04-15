from rest_framework import serializers
from .models import User, UserInfo  # 假设User模型在.models中定义

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # 设置密码不参与序列化
        }
        def create(self, validated_data):
            # 提取密码
            password = validated_data.pop('password')
            user = User.objects.create(**validated_data)
            user.set_password(password)  # 使用set_password加密密码
            user.save()
            return user

    # 序列化对象.Save()时会自动调用 不写就默认，写了可以自定义一些东西在里面比如密码的一些处理
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance
    #
    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

    # #自定义字段校验器 validate_字段名，它会根据字段名自动识别
    # def validate_username(self,value):
    #     if len(value) < 20:
    #         raise serializers.ValidationError('Username must be at least 20 characters.') #异常信息

    # def length_validate(value):
    #     if not (10 <= len(value) <= 20):
    #         raise serializers.ValidationError('字段的长度必须在10～20之间')
    #
    # class UserSerializer(serializers.Serializer):
    #     password = serializers.CharField(validators=[length_validate])

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'