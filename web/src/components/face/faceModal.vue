<template>
    <el-dialog v-if="visible" append-to-body :before-close="handleBeforeClose" width="50%" height="50%"
        v-model="visible" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" show-close="false"
        class="login-dialog" :class="['animate__animated', animationClass]">
        <Face ref="faceRef" v-if="visible" @close="handleClose" :visible="visible" />
    </el-dialog>
</template>

<script setup lang='ts'>
import 'animate.css';
import { ref } from 'vue';
import Face from '@/components/face/face.vue';
const visible = ref(false); // 初始状态设为true
const faceRef = ref<InstanceType<typeof Face> | null>(null);
// 定义一个响应式变量来存储当前的动画类
const animationClass = ref('animate__bounceIn');
// 定义一个方法来改变动画类
const changeBtnAnimation = (newAnimation: string) => {
    // 先移除当前动画类，触发重新渲染
    animationClass.value = '';

    // 微小延迟后重新应用动画类
    setTimeout(() => {
        animationClass.value = newAnimation;
    }, 10); // 延迟10毫秒
};
const showModal = () => {
    visible.value = true;
    changeBtnAnimation("animate__bounce");
    emit('showDialog');
};
const handleBeforeClose = (done: () => void) => {
    if (faceRef.value) {
        faceRef.value.closeFace();
    }
    done();
};
const handleClose = async (pictures: ['']) => {
    changeBtnAnimation("animate__bounceOut");
    visible.value = false;
    emit('closeDialog', pictures);
}
defineExpose({
    showModal
});
const emit = defineEmits(['closeDialog', 'loginSuccess', 'showDialog']);
</script>

<style scoped></style>