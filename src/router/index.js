import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Search from '../views/Search.vue'

import SightImage from '../views/sight/SightImage.vue'
import SightComment from '../views/sight/SightComment.vue'
import SightInfo from '../views/sight/SightInfo.vue'
import SightDetail from '../views/sight/SightDetail.vue'
import SightList from '../views/sight/SightList.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search',
    name: 'Search',
    component: Search

  },
    //景点列表
  {
    path: '/sight/list',
    name: 'SightList',
    component: SightList

  },
    //景点详情
  {
    path: '/sight/detail/:id',
    name: 'SightDetail',
    component: SightDetail

  },
    //景点介绍
  {
    path: '/sight/info/:id',
    name: 'SightInfo',
    component: SightInfo

  },
    //评论列表
  {
    path: '/sight/comment/:id',
    name: 'SightComment',
    component: SightComment
  },
    //景点图片
  {
    path: '/sight/image/:id',
    name: 'SightImage',
    component: SightImage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
