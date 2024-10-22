import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router";
import pinia from '/src/stores/PiniaConfig';
import DataVVue3 from '@kjgl77/datav-vue3';

createApp(App)
    .use(pinia)
    .use(router)
    .use(DataVVue3)
    .mount('#app')
