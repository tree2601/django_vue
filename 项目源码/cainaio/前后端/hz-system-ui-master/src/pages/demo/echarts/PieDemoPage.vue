<template>
  <n-el tag="div" class="box">
    <n-el tag="div" class="echarts-box">
      <hz-echarts-pie-simple id="pie_1" ref="pie_1"></hz-echarts-pie-simple>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-pie-doughnut id="pie_2" ref="pie_2"></hz-echarts-pie-doughnut>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-pie-half-donut id="pie_3" ref="pie_3"></hz-echarts-pie-half-donut>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-pie-border-radius id="pie_4" ref="pie_4"></hz-echarts-pie-border-radius>
    </n-el>
  </n-el>
</template>

<script lang="ts" setup>
import {onMounted} from "vue";
import HzEchartsPieSimple from "/@com/echarts/pie/Hz-Echarts-Pie-Simple.vue";
import HzEchartsPieDoughnut from "/@com/echarts/pie/Hz-Echarts-Pie-Doughnut.vue";
import HzEchartsPieHalfDonut from "/@com/echarts/pie/Hz-Echarts-Pie-Half-Donut.vue";
import HzEchartsPieBorderRadius from "/@com/echarts/pie/Hz-Echarts-Pie-BorderRadius.vue";

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