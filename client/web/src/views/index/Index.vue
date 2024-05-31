<template>
    <div class="blog-content">
        <el-row>
            <el-col :span="19">
                <el-main>
                    <el-scrollbar max-height="600px" wrap-class="scrollbar-wrapper">
                        <section class="blog-posts">
                            <h2>Latest Blog Posts</h2>
                            <el-row :gutter="20" class="post-row" v-for="post in posts" :key="post.id">
                                <el-col :span="24">
                                    <el-card class="blog-post-card">
                                        <template #header>
                                            <h3>{{ post.title }}</h3>
                                        </template>
                                        <template #default>
                                            <p>{{ post.content }}</p>
                                        </template>
                                        <template #footer>
                                            <el-button type="text" class="read-more" @click="goToPost(post.id)">Read
                                                More</el-button>
                                        </template>
                                    </el-card>
                                </el-col>
                            </el-row>
                        </section>
                    </el-scrollbar>
                </el-main>
            </el-col>
            <el-col :span="5">
                <el-aside width="300px" style="padding-right: 20px;">
                    <div class="blog-sidebar">
                        <h3>Popular Tags</h3>
                        <el-scrollbar max-height="200px">
                            <el-card class="tag-card" v-for="tag in tags" :key="tag.id">
                                <template #header>
                                    <span class="tag-name">{{ tag.name }}</span>
                                </template>
                            </el-card>
                        </el-scrollbar>
                    </div>
                    <Calendar />
                </el-aside>
            </el-col>
        </el-row>
    </div>
</template>

<script setup lang='ts'>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import Calendar from '@/components/calendar/Calendar.vue';
import type { ArticleInfo } from '@/API/API_Types/Article';
import { GetArtiecleListAPI } from '@/API/Article';

const router = useRouter();
const posts = ref<ArticleInfo[]>([]);
const tags = ref([
    { id: 1, name: 'Vue' },
    { id: 2, name: 'JavaScript' },
    { id: 3, name: 'Frontend' },
    { id: 4, name: 'CSS' },
]);

const goToPost = (articleId: number) => {
    router.push({ name: 'articleDetail', params: { articleId } });
};

const getArticleList = async () => {
    const res = await GetArtiecleListAPI();
    if (res.code >= 200 && res.code < 300) {
        posts.value = res.data;
    } else {
        // 处理错误
    }
};

onMounted(() => {
    getArticleList();
});
</script>

<style scoped>
.blog-content {
    padding: 20px;
}

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