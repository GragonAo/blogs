<template>
    <h1>文章查询</h1>
    <el-scrollbar height="500">
        <span v-if="articles.length === 0">暂无文章</span>
        <el-row v-for="article in articles" :key="article.id">
            <ArticleCard style="width: 99%;" :article="article" />
        </el-row>
    </el-scrollbar>
</template>

<script setup lang='ts'>
import type { ArticleBasicInfo } from '@/API/API_Types/Article';
import ArticleCard from '../components/ArticleCard.vue';
import { onMounted, ref } from 'vue';
import { searchAPI } from '@/API/Article';
import { useRoute } from 'vue-router';
import { ElLoading } from 'element-plus';
const articles = ref<ArticleBasicInfo[]>([]);
const getArticleList = async () => {
    const searchContent = useRoute().params.searchContent;
    const loading = ElLoading.service({
        lock: true,
        text: 'Loading',
        background: 'rgba(0, 0, 0, 0.7)',
    })
    await searchAPI(searchContent).then((res) => {
        if (res?.code === 200) {
            articles.value = res.data
        }
    }).finally(() => {
        loading.close();
    });
}
onMounted(() => {
    getArticleList();
})
</script>

<style scoped></style>