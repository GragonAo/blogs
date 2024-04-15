<template>
    <div class="article-detail">
        <h1 class="article-title">{{ article.title }}</h1>
        <p class="article-meta">Published on {{ article.publishedAt }} by {{ article.author }}</p>
        <div class="article-content" v-html="article.content"></div>
    </div>
</template>

<script setup lang='ts'>
import { reactive } from 'vue';

// 使用 reactive 创建一个响应式对象来存储文章数据  
const article = reactive({
    title: 'The Joy of Reading',
    author: 'Jane Smith',
    publishedAt: 'January 15, 2023',
    content: `  
        <p>Reading has always been a source of joy for me. Whether it's a thriller that keeps me on the edge of my seat or a heartwarming novel that tugs at my heartstrings, books have the power to transport me to different worlds.</p>  
          
        <p>One of my favorite aspects of reading is the escape it provides. In the busyness of daily life, it's easy to get caught up in the hustle and bustle, forgetting to take a moment for ourselves. But when I open a book, I am transported to a whole new world, where I can forget about my worries and immerse myself in the story.</p>  
          
        <p>Reading also has the ability to expand our horizons. Through the words of authors, we can gain insights into different cultures, perspectives, and experiences. It's a window to the world, allowing us to understand and appreciate the diversity of human life.</p>  
          
        <h2>The Power of Imagination</h2>  
          
        <p>What I love most about reading is the power of imagination it unlocks. As I read, my mind creates vivid images and scenes, bringing the story to life in my head. I can picture the characters, their expressions, and the settings of the story as if I were there myself.</p>  
          
        <p>This imaginative process is not only enjoyable but also beneficial for our cognitive development. It helps us to improve our visualization skills, enhance our creativity, and even boost our memory. Reading is truly a workout for the mind.</p>  
          
        <h2>The Joy of Discovery</h2>  
          
        <p>Another joy of reading comes from the discovery of new authors and genres. There's always something new to explore in the world of books. Whether it's a classic novel that has stood the test of time or a contemporary thriller that keeps you guessing until the end, there's always a new adventure waiting to be had.</p>  
          
        <p>As I delve deeper into the world of books, I discover more about myself as well. Reading challenges my thinking, prompts me to question my beliefs, and inspires me to pursue my passions. It's a journey of self-discovery that is as rewarding as it is enjoyable.</p>  
          
        <p>In conclusion, the joy of reading is infinite. It's a source of escape, a window to the world, a workout for the mind, and a journey of discovery. So, grab a book and let the magic of reading transport you to a whole new world.</p>  
    `
});  
</script>
<style scoped>
.article-detail {}

.article-title {
    margin-bottom: 10px;
    font-size: 2rem;
    /* 增大标题字体大小 */
    font-weight: bold;
    /* 设置标题为粗体 */
}

.article-meta {
    font-size: 0.875rem;
    color: #6c757d;
    margin-bottom: 20px;
}

.article-content {
    line-height: 1.6;
    font-size: 1rem;
    /* 设置内容字体大小 */
}

/* 添加一些边距和颜色以美化列表项 */
.article-content ul {
    list-style-type: disc;
    padding-left: 20px;
}

.article-content li {
    margin-bottom: 5px;
}
</style>