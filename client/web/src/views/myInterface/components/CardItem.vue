<template>
    <div class="card-group" style="display: flex; flex-wrap: wrap;">
        <el-card v-for="(card, index) in cards" :key="index" class="card" :style="{ width: cardWidth, }"
            style="height: 200px;" @mouseover="cardHovered(index)" @mouseout="cardLeft(index)">
            <div class="card-content">
                {{ card.content }}
            </div>
        </el-card>
    </div>
</template>

<script setup lang='ts'>
import { computed, ref } from 'vue';
// 假设的卡片数据    
const cards = ref([
    { content: 'Card 1 Content' },
    { content: 'Card 2 Content' },
    { content: 'Card 2 Content' },
    { content: 'Card 2 Content' },


    // ... 其他卡片数据  
]);

// 计算属性：卡片的宽度  
const cardWidth = computed(() => {
    return 'calc(50% - 20px)';
});

// 计算属性：卡片的高度，保持10/15的比例  
const cardHeight = computed(() => {
    return `calc(${cardWidth.value} * 10 / 13)`;
});

// 卡片悬停状态  
const hoveredCard = ref(null);

const cardHovered = (index) => {
    hoveredCard.value = index;
};

const cardLeft = () => {
    hoveredCard.value = null;
};
</script>

<style scoped>
.card-group {
    /* 让卡片从左边开始排列 */
    justify-content: flex-start;
}

.card {
    box-sizing: border-box;
    margin-right: 5px;
    margin-left: 5px;
    margin-bottom: 20px;
    background-color: #fff;
    /* 或者你想要的背景色 */
    transition: transform 0.2s ease-in-out;
    /* 添加过渡效果 */
    position: relative;
    /* 用于定位悬停效果 */
}

/* 清除每行最后一个卡片的右边距 */
.card-group .card:nth-last-child(1) {
    margin-right: 0;
}

/* 使用媒体查询在屏幕宽度较大时变为三个卡片一行 */
@media (min-width: 600px) {
    .card {
        flex: 0 0 calc(33.3333% - 20px);
    }

    /* 清除每行第三个卡片的右边距 */
    .card-group .card:nth-child(3n) {
        margin-right: 0;
    }

    /* 重新设置每行最后一个和倒数第二个卡片的右边距 */
    .card-group .card:nth-last-child(1),
    .card-group .card:nth-last-child(2) {
        margin-right: 20px;
    }
}

/* 卡片悬停效果 */
.card:hover {
    transform: scale(1.02);
    /* 稍微放大卡片 */
    z-index: 1;
    /* 提升卡片层级 */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    /* 添加阴影 */
}

/* 卡片内容样式 */
.card-content {
    padding: 10px;
    /* 根据需要调整内边距 */
}
</style>