<template>
    <div class="window-container" v-for="(window, index) in windows" :key="index"
        :style="{ top: window.top + 'px', left: window.left + 'px' }">
        <Window :title="window.title" :top="window.top" :left="window.left" :isOpen="window.isOpen"
            @close="closeWindow(index)" @update:top="onWindowTopUpdate(index, $event)"
            @update:left="onWindowLeftUpdate(index, $event)" />
    </div>
    <button @click="openNewWindow">打开新窗口</button>
</template>

<script setup lang='ts'>
import { ref } from 'vue';
import Window from './Window.vue';
import type { WindowsType } from './Desktop';
// 初始化窗口数组，每个窗口包含标题、是否打开状态、位置信息  
const windows = ref<WindowsType[]>([
    // 可以添加更多默认窗口，并设置初始位置  
]);
// 打开新窗口的方法  
const openNewWindow = () => {
    const newWindow: WindowsType = {
        title: `窗口 ${windows.value.length + 1}`,
        isOpen: true,
        top: 100, // 初始位置可以根据需要调整  
        left: 100 + windows.value.length * 50, // 假设每个窗口在水平方向上间隔50px  
    };
    windows.value.push(newWindow);
};

// 关闭窗口的方法  
const closeWindow = (index: number) => {
    console.log("close:  " + index);
    windows.value[index].isOpen = false;
};
const onWindowTopUpdate = (index: number, newTop: number) => {
    windows.value[index].top = newTop;
};

const onWindowLeftUpdate = (index: number, newLeft: number) => {
    windows.value[index].left = newLeft;
};

// 暴露给父组件或可能的兄弟组件使用的方法和数据  
defineExpose({
    windows,
    openNewWindow,
    closeWindow,
});  
</script>

<style scoped>
.window-container {
    position: absolute;
    /* 绝对定位，相对于 .desktop */
    /* 在这里可以添加窗口容器的样式 */
}
</style>