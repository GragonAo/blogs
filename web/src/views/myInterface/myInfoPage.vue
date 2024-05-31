<template>
    <div class="container">
        <header>
            <UserInfo :user="user" />
        </header>
        <div class="content">
            <aside class="sidebar">
                <UserAchievements :achievements="achievements" />
            </aside>
            <main class="main-content">
                <ArticleList :articles="articles" />
            </main>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import UserInfo from './components/UserHomeInfo.vue';
import UserAchievements from './components/UserAchievements.vue';
import ArticleList from './components/ArticleList.vue';

const user = ref({
    avatar: '/path/to/avatar.jpg', // 替换为你的头像路径
    name: 'Gragon-Li',
    totalViews: 30721,
    rank: 77,
    description: 'every effort has its rewards.',
    ipLocation: '福建省',
});

const achievements = ref([
    { title: '总访问量', count: 30721 },
    { title: '原创', count: 77 },
    { title: '排名', count: 1943259 },
]);

const articles = ref([
    {
        id: 1,
        title: 'NOIP2003提高组——加分二叉树',
        description: '题目：设一个节点的二叉树 tree 的中序遍历为(1,2,3,...,n1,2,3,...,n)，其中节点编号。',
        date: '2022-05-31',
        views: 232,
    },
    {
        id: 2,
        title: '凸多边形的划分',
        description: '题目：给定一个 n 个顶点的凸多边形，每个顶点的权值都是一个正整数。',
        date: '2022-05-31',
        views: 882,
    },
    {
        id: 3,
        title: 'LeetCode——1143. 最长公共子序列',
        description: '给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。',
        date: '2022-05-31',
        views: 1475,
    },
]);
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