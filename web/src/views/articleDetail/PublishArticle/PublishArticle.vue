<template>
    <h2>发布文章</h2>
    <TextEditor :initialTitle="article?.title" :initialContent="article?.content" titlePlaceholder="请输入文章标题（5~100个字）"
        editorHeight="500px" submitButtonText="发布文章" @saveDraft="handleSaveDraft" @submit="handleSubmit" />
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import TextEditor from '../components/TextEditor.vue';
import type { ArticleInfo } from '@/API/API_Types/Article';
import useArticleStore from '@/stores/Article';
import { CreateArticleAPI } from '@/API/Article';
import { ElMessage } from 'element-plus';
const article = ref<ArticleInfo>()
const handleSaveDraft = (article: { title: string, content: string }) => {
    console.log('草稿已保存:', article);
};

const handleSubmit = async (article: { title: string, content: string }) => {
    await CreateArticleAPI(article.title, article.content).then((res) => {
        if (res?.code == 200)
            ElMessage.success('发表成功');
        else ElMessage.error(res?.message);
    }).catch((err) => {
        ElMessage.error(err);
    });
};
onMounted(() => {
    article.value = useArticleStore().useArticleInfo;
})
</script>

<style scoped></style>
