<template>

    <div class="blog-content">
        <el-row>
            <el-col :span="18">
                <el-main>
                    <el-scrollbar max-height="600px" wrap-class="scrollbar-wrapper">
                        <section class="blog-posts">
                            <h2>Latest Blog Posts</h2>
                            <el-row :gutter="20" class="post-row" v-for="post in posts" :key="post.id">
                                <el-col :span="24">
                                    <el-card class="blog-post-card">
                                        <div slot="header" class="post-header">
                                            <h3>{{ post.title }}</h3>
                                        </div>
                                        <div slot="body" class="post-body">
                                            <p>{{ post.content }}</p>
                                        </div>
                                        <div slot="footer" class="post-footer">
                                            <el-button type="text" class="read-more" @click="goToPost(post.id)">Read
                                                More</el-button>
                                        </div>
                                    </el-card>
                                </el-col>
                            </el-row>
                        </section>
                    </el-scrollbar>
                </el-main>
            </el-col>
            <el-col :span="4">
                <el-aside width="300px">
                    <div class="blog-sidebar">
                        <h3>Popular Tags</h3>
                        <el-scrollbar max-height="200px">
                            <el-card class="tag-card" v-for="tag in tags" :key="tag.id">
                                <div slot="header" class="tag-header">
                                    <span class="tag-name">{{ tag.name }}</span>
                                </div>
                            </el-card>
                        </el-scrollbar>
                    </div>
                    <el-card class="calendar-card">
                        <el-calendar v-model="value" />
                    </el-card>
                </el-aside>
            </el-col>
        </el-row>
    </div>
</template>

<script setup lang='ts'>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import type { ArticleInfo } from '@/API/API_Types/Article';
import { GetArtiecleListAPI } from '@/API/Article';
const router = useRouter();
const value = ref(new Date())
// 模拟数据  
const posts = ref<ArticleInfo[]>();
const tags = ref([
    { id: 1, name: 'Vue' },
    { id: 2, name: 'JavaScript' },
    { id: 3, name: 'Frontend' },
    { id: 3, name: 'Frontend' },
    { id: 3, name: 'Frontend' },
    { id: 3, name: 'Frontend' },
    { id: 3, name: 'Frontend' },
    { id: 3, name: 'Frontend' },
    // 更多标签...  
]);

// 跳转到文章详情页的方法（假设您有一个路由配置来显示文章详情）  
const goToPost = (articleId: number) => {
    // 这里使用路由跳转，需要确保您的项目中已经安装并配置好了vue-router  
    router.push({ name: 'articleDetail', params: { articleId: articleId } });
}
const getArticleList = async () => {
    const res = await GetArtiecleListAPI();
    if (res!.code >= 200 && res!.code < 300) {
        posts.value = res!.data;
    } else {

    }
}
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
    /* 或者一个具体的宽度值 */
    overflow-x: hidden;
    /* 隐藏水平方向的滚动条 */
}

.tag-card {
    margin-bottom: 10px;
}

.scrollbar-wrapper {
    overflow-x: hidden;
    /* 确保滚动条容器本身也不会水平滚动 */
}

.blog-sidebar {
    /* 设定侧边栏的宽度 */
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

.calendar-card {
    margin-top: 30px;
    height: 300px;
}
</style>