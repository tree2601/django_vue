import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import {resolve} from "path";
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { NaiveUiResolver } from 'unplugin-vue-components/resolvers'

const pathResolve = (dir: string) => {
  return resolve(__dirname, '.', dir);
};

const alias: Record<string, string> = {
    '/@': pathResolve('./src/'),
    '/@com': pathResolve('./src/components'),
    '/@page': pathResolve('./src/pages'),
    '/@api': pathResolve('./src/api'),
    '/@utils': pathResolve('./src/utils'),
    '/@bean': pathResolve('./src/bean'),
    '/@stores': pathResolve('./src/stores'),
    '/@router': pathResolve('./src/router'),
    '/@assets': pathResolve('./src/assets'),
    '/@style': pathResolve('./src/style'),
    '/@views': pathResolve('./src/views'),
    '/@layout': pathResolve('./src/layout'),
    '/@hooks': pathResolve('./src/hooks'),
    '/@config': pathResolve('./src/config'),
};

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
      vue(),
      AutoImport({
        imports: [
          'vue',
          {
            'naive-ui': [
                'useDialog',
                'useMessage',
                'useNotification',
                'useLoadingBar',
                'NConfigProvider',
                'NLayout',
                'NLayoutContent',
                'NLayoutFooter',
                'NLayoutHeader',
                'NLayoutSider',
                'NMenu',
                'NIcon',
                'NSwitch',
                'NDropdown',
                'NEllipsis',
                'NEl',
                'NGradientText',
                'NSpace',
                'NButton',
                'NMessageProvider',
            ]
          },
          'vue-router',
            'pinia',
        ],
        dts: './auto-imports.d.ts',
      }),
      Components({
        resolvers: [NaiveUiResolver()]
      }),
  ],
    root: process.cwd(), // 项目根目录
    resolve: { alias }, // 路径别名配置
    base: '/', // 打包路径
    server: {
        host: '0.0.0.0', // 服务器地址
        port: 5173, // 服务器端口号
        open: true, // 是否自动打开浏览器
        hmr: true, // 启用热更新
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000',
                changeOrigin: true, // 允许跨域
                ws: false,
                rewrite: (pathStr) => pathStr.replace('/api', '/')
            }
        }
    }
})

