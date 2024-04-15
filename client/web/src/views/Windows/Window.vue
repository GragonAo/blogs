<template>
    <div v-if="isOpen" class="window" :class="{ 'is-open': isOpen }" :style="{ top: `${top}px`, left: `${left}px` }">
        <div class="window-header" @mousedown="startDrag">
            <h2>{{ title }}</h2>
            <button @click="closeWindow">关闭</button>
        </div>
        <div class="window-content">
            <MonacoEditor :codeEditBoxName="codeEditBoxId"></MonacoEditor>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, defineProps, defineEmits, computed } from 'vue';
import { G_WindowNormal } from './class/G_WindowNormal';
import G_WindowSystem from './class/G_WindowSystem';
import SingletonFactory from '@/G_FrameWork/SingletonFactory';
import MonacoEditor from '@/components/editor/MonacoEditor.vue'
const props = defineProps({
    windowId: Number,
    title: String,
    top: {
        type: Number,
        default: 0
    },
    left: {
        type: Number,
        default: 0
    },
});
const emit = defineEmits(['update:top', 'update:left', 'op:close', 'op:destroy']);
const windowRef = ref<G_WindowNormal | null>(null);
const isOpen = computed(() => windowRef.value?.IsOpen ?? false);
const top = computed({
    get() {
        return windowRef.value?.Top ?? props.top;
    },
    set(value) {
        emit('update:top', value);
    }
});

const left = computed({
    get() {
        return windowRef.value?.Left ?? props.left;
    },
    set(value) {
        emit('update:left', value);
    }
});

const codeEditBoxId = computed(() => {
    return "codeEditBox" + windowRef.value?.getWindowId();
});

const startDrag = (event: MouseEvent) => {
    if (!windowRef.value) return;
    windowRef.value.dragStartX = event.clientX - windowRef.value.Left;
    windowRef.value.dragStartY = event.clientY - windowRef.value.Top;
    document.addEventListener('mousemove', doDrag);
    document.addEventListener('mouseup', stopDrag);
};

const doDrag = (event: MouseEvent) => {
    if (!windowRef.value) return;
    const newLeft = event.clientX - windowRef.value.dragStartX;
    const newTop = event.clientY - windowRef.value.dragStartY;
    top.value = newTop;
    left.value = newLeft;
};

const stopDrag = () => {
    document.removeEventListener('mousemove', doDrag);
    document.removeEventListener('mouseup', stopDrag);
};
const closeWindow = () => {
    emit('op:close', windowRef.value?.getWindowId());
}
onMounted(() => {
    windowRef.value = SingletonFactory.getInstance(G_WindowSystem).getWindowById<G_WindowNormal>(props.windowId!);
});

onUnmounted(() => {
    // 移除事件监听器  
    document.removeEventListener('mousemove', doDrag);
    document.removeEventListener('mouseup', stopDrag);
    // 关闭窗口并清空引用  
    if (windowRef.value) {
        emit('op:destroy', windowRef.value.getWindowId());
        windowRef.value = null;
    }
});
</script>

<style scoped>
.window {
    position: absolute;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #fff;
    user-select: none;
    cursor: move;
    transition: top 0.2s, left 0.2s;
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
    width: 700px;
    height: 500px;
}
</style>
