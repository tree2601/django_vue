import {NIcon} from "naive-ui";
import {Component, h} from "vue";
import {useThemeConfig} from "../bean/GlobalConfig";
// @ts-ignore
import {CRUD_ColumnsOption, CRUD_ItemInfo} from "/@/bean/GlobalEntity";
import HzEchartsPieSimple from "/@com/echarts/pie/Hz-Echarts-Pie-Simple.vue";
import HzEchartsPieHalfDonut from "/@com/echarts/pie/Hz-Echarts-Pie-Half-Donut.vue";
import HzEchartsPieDoughnut from "/@com/echarts/pie/Hz-Echarts-Pie-Doughnut.vue";
import HzEchartsPieBorderRadius from "/@com/echarts/pie/Hz-Echarts-Pie-BorderRadius.vue";
import HzEchartsBarNegative from "/@com/echarts/bar/Hz-Echarts-Bar-Negative.vue";
import HzEchartsBarRace from "/@com/echarts/bar/Hz-Echarts-Bar-Race.vue";
import HzEchartsBarSimple from "/@com/echarts/bar/Hz-Echarts-Bar-Simple.vue";
import HzEchartsBarTangential from "/@com/echarts/bar/Hz-Echarts-Bar-Tangential.vue";
import HzEchartsKLineSimple from "/@com/echarts/kline/Hz-Echarts-KLine-Simple.vue";
import HzEchartsKLineSZ from "/@com/echarts/kline/Hz-Echarts-KLine-SZ.vue";
import HzEchartsLineArea from "/@com/echarts/line/Hz-Echarts-Line-Area.vue";
import HzEchartsLineAreaStacked from "/@com/echarts/line/Hz-Echarts-Line-AreaStacked.vue";
import HzEchartsLineSimple from "/@com/echarts/line/Hz-Echarts-Line-Simple.vue";
import HzEchartsLineSmooth from "/@com/echarts/line/Hz-Echarts-Line-Smooth.vue";
import HzEchartsLineStacked from "/@com/echarts/line/Hz-Echarts-Line-Stacked.vue";
import HzMapGaode from "/@com/echarts/map/Hz-Map-Gaode.vue";
import HzEchartsWrodCloud from "/@com/echarts/wrodcloud/Hz-Echarts-WrodCloud.vue";

export function renderIcon (icon: Component) {
    return () => h(NIcon, null, { default: () => h(icon) })
}

const storesThemeConfig = useThemeConfig();
const { themeConfig } = storeToRefs(storesThemeConfig);

const getThemeConfig = computed(() => {
    return themeConfig.value;
});

export function getEchartsTheme() :string | null{
    if(getThemeConfig.value.theme){
        return 'dark';
    }else{
        return null;
    }
}

export function getEchartsTextColor() :any{
    return getThemeConfig.value.theme ? "rgb(255,255,255)" : "rgb(0,0,0)"
}

// 根据CRUD_ItemInfo数组生成CRUD_ColumnsOption
export function grenateColumnsOption(itemInfo :CRUD_ItemInfo[]) :CRUD_ColumnsOption[]{
    let columnsOption :CRUD_ColumnsOption[] = []
    itemInfo.forEach((item :CRUD_ItemInfo) => {
        columnsOption.push({
            title: item.label,
            key: item.key,
            width: 100,
            ellipsis: {tooltip: true},
            disabled: item.disabled,
        })
    })
    return columnsOption
}

// 根据CRUD_ItemInfo数组生成From表单(以key为name,value为'')
export function grenateForm(itemInfo :CRUD_ItemInfo[]) : any{
    let form :any = {}
    itemInfo.forEach((item :CRUD_ItemInfo) => {
        form[item.key]  = ''
    })
    return form
}

// 保存文件到本地
export const saveFile = (content:any, fileName:any, fileType:any) => {
    const a = document.createElement('a')
    const file = new Blob([content], {type: fileType})
    a.href = URL.createObjectURL(file)
    a.download = fileName
    a.click()
    URL.revokeObjectURL(a.href)
}

// 根据name获取组件
export const getHzCom = (name:string):Component | null => {
    switch (name) {
        case 'HzEchartsPieSimple':
            return HzEchartsPieSimple;
        case 'HzEchartsPieHalfDonut':
            return HzEchartsPieHalfDonut;
        case 'HzEchartsPieDoughnut':
            return HzEchartsPieDoughnut;
        case 'HzEchartsPieBorderRadius':
            return HzEchartsPieBorderRadius;
        case 'HzEchartsBarNegative':
            return HzEchartsBarNegative;
        case 'HzEchartsBarRace':
            return HzEchartsBarRace;
        case 'HzEchartsBarSimple':
            return HzEchartsBarSimple;
        case 'HzEchartsBarTangential':
            return HzEchartsBarTangential;
        case 'HZEchartsKLineSimple':
            return HzEchartsKLineSimple;
        case 'HZEchartsKLineSZ':
            return HzEchartsKLineSZ;
        case 'HZEchartsLineArea':
            return HzEchartsLineArea;
        case 'HZEchartsLineAreaStacked':
            return HzEchartsLineAreaStacked;
        case 'HZEchartsLineSimple':
            return HzEchartsLineSimple;
        case 'HZEchartsLineSmooth':
            return HzEchartsLineSmooth;
        case 'HZEchartsLineStacked':
            return HzEchartsLineStacked;
        case 'HzMapGaode':
            return HzMapGaode;
        case 'HzEchartsWordCloud':
            return HzEchartsWrodCloud;
        default:
            return null;
    }
}