<template>
    <div class="user-info">
        <img :src="user.avatar" alt="User Avatar" class="avatar" />
        <div class="details">
            <h2>{{ user.name }}</h2>
            <p>{{ user.description }}</p>
            <div class="stats">
                <span>原创: {{ user.original }}</span>
                <span>周排名: {{ user.weekRank }}</span>
                <span>总排名: {{ user.totalRank }}</span>
            </div>
            <div class="badges">
                <img v-for="badge in user.badges" :src="badge" :key="badge" class="badge" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{
    user: {
        avatar: string;
        name: string;
        description: string;
        original: number;
        weekRank: number;
        totalRank: number;
        badges: string[];
    };
}>();
</script>

<style scoped>
.user-info {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

.details {
    text-align: center;
    margin-top: 10px;
}

.stats {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 5px;
}

.badges {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 10px;
}

.badge {
    width: 30px;
    height: 30px;
    margin: 2px;
}
</style>