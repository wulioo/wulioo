<template>
  <div class="home-fine">
    <!--    顶上导航   -->
    <van-cell title="精选景点"
              is-link
              value="更多"
              title-style="text-align:left"
              icon="location-o"/>
    <div class="box-main">
          <ListSingle v-for="(item,index) in FineList" :key="index" :item = "item"/>
    </div>
  </div>
</template>

<script>
import ListSingle from '@/components/common/ListSingle'

export default {
  name: "Fine",
  components: {
    ListSingle
  },
  data() {
    return {
      FineList: [
        {id: 1, img_url: '/static/home/hot/h1.jpg', title: '阿斯顿撒旦阿萨德阿斯顿撒', prices: 69,score:3.5},
        {id: 2, img_url: '/static/home/hot/h2.jpg', title: '阿斯顿撒旦阿萨德阿斯顿撒', prices: 69,score: 5},
      ],
      value: 3
    }
  }
}
</script>

<style scoped lang="less">
.home-fine {
  background-color: #fff;
  padding: 0 0.242rem 1.208rem;

  .van-cell {
    margin-top: 0.242rem;
    padding: 0.242rem 0;
  }

  .box-main {

  }
}

</style>