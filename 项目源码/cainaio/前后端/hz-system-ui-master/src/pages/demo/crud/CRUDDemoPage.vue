<template>
  <HZCRUD
      :itemInfo="itemInfo"
      :apiPath="apiPath"
  ></HZCRUD>
</template>

<script setup lang="ts">
import HZCRUD from "/@com/crud/HZ-CRUD.vue";

let itemInfo = [
  {label: 'id', key: 'id', type: 'input', disabled: true, show: true},
  {label: 'name', key: 'name', type: 'input', disabled: false, show: true},
  {label: 'age', key: 'age', type: 'input', disabled: false, show: true},
]

let apiPath = {
  list: '/api/list/',
  update: '/api/update/',
  add: '/api/add/',
  del: '/api/del/',
}

</script>

<style scoped>

</style>