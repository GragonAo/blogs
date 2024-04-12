<template>
    <div>
        <div class="window-container" v-for="(window, index) in windows" :key="index"
            :style="{ top: window.Top + 'px', left: window.Left + 'px' }">
            <Window :windowId="window.getWindowId()" :title="window.Title" :isOpen="window.IsOpen"
                @op:close="closeWindow(window.getWindowId())" @op:destroy="destroyWindow(window.getWindowId())"
                @update:top="onWindowTopUpdate(index, $event)" @update:left="onWindowLeftUpdate(index, $event)" />
        </div>
        <button @click="openNewWindow">打开新窗口</button>
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
    const id = windowSystem.value.addWindow(G_WindowNormal as unknown as WindowClass<G_WindowBase>, "New Window", 100, 100);
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
</style>
