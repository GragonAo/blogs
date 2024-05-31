import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useArticleStore = defineStore('article', () => {
    const useArticleInfo = ref<ArticleInfo | undefined>(undefined);
    const setArticleInfo = (value: ArticleInfo) => {
        useArticleInfo.value = value;
    };
    const clearArticleInfo = () => {
        useArticleInfo.value = undefined;
    };
    return {
        useArticleInfo,
        setArticleInfo,
        clearArticleInfo,
    };
});

/** 用户相关信息存储器类型接口 */
export interface UserStore {
    userLoginInfo: ArticleInfo | undefined;
    setUserInfo: (val: ArticleInfo) => void;
    clearUserInfo: () => void;
}
export type ArticleInfo = {
    title: string,
    content: string
}
export default useArticleStore;