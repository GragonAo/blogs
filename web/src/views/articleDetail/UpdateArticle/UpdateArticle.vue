<template>
    <h2>修改文章</h2>
    <TextEditor v-if="form" :initialTitle="form?.title" :initialContent="form?.content"
        titlePlaceholder="请输入文章标题（5~100个字）" editorHeight="500px" submitButtonText="修改文章" @saveDraft="handleSaveDraft"
        @submit="handleSubmit" />
</template>

<script lang="ts" setup>
import { useRoute } from 'vue-router';
import TextEditor from '../components/TextEditor.vue';
import { GetArticleAPI, UpdateArticleAPI } from '@/API/Article';
import type { ArticleInfo } from '@/API/API_Types/Article';
import { onMounted, ref } from 'vue';
import router from '@/router';
import { ElMessage } from 'element-plus';
import useUserStore from '@/stores/User';
const form = ref<ArticleInfo>()
const getArticleInfo = async () => {
    const articleId = useRoute().params.articleId;
    await GetArticleAPI(articleId).then((res) => {

        if (res?.code === 200 && res.data.user === useUserStore().token?.user_id) {
            console.log(res);
            form.value = res?.data
        }
        else {
            ElMessage.error('没有权限!');
            router.push({
                name: 'index'
            });
        }
    }).catch((err) => {
        ElMessage.error(err);
        router.push({
            name: 'index'
        });
    });
}
const article = ref<ArticleInfo>()
const handleSaveDraft = (article: { title: string, content: string }) => {
    console.log('草稿已保存:', article);
};

const handleSubmit = async (article: { title: string, content: string }) => {
    form.value!.title = article.title;
    form.value!.content = article.content;
    await UpdateArticleAPI(form.value!.id!, form.value!).then((res) => {
        if (res?.code == 200)
            ElMessage.success('修改成功');
        else ElMessage.error(res?.message);
    }).catch((err) => {
        ElMessage.error(err);
    });
};
onMounted(() => {
    getArticleInfo();
})
</script>

<style scoped>
.el-header {
    background-color: rgba(240, 244, 249, 0.3);
    padding: 20px;
    text-align: center;
}

.el-main {
    padding: 20px;
}

.sidebar {
    background-color: #fff;
    padding: 20px;
    border-right: 1px solid #ebeef5;
}
</style>