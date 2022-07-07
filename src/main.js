import { createApp } from 'vue'
import Vue from 'vue'
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
// 引入所有api集合在API对象上 放到Vue的$API上 所有的vm对象就有了这些方法 不需要在引入 this就有
import * as API from '@/utils/api'
app.config.globalProperties.API = API
app.use(Vant)
app.use(store).use(router).mount('#app')
