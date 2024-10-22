// @ts-ignore
import {defineStore} from "pinia";
import {ThemeConfigState, UserState} from "/@/type/pinia";

export const useThemeConfig = defineStore('themeConfig', {
    state: () : ThemeConfigState => ({
        themeConfig: {
            // 菜单位置 left | top
            menuPosition: 'left',
            // 主题颜色
            theme: true,
            // 是否是demo模式
            isDemo: false,
        },
    }),
    actions: {
        setThemeConfig(data:ThemeConfigState) {
            // @ts-ignore
            this.themeConfig = data
        }
    }
})

export const useUser = defineStore('user', {
    state: () : UserState => ({
        userInfo: {
            name: '',
            avatar: '',
            token: '',
        }
    }),
    actions: {
        setUserInfo(data:UserState) {
            // @ts-ignore
            this.userInfo = data
        }
    }
})
