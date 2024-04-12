<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <Cps_Headder></Cps_Headder>
            </el-header>
            <el-container>
                <el-aside width="180px">
                    <Cps_Aside></Cps_Aside>
                </el-aside>
                <el-main hidden="100%">
                    <!-- 这里将渲染由路由决定的组件 -->
                    <router-view></router-view>
                    <router-view name="test"></router-view>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script setup lang='ts'>
import Cps_Headder from './components/Cps_Header.vue';
import Cps_Aside from './components/Cps_Aside.vue';
</script>

<style scoped></style>