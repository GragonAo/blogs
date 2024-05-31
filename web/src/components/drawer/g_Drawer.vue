<template>
    <div class="my-drawer-container" v-show="open" @click="handleOutsideClick" ref="drawerContainer">
        <transition name="drawer" @after-enter="afterEnter">
            <div class="my-drawer" :style="{ transform: `translateX(${open ? '0' : '100%'})` }" @click.stop>
                <div class="my-drawer-content">
                    <slot></slot>
                </div>
            </div>
        </transition>
    </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref } from 'vue';

const props = defineProps({
    open: Boolean,
    withHeader: {
        type: Boolean,
        default: true
    }
});

const emit = defineEmits(['update:open']);
const drawerContainer = ref(null);

const handleOutsideClick = (event) => {
    if (drawerContainer.value && !drawerContainer.value.contains(event.target)) {
        closeDrawer();
    }
};

const afterEnter = () => {
    if (!open) {
        emit('update:open', false);
    }
};
</script>

<style scoped>
.my-drawer-container {
    position: fixed;
    top: 40px;
    right: 0;
    bottom: 0;
    width: 300px;
    background-color: rgba(0, 0, 0, 0.3);
    z-index: 999;
    display: flex;
    align-items: stretch;
}

.my-drawer {
    width: 100%;
    height: 100%;
    background-color: #fff;
    overflow: auto;
    box-shadow: -3px 0px 6px rgba(0, 0, 0, 0.16);
    will-change: transform;
    transform: translateX(100%);
}

.my-drawer-enter-active,
.my-drawer-leave-active {
    transition: transform 0.5s ease;
}

.my-drawer-enter,
.my-drawer-leave-to {
    transform: translateX(0);
}
</style>
