
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import App from './App.vue'
import router from './router'
import 'md-editor-v3/lib/style.css';

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)
// app.use(ElementPlus, { size: 'small', zIndex: 3000 })
app.mount('#app')
