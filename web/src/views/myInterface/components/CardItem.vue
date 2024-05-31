<template>
    <div class="card-group" style="display: flex; flex-wrap: wrap;">
        <el-card v-for="(card, index) in cards" :key="index" class="card" :style="{ width: cardWidth }"
            style="height: 200px;" @mouseover="cardHovered(index)" @mouseout="cardLeft(index)">
            <div class="card-content">
                <h3>{{ card.name }}</h3>
                <p>{{ card.description || 'No description available' }}</p>
                <p><strong>Language:</strong> {{ card.language || 'N/A' }}</p>
                <a :href="card.html_url" target="_blank">View on GitHub</a>
            </div>
        </el-card>
    </div>
</template>

<script setup lang="ts">
import Http from '@/G_FrameWork/Net/Http';
import SingletonFactory from '@/G_FrameWork/SingletonFactory';
import { computed, ref, onMounted } from 'vue';


interface Repo {
    name: string;
    description: string | null;
    html_url: string;
    language: string | null;
}

const cards = ref<Repo[]>([]);

const fetchGitHubRepos = async () => {
    try {
        const response = await SingletonFactory.getInstance(Http).get('https://api.github.com/users/MyHolleworld/repos');
        cards.value = response.data;
        console.log(cards.value)
    } catch (error) {
        console.error('Error fetching GitHub repositories:', error);
    }
};

onMounted(fetchGitHubRepos);

const cardWidth = computed(() => {
    return 'calc(50% - 20px)';
});

const cardHeight = computed(() => {
    return `calc(${cardWidth.value} * 10 / 13)`;
});

const hoveredCard = ref<number | null>(null);

const cardHovered = (index: number) => {
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