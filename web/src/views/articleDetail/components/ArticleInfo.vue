<template>
    <el-card>
        <div class="article-info">
            <el-row>
                <el-col :span="20">
                    <h1>{{ article.title }}</h1>
                    <div class="meta">
                        <span>{{ formatDate(article.update_time) }}</span>
                        <span>阅读量: {{ article.views }}</span>
                    </div>
                </el-col>
                <el-col :span="4">
                    <el-row justify="center">
                        <el-col :span="24" class="avatar-container">
                            <el-image style="width: 100px; height: 100px; border-radius: 50%;"
                                :src="APP_CONFIG.baseURL + article.avatar" />
                        </el-col>
                    </el-row>
                    <el-row justify="center">
                        <el-col :span="24" class="username-container">
                            <span>Username: {{ article.username }}</span>
                        </el-col>
                    </el-row>
                    <el-row v-if="article.user == user?.token?.user_id" justify="center" style="padding-top: 10px;">
                        <el-button-group class="ml-4">
                            <el-button type="primary" @click="goTOPath('updateArticle', { articleId: article.id })"
                                :icon="Edit" />
                            <el-button type="primary" @click="centerDialogVisible = true" :icon="Delete" />
                        </el-button-group>
                    </el-row>
                </el-col>
            </el-row>
            <el-divider />
            <el-row>
                <div class="content">
                    <MdPreview :modelValue="article.content" height="500px" />
                </div>
            </el-row>
        </div>
        <el-dialog v-model="centerDialogVisible" title="确定要删除该文章？" width="500" align-center>
            <div class="dialog-footer">
                <el-button @click="centerDialogVisible = false">取消</el-button>
                <el-button type="primary" @click="deleteArticle">
                    确定
                </el-button>
            </div>
        </el-dialog>
    </el-card>

</template>

<script setup lang="ts">
import { defineProps, ref } from 'vue';
import { MdPreview } from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import type { ArticleDetailInfo } from '@/API/API_Types/Article.d.ts';
import {
    Delete,
    Edit,
} from '@element-plus/icons-vue'
import useUserStore from '@/stores/User';
import { DeleteArticleAPI } from '@/API/Article';
import { ElMessage } from 'element-plus';
import router from '@/router';
import { APP_CONFIG } from '~/app.config';
const user = useUserStore();
const centerDialogVisible = ref(false)
const props = defineProps<{
    article: ArticleDetailInfo
}>();
const deleteArticle = async () => {
    if (props.article.id) {
        await DeleteArticleAPI(props.article.id).then((res) => {
            ElMessage.success('删除成功');
        }).catch((err) => {
            ElMessage.error(err);
        }).finally(() => {

        });
    }
}
const goTOPath = (name: string, param?: Record<string, any>) => {
    if (param) {
        router.push({
            name: name,
            params: param
        });
    } else {
        router.push({
            name: name,
        });
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
.article-info {
    margin: 20px;
}

.meta {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
    color: #888;
}

.content {
    margin-top: 20px;
}

.avatar-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 10px;
}

.username-container {
    text-align: center;
    font-weight: bold;
    margin-bottom: 10px;
}

.button-container {
    display: flex;
    justify-content: center;
}
</style>