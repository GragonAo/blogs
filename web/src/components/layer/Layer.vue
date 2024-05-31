<template>
    <div class="common-layout">
        <el-container>
            <el-header class="header">
                <Cps_Headder></Cps_Headder>
            </el-header>
            <el-container>
                <el-aside class="aside" width="180px">
                    <Cps_Aside></Cps_Aside>
                </el-aside>
                <el-main class="main-content">
                    <!-- 这里将渲染由路由决定的组件 -->
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script setup lang='ts'>
import Cps_Headder from './components/Cps_Header.vue';
import Cps_Aside from './components/Cps_Aside.vue';
</script>

<style scoped>
.common-layout {
    /* 可以设置一些全局样式，如 box-sizing */
    box-sizing: border-box;
}

.header {
    /* 设置 header 的高度 */
    height: 60px;
    line-height: 60px;
    /* 可选，使文本垂直居中 */
    /* 其他 header 样式 */
}

.aside {
    /* 你可以设置 aside 的样式，但通常不需要设置固定高度 */
    /* aside 的高度会由其内容自然撑开 */
    /* 其他 aside 样式 */
}

.main-content {
    /* 设置 main 的高度为视口高度减去 header 的高度 */
    height: calc(100vh - 60px);
    overflow-y: auto;
    /* 允许垂直滚动 */
    /* 其他 main 样式 */
}

/* 确保 el-scrollbar 的高度占据整个 el-main */
.el-scrollbar__wrap {
    height: 100%;
}
</style>