import { ref } from 'vue';
import { defineStore } from 'pinia';
import { useRouter } from 'vue-router'; // 引入 useRouter
import type { ResponseUserLogin, UserInfo, UserProfile } from '@/API/API_Types/User';

export const useUserStore = defineStore('user', () => {
  const userLoginInfo = ref<UserInfo | undefined>(undefined);
  const userProfile = ref<UserProfile | undefined>(undefined);
  const token = ref<ResponseUserLogin | undefined>();
  const router = useRouter(); // 使用 useRouter 钩子

  const setToken = (value: ResponseUserLogin) => {
    token.value = value;
    localStorage.setItem('token', JSON.stringify(value));
  }
  const setUserInfo = (value: UserInfo) => {
    userLoginInfo.value = value;
  };
  const setUserProfile = (value: UserProfile) => {
    userProfile.value = value;
  }
  const isLogin = () => {
    return token.value !== undefined;
  }
  const logOut = () => {
    clearToken();
    clearUserInfo();
    clearUserProfile();
    router.push('/'); // 在登出后跳转到 /
  }
  const clearToken = () => {
    token.value = undefined;
    localStorage.removeItem('token');
  }
  const clearUserInfo = () => {
    userLoginInfo.value = undefined;
  };
  const clearUserProfile = () => {
    userProfile.value = undefined;
  }
  const loadUserInfoFromBrowser = () => {
    const storedInfo = localStorage.getItem('token');
    if (storedInfo) {
      token.value = JSON.parse(storedInfo);
    }
  };

  loadUserInfoFromBrowser();

  return {
    userLoginInfo,
    token,
    setUserInfo,
    clearUserInfo,
    setToken,
    clearToken,
    setUserProfile,
    isLogin,
    logOut,
    userProfile
  };
});

/** 用户相关信息存储器类型接口 */
export interface UserStore {
  userLoginInfo: UserInfo | undefined;
  token: ResponseUserLogin | undefined;
  userProfile: UserProfile | undefined;
  setUserInfo: (val: UserInfo) => void;
  clearUserInfo: () => void;
  setToken: (val: ResponseUserLogin) => void;
  clearToken: () => void;
  setUserProfile: () => void;
  isLogin: () => Boolean;
  logOut: () => void;
}

// 导出时使用 useUserStore，这是 Pinia 的推荐做法  
export default useUserStore;