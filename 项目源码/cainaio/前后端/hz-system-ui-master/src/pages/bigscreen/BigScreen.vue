<template>
  <n-el class="out">
    <n-el class="out_title">
      <n-el class="time">{{ time }}</n-el>
      <n-el class="znawei"></n-el>
    <n-el class="title_text">基于大数据的学习资源推荐</n-el>
      <n-el class="znawei" style="width: 15%"></n-el>
    <n-el class="userInfo">
      <n-dropdown trigger="hover" :options="options" @select="handleSelect">

      <n-badge :value="value" :max="15" style="width: 50px;height: 50px; margin-top: 2px;">
        <n-avatar size="large" style="width: 50px;height: 50px;background-image: url('/src/assets/header.png');background-size: 100% 100%;
">

        </n-avatar>
      </n-badge>
    </n-dropdown>
    </n-el>
    </n-el>
    <n-el class="out_content">
      <n-el class="left">

        <n-el class="left_up ">
          <dv-border-box12 backgroundColor="rgba(7,142,224,0.6)">
          <n-el class="echars_title">类别统计图</n-el>
          <n-el class="echars_content">
            <Hz-Echarts-Bar-Simple id="simple_bar" ref="simple_bar"></Hz-Echarts-Bar-Simple>
          </n-el>
          </dv-border-box12>
        </n-el>


        <n-el class="left_down">
          <dv-border-box12  backgroundColor="rgba(7,142,224,0.6)">
          <n-el class="echars_title">收藏占比</n-el>
          <n-el class="echars_content">
          <Hz-Echarts-Pie-Simple id="simple_pie" ref="simple_pie"></Hz-Echarts-Pie-Simple>
          </n-el>
          </dv-border-box12>
        </n-el>
      </n-el>
      <n-el class="middle">
          <n-el class="middle_up">
            <dv-border-box12  backgroundColor="rgba(7,142,224,0.6)">
            <n-button  class="button" v-for="(item,index) in button_data" :key="index" @click="find_intitle(item)">{{item}}</n-button>
            </dv-border-box12>
              </n-el>

        <div
            id="drawer-target"
            style="
                position: relative;
                 width: 100%;
                  height: 30%;
                border: 1px solid rgba(128, 128, 128, 0.2);
                margin-top: 10px;
                display: flex;
                justify-content: center;
                align-items: center;


    "
        >
          <dv-border-box12  backgroundColor="rgba(7,142,224,0.6)">

          <n-el class="middle_down">

            <n-el class="in_title" v-for="(item,index) in intitle" :key="index" >
              <n-el @click="find_inin(item,'right')">{{item}}</n-el>
              <n-button @click="shouchang(item)" style="background-color: #078ee0">收藏</n-button>
            </n-el>
          </n-el>
            </dv-border-box12>

        </div>

        <n-el class="down_down">

            <n-el style="height: 98%;width: 98%;margin-left: 1%;margin-top: 1%">
              <dv-border-box12  backgroundColor="rgba(7,142,224,0.6)">
              <n-el class="content_title">{{content_title}}</n-el>
              <n-el class="content_content">{{content}}</n-el>
              </dv-border-box12>
              </n-el>

        </n-el>


      </n-el>
      <n-el class="right">
        <n-el class="left_up">
          <dv-border-box12  backgroundColor="rgba(7,142,224,0.6)">
          <n-el class="echars_title">语言热度排行</n-el>
          <n-el class="echars_content">
          <dv-capsule-chart :config="config" style="width:42rem;height:30rem" />
          </n-el>
          </dv-border-box12>
        </n-el>
        <n-el class="left_down" v-if="!change_re">
          <dv-border-box12  backgroundColor="rgba(7,142,224,0.6)">

          <n-el class="echars_title">推荐学习</n-el>
          <n-el class="echars_content">
            <n-el class="echars_in">
          <n-el class="list" v-for="(item,index) in tuijian" :key="index" @click="getnames(item)">{{item}}</n-el>

            </n-el>
          </n-el>
          </dv-border-box12>
        </n-el>

        <n-el class="left_down" v-if="change_re">
          <dv-border-box12  backgroundColor="rgba(7,142,224,0.6)">
          <n-el class="echars_title">我的收藏
            <n-button @click="change_return">返回</n-button>
          </n-el>
          <n-el class="echars_content">
            <n-el class="echars_in">
            <n-el class="list" v-for="(item,index) in myshoucang" :key="index" @click="shouchang_changes(item)">{{item}}</n-el>
            </n-el>
          </n-el>
          </dv-border-box12>
        </n-el>
      </n-el>
    </n-el>
  </n-el>
  <n-drawer
      v-model:show="active"
      :width="400"
      :height="600"
      :placement="placement"
      :trap-focus="false"
      :block-scroll="false"
      to="#drawer-target"
      class="drawer-out"
  >
    <n-drawer-content  backgroundColor="rgba(7,142,224,0.6)">
      <n-el class="intext">
        <n-el class="drawerin" @click="changes_content(item)" v-for="(item,index) in title_in" :key="index">{{item}}</n-el>
      </n-el>
    </n-drawer-content>
  </n-drawer>
</template>

<script setup lang="ts">
import {
  getAllWord, getAllWordByc,
  getcainiao,
  getlikebyid, getname,
  getNameByname, getTuijianForUser,
  getuserinfo,
  gitcontent,
  gitinintiitle,
  gitintiitle,
  putlike,
  registerAccount, TitleCountAll
} from "/@api/my-api";
import { BorderBox12 as DvBorderBox12 } from '@kjgl77/datav-vue3'
import { ref } from 'vue'
import { DrawerPlacement } from 'naive-ui'
import HzEchartsBarSimple from "/@com/echarts/bar/Hz-Echarts-Bar-Simple.vue";
import HzEchartsPieSimple from "/@com/echarts/pie/Hz-Echarts-Pie-Simple.vue";
import router from "/@/router";
const value = ref(5)
const intitle=ref([])
const button_data=ref('')
const active = ref(false)
const placement = ref<DrawerPlacement>('right')
const title_in = ref('')
const simple_pie = ref()
const content =ref('')
const content_title=ref('')
const change_re=ref(false)
const myshoucang=ref('')
const userid = ref('')
const tuijian = ref('')
const simple_bar = ref()
const message = useMessage()
const paihangbang = ref('')
const time = ref('')

const options =[

  {
    label: '我的收藏',
    key: "myinfo"
  },
  {
    label: '返回后台(管理员)',
    key: 'goto'
  },
  {
    label: '退出系统',
    key: 'userinfo',

  },
]
function getnames(item:string){
  console.log(item)
  getname({'name':item}).then(res => {
    console.log(res.data)
    intitle.value=[]
    intitle.value.push(res.data[0])
  })
}
function change_return(){
  change_re.value=false
  console.log(change_re.value)
}
onMounted(() => {

  //每秒刷新一次
  setInterval(() => {
    time.value=new Date().toLocaleString()
  }, 1000)
  getAllWordByc().then(res => {
    console.log(res.data)
    paihangbang.value=res.data

  })
  getAllWord().then(res => {
    console.log(res.data)
    simple_pie.value.refreshCharts({
      data:res.data
    })
  })
  TitleCountAll().then(res => {
    console.log(res.data)
    simple_bar.value.refreshCharts(res.data)
  })
  getuserinfo().then(res => {
    console.log(res.data)
    userid.value=res.data.username
  })
  registerAccount().then(res => {
    button_data.value=res.data
  })
//一秒后执行
  setTimeout(() => {
    getcainiao({user:userid.value}).then(res => {
      console.log(userid.value)
      console.log(res.data)
    })

    getTuijianForUser({user:userid.value}).then(res => {
      tuijian.value=res.data
    })
  }, 1000)

})

function  handleSelect (key: string | number) {
  if(key=='myinfo'){
    change_re.value=true
    getlikebyid({id:userid.value}).then(res => {
      myshoucang.value=res.data

      console.log(res.data)
      console.log(myshoucang.value)

    })
  }
  if (key == 'goto') {
    //跳转到后台http://127.0.0.1:8000/admin/
    window.location.href = 'http://127.0.0.1:8000/admin/'
  }
  if (key == 'userinfo') {
    //退出系统
    router.push("/login");
  }
}

const config = reactive({
  data: paihangbang,
  colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff'],
  unit: '热度'


})
function find_intitle(item:string){
  console.log(item)
  gitintiitle({'title':item}).then(res => {
    console.log(res.data)
    //清空intitle
    intitle.value=[]

    for (let i = 0; i < res.data.length; i++) {
      //存入intitle

      intitle.value.push(res.data[i].name)
    }
    console.log(intitle.value)
  })
}
function shouchang(item:string){

  console.log(item)
  let data = item
  let name = ''
  getuserinfo().then(res => {
    console.log(res.data)
    name = res.data.username
  })

  // putlike({'name':name,'data':data}).then(res => {
  //   console.log(res.data)
  // })
  //延时
  setTimeout(() => {
    console.log(name,data)
    putlike({'name':name,'data':data}).then(res => {
      console.log(res.data)
      message.info(res.data)
    })
  }, 500)
}
function find_inin(item:string,place:DrawerPlacement) {
  let str = item
  //如果item含有【】就取括号中的内容
  if (item.indexOf('【') != -1) {
    item = item.substring(item.indexOf('【') + 1, item.indexOf('】'))
  }
  //如果含有‘学习 ’就取‘学习’后面的内容
  if (item.indexOf('学习 ') != -1) {
    item = item.substring(item.indexOf('学习 ') + 3, item.length)
  }
  console.log(item)
  gitinintiitle({'title':str}).then(res => {
    console.log(res.data)
    title_in.value=res.data

  })
  active.value = true
  placement.value = place
}

function changes_content(item:string){
  console.log(item)
  gitcontent({'name':item}).then(res => {
    console.log(res.data)
    content_title.value=item
    content.value=res.data
  })
}


function shouchang_changes(item:string){
  console.log(item)
  intitle.value=[]
  intitle.value.push(item)



}



</script>

<style scoped>
.list{
  margin-top: 15px;
  width: 96%;
  height: 15%;
  background: #227d98;
  color: white;
  font-size: 20px;
  display: flex;
  align-items: center;

}
.out{
  width: 100%;
  height: 100%;
  background-image: url("/src/assets/bg.png");
}
.out_title{
  width: 100%;
  height: 10%;
  background-image: url("/src/assets/two.png");
  background-size: 100% 150%;
  display: flex;


}
.in_title{
  width: 100%;
  height: 20%;
  background: #076394;
  margin-top: 2px;
  color: white;
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.down_down{
  width: 100%;
  height:48%;

}
.out_content{
  width: 100%;
  height: 90%;
  display: flex;
}
.title_text{
  font-size: 50px;
  color: rgba(7, 142, 224, 1);
  font-weight: 700;
}
.znawei{
  width: 22%;
  height: 100%;

}
.time{
  width: 15%;
  height: 100%;
  color: #094cef;
  font-size: 30px;
  display: flex;
  justify-content: center;
}
.userInfo{
  width: 20%;
  height: 100%;
  display: flex;
  justify-content: flex-end;
}
.left{
  width: 30%;
  height: 100%;
}
.middle{
  width: 40%;
  height: 100%;
}
.intext{
  width: 100%;
  height: 95%;
  flex-wrap: wrap;
  overflow-y: scroll;

  &::-webkit-scrollbar {
    display: none;
  }
}
.drawer-out{
  overflow-y: scroll;
  &::-webkit-scrollbar {
    display: none;
  }
}
.right{
  width: 30%;
  height: 100%;
}
.middle_up{
  width: 100%;
  height: 20%;

  display: flex;
  flex-wrap: wrap;
  margin-left: 2px;

}
.middle_down{
  width: 96%;
  height: 90%;
  flex-wrap: wrap;
  overflow-y: scroll;
  &::-webkit-scrollbar {
    display: none;
  }
  margin-left: 2%;
  margin-top: 2%;

}
.button{
  width: 150px;
  height: 60px;
  margin-top: 9px;
  margin-left: 30px;
  background: #1bb9d5;
  color: #ffffff;
  font-size: 20px;
  font-weight: 700;
}
.left_up{
  width: 100%;
  height: 49%;


}
.left_down{
  width: 100%;
  height: 48%;
  margin-top: 4%;

}
.drawerin{
  background: #078ee0;
  width: 100%;
  height: 20%;
  margin-top: 5px;
  overflow-y: scroll;
  &::-webkit-scrollbar {
    display: none;
  }
  color: white;
  font-size: 20px;
  display: flex;
  align-items: center;
}

.content_title{
  width: 98%;
  height: 8%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 30px;
  margin-top: 1%;
  margin-left: 1%;
}
.content_content{
  width: 98%;
  height: 88%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 5;
  overflow: hidden;
  overflow-y: scroll;

  margin-left: 1%;
  &::-webkit-scrollbar {
    display: none;
  }
}
.echars_title
{
  width: 96%;
  height: 8%;
  color: white;
  font-size: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 1%;
  margin-left: 2%;
  font-weight: 700;
}
.echars_content{
  width: 98%;
  height:88%;
  display: flex;
  margin-top: 1%;
  margin-left: 2%;


}
.echars_in{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 5;
  overflow: hidden;
  overflow-y: scroll;
  &::-webkit-scrollbar {
    display: none;
  }
}
</style>