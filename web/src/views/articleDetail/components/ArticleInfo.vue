<template>
    <el-card>
        <div class="article-info">
            <h1>{{ title }}</h1>
            <div class="meta">
                <span>{{ date }}</span>
                <span>阅读量: {{ views }}</span>
            </div>
            <div class="content">
                <MdPreview :modelValue="content" height="500px" />
            </div>
        </div>
    </el-card>

</template>

<script setup lang="ts">
import { defineProps } from 'vue';
import { MdPreview } from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
const props = defineProps<{
    title: string;
    author: string;
    date: string;
    views: number;
    content: string;
}>();
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