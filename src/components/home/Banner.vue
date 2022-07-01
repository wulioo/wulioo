<template>
  <div class="home-banner">
    <van-nav-bar title="慕旅游网" />


    <van-swipe class="my-swipe" :autoplay="3000" indicator-color="white">
      <van-swipe-item v-for="(item,index) in bannerList" :key="index"><img :src="item.img_url" alt=""></van-swipe-item>

    </van-swipe>
  </div>

</template>

<script>
import {system} from "../../utils/api";

export default {
  name: "Banner",
  data(){
    return{
      bannerList:[
        {id:1,img_url:'/static/home/banner/banner1.jpg'},
        {id:2,img_url:'/static/home/banner/banner2.jpg'},
        {id:3,img_url:'/static/home/banner/banner3.jpg'}
      ],
    }
  },
  methods: {
    /**
     * 获取轮播图的数据
     */
    getBannerList () {
      let a = this.$API.system.sliderList().then(res => {
        console.log('res:', res)
        this.bannerList = res.data.objects
      })
    }
  },
  mounted() {
    this.getBannerList()
  }

}
</script>

<style scoped lang="less">
.home-banner{
   .my-swipe{
     //margin-bottom: 0.283rem;
   }
    img{
      width: 100%;
      height: 3.5rem;
    }

}
</style>