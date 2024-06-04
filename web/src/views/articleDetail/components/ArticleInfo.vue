<template>
    <el-card>
        <div class="article-info">
            <el-row>
                <el-col :span="20">
                    <h1>{{ article.title }}</h1>
                    <div class="meta">
                        <span>{{ article.update_time }}</span>
                        <span>阅读量: {{ article.views }}</span>
                    </div>
                </el-col>
                <el-col :span="4">
                    <el-row>
                        <el-col :span="24">
                            <el-image style="width: 100px; height: 100px; border-radius: 50%;"
                                :src="user.userLoginInfo?.avatar" />
                        </el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="24">
                            <span>Username:{{ user?.token?.user_id }}</span>
                        </el-col>
                    </el-row>
                    <el-row v-if="article.user == user?.token?.user_id" style="padding-top: 10px;">
                        <el-col :span="12">
                            <el-button type="primary" @click="goTOPath('updateArticle', { articleId: article.id })"
                                :icon="Edit" circle />
                        </el-col>
                        <el-col :span="12">
                            <el-button type="danger" @click="centerDialogVisible = true" :icon="Delete" circle />
                        </el-col>
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
import type { ArticleInfo } from '@/API/API_Types/Article.d.ts';
import {
    Delete,
    Edit,
} from '@element-plus/icons-vue'
import useUserStore from '@/stores/User';
import { DeleteArticleAPI } from '@/API/Article';
import { ElMessage } from 'element-plus';
import router from '@/router';
const user = useUserStore();
const centerDialogVisible = ref(false)
const props = defineProps<{
    article: ArticleInfo
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
</style>