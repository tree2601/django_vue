<!--K线图-->
<template>
  <div :id="props.id" style="width: 100%;height: 100%"></div>
</template>

<script setup lang="ts" name="HZEchartsKLineSimple">
import * as echarts from 'echarts';
import {onMounted} from "vue";
// @ts-ignore
import {getEchartsTextColor, getEchartsTheme} from "/@utils/GlobalFunction";

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
    default: '基础K线图'
  },
  data: {
    type: Array,
    default: () => {
      return {
        x: ['2017-10-24', '2017-10-25', '2017-10-26', '2017-10-27'],
        y: [
          [20, 34, 10, 38],
          [40, 35, 30, 50],
          [31, 38, 33, 44],
          [38, 15, 5, 42]
        ]
      }
    }
  }
});

const option = {
  backgroundColor: "rgba(0,0,0,0)",
  title: {
    text: props.title,
    left: 0,
    textStyle: {
      color: getEchartsTextColor(),
    },
    show: props.showTitle
  },
  xAxis: {
    data: props.data.x,
    axisLine: {
      lineStyle: {
        color: getEchartsTextColor(),
      }
    }
  },
  yAxis: {
    axisLine: {
      lineStyle: {
        color: getEchartsTextColor(),
      }
    }
  },
  tooltip: {
    axisPointer: {
      type: 'cross',
      label: {
        backgroundColor: '#6a7985'
      }
    },
    show: props.showTooltip
  },
  series: [
    {
      type: 'candlestick',
      data: props.data.y,
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

// @ts-ignore
watch(getEchartsTheme, () => {
  resetOption()
  init()
});

function resetOption() {
  option.title.textStyle.color = getEchartsTextColor()
  option.xAxis.axisLine.lineStyle.color = getEchartsTextColor()
  option.yAxis.axisLine.lineStyle.color = getEchartsTextColor()
}

// 刷新图表方式，该方法需要提供给外部调用
// eslint-disable-next-line no-unused-vars
const refreshCharts = (title:string,time:string [],data :number[][]) => {
  option.title.text = title;
  option.xAxis.data = time;
  option.series[0].data = data;
  const basicBar = echarts.init(document.getElementById(props.id),getEchartsTheme);
  basicBar.clear();
  basicBar.setOption(option);
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