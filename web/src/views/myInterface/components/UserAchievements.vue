<template>
    <div class="achievements">
        <h3>个人成就</h3>
        <canvas ref="achievementChart"></canvas>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

const props = defineProps<{
    achievements: {
        title: string;
        count: number;
    }[];
}>();

const achievementChart = ref<HTMLCanvasElement | null>(null);

onMounted(() => {
    if (achievementChart.value && props.achievements) {
        const ctx = achievementChart.value.getContext('2d');

        const labels = props.achievements.map(achievement => achievement.title);
        const data = props.achievements.map(achievement => achievement.count);

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: '成就数量',
                    data: data,
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
});
</script>

<style scoped>
.achievements {
    margin-top: 20px;
}

.achievements canvas {
    display: block;
    /* 确保canvas作为块级元素显示 */
    max-width: 100%;
    height: 300px;
    /* 设置一个具体的高度 */
}
</style>