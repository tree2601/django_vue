<template>
  <n-message-provider>
      <router-view></router-view>
  </n-message-provider>
</template>

<script lang="ts" setup>
import {NMessageProvider} from "naive-ui";
import {Local} from "/@utils/StorageTools";
import {useThemeConfig} from "/@bean/GlobalConfig";
const storesThemeConfig = useThemeConfig();

// 页面加载时
onMounted(() => {
  // 获取缓存中的主题配置
  if(Local.get('themeConfig')){
    // 保存到 pinia 中
    storesThemeConfig.setThemeConfig(Local.get('themeConfig'))
  }else {
    Local.set('themeConfig',storesThemeConfig.themeConfig)
  }
});

</script>

<style scoped lang="scss">

</style>