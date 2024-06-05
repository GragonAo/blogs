<template>
    <div class="container">
        <header>
            <UserInfo />
        </header>
        <div class="content">
            <aside class="sidebar">
                <UserAchievements :achievements="achievements" />
            </aside>
            <main class="main-content">
                <el-scrollbar height="500">
                    <el-row class="post-row" v-for="article in articles" :key="article.id">
                        <ArticleCard style="width: 99%;" :article="article" />
                    </el-row>
                </el-scrollbar>
            </main>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import UserInfo from './components/UserHomeInfo.vue';
import UserAchievements from './components/UserAchievements.vue';
import ArticleCard from '@/views/articleDetail/components/ArticleCard.vue';
import type { ArticleBasicInfo } from '@/API/API_Types/Article';
import { GetUserArticlesAPI } from '@/API/Article';
import { ElLoading, ElMessage } from 'element-plus';

const achievements = ref([
    { title: '总访问量', count: 0 },
    { title: '原创', count: 0 },
    { title: '排名', count: 0 },
]);

const articles = ref<ArticleBasicInfo[]>([]);

const calculateAchievements = () => {
    const totalViews = articles.value.reduce((sum, article) => sum + article.views!, 0);
    const originalArticlesCount = articles.value.length;
    const ranking = originalArticlesCount ? 100 - originalArticlesCount : 100;
    achievements.value = [
        { title: '总访问量', count: totalViews },
        { title: '原创', count: originalArticlesCount },
        { title: '排名', count: ranking },
    ];
};

const getArticle = async () => {
    const loading = ElLoading.service({
        lock: true,
        text: 'Loading',
        background: 'rgba(0, 0, 0, 0.3)',
    });
    await GetUserArticlesAPI().then((res) => {
        if (res?.code == 200) {
            articles.value = res?.data;
            calculateAchievements();
            ElMessage.success("查询成功");
        }
    }).catch((err) => {
        ElMessage.error(err);
        return;
    }).finally(() => {
        loading.close();
    });
};

onMounted(() => {
    getArticle();
});
</script>

<style scoped>
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    display: flex;
    justify-content: center;
    border-bottom: 1px solid #ddd;
    padding-bottom: 20px;
}

.content {
    display: flex;
    margin-top: 20px;
}

.sidebar {
    width: 300px;
    padding-right: 20px;
    border-right: 1px solid #ddd;
}

.main-content {
    flex: 1;
    padding-left: 20px;
}
</style>