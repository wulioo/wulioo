<template>
  <!--搜索页面-->
  <div class="page-search">
    <!--    标题-->
    <van-nav-bar :title="title" />
    <!--    搜索-->
    <van-search
        v-model="search_v"
        show-action
        label=""
        placeholder="请输入搜索关键词"
        @search="onSearch"
    >
      <template #action>
        <div @click="onSearch">搜索</div>
      </template>
    </van-search>
<!--    景点列表-->
    <div style=" background-color: white;">
      <ListSingle v-for="(item,index) in SearchList" :key="index" :item = "item"/>

    </div>
<!--    分页-->
    <van-pagination
        v-model="currentPage"
        :total-items="total_count"
        :items-per-page="per_page"
        force-ellipses
        @change="changePage"

    />
<!--    底部-->
    <Footer v-show="s_footer"/>

  </div>
</template>

<script>
import ListSingle from "@/components/common/ListSingle";
import Footer from "@/components/common/Footer";
import { Toast } from 'vant';

export default {
  name: "Search",
  // 监听,当路由发生变化的时候执行
  watch:{

  },
  components: {
    ListSingle,
    Footer
  },
  data() {
    return {
      search_v: '',
      s_footer:true,
      title:'搜索景点',
      currentPage:1,
      total_count:0,
      parma:{
        is_top: '',
        is_hot: '',
        name:'',
        p:1
      },
      SearchList:[
        // {id: 1, img_url: '/static/home/hot/h1.jpg', title: '阿斯顿撒旦阿萨德阿斯顿撒', prices: 69,score:3.5},
        // {id: 2, img_url: '/static/home/hot/h2.jpg', title: '阿斯顿撒旦阿萨德阿斯顿撒', prices: 69,score: 5},
      ]
    }
  },
  methods:{
    onSearch(){
      this.parma.name = this.search_v
      this.getSightList()
    },
    changePage(next){
      this.parma.p = next
      this.getSightList()
    },
    routerInit(){
      let query = this.$route.query
      if(JSON.stringify(query) !== "{}"){
        if(query.is_hot){
          this.title = '热门推荐'
          this.parma.is_hot = 1
        }
        if(query.is_top){
          this.title = '精选景点'
          this.parma.is_top = 1
        }

        this.s_footer = false
      }
    },
    /**
     * 获取景点数据
     */
    getSightList () {
      console.log(this.parma)
      this.API.sight.sightList(this.parma).then(({data}) => {
        this.SearchList = data.results
        this.total_count  = data.count
        this.per_page = data.per_page

      }).catch(error =>{
        console.log(error)
      })
    }
  },
  mounted() {
    this.routerInit()
    this.getSightList()

  }
}
</script>

<style scoped>

</style>