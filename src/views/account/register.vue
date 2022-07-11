<template>
  <div class="page-register">
    <van-nav-bar
        title="注册"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
    />
    <van-form @submit="onSubmit">
      <van-cell-group inset>
        <van-field
          v-model="form.telphone"
          name="手机号码"
          label="手机号码"
          placeholder="手机号码"
          :rules="[{ required: true, message: '请填写用户名' }]"
      />
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
        <van-field
            v-model="form.check_password"
            type="password"
            name="确认密码"
            label="确认密码"
            placeholder="确认密码"
            :rules="[{ required: true, message: '请填写密码' }]"
        />
      </van-cell-group>
      <div style="margin: 16px;">
        <van-button round block type="primary" native-type="submit">
          提交
        </van-button>
      </div>
    </van-form>
  </div>
</template>

<script>
export default {
  name: "Register",
  data(){
    return {
      form:{
        username:'',
        telphone:'',
        password:'',
        check_password:''
      }
    }
  },
  methods:{
    onClickLeft(){
      this.$router.go(-1)
    },
    onSubmit(){

    }
   }
}
</script>

<style scoped lang="less">
.page-register{
  .van-cell-group--inset{
    margin: 0;
    margin-top: 10px;
  }
}
</style>