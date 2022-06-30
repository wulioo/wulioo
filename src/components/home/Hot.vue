<template>
  <div class="home-hot">
<!--    顶上导航   -->
    <van-cell title="热门推荐"
              is-link
              value="全部榜单"
              title-style="text-align:left"
              icon="/static/home/hot/fire.png"/>
    <div class="box-main">
      <a href="" class="hot_item" v-for="(item,index) in hotList" :key="index">
        <div class="img">
          <span></span>
          <img :src="item.img_url" alt="">
        </div>

        <div class="title">{{ item.title }}</div>
        <div class="line-price">
          <span class="prices">￥{{item.prices}}</span>起</div>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "Hot",
  data() {
    return {
      hotList: [
        {id: 1, img_url: '/static/home/hot/h1.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
        {id: 2, img_url: '/static/home/hot/h2.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
        {id: 3, img_url: '/static/home/hot/h3.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
        {id: 4, img_url: '/static/home/hot/h4.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
        {id: 5, img_url: '/static/home/hot/h5.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
        {id: 6, img_url: '/static/home/hot/h6.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
        {id: 7, img_url: '/static/home/hot/h7.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
        {id: 8, img_url: '/static/home/hot/h8.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
        {id: 9, img_url: '/static/home/hot/h9.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
        {id: 10, img_url: '/static/home/hot/h10.jpg',title:'阿斯顿撒旦阿萨德阿斯顿撒',prices:69},
      ],
    }
  }
}
</script>

<style scoped lang="less">
.home-hot {
  background-color: #fff;
  padding: 0 0.242rem;
  /deep/ .van-cell {
    padding: 10px 0;
    img {
      margin-top: 3px;
      padding: 0;
    }

  }

  .box-main {
    display: flex;
    overflow-x: scroll;
    overflow-y: hidden;
    padding-top: 0.242rem;


    .hot_item {
      font-size: 0.338rem;
      display: flex;
      flex-direction: column;
      margin-right: 0.242rem;
      width: 2.415rem;
      margin-bottom: 0.214rem;
      .title {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }

      .line-price {
        padding-top: 3px;
        .prices {
          color: #f50;
          font-size: 0.338rem;
        }
      }
      .img{
        position: relative;
        span{
          position: absolute;
          left: 0;
          top: 0;
          display: inline-block;
          width: 1.014rem;
          height: 0.483rem;
          z-index: 10;
        }
        img {
          width: 100%;
          height: 2.415rem;
        }
      }
      &:first-child .img span{
        background: url("/static/home/hot/top1.png") no-repeat;
        background-size: 100% auto;
      }

      &:nth-child(2) .img span{
        background: url("/static/home/hot/top2.png") no-repeat;
        background-size: 100% auto;
      }

      &:nth-child(3) .img span{
        background: url("/static/home/hot/top3.png") no-repeat;
        background-size: 100% auto;
      }
    }

    &:after {
      content: "";
      display: block;
      clear: both;
    }


  }

}
</style>