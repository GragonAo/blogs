<template>
    <el-card>
        <el-form :model="form" label-width="80px">
            <el-form-item label="标题">
                <el-input v-model="form.title" placeholder="请输入文章标题（5~100个字）"></el-input>
            </el-form-item>
            <el-form-item label="内容">
                <md-editor v-model="form.content" height="500px" @onUploadImg="handleUploadImg" />
            </el-form-item>
        </el-form>
        <el-divider></el-divider>
        <div class="toolbar">
            <el-button @click="clearArticle">清空文章</el-button>
            <el-button v-if="isEditing" @click="isEditing = false">预览文章</el-button>
            <el-button v-else @click="isEditing = true">编辑文章</el-button>
            <el-button @click="handleSaveDraft">保存草稿</el-button>
            <el-button type="primary" @click="handlePublish">发布文章</el-button>
        </div>
    </el-card>

</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import { ElMessage } from 'element-plus';
import { MdEditor } from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import { useArticleStore } from '@/stores/Article';
import { CreateArticleAPI } from '@/API/Article';
import { UploadImgAPI } from '@/API/File.ts';
import { APP_CONFIG } from '~/app.config';
const isEditing = ref(true);
const form = ref({
    title: '',
    content: ''
});
const handleSaveDraft = () => {
    useArticleStore().setArticleInfo(form.value);
    ElMessage.success('草稿保存成功');
};
const clearArticle = () => {
    form.value.content = '';
    form.value.title = '';
}
const handlePublish = async () => {
    if (form.value.title.length < 5 || form.value.title.length > 100) {
        ElMessage.error('标题长度需在5到100个字之间');
        return;
    }
    if (!form.value.content) {
        ElMessage.error('内容不能为空');
        return;
    }
    const res = await CreateArticleAPI(form.value.title, form.value.content);
    if (res?.code === 200) {
        ElMessage.success('文章发布成功');
        form.value.content = '';
        form.value.title = '';
    }
};
const handleUploadImg = async (files: FileList, callback: (urls: string[]) => void) => {
    const uploadPromises = Array.from(files).map(async file => {
        let data = new FormData();
        data.append('imgs', file);
        const res = await UploadImgAPI(data);
        return APP_CONFIG.baseURL + res?.data?.imgs as string;
    });
    const urls = await Promise.all(uploadPromises);
    callback(urls);
};

onMounted(() => {
    if (useArticleStore().useArticleInfo) {
        form.value = useArticleStore().useArticleInfo!;
    }
});
</script>

<style scoped>
.el-card {
    margin: 5px;
}
</style>