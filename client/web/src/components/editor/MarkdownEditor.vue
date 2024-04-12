<template>
    <div class="markdown-editor">
        <div v-html="htmlText"></div>
    </div>
</template>

<script setup lang="ts">
import { ref, computed, defineProps } from 'vue';
import markdownIt from 'markdown-it';
import markdownItHighlightjs from 'markdown-it-highlightjs';
import 'highlight.js/styles/default.css'; // 引入你喜欢的highlight.js样式  

// 定义 props  
const props = defineProps({
    markdownText: {
        type: String,
        default: '',
    },
});
// 使用 markdown-it 创建实例并启用 highlight.js 插件  
const md = markdownIt({
    html: true,
    linkify: true,
    typographer: true,
}).use(markdownItHighlightjs);

// 使用 ref 和 computed 来处理 markdown 文本和渲染后的 HTML  
const htmlText = computed(() => md.render(props.markdownText));
</script>

<style scoped>
.markdown-editor {
    display: flex;
    flex-direction: column;
}
</style>