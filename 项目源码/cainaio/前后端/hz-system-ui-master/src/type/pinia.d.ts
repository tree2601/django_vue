import {darkTheme} from 'naive-ui';

// 布局配置
declare interface ThemeConfigState {
    themeConfig:{
        menuPosition: string;
        theme: boolean;
        isDemo: boolean;
    }
}

// 用户信息
declare interface UserState {
    userInfo: {
        name: string;
        avatar: string;
        token: string;
    };
}