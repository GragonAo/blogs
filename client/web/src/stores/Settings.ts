import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useSettingsStore = defineStore('settings', () => {
    const settings = ref<SettingsInfo | undefined>(undefined);

    const setSettings = (value: SettingsInfo) => {
        settings.value = value;
        localStorage.setItem('settings', JSON.stringify(value));
    };

    const clearSettings = () => {
        settings.value = undefined;
        localStorage.removeItem('settings');
    };
    const loadUserInfoFromBrowser = () => {
        const storedInfo = localStorage.getItem('settings');
        if (storedInfo) {
            settings.value = JSON.parse(storedInfo);
        }
    };

    // 在 store 创建时加载用户信息  
    loadUserInfoFromBrowser();

    return {
        settings,
        setSettings,
        clearSettings,
    };
});

/** 用户相关信息存储器类型接口 */
export interface SettingsStore {
    settings: SettingsInfo | undefined;
    setSettings: (val: SettingsInfo) => void;
    clearSettings: () => void;
}

export type SettingsInfo = {
    redirectPath: string
}

export default useSettingsStore;