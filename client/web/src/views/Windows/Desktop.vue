<template>
    <div class="desktop">
        <!-- 遍历图标 -->
        <WindowManger />
    </div>
</template>

<script setup lang="ts">
import WindowManger from './WindowManger.vue';
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
    width: 99vw;
    /* 使用视口宽度作为宽度 */
    height: 98vh;
    /* 使用视口高度作为高度 */
    background-image: url("/Users/gragon/Projects/Web/DjangoWeb/blogs/client/web/src/assets/imgs/DoesktopBg.jpg");
    background-size: cover;
    /* 图片覆盖整个容器 */
    background-position: center;
    /* 图片居中 */
    box-shadow: inset 0 0 100px rgba(90, 51, 51, 0.1);
    /* 内阴影效果 */
}
</style>
