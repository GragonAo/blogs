<template>
    <div class="desktop">
        <div class="common-layout">
            <el-container>
                <el-header style="width: 100%; height: 35px;">
                    <HeaderManager />
                </el-header>
                <el-main>
                    <!-- 遍历图标 -->
                    <WindowManger />
                    <TipsManager />
                </el-main>
                <el-footer></el-footer>
            </el-container>
        </div>

    </div>
</template>

<script setup lang="ts">
import WindowManger from './WindowManger.vue';
import HeaderManager from './HeaderManager.vue';
import TipsManager from './TipsManager.vue';
import { onMounted, onUnmounted, ref } from 'vue';
import G_DesktopSystem from './class/G_DesktopSystem';

const desktopSystem = ref(new G_DesktopSystem());

onMounted(() => {
    desktopSystem.value.start();
});

onUnmounted(() => {
    desktopSystem.value.stop();
});  
</script>

<style scoped>
.desktop {
    width: 98vw;
    /* 使用视口宽度作为宽度 */
    height: 97vh;
    /* 使用视口高度作为高度 */
    background-image: url("/Users/gragon/Projects/Web/DjangoWeb/blogs/client/web/src/assets/imgs/DoesktopBg.jpg");
    background-size: cover;
    /* 图片覆盖整个容器 */
    background-position: center;
    border-radius: 10px;
}
</style>
