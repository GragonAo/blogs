<template>
    <div class="user-info">
        <el-avatar :src="user.avatar" size="large" />
        <h3>{{ user.name }}</h3>
        <p>{{ user.age }}岁</p>
        <p>{{ user.location }}</p>
        <p>{{ user.jobTitle }}</p>
        <p>{{ user.university }}</p>
        <p>{{ user.bio }}</p>
        <el-divider />
        <div class="stats">
            <el-tag>{{ user.friends }} 朋友</el-tag>
            <el-tag>{{ user.photos }} 相片</el-tag>
            <el-tag>{{ user.comments }} 评论</el-tag>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { defineProps } from 'vue';

const props = defineProps<{ user: any }>();
</script>

<style scoped>
.user-info {
    text-align: center;
}

.el-avatar {
    margin-bottom: 20px;
}

.stats {
    display: flex;
    justify-content: space-around;
    margin-top: 15px;
}
</style>