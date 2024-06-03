<template>
    <el-row :gutter="20" class="article-card">
        <el-col :span="24">
            <el-card shadow="hover" class="box-card">
                <div class="card-header">
                    <h3>{{ article?.title }}</h3>
                </div>
                <div class="card-content">
                    <p>{{ article?.content }}</p>
                </div>
                <div class="card-footer">
                    <div class="meta-group">
                        <span class="meta">{{ formatDate(article?.create_time) }}</span>
                        <span class="meta">浏览: {{ article?.views }}</span>
                        <span class="meta">点赞: {{ article?.likes }}</span>
                        <span class="meta">分享: {{ article?.shares }}</span>
                    </div>
                    <div class="button-group">
                        <el-button type="primary" @click="viewArticle(article?.id)">查看详情</el-button>
                        <el-button v-if="user.userLoginInfo?.id === article?.user" type="primary"
                            @click="editArticle(article?.id)">修改</el-button>
                        <el-button v-if="user.userLoginInfo?.id === article?.user" type="danger"
                            @click="centerDialogVisible = true">删除</el-button>
                    </div>
                </div>
            </el-card>
        </el-col>
        <el-dialog v-model="centerDialogVisible" title="确定要删除这篇文章吗？" width="500" align-center>
            <div class="dialog-footer">
                <el-button @click="deleteArticle(article?.id)">确定</el-button>
                <el-button type="primary" @click="centerDialogVisible = false">
                    取消
                </el-button>
            </div>
        </el-dialog>
    </el-row>

</template>

<script setup lang="ts">
import router from '@/router';
import type { ArticleInfo } from '@/API/API_Types/Article';
import useUserStore from '@/stores/User';
import { DeleteArticleAPI } from '@/API/Article';
import { ref } from 'vue';
import { ElMessage } from 'element-plus';
const centerDialogVisible = ref(false)
const user = useUserStore();
defineProps<{
    article?: ArticleInfo
}>();

const viewArticle = (id?: number) => {
    if (id) {
        router.push({
            name: 'articlePage',
            params: { articleId: id }
        });
    } else {
        console.warn('Article ID is undefined');
    }
}
const editArticle = (id?: number) => {
    if (id) {
        router.push({
            name: 'articlePage',
            params: { articleId: id }
        });
    } else {
        console.warn('Article ID is undefined');
    }
}
const deleteArticle = async (id?: number) => {
    if (id) {
        await DeleteArticleAPI(id).then((res) => {
            ElMessage.success(res?.message);
        }).catch((err) => {
            ElMessage.error(err);
        });
    } else {
        console.warn('Article ID is undefined');
    }
}

const formatDate = (date: string | undefined) => {
    if (!date) return '';
    const options: Intl.DateTimeFormatOptions = {
        year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
    };
    return new Date(date).toLocaleDateString('zh-CN', options);
}
</script>

<style scoped>
.article-card {
    margin-bottom: 20px;
}

.box-card {
    transition: all 0.3s ease;
}

.box-card:hover {
    transform: translateY(-5px);
}

.card-header {
    border-bottom: 1px solid #ebeef5;
    margin-bottom: 10px;
}

.card-header h3 {
    font-size: 22px;
    margin: 0;
    color: #333;
}

.card-content p {
    font-size: 16px;
    color: #666;
    margin: 0 0 10px;
}

.card-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid #ebeef5;
    padding-top: 10px;
    margin-top: 10px;
}

.meta {
    font-size: 14px;
    color: #999;
}

.el-button {
    margin-left: auto;
}

.meta-group {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.button-group {
    display: flex;
    gap: 10px;
}
</style>