复制代码
<template>
    <el-row>
        <el-col :span="18">
            <el-main>
                <h2>最新文章</h2>
                <el-scrollbar height="500">
                    <el-progress v-if="loading" :percentage="progress" :indeterminate="false" />
                    <el-row v-for="article in articles" :key="article.id">
                        <ArticleCard style="width: 99%;" :article="article" />
                    </el-row>
                </el-scrollbar>
            </el-main>
        </el-col>
        <el-col :span="6">
            <el-aside style="padding-right: 5px;">
                <TimeCard style="margin-top:50px;" />
                <Calendar />
            </el-aside>
        </el-col>
    </el-row>
</template>

<script setup lang='ts'>
import { onMounted, ref } from 'vue';
import Calendar from '@/components/calendar/Calendar.vue';
import TimeCard from '@/components/TimeCard/TimeCard.vue';
import type { ArticleBasicInfo } from '@/API/API_Types/Article';
import { GetArtiecleListAPI } from '@/API/Article';
import ArticleCard from '../articleDetail/components/ArticleCard.vue';

const articles = ref<ArticleBasicInfo[]>([]);
const loading = ref<boolean>(false);
const progress = ref<number>(0);

const getArticleList = async () => {
    loading.value = true;
    progress.value = 0;
    const interval = setInterval(() => {
        if (progress.value < 90) {
            progress.value += 10;
        }
    }, 300);
    await GetArtiecleListAPI().then((res) => {
        articles.value = res!.data;
    }).catch((err) => {
        console.error('Error fetching articles:', err);
    }).finally(() => {
        clearInterval(interval);
        progress.value = 100;
        loading.value = false;
    })
}

onMounted(() => {
    getArticleList();
});
</script>

<style scoped>
.blog-main-content {
    display: flex;
}

.blog-posts {
    flex: 1;
    width: 100%;
    overflow-x: hidden;
}

.tag-card {
    margin-bottom: 10px;
}

.scrollbar-wrapper {
    overflow-x: hidden;
}

.blog-sidebar {
    background-color: #f5f5f5;
    padding: 10px;
    margin-left: 20px;
}

.blog-post-card {
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    border-radius: 4px;
    margin-bottom: 20px;
    overflow: hidden;
}

.post-header {
    padding: 15px;
    border-bottom: 1px solid #eee;
}

.post-header h3 {
    margin: 0;
    font-size: 18px;
    line-height: 1.5;
}

.post-body {
    padding: 15px;
}

.post-body p {
    margin: 0;
}

.post-footer {
    padding: 10px 15px;
    border-top: 1px solid #eee;
    text-align: right;
}

.read-more {
    color: blue;
    text-decoration: underline;
}
</style>