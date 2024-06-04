<template>
    <el-progress style="margin-top: 50px;" v-if="loading" :percentage="progress" :indeterminate="false" />
    <div class="container">
        <el-scrollbar height="600px" class="scrollbar">
            <el-row gutter="20">
                <el-col :span="24">
                    <Article v-if="article" :article="article!" />
                </el-col>
            </el-row>
        </el-scrollbar>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import Article from './components/ArticleInfo.vue';
import { GetArticleAPI } from '@/API/Article';
import type { ArticleDetailInfo } from '@/API/API_Types/Article';
const loading = ref<boolean>(false);
const progress = ref<number>(0);
const route = useRoute();
const article = ref<ArticleDetailInfo>();
const getArticleInfo = async () => {
    const id = route.params.articleId; // 获取路径参数中的id
    loading.value = true;
    progress.value = 0;
    // 模拟进度条加载
    const interval = setInterval(() => {
        if (progress.value < 90) {
            progress.value += 10;
        }
    }, 300);
    await GetArticleAPI(id).then((res) => {
        if (res?.code === 200) {
            article.value = res.data; // 假设返回的数据结构是正确的
        }
    }).finally(() => {
        clearInterval(interval);
        progress.value = 100;
        loading.value = false;
    });
}
onMounted(() => {
    getArticleInfo();
});
</script>

<style scoped>
.container {
    display: flex;
    padding-top: 20px;
    height: 100%;
    width: 100%;
}

.scrollbar {
    width: 100%;
    padding: 20px;
}

.sidebar {
    width: 250px;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.subscribe {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}

.btn {
    background-color: #409eff;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn:hover {
    background-color: #66b1ff;
}

.promotion {
    margin-top: 20px;
}

.promotion img {
    width: 100%;
    border-radius: 8px;
}

.main-content {
    flex: 1;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
</style>