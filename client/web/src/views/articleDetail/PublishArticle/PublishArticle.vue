<template>
    <el-container>
        <el-header>
            <h2>发布文章</h2>
        </el-header>
        <el-main>
            <TextEditor />
        </el-main>
    </el-container>
</template>

<script lang="ts" setup>
import TextEditor from './components/TextEditor.vue';
</script>

<style scoped>
.el-header {
    background-color: #f0f2f5;
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