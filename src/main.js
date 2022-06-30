import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// 重置初始化样式
import './assets/css/reset.css'

// 自适应
import  './assets/js/flexible'

//引入vant样式
import Vant from 'vant';
import 'vant/lib/index.css';


const  app = createApp(App)
app.use(Vant)
app.use(store).use(router).mount('#app')
