<template>
    <div class="achievements">
        <h3>个人成就</h3>
        <ul>
            <li v-for="achievement in achievements" :key="achievement.title">
                {{ achievement.title }}: {{ achievement.count }}
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{
    achievements: {
        title: string;
        count: number;
    }[];
}>();
</script>

<style scoped>
.achievements {
    margin-top: 20px;
}

.achievements ul {
    list-style: none;
    padding: 0;
}

.achievements li {
    margin: 5px 0;
}
</style>