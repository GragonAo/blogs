<template>
    <FaceModal ref="faceRef" @close-dialog="submitFormFace" />
    <ChangePassword ref="pwdRef" />
    <span style="margin: 30px 20px 30px 20px; font-size: 20px;">隐私和安全</span>
    <el-card style="border-radius: 20px; margin-top:10px; width: 70%;">
        <el-row>
            <el-col :span="24">
                <el-button @click="faceRef?.showModal();" class="btn">人脸录入</el-button>
            </el-col>
        </el-row>
        <el-divider />
        <el-row>
            <el-col :span="24">
                <el-button @click="pwdRef?.showModal();" class="btn">修改密码</el-button>
            </el-col>
        </el-row>
    </el-card>


</template>

<script setup lang='ts'>
import { UploadUserPhotoAPI } from '@/API/User';
import FaceModal from '@/components/face/faceModal.vue';
import ChangePassword from './components/ChangePassword.vue';
import { ElMessage } from 'element-plus';
import { ref } from 'vue';
import Base64Tool from '@/G_FrameWork/Tool/Base64Tool';

const faceRef = ref<InstanceType<typeof FaceModal> | null>(null);
const pwdRef = ref<InstanceType<typeof ChangePassword> | null>(null);
const submitFormFace = async (pictures: ['']) => {
    if (pictures.length < 1) {
        ElMessage.error('人脸录入失败');
        return;
    }
    let formData = new FormData();
    pictures.forEach((picture, index) => {
        const file = Base64Tool.base64ToFile(picture, `uploaded_image_${index}.png`);
        formData.append('faces', file);  // 这里确保所有文件都添加到 'faces' 字段中
    });
    console.log(formData)
    const res = await UploadUserPhotoAPI(formData);
    console.log(res);
}
</script>

<style scoped>
.btn {
    width: 100%;
    height: 100%;
}
</style>