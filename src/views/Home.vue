<template>
  <div class="page-home">
<!--  Banner轮播图  -->
    <Banner/>
<!--  热门景点  -->
    <Hot/>
<!--  精选景点   -->
    <Fine/>
<!--   底部-->
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Banner from "@/components/home/Banner";
import Hot from "@/components/home/Hot";
import Fine from "@/components/home/Fine";
import Footer from "@/components/common/Footer";

export default {
  name: 'Home',
  components: {
    Banner,
    Hot,
    Fine,
    Footer
  }
}
</script>
