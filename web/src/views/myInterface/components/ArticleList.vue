<template>
    <div class="article-list">
        <h3>最近文章</h3>
        <ul>
            <li v-for="article in articles" :key="article.id">
                <h4>{{ article.title }}</h4>
                <p>{{ article.description }}</p>
                <p class="meta">
                    <span>发布于 {{ article.date }}</span>
                    <span>阅读量: {{ article.views }}</span>
                </p>
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{
    articles: {
        id: number;
        title: string;
        description: string;
        date: string;
        views: number;
    }[];
}>();
</script>

<style scoped>
.article-list {
    margin-top: 20px;
}

.article-list ul {
    list-style: none;
    padding: 0;
}

.article-list li {
    margin-bottom: 20px;
}

.meta {
    color: #888;
}
</style>