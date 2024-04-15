<template>
    <div class="responsive-calendar-container">
        <table class="responsive-calendar">
            <thead>
                <tr>
                    <th v-for="day in weekDays" :key="day">{{ day }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(week, index) in weeks" :key="index">
                    <td v-for="day in week" :key="day.date" @click="handleDateClick(day)">
                        {{ day.date.getDate() }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';

const currentMonth = ref(new Date());
const weekDays = ref(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']);
const weeks = ref([]);

const handleDateClick = (date: Date) => {
    console.log('Date clicked:', date);
    // 你可以在这里发出事件或者执行其他逻辑  
};

// 计算属性，用于生成日历数据  
const computedWeeks = computed(() => {
    const firstDay = new Date(currentMonth.value.getFullYear(), currentMonth.value.getMonth(), 1);
    const lastDay = new Date(currentMonth.value.getFullYear(), currentMonth.value.getMonth() + 1, 0);

    let date = new Date(firstDay);
    const days: { date: Date; isCurrentMonth: boolean }[] = [];
    let week: { date: Date; isCurrentMonth: boolean }[] = [];

    while (date <= lastDay) {
        week.push({ date, isCurrentMonth: date.getMonth() === currentMonth.value.getMonth() });

        if (week.length === 7 || date.getDate() === lastDay.getDate()) {
            days.push(...week);
            week = [];
        }

        date.setDate(date.getDate() + 1);
    }

    return chunkArray(days, 7); // 使用chunkArray函数将数组分割成每周的数组  
});

// 辅助函数，用于将数组分割成指定大小的块  
function chunkArray(array: any[], chunkSize: number) {
    const result = [];
    for (let i = 0; i < array.length; i += chunkSize) {
        const chunk = array.slice(i, i + chunkSize);
        result.push(chunk);
    }
    return result;
}

// 根据窗口大小调整日历样式（响应式逻辑）  
function adjustCalendarStyle() {
    const windowWidth = window.innerWidth;
    // 这里添加你的响应式逻辑，比如改变表格的样式等  
}

onMounted(() => {
    weeks.value = computedWeeks.value;
    window.addEventListener('resize', adjustCalendarStyle);
    adjustCalendarStyle();
});

onBeforeUnmount(() => {
    window.removeEventListener('resize', adjustCalendarStyle);
});
</script>

<style scoped>
.responsive-calendar-container {
    width: 100%;
    max-width: 100%;
    overflow-x: auto;
    /* 允许水平滚动 */
}

.responsive-calendar {
    width: 100%;
    border-collapse: collapse;
    user-select: none;
    /* 禁止选择文本 */
}

.responsive-calendar th,
.responsive-calendar td {
    text-align: center;
    border: 1px solid #ddd;
    padding: 10px;
    /* 根据需要动态调整 */
    cursor: pointer;
    /* 点击效果 */
}

/* 根据需要添加更多样式 */
</style>