import axios from "axios";
// @ts-ignore
import {ApiEntity} from "/@/bean/GlobalEntity";

// 跨域请求，允许保存cookie
axios.defaults.withCredentials = true;

// 返回状态码
axios.defaults.validateStatus = function (status) {
    return status >= 200 && status <= 500; // 默认的
}

// 超时设置
axios.defaults.timeout = 10000;

// 获取cookie
export function getCookie(name :string) {
    let arr;
    const reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    return (arr = document.cookie.match(reg)) ? arr[2] : null;
}

// 请求拦截器
axios.interceptors.request.use(
    config => {
        // 如果是Post请求则进行序列化
        if(config.method  === 'post' || config.method  === 'put'){
            config.headers['Content-Type'] = 'application/x-www-form-urlencoded';
        }
        return config;
    },error => {
        return Promise.reject(error);
    }
);

// 响应拦截器
axios.interceptors.response.use(
    // @ts-ignore
    response => {
        const status = Number(response.status) || 200;
        if(status === 200){
            let results :ApiEntity ={
                code: response.data.code,
                data: response.data.data,
                msg: response.data.msg
            }
            return results;
        }else{
            let results : { msg: string; code: number } ={
                code: status,
                msg: response.statusText
            }
            return results;
        }
    }
);

export default axios;