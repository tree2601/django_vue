<!-- 正负柱状图 -->
<template>
  <div :id="props.id" class="wh100"></div>
</template>

<script setup lang="ts" name="HzEchartsBarNegative">
import * as echarts from 'echarts';
import {onMounted} from "vue";
//@ts-ignore
import {getEchartsTextColor, getEchartsTheme} from "/@utils/GlobalFunction";
//@ts-ignore
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
    default: '正负柱状图'
  },
  data: {
    type: Object,
    default: () => {
      return {
        x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        y: [-1, 1, -1, 1, -1, 1, -1]
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
  xAxis: {
    type: 'value',
    position: 'top',
    axisLine: {
      lineStyle: {
        color: getEchartsTextColor()
      }
    },
    splitLine: {
      lineStyle: {
        type: 'dashed'
      }
    },
  },
  yAxis: {
    type: 'category',
    axisLabel: { show: false },
    axisTick: { show: false },
    splitLine: { show: false },
    data: props.data.x,
    axisLine: {
      show: false,
      lineStyle: {
        color: getEchartsTextColor()
      }
    }
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
  series: [
    {
      name: 'Access From',
      type: 'bar',
      stack: 'Total',
      data : props.data.y,
      label: {
        show: true,
        color: getEchartsTextColor(),
        position: 'right',
        valueAnimation: true,
      },
      itemStyle: {
        color: function (params: any) {
          return params.value >= 0 ? '#00d887' : '#0086c3';
        }
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
    option.xAxis.axisLine.lineStyle.color = getEchartsTextColor()
    option.yAxis.axisLabel.color = getEchartsTextColor()
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