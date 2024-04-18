<template>
    <el-descriptions class="margin-top" title="With border" :column="3" :size="10" border>
        <template #extra>
            <el-button type="primary">Operation</el-button>
        </template>
        <el-descriptions-item>
            <template #label>
                <div class="cell-item">
                    <el-icon :style="iconStyle">
                        <user />
                    </el-icon>
                    Username
                </div>
            </template>
            kooriookami
        </el-descriptions-item>
        <el-descriptions-item>
            <template #label>
                <div class="cell-item">
                    <el-icon :style="iconStyle">
                        <iphone />
                    </el-icon>
                    Telephone
                </div>
            </template>
            18100000000
        </el-descriptions-item>
        <el-descriptions-item>
            <template #label>
                <div class="cell-item">
                    <el-icon :style="iconStyle">
                        <location />
                    </el-icon>
                    Place
                </div>
            </template>
            Suzhou
        </el-descriptions-item>
        <el-descriptions-item>
            <template #label>
                <div class="cell-item">
                    <el-icon :style="iconStyle">
                        <tickets />
                    </el-icon>
                    Remarks
                </div>
            </template>
            <el-tag size="small">School</el-tag>
        </el-descriptions-item>
        <el-descriptions-item>
            <template #label>
                <div class="cell-item">
                    <el-icon :style="iconStyle">
                        <office-building />
                    </el-icon>
                    Address
                </div>
            </template>
            No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu Province
        </el-descriptions-item>
    </el-descriptions>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import {
    Iphone,
    Location,
    OfficeBuilding,
    Tickets,
    User,
} from '@element-plus/icons-vue'
const iconStyle = computed(() => {
    return {
        marginRight: '10px'
    }
})
</script>

<style scoped>
.el-descriptions {
    margin-top: 20px;
}

.cell-item {
    display: flex;
    align-items: center;
}

.margin-top {
    margin-top: 20px;
}
</style>