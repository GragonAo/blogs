<template>
    <div class="container">
        <aside class="sidebar">
            <UserInfo :user="user" />
            <div class="subscribe">
                <button>私信</button>
                <button>关注</button>
            </div>
            <div class="promotion">
                <img src="" alt="Promotion" />
            </div>
        </aside>
        <main class="main-content">
            <ArticleInfo title="【架构之路】提升后端接口性能的实战技巧" author="The-Venus" date="2024-05-17 08:00:00" :views="5000"
                content="<h2>你眼中的IT行业现状与未来趋势</h2><p>文章内容...</p>" />
        </main>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import UserInfo from './components/UserInfo.vue';
import ArticleInfo from './components/ArticleInfo.vue';

const user = ref({
    avatar: '', // 替换为你的头像路径
    name: 'The-Venus',
    description: '全栈领域优质创作者',
    original: 271,
    weekRank: 36,
    totalRank: 471,
    badges: ['', '', ''], // 替换为你的徽章路径
});
</script>

<style scoped>
.container {
    display: flex;
}

.sidebar {
    width: 250px;
    padding: 20px;
    border-right: 1px solid #ddd;
}

.subscribe {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}

.promotion {
    margin-top: 20px;
}

.promotion img {
    width: 100%;
}

.main-content {
    flex: 1;
    padding: 20px;
}
</style>