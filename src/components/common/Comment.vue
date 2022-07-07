<template>
  <div class="comment">
    <div class="cmt-header">
      <van-rate v-model="item.score" size="13px"/>
      <div class="user">{{ item.user }}*** {{ item.created_at }}</div>
    </div>
    <div class="cmt-content">
      <p>{{item.content}}</p>
    </div>
    <div class="cmt-img">
      <van-grid :border="false" :column-num="3">
        <van-grid-item>
          <van-image
              src="/static/sight/comment1.jpg"
          />
        </van-grid-item>
        <van-grid-item>
          <van-image
              src="/static/sight/comment2.jpg"
              @click="show = true"

          />
        </van-grid-item>
        <van-grid-item>
          <van-image
              src="/static/sight/comment3.jpg"
          />
        </van-grid-item>
        <van-grid-item>
          <van-image
              src="/static/sight/comment4.jpg"
          />
        </van-grid-item>
        <van-image-preview v-model:show="show" :images="images" @change="onChange">
          <template v-slot:index>第{{ index }}页</template>
        </van-image-preview>
      </van-grid>



    </div>

  </div>
</template>

<script>
export default {
  name: "Comment",
  props:['item'],
  data(){
    return {
      value: 3,
      show:false,
      index:1,
      images:[
        'https://fastly.jsdelivr.net/npm/@vant/assets/apple-1.jpeg',
        'https://fastly.jsdelivr.net/npm/@vant/assets/apple-2.jpeg',
      ],

    }
  },
  methods:{
    onChange(newIndex){
      this.index = newIndex;
    }
  },
  mounted() {

  }
}
</script>
<style scoped lang="less">
.comment{
  background-color: white;
  border-bottom: 1px solid #f6f6f6;
  padding: 0.242rem;
  .cmt-header{
    display: flex;
    font-size: 0.314rem;
    justify-content: space-between;
    .user{
      //line-height: 0.58rem;
    }
  }
  .cmt-content{
    font-size: 0.29rem;
    text-align: left;
    margin-top: 0.243rem;
    margin-bottom: 0.242rem;
  }
  .cmt-img{
    /deep/ .van-grid  .van-grid-item .van-grid-item__content{
      padding: 4px;
    }

  }
}

</style>