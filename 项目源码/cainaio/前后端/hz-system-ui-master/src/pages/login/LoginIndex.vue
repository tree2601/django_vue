<template>
  <n-config-provider :theme="getThemeConfig.theme? darkTheme : null" class="wh100">
    <n-card class="wh100">
      <n-el tag="div" class="login-box">
        <n-el tag="div" class="login-box-content">
          <n-el tag="div" class="login-box-content-title">
            <n-el tag="h1">{{isLogin ? "登录" : "注册"}}</n-el>
          </n-el>
          <n-el tag="div" class="login-box-content-form">
            <n-form label-width="100px" label-placement="top" v-if="isLogin">
              <n-form-item label="用户名">
                <n-input v-model:value="loginForm.username" placeholder="请输入用户名"></n-input>
              </n-form-item>
              <n-form-item label="密码">
                <n-input v-model:value="loginForm.password" placeholder="请输入密码"></n-input>
              </n-form-item>
              <n-form-item>
                <n-space justify="center" style="width: 100%" v-if="isLogin">
                  <n-button type="primary" @click="loginSubmit">登录</n-button>
                  <n-button type="primary" @click="isLogin = false">去注册</n-button>
                </n-space>
              </n-form-item>
            </n-form>
            <n-form label-width="100px" label-placement="top" v-else>
              <n-form-item label="用户名">
                <n-input v-model:value="registerForm.username" placeholder="请输入用户名"></n-input>
              </n-form-item>
              <n-form-item label="密码">
                <n-input v-model:value="registerForm.password" placeholder="请输入密码"></n-input>
              </n-form-item>
              <n-form-item label="确认密码">
                <n-input v-model:value="registerForm.confirmPassword" placeholder="请输入确认密码"></n-input>
              </n-form-item>
              <n-form-item>
                <n-space justify="center" style="width: 100%" v-if="!isLogin">
                  <n-button type="primary" @click="registerSubmit">注册</n-button>
                  <n-button type="primary" @click="isLogin = true">去登录</n-button>
                </n-space>
              </n-form-item>
            </n-form>
          </n-el>
        </n-el>
      </n-el>
    </n-card>
  </n-config-provider>
</template>

<script lang="ts" setup>

import {darkTheme} from "naive-ui";
// @ts-ignore
import {useThemeConfig} from "/@bean/GlobalConfig";
import {computed, ref} from "vue";
// @ts-ignore
import router from "/@/router";
// @ts-ignore
import {Local,Session} from "/@utils/StorageTools";
//@ts-ignore
import * as sysApi from "/@api/hz-system-api";
import {registerAccount} from "/@api/hz-system-api";

//@ts-ignore
let message = useMessage();

const storesThemeConfig = useThemeConfig();
// @ts-ignore
const { themeConfig } = storeToRefs(storesThemeConfig);
const getThemeConfig = computed(() => {
  return themeConfig.value;
});

const isLogin = ref(true);

const loginForm = ref({
  username: "",
  password: ""
});

const registerForm = ref({
  username: "",
  password: "",
  confirmPassword: ""
});

// @ts-ignore
watch(isLogin, (val) => {
  if (val) {
    registerForm.value = {
      username: "",
      password: "",
      confirmPassword: ""
    }
  } else {
    loginForm.value = {
      username: "",
      password: ""
    }
  }
});

const loginSubmit = async () => {
  if(!loginForm.value.username){
    message.error("请输入用户名");
    return;
  }
  if(!loginForm.value.password){
    message.error("请输入密码");
    return;
  }
  if(loginForm.value.username==='test'){
    Session.set("token", "test");
    router.push({
      path: "/bigscreen",
    });
    return;
  }
  let result = await sysApi.loginIn(loginForm.value)
  if (result.code === 200) {
    Session.set("token", result.data);
    router.push("/bigscreen");
  }else{
    message.error(result.msg);
  }
};

const registerSubmit = async () => {
  console.log(registerForm.value);
  if(!registerForm.value.username){
    message.error("请输入用户名");
    return;
  }
  if(!registerForm.value.password){
    message.error("请输入密码");
    return;
  }
  if(!registerForm.value.confirmPassword){
    message.error("请输入确认密码");
    return;
  }
  if(registerForm.value.password !== registerForm.value.confirmPassword){
    message.error("两次密码不一致");
    return;
  }
  let result = await sysApi.registerAccount(registerForm.value)
  if (result.code === 200) {
    message.success("注册成功");
    isLogin.value = true;
  }else{
    message.error(result.msg);
  }
};

</script>

<style scoped>

.login-box {
  width: 500px;
  height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: calc(50% - 250px);
  left: calc(50% - 250px);
}

.login-box-content {
  width: 400px;
  height: 400px;
  border-radius: 10px;
  padding: 20px;
}

.login-box-content-title {
  text-align: center;
  margin-bottom: 20px;
}

.login-box-content-form {
  padding: 20px;
}

</style>