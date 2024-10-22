import {Component} from "vue";

export interface ApiEntity {
    code : number | null;
    data : any | null;
    msg : string;
}

// 用于CRUD的itemInfo
export interface CRUD_ItemInfo {
    label : string;
    key : string;
    disabled : boolean;
    show : boolean;
    type : string;
}

// 用于CRUD 表格的columnsOption
export interface CRUD_ColumnsOption {
    title : string;
    key : string;
    width : number;
    ellipsis : any; //文本溢出的设置
    disabled : boolean; //是否禁用
}

// 用于Echarts的数据格式
export interface EchartsData {
    title : string;
    name :string[];
    data : {name:string,value:number}[];
    x : string[];
    y : number[] | number[][];
}

// 用于大屏拖拽组件的数据格式
export interface DragData {
    id : string;
    position : {w:number,h:number,x:number,y:number};
    component : {id:string,com:Component | null,name:string,update:boolean,updateTime:number};
}