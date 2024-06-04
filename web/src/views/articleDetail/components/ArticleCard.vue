<template>
    <el-row :gutter="20" class="article-card">
        <el-col :span="24">
            <el-card shadow="hover" class="box-card">
                <div class="card-header">
                    <h3>{{ article?.title }}</h3>
                </div>
                <div class="card-content">
                    <p>{{ truncatedContent }}</p>
                </div>
                <div class="card-footer">
                    <div class="meta-group">
                        <span class="meta">{{ formatDate(article?.create_time) }}</span>
                        <span class="meta">浏览: {{ article?.views }}</span>
                        <span class="meta">点赞: {{ article?.likes }}</span>
                        <span class="meta">分享: {{ article?.shares }}</span>
                    </div>
                    <div class="button-group">
                        <el-button type="primary" @click="viewArticle(article?.id)">查看详情</el-button>
                    </div>
                </div>
            </el-card>
        </el-col>
    </el-row>
</template>

<script setup lang="ts">
import router from '@/router';
import type { ArticleInfo } from '@/API/API_Types/Article';
import { computed } from 'vue';

// 使用 defineProps 定义 props
const props = defineProps<{
    article?: ArticleInfo
}>();

// 定义截断内容的计算属性
const truncatedContent = computed(() => {
    if (!props.article || !props.article.content) return '';
    const maxLength = 100;
    return props.article.content.length > maxLength
        ? props.article.content.slice(0, maxLength) + '...'
        : props.article.content;
});

// 定义查看文章的函数
const viewArticle = (id?: number) => {
    if (id) {
        router.push({
            name: 'articlePage',
            params: { articleId: id }
        });
    } else {
        console.warn('Article ID is undefined');
    }
}

// 定义格式化日期的函数
const formatDate = (date: string | undefined) => {
    if (!date) return '';
    const options: Intl.DateTimeFormatOptions = {
        year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
    };
    return new Date(date).toLocaleDateString('zh-CN', options);
}
</script>

<style scoped>
.article-card {
    margin-bottom: 20px;
}

.box-card {
    transition: all 0.3s ease;
}

.box-card:hover {
    transform: translateY(-5px);
}

.card-header {
    border-bottom: 1px solid #ebeef5;
    margin-bottom: 10px;
}

.card-header h3 {
    font-size: 22px;
    margin: 0;
    color: #333;
}

.card-content p {
    font-size: 16px;
    color: #666;
    margin: 0 0 10px;
}

.card-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid #ebeef5;
    padding-top: 10px;
    margin-top: 10px;
}

.meta {
    font-size: 14px;
    color: #999;
}

.el-button {
    margin-left: auto;
}

.meta-group {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.button-group {
    display: flex;
    gap: 10px;
}
</style>
