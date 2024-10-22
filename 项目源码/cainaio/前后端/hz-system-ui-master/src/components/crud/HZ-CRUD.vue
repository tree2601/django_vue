<template>
  <n-space vertical>
    <n-space justify="space-between">
      <n-button type="primary" @click="showModelBox(null,'add')">新增</n-button>
      <n-button type="primary" @click="loadData">刷新</n-button>
    </n-space>
    <n-space>
      <n-data-table
          :columns="columns"
          :data="datas"
          :bordered="true"
          :scroll-x="columns.length * 100"
          striped
          max-height="600px"
          :loading="loading"
      />
    </n-space>
    <n-space justify="end">
      <n-pagination
          v-model:page="pagination.page"
          v-model:pageSize="pagination.pageSize"
          :pageCount="pagination.pageCount"
          :showSizePicker="pagination.showSizePicker"
          :show-quick-jumper="pagination.showQuickJumper"
          :pageSizes="pagination.pageSizes"
          @update:page="loadData"
          @update:pageSize="loadData"
      />
    </n-space>
  </n-space>
  <n-modal
      v-model:show="modelOption.showModal"
      preset="dialog"
      :title="modelOption.title === 'update' ? '编辑' : modelOption.title === 'delete' ? '删除' : '新增'"
      :bordered="modelOption.bordered"
      positive-text="确认"
      negative-text="取消"
      :mask-closable="false"
      @positive-click="submitCallback"
      @negative-click="cancelCallback"
      @close="cancelCallback"
      style="width: 50%"
  >
    <n-form
        :model="fromItem"
        label-placement="left"
        label-width="100px"
    >
      <n-grid :cols="24" :x-gap="24">
        <n-form-item-gi :span="12" v-for="item in itemInfo" :label="item.label" :key="item.key" v-show="item.show">
          <n-input v-if="item.type === 'input'" type="text" v-model:value="fromItem[item.key]"
                   :disabled="item.disabled || modelOption.title === 'delete'"  />
        </n-form-item-gi>
      </n-grid>
    </n-form>
  </n-modal>
</template>

<script setup lang="ts">

import {onMounted} from "vue";
import {NButton, NFormItemGi, NGrid} from "naive-ui";
//@ts-ignore
import {grenateColumnsOption, grenateForm} from "/@utils/GlobalFunction";
//@ts-ignore
import {CRUD_ItemInfo} from "/@bean/GlobalEntity";
//@ts-ignore
import result from '/@utils/axios'

const props = defineProps({
  itemInfo: {
    type: Array as () => CRUD_ItemInfo[],
    default: [
      {label: 'id', key: 'id', type: 'input', disabled: true, show: true},
      {label: 'name', key: 'name', type: 'input', disabled: false, show: true},
      {label: 'age', key: 'age', type: 'input', disabled: false, show: true},
    ]
  },
  apiPath: {
    type: Object,
    default: {
      list: '/api/list/',
      update: '/api/update/',
      add: '/api/add/',
      del: '/api/del/',
    }
  }
});

//@ts-ignore
let loading = ref(true)

//@ts-ignore
let columns : any = ref([
  {title:'Action', key: 'action',fixed: 'right',width: 100,
    render: (row:string) => {
      //@ts-ignore
      return h(
          //@ts-ignore
          NSpace,
          {
            style: {
              display: 'flex',
              alignItems: 'center',
            },
          },
          {
            default: () => [
              //@ts-ignore
              h(NButton, { size: 'small',type:'info',
                onClick: () => {
                  showModelBox(row,'update')
                }
              }, { default: () => '编辑' }),
              //@ts-ignore
              h(NButton, { size: 'small',type:'error',
                onClick: () => {
                  showModelBox(row,'delete')
                }
              }, { default: () => '删除' }),
            ],
          }
      )
    }
  },
])

//@ts-ignore
let fromItem : any = ref({})

//@ts-ignore
let pagination = ref({
  page: 1,
  pageSize: 10,
  pageCount: 100,
  showSizePicker: true,
  showQuickJumper: true,
  pageSizes: [
    {
      label: '10 每页',
      value: 10
    },
    {
      label: '20 每页',
      value: 20
    },
    {
      label: '30 每页',
      value: 30
    },
    {
      label: '40 每页',
      value: 40
    }
  ],
})

//@ts-ignore
let datas : any = ref([
  {id: 1,name: '张三',age: 18},
  {id: 2,name: '李四',age: 19},
  {id: 3,name: '王五',age: 20},
  {id: 4,name: '赵六',age: 21},
  {id: 5,name: '田七',age: 22},
  {id: 6,name: '周八',age: 23},
  {id: 7,name: '吴九',age: 24},
  {id: 8,name: '郑十',age: 25},
  {id: 9,name: '钱十一',age: 26},
  {id: 10,name: '孙十二',age: 27},
])

//@ts-ignore
let modelOption: any = ref({
  showModal : false,
  title: 'none',
  bordered: true,
})

//@ts-ignore
let message = useMessage();

onMounted(() => {
  columns.value = grenateColumnsOption(props.itemInfo).concat(columns.value)
  fromItem.value = grenateForm(props.itemInfo)
  loadData()
})

function loadData() {
  loading.value = true
  // @ts-ignore
  api.list({
    page: pagination.value.page,
    size: pagination.value.pageSize,
    // @ts-ignore
  }).then(res => {
    if (res.code === 200) {
      datas.value = res.data.items
      pagination.value.pageCount = res.data.totalPage
      loading.value = false
    }else if(res.code===404){
      message.error('[404][模拟]获取数据成功')
      pagination.value.pageCount = 1
      pagination.value.page = 1
      pagination.value.pageSize = 10
      loading.value = false
    }else {
      message.error(res.msg)
    }
  })
}

function submitCallback() {
  if(modelOption.value.title === 'update'){
    // @ts-ignore
    api.update(fromItem.value).then(res => {
      console.log(res)
      if (res.code === 200) {
        message.success('更新成功')
        modelOption.value.showModal = false
        loadData()
      }else if(res.code===404){
        message.error('[404][模拟]更新成功')
        modelOption.value.showModal = false
        // 从datas中更新
        datas.value[datas.value.findIndex((item:any) => String(item.id) === fromItem.value.id)].id = fromItem.value.id
        datas.value[datas.value.findIndex((item:any) => String(item.id) === fromItem.value.id)].name = fromItem.value.name
        datas.value[datas.value.findIndex((item:any) => String(item.id) === fromItem.value.id)].age = fromItem.value.age
        console.log(datas.value)
        loadData()
      } else {
        message.error(res.msg)
      }
    })
  }else if(modelOption.value.title === 'delete'){
    // @ts-ignore
    api.del({
      id: fromItem.value.id
    }).then(res => {
      if (res.code === 200) {
        message.success('删除成功')
        modelOption.value.showModal = false
        loadData()
      }else if(res.code===404){
        message.error('[404][模拟]删除成功')
        modelOption.value.showModal = false
        // 从datas中删除
        datas.value.splice(datas.value.findIndex((item:any) => String(item.id) === fromItem.value.id), 1)
        loadData()
      } else {
        message.error(res.msg)
      }
    })
  }else if(modelOption.value.title === 'add'){
    // @ts-ignore
    api.add(fromItem.value).then(res => {
      if (res.code === 200) {
        message.success('新增成功')
        modelOption.value.showModal = false
        loadData()
      }else if(res.code===404){
        message.error('[404][模拟]新增成功')
        modelOption.value.showModal = false
        fromItem.value.id = datas.value.length + 1
        datas.value.push({
          id: fromItem.value.id,
          name: fromItem.value.name,
          age: fromItem.value.age,
        })
        loadData()
      } else {
        message.error(res.msg)
      }
    })
  }else{
    message.error('未知操作')
  }
}

function cancelCallback() {
  modelOption.value.showModal = false
  modelOption.value.title = 'none'
  fromItem.value = grenateForm(props.itemInfo)
}

function showModelBox(row:any, type:string) {
  if (type === 'update') {
    modelOption.value.title = 'update'
    modelOption.value.showModal = true
    for (let key in fromItem.value) {
      // @ts-ignore
      fromItem.value[key] = row[key] + ''
    }
  } else if (type === 'delete') {
    modelOption.value.title = 'delete'
    modelOption.value.showModal = true
    for (let key in fromItem.value) {
      // @ts-ignore
      fromItem.value[key] = row[key] + ''
    }
  }else if (type === 'add') {
    modelOption.value.title = 'add'
    modelOption.value.showModal = true
    for (let key in fromItem.value) {
      // @ts-ignore
      fromItem.value[key] = ''
    }
  }else{
    message.error('未知操作')
  }
}

let api = {
  list,
  update,
  add,
  del,
}

function list(query : any) {
  return result({
    url: props.apiPath.list,
    method:'get',
    params:query
  })
}

function update(query : any) {
  return result({
    url: props.apiPath.update,
    method:'post',
    data:query
  })
}

function add(query : any) {
  return result({
    url: props.apiPath.add,
    method:'put',
    data:query
  })
}

function del(query : any) {
  return result({
    url: props.apiPath.del,
    method:'delete',
    params:query
  })
}

</script>

<style scoped>

</style>