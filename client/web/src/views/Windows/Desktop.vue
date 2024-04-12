<template>
    <div class="desktop">
        <!-- 遍历图标 -->
        <WindowManger />
    </div>
</template>

<script setup lang="ts">
import WindowManger from './WindowManger.vue'
</script>

<style scoped>
.desktop {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    width: 100vw;
    background-image: "src/assets/imgs/DoesktopBg.jpg";
    /* 桌面背景色 */
    overflow: hidden;
    /* 隐藏超出视口的内容 */
    position: relative;
    /* 为了子窗口定位 */
}
</style>