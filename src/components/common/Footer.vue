<template>
  <div>
    <van-tabbar v-model="active" route placeholder>
      <van-tabbar-item name="home" icon="home-o" :to="{name:'Home'}">首页</van-tabbar-item>
      <van-tabbar-item name="search" icon="search" :to="{name:'Search'}">搜索</van-tabbar-item>
      <van-tabbar-item name="friends" icon="friends-o" badge="5">我的</van-tabbar-item>
    </van-tabbar>
  </div>

</template>

<script>
import { ref } from 'vue';
export default {
  name: "Footer",
  data(){
    return {
      active:'home',
    };
  }
}
</script>

<style scoped>

</style>