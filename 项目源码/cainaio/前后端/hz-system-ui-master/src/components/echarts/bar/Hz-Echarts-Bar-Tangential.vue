<!-- 极坐标 -->
<template>
  <div :id="props.id" class="wh100"></div>
</template>

<script setup lang="ts" name="HzEchartsBarTangential">
import * as echarts from 'echarts';
import {onMounted} from "vue";
import {getEchartsTextColor, getEchartsTheme} from "/@utils/GlobalFunction";
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
    default: '极坐标'
  },
  data: {
    type: Object,
    default: () => {
      return {
        x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        y: [820, 932, 901, 934, 1290, 1330, 1320]
      }
    }
  }
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
  polar: {
    radius: [30, '80%']
  },
  angleAxis: {
    max: getMaxValue(props.data.y)+100,
    startAngle: 75
  },
  radiusAxis: {
    type: 'category',
    data: props.data.x,
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    },
    show:props.showTooltip
  },
  legend: {
    show:props.showLegend
  },
  series: [
    {
      name: 'Access From',
      type: 'bar',
      data: props.data.y,
      coordinateSystem: 'polar',
      label: {
        show: true,
        position: 'middle',
        formatter: '{b}: {c}',
        color: getEchartsTextColor()
      },
    }
  ]
};



onMounted(() => {
  init()
});

const basicBar = ref();

function init() {
  basicBar.value = markRaw(echarts.init(document.getElementById(props.id), getEchartsTheme));
  basicBar.value.setOption(option);
  window.addEventListener('resize', () => {
    basicBar.value.resize();
  });
}

//@ts-ignore
watch(getEchartsTheme, () => {
  resetOption()
  init()
});

function resetOption() {
  option.title.textStyle.color = getEchartsTextColor()
  option.series[0].label.color = getEchartsTextColor()
}

// 刷新图表方式，该方法需要提供给外部调用
// eslint-disable-next-line no-unused-vars
const refreshCharts = (data : EchartsData) => {
  option.title.text = data.title;
  option.radiusAxis.data = data.x;
  option.series[0].data = data.y as number[]
  option.angleAxis.max = getMaxValue(data.y as number[])+100
  init()
};

function getMaxValue(data : number[]) :number{
  let max = 0;
  for(let i = 0; i < data.length; i++){
    if(data[i] > max){
      max = data[i]
    }
  }
  return max
}

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