<template>
    <el-dialog :before-close="closeModal" width="40%" v-model="visible" :close-on-click-modal="false" :modal="false"
        :close-on-press-escape="false" show-close="false" class="login-dialog"
        :class="['animate__animated', animationClass]">
        <h2 style="text-align: center; margin-bottom: 20px;">登录</h2>
        <el-form label-position="left" :model="form" :rules="rules" ref="loginForm">
            <el-form-item label="用户名" :label-width="formLabelWidth" prop="username">
                <el-input v-model="form.username" autocomplete="off" />
            </el-form-item>
            <el-form-item label="密码" :label-width="formLabelWidth" prop="password">
                <el-input v-model="form.password" autocomplete="off" show-password />
            </el-form-item>
            <el-form-item>
                <el-button v-if="!form.password" type="primary" @click="submitFace">开启人脸登录</el-button>
                <el-button v-else type="primary" @click="submitForm">登录</el-button>
            </el-form-item>
            <el-form-item>
                <el-button type="default" @click="register">立即注册</el-button>
            </el-form-item>
        </el-form>
        <FaceModal ref="faceRef" @close-dialog="submitFormFace" />
    </el-dialog>
</template>
<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { LoginUserAPI } from '@/API/User';
import { useUserStore } from '@/stores/User';
import { useSettingsStore } from '@/stores/Settings';
import { useRouter } from 'vue-router';
import { ElLoading, ElMessage, type FormInstance } from 'element-plus';
import 'animate.css';
import FaceModal from '../face/faceModal.vue';
const formLabelWidth = '70px';
const visible = ref(true);
const userStore = useUserStore();
const router = useRouter();
const faceRef = ref<InstanceType<typeof FaceModal> | null>(null);
const animationClass = ref('animate__bounceIn');
const changeBtnAnimation = (newAnimation: string) => {
    animationClass.value = '';
    setTimeout(() => {
        animationClass.value = newAnimation;
    }, 10);
};
const form = ref({
    username: '',
    password: '',
});
const faceLogin = ref(false);
const rules = {
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' },
        { min: 3, message: '用户名至少为3个字符', trigger: 'blur' },
    ],
    password: [
        { required: !faceLogin, message: '请输入密码', trigger: 'blur' },
        { min: 6, message: '密码至少为6个字符', trigger: 'blur' },
    ],
};
const showModal = () => {
    faceLogin.value = false;
    visible.value = true;
    changeBtnAnimation("animate__bounce");
    emit('showDialog');
};
const closeModal = () => {
    visible.value = false;
    form.value = {
        username: '',
        password: '',
    };
    emit('closeDialog');
};
const loginForm = ref<FormInstance | null>(null);
const submitFace = () => {
    faceLogin.value = true;
    if (loginForm.value) {
        loginForm.value.validate((valid) => {
            if (valid) {
                if (faceRef.value) {
                    faceRef.value.showModal();
                }
            } else {
                ElMessage.error('表单中有错误，请检查后提交！');
                changeBtnAnimation("animate__wobble");
                return false;
            }
        });
    }
}
const submitFormFace = async (pictures: ['']) => {
    console.log(pictures);
    if (pictures.length < 1) return;
    login(form.value.username, "*", pictures);
}
const login = async (username: string, password: string, pictures?: ['']) => {
    const loading = ElLoading.service({
        lock: true,
        text: 'Loading',
        background: 'rgba(0, 0, 0, 0.7)',
    })
    const result = await LoginUserAPI(username, password, pictures);
    if (result?.code == 200) {
        userStore.setToken(result!.data);
        closeModal();
        router.push({ path: useSettingsStore().settings?.redirectPath });
    } else {
        ElMessage.error('登录失败，请检查用户名或密码');
        changeBtnAnimation("animate__wobble");
    }
    loading.close()
}
const submitForm = async () => {
    loginForm.value?.validate(async (valid) => {
        if (valid) {
            login(form.value.username, form.value.password);
        } else {
            ElMessage.error('表单中有错误，请检查后提交！');
            changeBtnAnimation("animate__wobble");
            return false;
        }
    });
};

const register = () => {
    router.push({ name: 'register' });
};

onMounted(() => {
    showModal();
});
const emit = defineEmits(['closeDialog', 'loginSuccess', 'showDialog']);
</script>
<style scoped>
login-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.5);
}

.login-dialog {
    border-radius: 10px;
    padding: 30px;
    width: 100%;
    max-width: 400px;
}

.el-form-item {
    margin-bottom: 16px;
}

.el-input {
    height: 40px;
    /* 调整输入框高度 */
    font-size: 14px;
    /* 字体大小适中 */
}

.el-button {
    width: 100%;
    line-height: 38px;
    /* 保证文字居中 */
    font-size: 16px;
    /* 调整字体大小 */
    height: 35px;
    /* 调整按钮高度 */
}

.el-form-item.is-error .el-input {
    border-color: #f56c6c;
    /* 错误时的边框颜色 */
}

.el-form-item.is-success .el-input {
    border-color: #67c23a;
    /* 通过验证时的边框颜色 */
}

.el-dialog {
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>