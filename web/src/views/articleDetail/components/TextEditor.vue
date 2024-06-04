<template>
    <el-card>
        <el-form :model="form" label-width="80px">
            <el-form-item label="标题">
                <el-input v-model="form.title" :placeholder="titlePlaceholder"></el-input>
            </el-form-item>
            <el-form-item label="内容">
                <md-editor v-model="form.content" :height="editorHeight" @onUploadImg="handleUploadImg" />
            </el-form-item>
        </el-form>
        <el-divider></el-divider>
        <div class="toolbar">
            <el-button @click="clearArticle">清空文章</el-button>
            <el-button @click="handleSaveDraft">保存草稿</el-button>
            <el-button type="primary" @click="handleSubmit">{{ submitButtonText }}</el-button>
        </div>
    </el-card>
</template>

<script lang="ts" setup>
import { onMounted, ref, defineProps, defineEmits } from 'vue';
import { ElMessage } from 'element-plus';
import { MdEditor } from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import { useArticleStore } from '@/stores/Article';
import { UploadImgAPI } from '@/API/File.ts';
import { APP_CONFIG } from '~/app.config';

const props = defineProps<{
    initialTitle?: string,
    initialContent?: string,
    titlePlaceholder?: string,
    editorHeight?: string,
    submitButtonText?: string
}>();

const emit = defineEmits(['saveDraft', 'submit']);

const form = ref({
    title: props.initialTitle || '',
    content: props.initialContent || ''
});

const handleSaveDraft = () => {
    useArticleStore().setArticleInfo(form.value);
    ElMessage.success('草稿保存成功');
    emit('saveDraft', form.value);
};

const clearArticle = () => {
    form.value.content = '';
    form.value.title = '';
};

const handleSubmit = async () => {
    if (form.value.title.length < 5 || form.value.title.length > 100) {
        ElMessage.error('标题长度需在5到100个字之间');
        return;
    }
    if (!form.value.content) {
        ElMessage.error('内容不能为空');
        return;
    }
    emit('submit', form.value);
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
</script>

<style scoped>
.el-card {
    margin: 5px;
}

.toolbar {
    display: flex;
    gap: 10px;
}
</style>
