<template>
    <div class="container">
        <el-scrollbar height="500px" class="scrollbar">
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
import type { ArticleInfo } from '@/API/API_Types/Article';

const route = useRoute();
const user = ref({
    avatar: '', // 替换为你的头像路径
    name: 'The-Venus',
    description: '全栈领域优质创作者',
    original: 271,
    weekRank: 36,
    totalRank: 471,
    badges: [], // 替换为你的徽章路径
});

const article = ref<ArticleInfo>();

const getArticleInfo = async () => {
    const id = route.params.articleId; // 获取路径参数中的id
    console.log(id);
    const res = await GetArticleAPI(id);
    console.log(res);
    if (res?.code === 200) {
        article.value = res.data; // 假设返回的数据结构是正确的
    }
}
const formatDate = (date: string | undefined) => {
    if (!date) return '';
    const options: Intl.DateTimeFormatOptions = {
        year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
    };
    return new Date(date).toLocaleDateString('zh-CN', options);
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