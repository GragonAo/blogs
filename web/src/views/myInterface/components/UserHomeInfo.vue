<template>
    <div class="user-info">
        <el-image class="avatar" :src="APP_CONFIG.baseURL + user.userLoginInfo?.avatar" :zoom-rate="1.2" :max-scale="7"
            :min-scale="0.2" fit="cover" />
        <div class="details">
            <h2>{{ user.userLoginInfo?.username }}</h2>
        </div>
    </div>
</template>

<script setup lang="ts">
import useUserStore from '@/stores/User';
import { APP_CONFIG } from '~/app.config';


const user = useUserStore();
</script>

<style scoped>
.user-info {
    display: flex;
    align-items: center;
}

.avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

.details {
    margin-left: 20px;
}

.stats,
.description,
.ip-location {
    margin: 5px 0;
}
</style>