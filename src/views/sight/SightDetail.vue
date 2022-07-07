<template>
  <div class="page-sight-detail">
    <!--    导航-->
    <van-nav-bar
        title=""
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
    />
    <!--    banner-->
    <div class="banner" :style='{"background":"url("+detailData.banner_img+")","background-repeat":"no-repeat"}'>
      <div class="tips">
        <router-link to="/asd" class="pic-sts">
          <van-icon name="video-o"/>
          <span>5 图片</span>
        </router-link>
        <div class="title">{{ detailData.name}}</div>
      </div>
    </div>
    <!-- 景点详情   -->
    <div class="sight-info">
      <div class="left">
        <div class="info-tile">
          <strong>{{detailData.score}}分</strong>
          <small>很棒</small>
        </div>
        <div class="info-tips">2评论</div>
        <van-icon name="arrow"/>
      </div>
      <div class="right">
        <div class="info-tile">
          <span>景点介绍</span>
        </div>
        <div class="info-tips">开放时间、贴士</div>
        <van-icon name="arrow"/>
      </div>
    </div>
    <van-cell :title="detailData.province+detailData.city+detailData.area+detailData.town" is-link icon="location-o" style="text-align: left"/>

    <!--    景点门票-->
    <div class="sight-ticket">
      <van-cell value="门票" icon="bookmark-o"/>
      <div class="ticket-item" v-for="(item,index) in ticketData" :key="index">
        <div class="left">
          <div class="title">{{ item.name }}</div>
          <div class="tips">
            <van-icon name="clock-o" color="deepskyblue"/>
            <span>23:52前可订明日</span>
          </div>
          <div class="tags">
            <van-tag mark type="primary" color="#969799">无需换票</van-tag>
          </div>
        </div>

        <div class="right">
          <div class="price"><span>￥</span><strong>{{ item.price }}</strong></div>
          <router-link :to="/order/" class="buy">
            <van-button type="warning" size="small">预订</van-button>

          </router-link>
        </div>
      </div>

    </div>

    <!--    热门评论-->
    <van-cell value="热门评论" icon="chat-o" style="margin-top: 0.242rem;"/>
    <Comment v-for="(item,index) in commentData" :key="index" :item="item"/>

  </div>
</template>

<script>
import Comment from '@/components/common/Comment.vue'

export default {
  name: "SightDetail",
  components: {
    Comment
  },
  data() {
    return {
      id:'',
      detailData:'',
      ticketData:'',
      commentData:'',
      sight:''
    }
  },
  computed:{
    // sight(){
    //   return this.detailData.sight
    // }
  },
  methods: {
    onClickLeft() {
      this.$router.go(-1)
    },
    getSightDetail() {

      this.API.sight.sightDetail(this.id).then(({data}) => {
        this.detailData = data
        // this.sight = data.sight
      })
    },
    getTicketDetail() {
      this.API.sight.ticketDetail({sight_id:this.id}).then(({data}) => {
        this.ticketData = data
      })
    },
    getCommentDetail() {
      this.API.sight.commentDetail({sight_id:this.id}).then(({data}) => {
        this.commentData = data
      })
    }
  },
  mounted() {
    this.id  = this.$route.params.id;
    this.getSightDetail()
    this.getTicketDetail()
    this.getCommentDetail()
  }
}

</script>

<style scoped lang="less">
.page-sight-detail {
  .van-nav-bar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: transparent;
  }

  .banner {
    width: 100%;
    height: 5.483rem;
    position: relative;
    background: url("/static/home/hot/h2_max.jpg") no-repeat;
    background-size: cover;

    .tips {
      color: #fff;
      font-size: 0.338rem;
      position: absolute;
      bottom: 0;

      .pic-sts {
        color: #fff;
        border-radius: 0.725rem;
        background-color: rgba(0, 0, 0, .4);
      }

      .title {
        margin: 0.242rem;
      }
    }
  }

  .sight-info {
    display: flex;
    background-color: white;
    border-bottom: 1px solid #f6f6f6;

    .left, .right {
      flex: 1;
      position: relative;
      padding: 10px;
      text-align: left;

      .van-badge__wrapper {
        position: absolute;
        right: 0.121rem;
        top: 0.242rem;
        font-size: 0.438rem;
      }

      .info-tips {
        color: #999;
        font-size: 0.29rem;
        margin: 15px 0 3px 0;
      }
    }

    .left {
      .info-tile {
        font-size: 0.338rem;

        strong {
          color: #ff8300;
        }
      }


    }

    .right {
      border-left: 1px solid #f6f6f6;

      .info-tile {
        font-size: 0.338rem;

      }
    }
  }

  .sight-ticket {
    margin-top: 0.242rem;
    background-color: white;

    .ticket-item {
      //color: deepskyblue;
      font-size: 0.338rem;
      border-bottom: 1px solid #f6f6f6;
      display: flex;

      .left {
        flex: 2;
        text-align: left;
        padding: 0.121rem 0.242rem;

        .title {
          margin: 10px 0;
          font-size: 0.386rem;
        }
      }

      .right {
        flex: 1;

        .price {
          margin-top: 0.121rem;
          font-size: 20px;
          color: #ff9800;
        }

        .van-button {
          min-width: 1.449rem;
        }
      }
    }
  }
}

</style>