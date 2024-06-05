<template>
    <div class="achievements">
        <h3>个人成就</h3>
        <canvas ref="achievementChart"></canvas>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

const props = defineProps<{
    achievements: {
        title: string;
        count: number;
    }[];
}>();

const achievementChart = ref<HTMLCanvasElement | null>(null);
let chartInstance: Chart | null = null;

const createChart = () => {
    if (achievementChart.value) {
        const ctx = achievementChart.value.getContext('2d');

        if (ctx) {
            if (chartInstance) {
                chartInstance.destroy(); // 销毁旧图表实例
            }

            const labels = props.achievements.map(achievement => achievement.title);
            const data = props.achievements.map(achievement => achievement.count);

            chartInstance = new Chart(ctx, {
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
    }
};

onMounted(() => {
    createChart();
});

watch(() => props.achievements, () => {
    createChart();
});
</script>

<style scoped>
.achievements {
    margin-top: 20px;
}

.achievements canvas {
    display: block;
    max-width: 100%;
    height: 300px;
}
</style>