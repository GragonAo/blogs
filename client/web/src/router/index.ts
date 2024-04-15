import Layer from '@/components/layer/Layer.vue';
import myInterface from '@/views/myInterface/myInterface.vue';
import index from '@/views/index/index.vue';
import study from '@/views/study/study.vue';
import articleDetail from '@/views/articleDetail/articleDetail.vue';
import cloudDesktop from '@/views/Windows/cloudDesktop.vue'
import { createRouter, createWebHistory } from 'vue-router';
import Test from '@/views/test/Test.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'layer',
      component: Layer, // 使用 Layer 组件作为布局  
      children: [ // 子路由定义在 Layer 组件内部的 <router-view> 中渲染的内容 
        {
          path: '/', // 当访问 '/' 时，默认渲染此组件  
          name: 'index',
          component: index // 渲染 Index 组件到 Layer 的 <router-view> 中  
        },
        {
          path: 'myInterface', // 当访问 '/' 时，默认渲染此组件  
          name: 'myInterface',
          component: myInterface // 渲染 Index 组件到 Layer 的 <router-view> 中  
        },
        {
          path: 'articleDetail',
          name: 'articleDetail',
          component: articleDetail // 渲染 Index 组件到 Layer 的 <router-view> 中  
        },
        {
          path: 'study',
          name: 'study',
          component: study // 渲染 Index 组件到 Layer 的 <router-view> 中  
        },
        // ... 其他子路由，例如其他页面组件  
      ]
    },
    {
      path: '/cloudDesktop',
      name: 'cloudDesktop',
      component: cloudDesktop, // 使用 Layer 组件作为布局 
    },
    {
      path: '/Test',
      name: 'Test',
      component: Test,
    }
  ]
});
export default router;