import MarkdownEditor from '@/components/editor/MarkdownEditor.vue';
import Layer from '@/components/layer/Layer.vue';
import Index from '@/views/index/Index.vue';
import Test from '@/views/test/Test.vue';
import Desktop from '@/views/Windows/Desktop.vue'
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'layer',
      component: Layer, // 使用 Layer 组件作为布局  
      children: [ // 子路由定义在 Layer 组件内部的 <router-view> 中渲染的内容  
        {
          path: '', // 当访问 '/' 时，默认渲染此组件  
          name: 'index',
          component: Index // 渲染 Index 组件到 Layer 的 <router-view> 中  
        },
        {
          path: 'test',
          name: 'test',
          component: Test // 渲染 Index 组件到 Layer 的 <router-view> 中  
        },
        // ... 其他子路由，例如其他页面组件  
      ]
    },
    {
      path: '/Desktop',
      name: 'desktop',
      component: Desktop, // 使用 Layer 组件作为布局 
    }
  ]
});

export default router;