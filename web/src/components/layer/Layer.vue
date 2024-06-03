<template>
    <div class="layout">
        <el-row class="header-row">
            <el-col :span="24">
                <Cps_Headder></Cps_Headder>
            </el-col>
        </el-row>
        <el-row class="main-row">
            <el-col :span="3" class="aside">
                <Cps_Aside></Cps_Aside>
            </el-col>
            <el-col :span="21" class="content">
                <router-view></router-view>
            </el-col>
        </el-row>
    </div>
</template>

<script setup lang='ts'>
import Cps_Headder from './components/Cps_Header.vue';
import Cps_Aside from './components/Cps_Aside.vue';
</script>

<style scoped>
.layout {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.header-row {
    flex: 0 0 auto;
}

.main-row {
    display: flex;
    flex-direction: row;
    width: 100%;
}

.aside {
    flex: 0 0 3%;
    min-width: 200px;
    /* 最小宽度，确保侧边栏不会太窄 */
}

.content {
    flex: 1;
}

@media (max-width: 768px) {
    .main-row {
        flex-direction: column;
    }

    .aside {
        flex: 0 0 auto;
        width: 100%;
    }

    .content {
        width: 100%;
    }
}
</style>