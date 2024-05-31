<template>
    <div class="user-info">
        <img :src="user.avatar" alt="User Avatar" class="avatar" />
        <div class="details">
            <h2>{{ user.name }}</h2>
            <p class="stats">总访问量: {{ user.totalViews }} 排名: {{ user.rank }}</p>
            <p class="description">{{ user.description }}</p>
            <p class="ip-location">IP 属地: {{ user.ipLocation }}</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{
    user: {
        avatar: string;
        name: string;
        totalViews: number;
        rank: number;
        description: string;
        ipLocation: string;
    };
}>();
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