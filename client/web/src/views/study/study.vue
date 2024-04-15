<template>
    <div class="learning-interface">
        <div class="timeline-container">
            <div class="timeline">
                <div v-for="(item, index) in timelineItems" :key="index" class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <h3>{{ item.title }}</h3>
                        <p>{{ item.description }}</p>
                        <button @click="showContent(item)">查看详情</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const timelineItems = ref([
    {
        title: '学习阶段 1',
        description: '这是学习阶段 1 的描述',
        // chartData: { /* 图表数据 */ },  
    },
    {
        title: '学习阶段 2',
        description: '这是学习阶段 2 的描述',
        // chartData: { /* 图表数据 */ },  
    },
    // ...更多学习阶段  
]);

const currentItemIndex = ref(0);

const showContent = (item: any) => {
    currentItemIndex.value = timelineItems.value.indexOf(item);
    // 这里可以添加显示图表的逻辑  
};  
</script>

<style scoped>
.learning-interface {
    display: flex;
    flex-direction: column;
    height: 100vh;
    padding: 20px;
    box-sizing: border-box;
    background-color: #f5f5f5;
    /* 添加背景色 */
}

.timeline-container {
    width: 100%;
    /* 确保容器宽度 */
    max-width: 800px;
    /* 可选：设置最大宽度 */
    margin: 0 auto;
    /* 水平居中 */
}

.timeline {
    display: flex;
    flex-direction: column;
    list-style: none;
    /* 移除默认的列表样式 */
    padding: 0;
    /* 移除默认的列表内边距 */
}

.timeline-item {
    position: relative;
    padding-left: 30px;
    /* 为时间线标记留出空间 */
    margin-bottom: 20px;
}

.timeline-marker {
    width: 10px;
    height: 10px;
    background-color: #3498db;
    border-radius: 50%;
    position: absolute;
    left: 0;
    top: 5px;
}

.timeline-content {
    /* 无需额外样式，保持左对齐即可 */
}

/* 添加按钮样式 */
.timeline-content button {
    margin-top: 10px;
    padding: 5px 10px;
    background-color: #3498db;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

/* 可选：添加hover效果 */
.timeline-content button:hover {
    background-color: #2980b9;
}
</style>