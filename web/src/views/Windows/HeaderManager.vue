<template>
    <div class="header-manager" style="cursor: default;">
        <el-button plain class="header-logo" @click="handleRoute('index')">Logo</el-button>
        <el-button class="header-buttons" @click="toggleDrawer">
            <div>4月13日 周六</div>
        </el-button>
        <g_Drawer :open="drawer" :with-header="false" @update:open="drawer = $event">
            <span>Hi there!</span>
        </g_Drawer>
    </div>
</template>

<script setup lang="ts">
import g_Drawer from '@/components/drawer/g_Drawer.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const drawer = ref(false)
const handleRoute = (routeName: string) => {
    router.push({ name: routeName }) // 假设您使用的是命名路由  
}

const toggleDrawer = () => {
    drawer.value = !drawer.value
}
</script>

<style scoped>
.header-manager {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    padding: 0 10px;
    background-color: rgba(254, 238, 197, 0.7);
}

.header-logo {
    /* Logo 的样式 */
    font-size: 20px;
    font-weight: bold;
    cursor: default;
    border: none;
    background-color: transparent;
}

.header-buttons {
    /* 按钮组的样式 */
    display: flex;
    cursor: default;
    border: none;
    background-color: transparent;
}
</style>