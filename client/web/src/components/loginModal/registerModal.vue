<template>
    <el-dialog v-model="visible" title="登录" width="500">
        <el-form :model="form">
            <el-form-item label="用户名" :label-width="formLabelWidth">
                <el-input v-model="form!.username" autocomplete="off" />
            </el-form-item>
            <el-form-item label="邮箱" :label-width="formLabelWidth">
                <el-input v-model="form!.email" autocomplete="off" />
            </el-form-item>
            <el-form-item label="手机号" :label-width="formLabelWidth">
                <el-input v-model="form!.mobile" autocomplete="off" />
            </el-form-item>
            <el-form-item label="密码" :label-width="formLabelWidth">
                <el-input v-model="form!.password" autocomplete="off" show-password="true" />
            </el-form-item>
            <el-form-item label="确认密码" :label-width="formLabelWidth">
                <el-input v-model="form!.password_confirm" autocomplete="off" show-password="true" />
            </el-form-item>
        </el-form>
        <template #footer>
            <div class="dialog-footer">
                <el-button @click="closeModal">Cancel</el-button>
                <el-button type="primary" @click="submitForm">
                    Confirm
                </el-button>
            </div>
        </template>
    </el-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { RegisterUserAPI } from '@/API/User';
import type { UserRegister } from '@/API/API_Types/User.d.ts';
import type { Result } from '@/API/API_Types/Base';

const formLabelWidth = '140px'
const visible = ref(true); // 初始状态设为false，除非你需要默认打开对话框  
const form = ref<UserRegister>({
    username: '',
    password: '',
    password_confirm: '',
    email: '',
});

const showModal = () => {
    visible.value = true;
};

const closeModal = () => {
    visible.value = false;
    form.value = {
        username: '',
        password: '',
        password_confirm: '',
        mobile: 0,
        email: '',
    };
    // emit('login-cancel'); 如果父组件需要知道这个事件，可以取消注释  
};

const submitForm = async () => {
    const result = await RegisterUserAPI(form.value);
    console.log(result)
    if (result!.code >= 200 && result!.code < 300) {
        // 处理登录成功的情况，例如跳转到其他页面或显示成功的消息  
        closeModal();
    }
    else {
        //密码错误等处理
    }
};

// 如果父组件需要调用showModal方法，可以通过defineExpose暴露这个方法  
defineExpose({
    showModal,
});
</script>

<style scoped></style>