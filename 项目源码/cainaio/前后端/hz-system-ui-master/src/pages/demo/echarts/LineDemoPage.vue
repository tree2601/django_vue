<template>
  <n-el tag="div" class="box">
    <n-el tag="div" class="echarts-box">
      <hz-echarts-line-simple id="line1"></hz-echarts-line-simple>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-line-smooth id="line2"></hz-echarts-line-smooth>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-line-stacked id="line3"></hz-echarts-line-stacked>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-line-area id="line4"></hz-echarts-line-area>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-line-area-stacked id="line5"></hz-echarts-line-area-stacked>
    </n-el>
  </n-el>
</template>

<script lang="ts" setup>
import {onMounted,ref} from "vue";
import HzEchartsLineSimple from "/@com/echarts/line/Hz-Echarts-Line-Simple.vue";
import HzEchartsLineSmooth from "/@com/echarts/line/Hz-Echarts-Line-Smooth.vue";
import HzEchartsLineStacked from "/@com/echarts/line/Hz-Echarts-Line-Stacked.vue";
import HzEchartsLineArea from "/@com/echarts/line/Hz-Echarts-Line-Area.vue";
import HzEchartsLineAreaStacked from "/@com/echarts/line/Hz-Echarts-Line-AreaStacked.vue";


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