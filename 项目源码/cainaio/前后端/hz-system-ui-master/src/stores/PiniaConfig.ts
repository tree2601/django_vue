// https://pinia.vuejs.org/
// @ts-ignore
import { createPinia } from 'pinia';
// @ts-ignore
import piniaPluginPersist from 'pinia-plugin-persist';

// 创建
const pinia = createPinia();
pinia.use(piniaPluginPersist);

// 导出
export default pinia;
