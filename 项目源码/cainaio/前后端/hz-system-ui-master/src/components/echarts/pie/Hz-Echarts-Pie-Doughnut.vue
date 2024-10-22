<!-- 饼图 -->
<template>
  <div :id="props.id" class="wh100"></div>
</template>

<script setup lang="ts" name="HzEchartsPieDoughnut">
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
        {value: 0, name: '搜索引擎'},
        {value: 0, name: '直接访问'},
        {value: 0, name: '邮件营销'},
        {value: 0, name: '联盟广告'},
        {value: 0, name: '视频广告'}
      ]
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
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)',
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
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      data: props.data,
      left: '0%',
      right: '0%',
      bottom: '0%',
      top: '0%',
      emphasis: {
        label: {
          show: true,
          fontSize: 40,
          fontWeight: 'bold'
        }
      },
      containLabel: true,
      label: {
        color: getEchartsTextColor(),
        show: false,
        position: 'center'
      },
      labelLine: {
        show: false
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