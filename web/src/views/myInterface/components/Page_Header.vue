<template>
    <div class="page-header">
        <el-row class="header-row">
            <el-col :span="4" class="avatar-col">
                <el-image class="avatar-image" :src="APP_CONFIG.baseURL + userStores.userLoginInfo?.avatar"
                    :zoom-rate="1.2" :max-scale="7" :min-scale="0.2" fit="cover" />
                <input ref="fileInput" type="file" accept="image/*" style="display: none;" @change="handleFileChange" />
                <el-button text round size="small" type="primary" @click="triggerFileInput">
                    上传头像
                    <el-icon class="el-icon--right">
                        <Upload />
                    </el-icon>
                </el-button>
            </el-col>
            <el-col :span="19" :offset="1" class="info-cols">
                <el-descriptions :title="userStores.userLoginInfo?.username" :column="2" class="user-info">
                    <el-descriptions-item label="Email">{{ userStores.userLoginInfo?.email }}</el-descriptions-item>
                    <el-descriptions-item label="Telephone">{{ userStores.userLoginInfo?.mobile
                        }}</el-descriptions-item>
                    <el-descriptions-item label="Place">Suzhou</el-descriptions-item>
                    <el-descriptions-item label="Remarks">
                        <el-tag size="small">School</el-tag>
                    </el-descriptions-item>
                    <el-descriptions-item label="Address">
                        No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu Province
                    </el-descriptions-item>
                </el-descriptions>
            </el-col>
        </el-row>
        <p class="mt-4 text-sm">
            我是 黄可钊 我又是 朱必利
        </p>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { ElMessage } from 'element-plus';
import { UploadUserAvatarAPI } from '@/API/User';
import { useUserStore } from '@/stores/User';
import { Upload } from '@element-plus/icons-vue';
import { GetUserInfoAPI } from '@/API/User';
import { APP_CONFIG } from '~/app.config';
const userStores = useUserStore();
const fileInput = ref<HTMLInputElement | null>(null);
onMounted(() => {
    init();
});
const init = async () => {
    if (userStores.userLoginInfo === undefined) {
        const res = await GetUserInfoAPI();
        if (res?.code === 200) {
            userStores.setUserInfo(res.data);
        }
    }
}
const triggerFileInput = () => {
    fileInput.value?.click();
}

const handleFileChange = async (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files[0]) {
        const file = target.files[0];
        // 检查文件类型和大小
        const isJPG = file.type === 'image/jpeg' || file.type === 'image/png';
        const isLt300KB = file.size / 1024 / 1024 < 0.3;

        if (!isJPG) {
            ElMessage.error('上传头像图片只能是 JPG 或 PNG 格式!');
            return;
        }
        if (!isLt300KB) {
            ElMessage.error('上传头像图片大小不能超过 300KB!');
            return;
        }
        // 上传文件
        try {
            const formData = new FormData();
            formData.append('avatar', file);
            const res = await UploadUserAvatarAPI(formData);
            if (res?.data.avatar) {
                if (userStores.userLoginInfo) {
                    userStores.userLoginInfo.avatar = res.data.avatar;
                    ElMessage.success('头像上传成功');
                } else {
                    ElMessage.error('头像上传失败');
                }
            } else {
                ElMessage.error('头像上传失败');
            }
        } catch (error) {
            console.error('上传失败:', error);
            ElMessage.error('上传失败，请稍后再试');
        }
    }
}

const submitAvatar = () => {
    if (fileInput.value) {
        fileInput.value.click();
    } else {
        ElMessage.error('文件输入未初始化');
    }
}
</script>

<style scoped>
.page-header {
    padding: 20px;
    border-radius: 10px;
}

.header-row {
    display: flex;
    align-items: center;
}

.avatar-col {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.avatar-image {
    border-radius: 50%;
    width: 120px;
    height: 120px;
    margin-bottom: 10px;
    border: 2px solid #409eff;
}

.info-cols {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.user-info {
    width: 100%;
    margin-top: 20px;
}

.el-descriptions-item__label {
    font-weight: bold;
}

.mt-4 {
    margin-top: 16px;
}

.text-sm {
    font-size: 14px;
}
</style>