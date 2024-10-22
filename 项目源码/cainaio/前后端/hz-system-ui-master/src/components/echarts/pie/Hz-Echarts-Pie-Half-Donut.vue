<!-- 饼图 -->
<template>
  <div :id="props.id" class="wh100"></div>
</template>

<script setup lang="ts" name="HzEchartsPieHalfDonut">
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
    default: '圆角空心饼图'
  },
  data: {
    type: Array,
    default: () => {
      return [
        { value: 1048, name: 'Search Engine' },
        { value: 735, name: 'Direct' },
        { value: 580, name: 'Email' },
        { value: 484, name: 'Union Ads' },
        { value: 300, name: 'Video Ads' },
        {
          // make an record to fill the bottom 50%
          value: 1048 + 735 + 580 + 484 + 300,
          itemStyle: {
            // stop the chart from rendering this piece
            color: 'none',
            decal: {
              symbol: 'none'
            }
          },
          label: {
            show: false
          }
        }
      ]
    }
  }
});

const option = {
  backgroundColor: "rgba(0,0,0,0)",
  title: {
    text: props.title,
    left: 'center',
    top: 40,
    textStyle: {
      color: getEchartsTextColor()
    },
    show: props.showTitle
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)',
    show: props.showTooltip
  },
  legend: {
    left: 'center',
    textStyle: {
      color: getEchartsTextColor()
    },
    selectedMode: false,
    show: props.showLegend
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: ['40%', '70%'],
      center: ['50%', '70%'],
      startAngle: 180,
      data: props.data,
      left: '0%',
      right: '0%',
      bottom: '0%',
      top: '0%',
      containLabel: true,
      label: {
        color: getEchartsTextColor(),
        show: true,
        formatter(param : any) {
          // correct the percentage
          return param.name + ' (' + param.percent * 2 + '%)';
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
  option.legend.textStyle.color = getEchartsTextColor()
  option.series[0].label.color = getEchartsTextColor()
}

// 刷新图表方式，该方法需要提供给外部调用
// eslint-disable-next-line no-unused-vars
const refreshCharts = (data : EchartsData) => {
  option.title.text = data.title;
  option.series[0].data = data.data;
  let total = 0;
  data.data.forEach((item) => {
    total += item.value;
  });
  option.series[0].data.push({
    value: total,
    itemStyle: {
      // stop the chart from rendering this piece
      color: 'none',
      decal: {
        symbol: 'none'
      }
    },
    label: {
      show: false
    }
  })
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