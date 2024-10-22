<template>
  <n-el tag="div" class="box">
    <n-el tag="div" class="echarts-box">
      <hz-echarts-k-line-simple id="'kline1'"/>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-k-line-s-z id="'kline2'"/>
    </n-el>
  </n-el>
</template>

<script lang="ts" setup>
import {onMounted,ref} from "vue";
import HzEchartsKLineSimple from "/@com/echarts/kline/Hz-Echarts-KLine-Simple.vue";
import HzEchartsKLineSZ from "/@com/echarts/kline/Hz-Echarts-KLine-SZ.vue";


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