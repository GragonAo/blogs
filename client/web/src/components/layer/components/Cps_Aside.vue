<template>
    <el-menu default-active="2" class="el-menu-vertical-demo" :collapse="isCollapse" @open="handleOpen"
        @close="handleClose">
        <el-menu-item v-for="(item, index) in CurNavigation" :key="index" index="index"
            @click="handleRoute(item.path_name)">
            <el-icon><icon-menu /></el-icon>
            <template #title>{{ item.to_name }}</template>
        </el-menu-item>
    </el-menu>
</template>

<script lang="ts" setup>
import { computed, ref, watch, type ComputedRef } from 'vue'
import {
    Document,
    Menu as IconMenu,
    Location,
    Setting,
} from '@element-plus/icons-vue'
import { useRouter, type RouteRecordName } from 'vue-router'
const router = useRouter();
const isCollapse = ref(false);
type NavigationObject = {
    root_name: string;
    nav: { to_name: string, path_name: string }[];
};
const navigations = ref<NavigationObject[]>([
    {
        root_name: "index", nav:
            [
                { to_name: "首页", path_name: "index" },
            ]
    },
    {
        root_name: "myInterface", nav: [
            { to_name: "我的主页", path_name: "myInterface" },
            { to_name: "我的文章", path_name: "myInfoPage" },
            { to_name: "我的信息", path_name: "myUserProfile" },
            { to_name: "隐私与安全", path_name: "mySecuritySettings" },
        ]
    },
    {
        root_name: "myInfoPage", nav: [
            { to_name: "我的主页", path_name: "myInterface" },
            { to_name: "我的文章", path_name: "myInfoPage" },
            { to_name: "我的信息", path_name: "myUserProfile" },
            { to_name: "隐私与安全", path_name: "mySecuritySettings" },
        ]
    },
    {
        root_name: "myUserProfile", nav: [
            { to_name: "我的主页", path_name: "myInterface" },
            { to_name: "我的文章", path_name: "myInfoPage" },
            { to_name: "我的信息", path_name: "myUserProfile" },
            { to_name: "隐私与安全", path_name: "mySecuritySettings" },
        ]
    },
    {
        root_name: "mySecuritySettings", nav: [
            { to_name: "我的主页", path_name: "myInterface" },
            { to_name: "我的文章", path_name: "myInfoPage" },
            { to_name: "我的信息", path_name: "myUserProfile" },
            { to_name: "隐私与安全", path_name: "mySecuritySettings" },
        ]
    },
]);
const cur_name = ref(router.currentRoute.value.name);
// 监听路由变化  
watch(
    () => router.currentRoute.value.name, // 监听 route.name 的变化  
    (newName) => {
        cur_name.value = newName; // 当路由名称变化时，更新 cur_name  
    },
    { immediate: true } // 立即执行一次回调函数，以获取初始的路由名称  
);
const CurNavigation: ComputedRef<{ to_name: string, path_name: string }[] | undefined> = computed(() => {
    return navigations.value.find((nav: { root_name: RouteRecordName | null | undefined; }) => nav.root_name === cur_name.value)?.nav;
});
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleRoute = (routeName: string) => {
    console.log(routeName)
    router.push({ name: routeName })
}
</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
    padding-top: 30px;
}
</style>