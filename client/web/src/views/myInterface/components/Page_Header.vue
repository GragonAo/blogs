<template>
    <div class="page-header">
        <el-row class="header-row">
            <el-col :span="3" class="avatar-col">
                <el-image class="avatar-image" :src="userStores.userLoginInfo?.avatar" :zoom-rate="1.2" :max-scale="7"
                    :min-scale="0.2" :initial-index="4" fit="cover" />
            </el-col>
            <el-col :span="20" class="info-cols">
                <el-descriptions class="margin-top" :title="userStores.userLoginInfo?.username" :column="2" size="80px"
                    style="margin-top: 20px;">
                    <el-descriptions-item label="Email">{{ userStores.userLoginInfo?.email }}</el-descriptions-item>
                    <el-descriptions-item label="Telephone">{{ userStores.userLoginInfo?.mobile
                        }}</el-descriptions-item>
                    <el-descriptions-item label="Place">Suzhou</el-descriptions-item>
                    <el-descriptions-item label="Remarks">
                        <el-tag size="small">School</el-tag>
                    </el-descriptions-item>
                    <el-descriptions-item label="Address">
                        No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu Province
                    </el-descriptions-item>
                </el-descriptions>
            </el-col>
        </el-row>
        <p class="mt-4 text-sm">
            我是 黄可钊 我又是 朱必利
        </p>
    </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/User'
const userStores = useUserStore();
</script>
<style scoped>
.page-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    /* 添加其他全局样式 */
}

.avatar-col {
    margin-top: 20px;
    /* 头像列样式 */
}

.avatar-image {
    border-radius: 15px;
    /* 添加其他图片样式 */
}

.info-cols {
    display: flex;
    align-items: center;
    margin-left: 20px;
}

.info-col {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* 添加列样式 */
}

.cell-item {
    display: flex;
    align-items: center;
}

.margin-top {
    margin-top: 20px;
}
</style>