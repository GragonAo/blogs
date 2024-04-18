import { ref } from 'vue';
import { defineStore } from 'pinia';
import type { UserLoginInfo } from '@/API/API_Types/User';

export const useUserStore = defineStore('user', () => {
  const userLoginInfo = ref<UserLoginInfo | undefined>(undefined);

  const setUserInfo = (value: UserLoginInfo) => {
    userLoginInfo.value = value;
    // 这里可以添加将用户信息写入浏览器的代码  
    // 例如，写入 localStorage:  
    localStorage.setItem('userInfo', JSON.stringify(value));
  };

  const clearUserInfo = () => {
    userLoginInfo.value = undefined;
    // 这里可以添加清除浏览器中用户信息的代码  
    // 例如，从 localStorage 中移除:  
    localStorage.removeItem('userInfo');
  };

  // 如果需要，可以添加一个从浏览器中读取用户信息的方法  
  const loadUserInfoFromBrowser = () => {
    const storedInfo = localStorage.getItem('userInfo');
    if (storedInfo) {
      userLoginInfo.value = JSON.parse(storedInfo);
    }
  };

  // 在 store 创建时加载用户信息  
  loadUserInfoFromBrowser();

  return {
    userLoginInfo,
    setUserInfo,
    clearUserInfo,
  };
});

/** 用户相关信息存储器类型接口 */
export interface UserStore {
  userLoginInfo: UserLoginInfo | undefined;
  setUserInfo: (val: UserLoginInfo) => void;
  clearUserInfo: () => void;
}

// 导出时使用 useUserStore，这是 Pinia 的推荐做法  
export default useUserStore;