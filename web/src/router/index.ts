import Layer from '@/components/layer/Layer.vue';
import myInterface from '@/views/myInterface/myInterface.vue';
import mySecuritySettings from '@/views/myInterface/mySecuritySettings.vue';
import myInfoPage from '@/views/myInterface/myInfoPage.vue';
import myUserProfile from '@/views/myInterface/myUserProfile.vue';
import index from '@/views/index/index.vue';
import publishArticle from '@/views/articleDetail/PublishArticle/PublishArticle.vue';
import UpdateArticle from '@/views/articleDetail/UpdateArticle/UpdateArticle.vue';
import articlePage from '@/views/articleDetail/articlePage.vue';
import cloudDesktop from '@/views/Windows/cloudDesktop.vue'
import loginModal from '@/components/loginModal/loginModal.vue'
import registerModal from '@/components/loginModal/registerModal.vue'
import { createRouter, createWebHistory } from 'vue-router';
import Test from '@/views/test/Test.vue';
import useUserStore from '@/stores/User';
import useSettingsStore from '@/stores/Settings';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'layer',
      component: Layer,
      children: [
        {
          path: '/',
          name: 'index',
          component: index,
        },
        {
          path: '/myInterface',
          name: 'myInterface',
          component: myInterface,
          meta: { requiresAuth: true },
        },
        {
          path: '/articleDetail/:articleId',
          name: 'articlePage',
          component: articlePage
        },
        {
          path: '/articleDetail/publishArticle',
          name: 'publishArticle',
          component: publishArticle,
          meta: { requiresAuth: true },
        }, {
          path: '/articleDetail/updateArticle/:articleId',
          name: 'updateArticle',
          component: UpdateArticle,
          meta: { requiresAuth: true },
        },
        {
          path: '/myInterface/mySecuritySettings',
          name: 'mySecuritySettings',
          component: mySecuritySettings,
          meta: { requiresAuth: true },
        },
        {
          path: '/myInterface/myInfoPage',
          name: 'myInfoPage',
          component: myInfoPage,
          meta: { requiresAuth: true },
        },
        {
          path: '/myInterface/myUserProfile',
          name: 'myUserProfile',
          component: myUserProfile,
          meta: { requiresAuth: true },
        },
        {
          path: '/register',
          name: 'register',
          component: registerModal
        }
      ]
    },
    {
      path: '/cloudDesktop',
      name: 'cloudDesktop',
      component: cloudDesktop,
      meta: { requiresAuth: true },
    },
    {
      path: '/Test',
      name: 'Test',
      component: Test,
    },
    {
      path: '/login',
      name: 'login',
      component: loginModal,
    },
  ]
});
router.beforeEach((to, from, next) => {
  // 检查即将进入的路由是否需要登录  
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // 检查用户是否已登录  
    console.log(useUserStore().isLogin());
    if (useUserStore().isLogin()) {
      next();
    } else {
      const fullpath = to.fullPath
      let setting = useSettingsStore().settings;
      if (setting) {
        setting!.redirectPath = fullpath
        useSettingsStore().setSettings(setting!);
      } else {
        useSettingsStore().setSettings({ redirectPath: fullpath });
      }
      useSettingsStore().setLoginDialogVisible(true);
      next('/'); // 如果未登录，重定向到登录页面  
      // 停止当前导航  
      return;
    }
  } else {
    // 不需要登录，继续导航  
    next();
  }
});
export default router;