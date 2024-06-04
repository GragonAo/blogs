<template>
    <div class="card-group">
        <el-card v-for="(card, index) in cards" :key="index" class="card" :style="{ width: cardWidth }"
            @mouseover="cardHovered(index)" @mouseout="cardLeft(index)">
            <div class="card-content">
                <h3 class="card-title">{{ card.name }}</h3>
                <p class="card-description">{{ card.description || 'No description available' }}</p>
                <p class="card-language"><strong>Language:</strong> {{ card.language || 'N/A' }}</p>
                <a :href="card.html_url" target="_blank" class="card-link">View on GitHub</a>
            </div>
        </el-card>
    </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { GetGetHubProject } from '@/API/User';
import type { Repo } from '@/API/API_Types/User';

const cards = ref<Repo[]>([]);

const fetchGitHubRepos = async () => {
    await GetGetHubProject().then((res) => {
        if (res?.code == 200) {
            cards.value = res.data;
        }
    });
};

onMounted(fetchGitHubRepos);

const cardWidth = computed(() => 'calc(50% - 20px)');
const hoveredCard = ref<number | null>(null);

const cardHovered = (index: number) => {
    hoveredCard.value = index;
};

const cardLeft = () => {
    hoveredCard.value = null;
};
</script>

<style scoped>
.card-group {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
}

.card {
    box-sizing: border-box;
    margin: 10px;
    background-color: #fff;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    cursor: pointer;
    border-radius: 8px;
    overflow: hidden;
}

.card:hover {
    transform: scale(1.05);
    z-index: 1;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card-content {
    padding: 16px;
}

.card-title {
    font-size: 1.5em;
    margin: 0 0 10px 0;
    color: #333;
}

.card-description {
    font-size: 1em;
    color: #666;
    margin-bottom: 10px;
}

.card-language {
    font-size: 0.875em;
    color: #999;
}

.card-link {
    display: inline-block;
    margin-top: 10px;
    color: #42b983;
    text-decoration: none;
    font-weight: bold;
}

.card-link:hover {
    text-decoration: underline;
}

/* 响应式调整 */
@media (min-width: 600px) {
    .card {
        flex: 0 0 calc(33.3333% - 20px);
    }

    .card-group .card:nth-child(3n) {
        margin-right: 0;
    }

    .card-group .card:nth-last-child(1),
    .card-group .card:nth-last-child(2) {
        margin-right: 20px;
    }
}

@media (max-width: 599px) {
    .card {
        flex: 0 0 calc(100% - 20px);
    }
}
</style>