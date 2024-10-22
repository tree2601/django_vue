<template>
  <n-el tag="div" class="box">
    <n-el tag="div" class="echarts-box">
      <hz-echarts-wrod-cloud id="wrodcloud1" ref="wrodcloud1"></hz-echarts-wrod-cloud>
    </n-el>
  </n-el>
</template>

<script lang="ts" setup>
import {onMounted} from "vue";
import HzEchartsWrodCloud from "/@com/echarts/wrodcloud/Hz-Echarts-WrodCloud.vue";


onMounted(() => {

});

</script>

<style scoped lang="scss">
.box{
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.echarts-box{
  width: 33%;
  height: 300px;
}
</style>