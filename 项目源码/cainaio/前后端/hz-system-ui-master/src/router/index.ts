import {createRouter, createWebHashHistory} from "vue-router";
import {Session} from "/@utils/StorageTools";
// 静态路由
const router = createRouter({
    history : createWebHashHistory(),
    routes: [
        {
            name:'MainIndex',
            path:'/',
            // @ts-ignore
            component:()=>import('/@page/MainIndex.vue'),
            children:[
                {
                    name:'BarDemoPage',
                    path:'/demo/barDemoPage',
                    // @ts-ignore
                    component:()=>import('/@page/demo/echarts/BarDemoPage.vue')
                },
                {
                    name:'KLineDemoPage',
                    path:'/demo/kLineDemoPage',
                    // @ts-ignore
                    component:()=>import('/@page/demo/echarts/KLineDemoPage.vue')
                },
                {
                    name:'LineDemoPage',
                    path:'/demo/LineDemoPage',
                    // @ts-ignore
                    component:()=>import('/@page/demo/echarts/LineDemoPage.vue')
                },
                {
                    name:'MapDemoPage',
                    path:'/demo/MapDemoPage',
                    // @ts-ignore
                    component:()=>import('/@page/demo/echarts/MapDemoPage.vue')
                },
                {
                    name:'PieDemoPage',
                    path:'/demo/PieDemoPage',
                    // @ts-ignore
                    component:()=>import('/@page/demo/echarts/PieDemoPage.vue')
                },
                {
                    name:'CRUDDemoPage',
                    path:'/demo/CRUDDemoPage',
                    // @ts-ignore
                    component:()=>import('/@page/demo/crud/CRUDDemoPage.vue')
                },
                {
                    name:'WordCloudDemoPage',
                    path:'/demo/WordCloudDemoPage',
                    // @ts-ignore
                    component:()=>import('/@page/demo/echarts/WrodCloudDemoPage.vue')
                },
            ]
        },
        {
            name:'LoginPage',
            path:'/login',
            // @ts-ignore
            component:()=>import('/@page/login/LoginIndex.vue')
        },
        {
            name:'BigScreenPage',
            path:'/bigScreen',
            // @ts-ignore
            component:()=>import('/@page/bigScreen/BigScreen.vue')
        },
        {
            name:'BigScreenPageEdit',
            path:'/bigScreenEdit',
            // @ts-ignore
            component:()=>import('/@page/bigScreen/BigScreenEdit.vue')
        }
    ]
})


// 登录拦截
router.beforeEach((to, from, next):void => {
    // 正则匹配 以 /demo 开头的路由 或者 /login /register 及/ 本身 无需登录即可访问
    if (to.path.match(/^\/demo/) || to.path === '/login' || to.path === '/register') {
        next()
    }
    else {
        let token = Session.get('token')
        if (token === null || token === '' || token === undefined) {
            next('/login')
        } else {
            next()
        }
    }
})

export default router
    