<template>
    <div class="login-container" v-if="visible">
        <div class="login-dialog">
            <h2>注册</h2>
            <el-form :model="form" :rules="rules" ref="formRef" label-width="120px">
                <el-form-item label="用户名" prop="username">
                    <el-input v-model="form.username" autocomplete="off" />
                </el-form-item>
                <el-form-item label="邮箱" prop="email">
                    <el-input v-model="form.email" autocomplete="off" />
                </el-form-item>
                <el-form-item label="手机号" prop="mobile">
                    <el-input v-model="form.mobile" autocomplete="off" />
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-input v-model="form.password" autocomplete="off" show-password />
                </el-form-item>
                <el-form-item label="确认密码" prop="password_confirm">
                    <el-input v-model="form.password_confirm" autocomplete="off" show-password />
                </el-form-item>
                <el-form-item label="验证码" prop="verificatory">
                    <el-input v-model="form.verificatory" autocomplete="off" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm" class="submit-button">
                        注册
                    </el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { RegisterUserAPI } from '@/API/User';
import type { UserRegister } from '@/API/API_Types/User.d.ts';
import { useRouter } from 'vue-router';

const formLabelWidth = '140px';
const visible = ref(true);
const router = useRouter();
const form = ref<UserRegister>({
    username: '',
    password: '',
    password_confirm: '',
    email: '',
    mobile: '',
    verificatory: '',
});

const rules = ref({
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' },
        { min: 3, max: 15, message: '用户名长度在 3 到 15 个字符', trigger: 'blur' }
    ],
    email: [
        { required: true, message: '请输入邮箱', trigger: 'blur' },
        { type: 'email', message: '请输入有效的邮箱地址', trigger: 'blur' }
    ],
    mobile: [
        { required: true, message: '请输入手机号', trigger: 'blur' },
        { pattern: /^[0-9]{10,11}$/, message: '请输入有效的手机号', trigger: 'blur' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 6, message: '密码长度至少为 6 个字符', trigger: 'blur' }
    ],
    password_confirm: [
        { required: true, message: '请确认密码', trigger: 'blur' },
        {
            validator: (rule, value, callback) => {
                if (value !== form.value.password) {
                    callback(new Error('两次输入的密码不一致'));
                } else {
                    callback();
                }
            }, trigger: 'blur'
        }
    ],
    verificatory: [
        { required: true, message: '请输入验证码', trigger: 'blur' }
    ]
});

const formRef = ref();

const showModal = () => {
    visible.value = true;
};

const closeModal = () => {
    visible.value = false;
    form.value = {
        username: '',
        password: '',
        password_confirm: '',
        mobile: '',
        email: '',
        verificatory: '',
    };
};

const submitForm = () => {
    formRef.value.validate(async (valid) => {
        if (valid) {
            const result = await RegisterUserAPI(form.value);
            console.log(result);
            if (result!.code >= 200 && result!.code < 300) {
                // 处理登录成功的情况，例如跳转到其他页面或显示成功的消息
                closeModal();
                router.push({ name: 'index' });
            } else {
                // 处理错误，例如显示错误消息
            }
        } else {
            console.log('表单验证失败');
        }
    });
};

// 如果父组件需要调用showModal方法，可以通过defineExpose暴露这个方法
defineExpose({
    showModal,
});
</script>

<style scoped>
.login-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(5px);
}

.login-dialog {
    background-color: #fff;
    border-radius: 8px;
    padding: 30px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    position: relative;
    max-width: 400px;
    width: 100%;
    pointer-events: auto;
}

h2 {
    text-align: center;
    margin-bottom: 20px;
}

.el-form-item {
    margin-bottom: 20px;
}

.el-input {
    width: 100%;
}

.submit-button {
    width: 100%;
    background-color: #409EFF;
    color: #fff;
    font-size: 16px;
    padding: 10px;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.submit-button:hover {
    background-color: #66b1ff;
}
</style>
