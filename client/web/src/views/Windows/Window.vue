<template>
    {{ window?.Get_Top() }}
    <div v-if="window?.Get_IsOpen" class="window" :class="{ 'is-open': window?.Get_IsOpen }"
        style="top: {{ window?.Get_Top() }}px; left: {{ window?.Get_Left()}}px;">
        <div class="window-header" @mousedown="startDrag">
            <h2>{{ title }}</h2>
            <button @click="window!.closeWindow()">关闭</button>
        </div>
        <div class="window-content">
            窗口内容
            窗口内容
            窗口内容
            窗口内容
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { G_WindowNormal } from './class/G_WindowNormal';
const props = defineProps({
    title: String,
    isOpen: Boolean,
    top: Number,
    left: Number,
});
let window: G_WindowNormal | undefined = undefined;
const emit = defineEmits(['close']);
// 监听鼠标按下事件开始拖拽  
const startDrag = (event: MouseEvent) => {
    window!.dragStartX = event.clientX - window!.Get_Left();
    window!.dragStartY = event.clientY - window!.Get_Top();
    document.addEventListener('mousemove', doDrag);
    document.addEventListener('mouseup', stopDrag);
};
// 处理拖拽过程中的鼠标移动事件  
const doDrag = (event: MouseEvent) => {
    const newLeft = event.clientX - window!.dragStartX;
    const newTop = event.clientY - window!.dragStartY;
    // 更新窗口位置  
    window!.Set_Top(newLeft);
    window!.Set_Left(newTop);
    // 通知父组件更新位置  
    emit('update:top', newTop);
    emit('update:left', newLeft);
};
// 停止拖拽  
const stopDrag = () => {
    document.removeEventListener('mousemove', doDrag);
    document.removeEventListener('mouseup', stopDrag);
};

// 组件挂载时初始化窗口位置  
onMounted(() => {
    window = new G_WindowNormal(props.title!, props.top!, props.left!);
});

// 组件卸载时移除事件监听  
onUnmounted(() => {
    document.removeEventListener('mousemove', doDrag);
    document.removeEventListener('mouseup', stopDrag);
    window!.closeWindow();
});
</script>

<style scoped>
.window {
    position: absolute;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #fff;
    user-select: none;
    /* 禁止文本选择 */
    cursor: move;
    /* 鼠标悬停时显示可拖拽的样式 */
    transition: top 0.2s, left 0.2s;
    /* 平滑过渡效果 */
}

.window.is-open {
    /* 开放状态的样式 */
}

.window-header {
    padding: 10px;
    background-color: #f0f0f0;
    border-bottom: 1px solid #ccc;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.window-header h2 {
    margin: 0;
}

.window-content {
    padding: 10px;
    width: 400px;
    height: 300px;
    /* 窗口内容的样式 */
}
</style>