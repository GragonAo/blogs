<template>
    <el-dialog v-model="visible" title="登录" width="350" class="login">
        <el-form :model="form" ref="form" label-width="80px">
            <el-form-item label="用户名">
                <el-input v-model="form.username"></el-input>
            </el-form-item>
            <el-form-item label="密码">
                <el-input type="password" v-model="form.password"></el-input>
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
const visible = ref(true);
const form = ref({
    username: '',
    password: '',
});

const showModal = () => {
    visible.value = true;
};

const closeModal = () => {
    visible.value = false;
    form.value = {
        username: '',
        password: '',
    };
    // emit('login-cancel');
};

const submitForm = async () => {
    try {
        // 发送登录请求到后端API的逻辑  
        // const result = await login(form.value.username, form.value.password);  
        // 根据你的后端API返回结果处理登录逻辑  
        // 如果登录成功，则触发 'login-success' 事件  
        // emit('login-success', result.user);  
        // 示例：直接模拟登录成功  
        // emit('login-success', { name: form.value.username });
        closeModal();
    } catch (error) {
        // 处理登录失败的情况  
        console.error('登录失败:', error);
        // 这里可以选择显示错误信息给用户  
        // 或者触发一个 'login-error' 事件  
        // 例如：ElMessageBox.alert('登录失败: ' + error.message);  
    }
};

defineExpose({
    showModal,
});  
</script>

<style scoped>
.login {
    border-radius: 10px;
}
</style>