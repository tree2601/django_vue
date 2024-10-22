<!-- 基础面积图 -->
<template>
  <div :id="props.id" class="wh100"></div>
</template>

<script setup lang="ts" name="HZEchartsLineArea">
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
    default: '基础折线图'
  },
  data: {
    type: Object,
    default: () => {
      return {
        x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        y: [150, 230, 224, 218, 135, 147, 260]
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
      color: '#ffffff'
    },
    show:props.showTitle
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
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
  series: [
    {
      name: 'Access From',
      type: 'line',
      areaStyle: {},
      data: props.data.y,
      left: '0%',
      right: '0%',
      bottom: '0%',
      top: '0%',
      smooth:'line',
      containLabel: true,
      label: {
        show: true,
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

// @ts-ignore
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
  option.xAxis.data = data.x;
  option.series[0].data = data.y as number[];
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