<script setup lang="ts">
import { RouterView } from 'vue-router';
import LoginForm from '@/components/loginModal/loginModal.vue'; // 引入你的登录组件
import useSettingsStore from './stores/Settings';
import { computed } from 'vue';
const settingStore = useSettingsStore();
const updateLoginState = () => {
  settingStore.setLoginDialogVisible(false);
}
const loginState = computed(() => {
  return settingStore.settings?.loginDialogVisible;
});
</script>
<template>
  <LoginForm v-if="loginState" @close-dialog="updateLoginState" />
  <router-view></router-view>
</template>

<style scoped></style>
