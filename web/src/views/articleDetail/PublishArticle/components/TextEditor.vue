<template>
    <el-card>
        <el-form :model="form" label-width="80px">
            <el-form-item label="标题">
                <el-input v-model="form.title" placeholder="请输入文章标题（5~100个字）"></el-input>
            </el-form-item>
            <el-form-item label="内容">
                <el-card style="width: 100%;">
                    <el-input v-if="isEditing" type="textarea" v-model="form.content" placeholder="请输入文章内容"
                        rows="10"></el-input>
                    <MarkDownEditor v-else :markdown-text="form.content" />
                </el-card>
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
import MarkDownEditor from '@/components/editor/MarkdownEditor.vue'
import { useArticleStore } from '@/stores/Article';
import { CreateArticleAPI } from '@/API/Article';
const isEditing = ref(true);
const form = ref({
    title: '',
    content: ''
});
const handleSaveDraft = () => {
    useArticleStore().setArticleInfo(form.value);
    // 保存草稿逻辑
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
    }
};
onMounted(() => {
    if (useArticleStore().useArticleInfo) {
        form.value = useArticleStore().useArticleInfo!;
    }
});
</script>

<style scoped>
.el-card {
    margin: 20px;
}

.toolbar {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
}
</style>