import {NAvatar, NText} from "naive-ui";
import {
    BookOutline,
    ExitOutline,
    BarChart,
    BarChartOutline,
    GitNetworkOutline,
    GolfOutline,
    HeadsetOutline, ListOutline, NuclearOutline, PartlySunnyOutline, LibraryOutline, MoonOutline
} from "@vicons/ionicons5";
import {renderIcon} from "/@/utils/GlobalFunction";
import {h, ref} from "vue";
import defaultHeader from "../assets/header.png";
import {RouterLink} from "vue-router";
import {useThemeConfig} from "/@bean/GlobalConfig";

const storesThemeConfig = useThemeConfig();
const { themeConfig } = storeToRefs(storesThemeConfig);

const getThemeConfig = computed(() => {
    return themeConfig.value;
});

// 主菜单
export const mainMenuOptions = ref([
    {
        label: 'Echarts',
        key: 'echarts',
        icon: renderIcon(BarChartOutline),
        show: getThemeConfig.value.isDemo,
        children: [
            {
                label: () => h(
                    RouterLink,
                    {
                        to: '/demo/barDemoPage',
                    },
                    {default: () => '柱状图'}
                ),
                icon: renderIcon(GitNetworkOutline),
                key: 'bar-demo',
            },
            {
                label: () => h(
                    RouterLink,
                    {
                        to: '/demo/kLineDemoPage',
                    },
                    {default: () => 'K线图'}
                ),
                icon: renderIcon(GolfOutline),
                key: 'k-line-demo',
            },
            {
                label: () => h(
                    RouterLink,
                    {
                        to: '/demo/LineDemoPage',
                    },
                    {default: () => '折线图'}
                ),
                icon: renderIcon(HeadsetOutline),
                key: 'line-demo',
            },
            {
                label: () => h(
                    RouterLink,
                    {
                        to: '/demo/PieDemoPage',
                    },
                    {default: () => '饼图'}
                ),
                icon: renderIcon(ListOutline),
                key: 'pie-demo',
            },
            {
                label: () => h(
                    RouterLink,
                    {
                        to: '/demo/MapDemoPage',
                    },
                    {default: () => '地图'}
                ),
                icon: renderIcon(NuclearOutline),
                key: 'map-demo',
            },
            {
                label: () => h(
                    RouterLink,
                    {
                        to: '/demo/WordCloudDemoPage',
                    },
                    {default: () => '词云图'}
                ),
                icon: renderIcon(PartlySunnyOutline),
                key: 'word-cloud-demo',
            }
        ]
    },
    {
        label: '组件',
        key: 'components',
        show: getThemeConfig.value.isDemo,
        icon: renderIcon(LibraryOutline),
        children: [
            {
                label: () => h(
                    RouterLink,
                    {
                        to: '/demo/CRUDDemoPage',
                    },
                    {default: () => 'CRUD'}
                ),
                icon: renderIcon(MoonOutline),
                key: 'crud-demo',
            }
        ]
    }
])

// 快捷菜单（右上角
export const shortcutMenuOptions =ref([
    {
        key: 'header',
        type: 'render',
        render: () => h(
            "div",
            {
                style: "display: flex; align-items: center; padding: 8px 12px;"
            },
            [
                h(NAvatar, {
                    round: true,
                    style: "margin-right: 12px;",
                    src: userInfo.value.avatar
                }),
                h("div", null, [
                    h("div", null, [h(NText, { depth: 2 }, { default: () => userInfo.value.name })]),
                    h("div", { style: "font-size: 12px;" }, [
                        h(
                            NText,
                            { depth: 3 },
                            { default: () => userInfo.value.desc }
                        )
                    ])
                ])
            ]
        )
    },
    {
        label: '返回大屏',
        key: 'bigScreen',
        icon: renderIcon(BarChart),
    },
    {
        label: '退出登录',
        key: 'logout',
        icon: renderIcon(ExitOutline),
    }
]);

const userInfo = ref({
    name : 'hz',
    avatar: defaultHeader,
    desc: '一位全栈工程师'
})