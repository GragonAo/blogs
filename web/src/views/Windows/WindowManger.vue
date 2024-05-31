<template>
    <div>
        <div class="window-container" v-for="(window, index) in windows" :key="index"
            :style="{ top: window.Top + 'px', left: window.Left + 'px' }">
            <Window :windowId="window.getWindowId()" :title="window.Title" :isOpen="window.IsOpen"
                @op:close="closeWindow(window.getWindowId())" @op:destroy="destroyWindow(window.getWindowId())"
                @update:top="onWindowTopUpdate(index, $event)" @update:left="onWindowLeftUpdate(index, $event)" />
        </div>

        <el-button class="editorIcon" @dblclick="openNewWindow">
            <span class="editor-text">编辑器</span>
        </el-button>
    </div>
</template>

<script setup lang='ts'>
import { ref, defineExpose, onMounted } from 'vue';
import Window from './Window.vue';
import G_WindowSystem, { type WindowClass } from './class/G_WindowSystem';
import SingletonFactory from '@/G_FrameWork/SingletonFactory';
import { G_WindowNormal } from './class/G_WindowNormal';
import type { G_WindowBase } from './class/G_WindowBase';
const windowSystem = ref<G_WindowSystem | null>(null);
const windows = ref<G_WindowBase[]>([]);
const updateWindows = () => {
    if (!windowSystem.value) return;
    windows.value = windowSystem.value.getWindowList();
};
onMounted(() => {
    windowSystem.value = SingletonFactory.getInstance(G_WindowSystem);
    updateWindows();
});
const openNewWindow = () => {
    if (!windowSystem.value) return;
    const id = windowSystem.value.addWindow(G_WindowNormal as unknown as WindowClass<G_WindowBase>, "G_Editor", 50, 180);
    if (id !== -1) {
        updateWindows();
        windowSystem.value.openWindow(id);
    }
};
const closeWindow = (id: number) => {
    console.log("closeWindow:   " + id);
    if (!windowSystem.value) return;
    windowSystem.value.closeWindow(id);
};
const destroyWindow = (id: number) => {
    console.log("destroyWindow:   " + id);
    if (!windowSystem.value) return;
    const index = windows.value.findIndex(window => window.getWindowId() === id);
    windowSystem.value.destroyWindow(id);
    if (index !== -1) {
        windows.value.splice(index, 1); // 从数组中删除销毁的窗口对象
    }
};
const onWindowTopUpdate = (index: number, newTop: number) => {
    if (!windowSystem.value) return;
    if (index < 0 || index >= windows.value.length) return;
    windows.value[index].Top = newTop;
};
const onWindowLeftUpdate = (index: number, newLeft: number) => {
    if (!windowSystem.value) return;
    if (index < 0 || index >= windows.value.length) return;
    windows.value[index].Left = newLeft;
};
defineExpose({
    windows,
    openNewWindow,
    closeWindow,
});
</script>

<style scoped>
.window-container {
    position: absolute;
}

.editorIcon {
    position: relative;
    /* 为子元素提供定位上下文 */
    width: 66px;
    height: 88px;
    /* 假设您想要给文字留下一些空间 */
    cursor: pointer;
    border-radius: 10px;
    overflow: hidden;
    /* 确保子元素不会溢出按钮 */
}

.editorIcon {
    position: relative;
    width: 66px;
    height: 66px;
    background-image: url('/Users/gragon/Projects/Web/DjangoWeb/blogs/client/web/src/assets/imgs/icon_Editor.png');
    /* 使用正确的图片路径 */
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    cursor: pointer;
    border: none;
    /* 确保没有边框 */
    /* 移除可能的边框和底色 */
    border-radius: 0;
    box-shadow: none;
    background-color: transparent;
    /* 确保背景透明 */
    border-radius: 10px;
}

.editor-text {
    position: absolute;
    bottom: 0;
    /* 文字显示在图标下方 */
    left: 0;
    right: 0;
    padding: 5px;
    /* 为文字添加一些内边距 */
    color: #fff;
    /* 设置文字颜色，确保与背景图片对比度高 */
    text-align: center;
    /* 文字居中 */
    opacity: 0;
    /* 初始时不显示文字 */
    transition: opacity 0.3s ease;
    /* 添加过渡效果 */
    pointer-events: none;
    /* 防止文字干扰鼠标事件 */
    background-color: rgba(0, 0, 0, 0.5);
    /* 可选：半透明背景，帮助文字在图片上可见 */
}

.editorIcon:hover .editor-text {
    opacity: 1;
    /* 鼠标悬停时显示文字 */
}
</style>
