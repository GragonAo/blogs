<template>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false"
        @select="handleSelect">
        <el-menu-item index="0">
            <div class="logo" @click="handleRoute('index')">
                Gragon's Blog
            </div>
        </el-menu-item>
        <div class="flex-grow" />
        <el-input v-model="input3" class="input-with-select el-input-long" placeholder="Please input">
            <template #append>
                <el-button :icon="Search" />
            </template>
        </el-input>
        <el-menu-item index="1" @click="handleRoute('publishArticle')">发布文章</el-menu-item>
        <el-sub-menu index="2">
            <template #title>工作空间</template>
            <el-menu-item index="2-1" @click="handleRoute('myInterface')">我的界面</el-menu-item>
            <el-menu-item index="2-2" @click="handleRoute('console')">控制台</el-menu-item>
            <el-menu-item index="2-3" @click="handleRoute('cloudDesktop')">云端桌面</el-menu-item>
            <el-menu-item v-if="useUserStore().isLogin()" index="2-4" @click="logout">注销</el-menu-item>
        </el-sub-menu>
    </el-menu>
</template>

<script lang="ts" setup>
import useUserStore from '@/stores/User';
import { Search } from '@element-plus/icons-vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const activeIndex = ref('1')
const input3 = ref('')
const handleRoute = (routeName: string) => {
    router.push({ name: routeName }) // 假设您使用的是命名路由  
}
// 如果还需要处理原始的 select 事件  
const handleSelect = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const logout = () => {
    useUserStore().logOut();
    handleRoute('index');
}
</script>

<style>
.logo {
    font-family: 'Pacifico', cursive;
    font-size: 50px;
    color: #3498db;
    /* Light blue color */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    /* Light background */
}

.flex-grow {
    flex-grow: 1;
}

.input-with-select .el-input-group__prepend {
    background-color: var(--el-fill-color-blank);
}

/* 添加新的样式类以调整输入框的大小 */
.el-input-long {
    width: 25%;
    /* 或者使用具体的像素值，如 500px */
    font-size: 16px;
    /* 根据需要调整字体大小 */
    padding: 10px;
    /* 调整内边距以增大输入框的高度 */
}

/* 如果需要，也可以调整按钮的样式以匹配输入框的大小 */
.el-input-long .el-button {
    /* 调整按钮的内边距 */
    font-size: 16px;
    /* 调整按钮的字体大小 */
}
</style>