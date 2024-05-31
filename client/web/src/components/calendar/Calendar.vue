<template>
    <el-card class="calendar-card">
        <div class="quote">
            <span>我们的征途是星辰大海</span>
        </div>
        <div class="custom-calendar">

            <div class="calendar-header">
                <span>{{ monthNames[currentMonth] }} {{ currentYear }}</span>
            </div>
            <div class="calendar-body">
                <div class="calendar-day" v-for="day in previousMonthDays" :key="'prev' + day">
                    <span class="day-text">{{ day }}</span>
                </div>
                <div class="calendar-day current-month" v-for="day in daysInMonth" :key="day">
                    <span v-if="currentDay !== day" class="day-text">{{ day }}</span>
                    <span v-else class="day-cur-ext">{{ day }}</span>
                </div>
                <div class="calendar-day" v-for="day in nextMonthDays" :key="'next' + day">
                    <span class="day-text">{{ day }}</span>
                </div>
            </div>
        </div>
    </el-card>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';

const value = ref(new Date());

const currentYear = computed(() => value.value.getFullYear());
const currentMonth = computed(() => value.value.getMonth());
const daysInMonth = computed(() => {
    return Array.from({ length: new Date(currentYear.value, currentMonth.value + 1, 0).getDate() }, (_, i) => i + 1);
});
const currentDay = computed(() => value.value.getDate());
const startDayOfWeek = computed(() => {
    return new Date(currentYear.value, currentMonth.value, 1).getDay();
});

const previousMonthDays = computed(() => {
    const previousMonthLastDay = new Date(currentYear.value, currentMonth.value, 0).getDate();
    return Array.from({ length: startDayOfWeek.value }, (_, i) => previousMonthLastDay - startDayOfWeek.value + i + 1);
});

const nextMonthDays = computed(() => {
    const endDayOfWeek = new Date(currentYear.value, currentMonth.value + 1, 0).getDay();
    return Array.from({ length: 6 - endDayOfWeek }, (_, i) => i + 1);
});

const monthNames = [
    '一月', '二月', '三月', '四月', '五月', '六月',
    '七月', '八月', '九月', '十月', '十一月', '十二月'
];
</script>

<style scoped>
.calendar-card {
    margin-top: 30px;
    height: 315px;
    border-radius: 20px;
    background-image: url('@/assets/imgs/calendar.jpeg');
    background-size: cover;
    position: relative;
    color: #fff;
}

.custom-calendar {
    padding: 10px;
    color: #fff;
}

.calendar-header {
    display: flex;
    justify-content: center;
    margin-bottom: 10px;
    font-size: 18px;
    font-weight: bold;
}

.calendar-body {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 5px;
}

.calendar-day {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 40px;
    border-radius: 4px;
    background-color: rgba(255, 255, 255, 0.183);
}

.current-month {
    background-color: rgba(255, 255, 255, 0.4);
}

.calendar-day .day-text {
    color: #fff;
}

.day-cur-ext {
    color: rgb(200, 255, 0);
}

.calendar-footer {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
    padding: 0 10px;
}

.weather-info {
    display: flex;
    align-items: center;
}

.weather-icon {
    width: 24px;
    height: 24px;
    margin-right: 5px;
}

.quote {
    font-size: 14px;
    font-style: italic;
}
</style>