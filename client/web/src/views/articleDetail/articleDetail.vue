<template>
    <el-table v-if="!article" v-loading="!article" style="width: 100%"></el-table>
    <div class="article-detail" v-if="article">
        <h1 class="article-title">{{ article.title }}</h1>
        <p class="article-meta">Published on {{ article.create_time }} by {{ article.user }}</p>
        <div class="article-content" v-html="article.content"></div>
    </div>
</template>

<script setup lang='ts'>
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import type { ArticleInfo } from '@/API/API_Types/Article';
import { GetArticleAPI } from '@/API/Article';
// 使用 reactive 创建一个响应式对象来存储文章数据  
const article = ref<ArticleInfo | null>(null);
const route = useRoute();

const getArticle = async (articleId: number) => {
    const res = await GetArticleAPI(articleId);
    if (res!.code >= 200 && res!.code < 300) {
        article.value = res!.data;
    } else {

    }
};
onMounted(() => {
    // 假设路由路径是 /article/:id  
    console.log(route.params); // 打印整个路由参数对象  
    const articleId = parseInt(route.params.articleId as string, 10);
    console.log(articleId);
    getArticle(articleId);
});

// 监听路由参数的变化  
watch(() => route.params.id, (newId) => {

    const articleId = parseInt(newId as string, 10);
    getArticle(articleId);
});  
</script>
<style scoped>
.article-detail {}

.article-title {
    margin-bottom: 10px;
    font-size: 2rem;
    /* 增大标题字体大小 */
    font-weight: bold;
    /* 设置标题为粗体 */
}

.article-meta {
    font-size: 0.875rem;
    color: #6c757d;
    margin-bottom: 20px;
}

.article-content {
    line-height: 1.6;
    font-size: 1rem;
    /* 设置内容字体大小 */
}

/* 添加一些边距和颜色以美化列表项 */
.article-content ul {
    list-style-type: disc;
    padding-left: 20px;
}

.article-content li {
    margin-bottom: 5px;
}
</style>