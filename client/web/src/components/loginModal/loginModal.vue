<template>
    <!-- <el-dialog v-model="visible" title="登录" width="500" close-on-press-escape="false" close-on-click-modal="false"
        show-close="false">
        <el-form :model="form">
            <el-form-item label="用户名" :label-width="formLabelWidth">
                <el-input v-model="form.username" autocomplete="off" />
            </el-form-item>
            <el-form-item label="密码" :label-width="formLabelWidth">
                <el-input v-model="form.password" autocomplete="off" show-password="true" />
            </el-form-item>
        </el-form>
        <template #footer>
            <div class="dialog-footer">

            </div>
        </template>
</el-dialog> -->
    <div class="login-container" v-if="visible">
        <div class="login-dialog">
            <h2>登录</h2>
            <el-form :model="form">
                <el-form-item label="用户名" :label-width="formLabelWidth">
                    <el-input v-model="form.username" autocomplete="off" />
                </el-form-item>
                <el-form-item label="密码" :label-width="formLabelWidth">
                    <el-input v-model="form.password" autocomplete="off" show-password="true" />
                </el-form-item>
            </el-form>
            <el-button type="primary" @click="submitForm">
                Confirm
            </el-button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { GetUserInfoAPI, LoginUserAPI } from '@/API/User';
import { useUserStore } from '@/stores/User'
import { useSettingsStore } from '@/stores/Settings'
import type { UserLoginInfo } from '@/API/API_Types/User';
import { useRouter } from 'vue-router';
const formLabelWidth = '140px'
const visible = ref(true); // 初始状态设为false，除非你需要默认打开对话框  
const userStore = useUserStore();
const router = useRouter();
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
    // emit('login-cancel'); 如果父组件需要知道这个事件，可以取消注释  
};

const submitForm = async () => {
    const result = await LoginUserAPI(form.value.username, form.value.password);
    console.log(result)
    if (result!.code >= 200 && result!.code < 300)
        userStore.setUserInfo(result!.data as UserLoginInfo);
    const info = await GetUserInfoAPI(userStore.userLoginInfo!.id);
    console.log(info);
    if (info!.code >= 200 && info!.code < 300) {
        useUserStore().setUserInfo(info!.data as UserLoginInfo);
        closeModal();
        router.push({ path: useSettingsStore().settings?.redirectPath });
    }

    else {
        //密码错误等处理
    }
};
onMounted(() => {
    visible.value = true;
});
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
    pointer-events: none;
}

.login-dialog {
    background-color: #fff;
    border-radius: 4px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    position: relative;
    max-width: 400px;
    pointer-events: auto;
}
</style>