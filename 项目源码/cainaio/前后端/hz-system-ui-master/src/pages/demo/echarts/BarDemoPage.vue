<template>
  <n-el tag="div" class="box">
    <n-el tag="div" class="echarts-box">
      <hz-echarts-bar-simple id="bar1" ref="bar1"></hz-echarts-bar-simple>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-bar-race id="bar2" ref="bar2"></hz-echarts-bar-race>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-bar-negative id="bar3" ref="bar3"></hz-echarts-bar-negative>
    </n-el>
    <n-el tag="div" class="echarts-box">
      <hz-echarts-bar-tangential id="bar4" ref="bar4"></hz-echarts-bar-tangential>
    </n-el>
  </n-el>
</template>

<script lang="ts" setup>
import {onMounted,ref} from "vue";
import HzEchartsBarRace from "/@com/echarts/bar/Hz-Echarts-Bar-Race.vue";
import HzEchartsBarSimple from "/@com/echarts/bar/Hz-Echarts-Bar-Simple.vue";
import HzEchartsBarNegative from "/@com/echarts/bar/Hz-Echarts-Bar-Negative.vue";
import HzEchartsBarTangential from "/@com/echarts/bar/Hz-Echarts-Bar-Tangential.vue";

const bar1 = ref();
const bar2 = ref();
const bar3 = ref();
const bar4 = ref();

onMounted(() => {
  const data = {
    title: '柱状图',
    x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    y: [820, 932, 901, 934, 1290, 1330, 1320]
  }
  bar1.value.refreshCharts(data)
  const data2 = {
    title: '动态排序',
    x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    y: [820, 932, 901, 934, 1290, 1330, 1320]
  }
  bar2.value.refreshCharts(data2)
  const data3 = {
    title: '正负折线图',
    x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    y: [-820, 932, 901, 934, -1290, 1330, -1320]
  }
  bar3.value.refreshCharts(data3)
  const data4 = {
    title: '极坐标',
    x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    y: [820, 932, 901, 934, 1290, 1330, 1320]
  }
  bar4.value.refreshCharts(data4)
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