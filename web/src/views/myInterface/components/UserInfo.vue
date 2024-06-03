<template>
    <div class="user-info">
        <el-avatar :src="user?.userLoginInfo?.avatar" size="large" />
        <h3>{{ user?.userLoginInfo?.username }}</h3>
        <p>{{ user?.userProfile?.age }}岁</p>
        <p>{{ user?.userProfile?.address }}</p>
        <p>{{ user?.userProfile?.city }}, {{ user?.userProfile?.state }}, {{ user?.userProfile?.zip }}</p>
        <p>{{ user?.userProfile?.school }}</p>
        <p>{{ user?.userProfile?.degree }} in {{ user?.userProfile?.major }}</p>
        <p>{{ user?.userProfile?.job_title }} at {{ user?.userProfile?.company_name }}</p>
        <p>{{ user?.userProfile?.job_description }}</p>
        <p>{{ user?.userProfile?.skills }}</p>
        <p>{{ user?.userProfile?.certificates }}</p>
        <p>{{ user?.userProfile?.languages }}</p>
        <el-divider />
        <!-- <div class="stats">
            <el-tag>{{ user?.friends }} 朋友</el-tag>
            <el-tag>{{ user?.photos }} 相片</el-tag>
            <el-tag>{{ user?.comments }} 评论</el-tag>
        </div> -->
    </div>
</template>

<script lang="ts" setup>
import useUserStore from '@/stores/User';
const user = useUserStore();
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