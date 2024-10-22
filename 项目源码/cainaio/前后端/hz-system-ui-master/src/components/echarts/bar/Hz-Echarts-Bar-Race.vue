<!-- 动态排序柱状图 -->
<template>
  <div :id="props.id" class="wh100"></div>
</template>

<script setup lang="ts" name="HzEchartsBarRace">
import * as echarts from 'echarts';
import {onMounted} from "vue";
// @ts-ignore
import {getEchartsTextColor, getEchartsTheme} from "/@utils/GlobalFunction";
// @ts-ignore
import {theme} from "/@bean/GlobalConfig";
import {EchartsData} from "/@bean/GlobalEntity";

// eslint-disable-next-line no-undef
const props = defineProps({
  id: {
    type: String,
    default: 'pie-simple'
  },
  showTitle: {
    type: Boolean,
    default: true
  },
  showLegend: {
    type: Boolean,
    default: true
  },
  showTooltip: {
    type: Boolean,
    default: true
  },
  title: {
    type: String,
    default: '动态排序柱状图'
  },
});

const option : any = {
  backgroundColor: "rgba(0,0,0,0)",
  title: {
    text: props.title,
    left: 'center',
    textStyle: {
      color: getEchartsTextColor()
    },
    show:props.showTitle
  },
  xAxis: {
    max: 'dataMax',
    axisLine: {
      lineStyle: {
        color: getEchartsTextColor()
      }
    },
  },
  yAxis: {
    type: 'category',
    axisLine: {
      lineStyle: {
        color: getEchartsTextColor()
      }
    },
    data: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    inverse: true,
    animationDuration: 300,
    animationDurationUpdate: 300,
    max: 10 // only the largest 3 bars will be displayed
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    },
    show:props.showTooltip
  },
  legend: {
    orient: 'vertical',
    left: 'left',
    textStyle: {
      color: getEchartsTextColor()
    },
    show:props.showLegend
  },
  animationDuration: 0,
  animationDurationUpdate: 1000,
  animationEasing: 'linear',
  animationEasingUpdate: 'linear',
  series: [
    {
      realtimeSort: true,
      name: 'Access From',
      type: 'bar',
      data: getRandomData(),
      label: {
        show: true,
        color: getEchartsTextColor(),
        position: 'right',
        valueAnimation: true,
      },
    }
  ]
};

let data :number [] = []
let tempdata :number [] = []

function getRandomData(){
  let data = [0, 0, 0, 0, 0, 0, 0]
  let datas = []
  for (var i=0;i<data.length;i++){
    datas.push(0)
  }
  return datas
}

function run():boolean{
  let max_num = 0
  for(var i=0;i<tempdata.length;i++){
    if(data[i] == null){
      data[i] = 0
    }if(data[i]>=tempdata[i]){
      data[i] = tempdata[i]
      max_num += 1
    }else{
      data[i] = data[i] + Math.random() * 100
    }
  }
  option.series[0].data = data
  if (max_num == tempdata.length){
    return false
  }
  return true
}

function start(data:number[]){
  tempdata = data
  option.yAxis.max = tempdata.length
}



let interval: any = null

onMounted(() => {
  init()
  start([150, 230, 224, 218, 135, 147, 260])
  interval = setInterval(() => {
    let isRun = run()
    if (!isRun) {
      clearInterval(interval)
    }else{
      init()
    }
  }, 1000)
});

const basicBar = ref();

function init() {
  try{
    basicBar.value = markRaw(echarts.init(document.getElementById(props.id), getEchartsTheme));
    basicBar.value.setOption(option);
    window.addEventListener('resize', () => {
      basicBar.value.resize();
    });
  }catch (e) {
    clearInterval(interval)
  }

}

//@ts-ignore
watch(getEchartsTheme, () => {
  resetOption()
  init()
});

function resetOption() {
  option.title.textStyle.color = getEchartsTextColor()
  option.xAxis.axisLine.lineStyle.color = getEchartsTextColor()
  option.yAxis.axisLine.lineStyle.color = getEchartsTextColor()
  option.legend.textStyle.color = getEchartsTextColor()
  option.series[0].label.color = getEchartsTextColor()
}

// 刷新图表方式，该方法需要提供给外部调用
// eslint-disable-next-line no-unused-vars
const refreshCharts = (data : EchartsData) => {
  option.title.text = data.title;
  option.yAxis.data = data.x;
  init()
  clearInterval(interval)
  start(data.y as number[])
  interval = setInterval(() => {
    let isRun = run()
    if (!isRun) {
      clearInterval(interval)
    }else{
      init()
    }
  }, 1000)
};

// 重置图表大小
const resizeEcharts = () => {
  basicBar.value.resize();
}

// eslint-disable-next-line no-undef
defineExpose({
  refreshCharts,
  resizeEcharts
});
</script>

<style scoped>

</style>