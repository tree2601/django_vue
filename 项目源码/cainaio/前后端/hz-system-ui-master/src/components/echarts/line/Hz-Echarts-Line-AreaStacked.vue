<!-- 堆叠面积图 -->
<template>
  <div :id="props.id" class="wh100"></div>
</template>

<script setup lang="ts" name="HZEchartsLineAreaStacked">
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
    default: '堆叠折线图'
  },
  data: {
    type: Object,
    default: () => {
      return {
        x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        y: [
          [120, 132, 101, 134, 90, 230, 210],
          [220, 182, 191, 234, 290, 330, 310],
          [150, 230, 224, 218, 135, 147, 260],
          [320, 332, 301, 334, 390, 330, 320],
          [820, 932, 901, 934, 1290, 1330, 1320],
        ]
      }
    }
  }
});

const option = {
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
    type: 'category',
    data: props.data.x,
    axisLine: {
      lineStyle: {
        color: getEchartsTextColor(),
      }
    }
  },
  yAxis: {
    type: 'value',
    axisLine: {
      lineStyle: {
        color: getEchartsTextColor(),
      }
    }
  },
  tooltip: {
    trigger: 'axis',
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
  series: getSeries(props.data.x,props.data.y)
};

// 分割props.data.y 为多个series
function getSeries(name : string[],y : number[][]) {
  let series = [];
  for (let i = 0; i < y.length; i++) {
    series.push({
      name: name[i],
      type: 'line',
      stack: 'Total',
      areaStyle: {},
      data: y[i],
      containLabel: true,
      label: {
        show: true,
        color: getEchartsTextColor()
      },
    })
  }
  return series;
}

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

// @ts-ignore
watch(getEchartsTheme, () => {
  resetOption()
  init()
});

function resetOption() {
  option.title.textStyle.color = getEchartsTextColor();
  option.xAxis.axisLine.lineStyle.color = getEchartsTextColor();
  option.yAxis.axisLine.lineStyle.color = getEchartsTextColor();
  option.legend.textStyle.color = getEchartsTextColor();
  option.series.forEach((item) => {
    item.label.color = getEchartsTextColor();
  })
}

// 刷新图表方式，该方法需要提供给外部调用
// eslint-disable-next-line no-unused-vars
const refreshCharts = (data : EchartsData) => {
  option.title.text = data.title;
  option.xAxis.data = data.x;
  option.series = getSeries(data.name,data.y as number[][]);
  init()
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