<template>
    <Monaco :textValue="textValue" @update:textValue="handleTextValueUpdate"></Monaco>
    <Markdown :markdownText="textValue"></Markdown>
</template>

<script setup lang='ts'>
import Monaco from '@/components/editor/MonacoEditor.vue'
import Markdown from '@/components/editor/MarkdownEditor.vue'
import { ref } from 'vue'
const textValue = ref('Hello')

const handleTextValueUpdate = (newValue: string) => {
    textValue.value = newValue;
    console.log(textValue.value);
};  
</script>

<style scoped></style>