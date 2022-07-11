<template>
  <div class="page-login">
    <van-nav-bar
        title="登录"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
    />
    <van-form @submit="onSubmit">
      <van-cell-group inset>
        <van-field

            v-model="form.username"
            name="用户名"
            label="用户名"
            placeholder="用户名"
            :rules="[{ required: true, message: '请填写用户名' }]"
        />
        <van-field
            v-model="form.password"
            type="password"
            name="密码"
            label="密码"
            placeholder="密码"
            :rules="[{ required: true, message: '请填写密码' }]"
        />
      </van-cell-group>
      <div style="margin: 16px;">
        <van-button round block type="primary" native-type="submit">
          提交
        </van-button>
      </div>
    </van-form>
    <div>
      <span>没有账号？</span>
      <router-link :to="{name:'register'}">点击注册</router-link>
    </div>
  </div>


</template>

<script>
export default {
  name: "Login",
  data(){
    return {
      form:{
        username:'',
        password:''
      }
    }
  },
  methods:{
    onClickLeft(){

    },
    onSubmit(val){
      console.log(val)
    }
  }
}
</script>

<style scoped lang="less">
.page-login{
  .van-cell-group--inset{
    margin: 0;
    margin-top: 10px;
  }
}

</style>