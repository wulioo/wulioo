<template>
  <router-link class="hot_item" :to="{name:'SightDetail',params:{id:item.id}}">
    <img :src="item.main_img" alt="">
    <div class="right">
      <div class="title">{{ item.name }}</div>
      <van-rate
          v-model="item.score"
          :size="18"
          color="#ffd21e"
          void-icon="star"
          void-color="#eee"
      />
      <div class="tips">4人点评 | 100%满意</div>
      <div class="tips light">{{item.province}}-{{ item.city }}</div>
      <div class="line-price">
        <span class="prices">￥{{ item.min_price }}起</span>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "ListSingle",
  props: ['item'],
  data() {
    return {}
  }
}
</script>

<style scoped lang="less">
.hot_item {
  display: flex;
  font-size: 0.386rem;
  //padding-top: 0.242rem;
  border-bottom: 1px solid #f6f6f6;

  margin-top: 10px;
  padding: 10px;
  .van-rate {
    margin: 0.193rem 0;
  }


  img {
    width: 2.415rem;
    height: 2.415rem;
  }

  .right {
    flex: 1;
    text-align: left;
    padding-left: 0.1rem;
    position: relative;

    .title {
      font-weight: 600;
      font-size: 0.348rem;
      padding: 0.097rem 0;
    }

    .tips {
      font-size: 0.29rem;
      color: #666;

      &.light {
        margin-top: 0.145rem;
      }
    }

    .line-price {
      position: absolute;
      top: 0.483rem;
      right: 0.242rem;

      .prices {
        color: #f50;
        font-size: 0.438rem;
        font-weight: bold;
      }
    }
  }

}
</style>