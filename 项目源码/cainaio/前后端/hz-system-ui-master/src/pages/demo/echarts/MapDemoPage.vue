<template>
  <n-el tag="div" class="box">
    <n-el tag="div" class="gaode-map">
      <hz-map-gaode id="map1" ref="test_map"></hz-map-gaode>
    </n-el>
    <n-el tag="div" style="width: 100%;display: flex;flex-direction: row;margin-top: 50px">
      <n-el tag="div" class="optionBox">
        <n-form
            ref="formRef"
            :label-width="120"
            :model="lntlatForm"
            label-placement="left"
        >
          <n-form-item label="起点lnt">
            <n-input v-model:value="lntlatForm.start[0]" placeholder="请输入起点lnt"/>
          </n-form-item>
          <n-form-item label="起点lat">
            <n-input v-model:value="lntlatForm.start[1]" placeholder="请输入起点lat"/>
          </n-form-item>
          <n-form-item label="终点lnt">
            <n-input v-model:value="lntlatForm.end[0]" placeholder="请输入终点lnt"/>
          </n-form-item>
          <n-form-item label="终点lat">
            <n-input v-model:value="lntlatForm.end[1]" placeholder="请输入终点lat"/>
          </n-form-item>
          <n-form-item label="操作">
            <n-button type="primary" @click="test_map.searchDriving_lnglat(lntlatForm.start,lntlatForm.end)">驾车导航</n-button>
          </n-form-item>
        </n-form>
      </n-el>
      <n-el tag="div" class="optionBox">
        <n-form
            ref="formRef"
            :label-width="120"
            :model="pointsFrom"
            label-placement="left"
        >
          <n-form-item label="起点">
            <n-input v-model:value="pointsFrom[0]" placeholder="请输入起点"/>
          </n-form-item>
          <n-form-item label="终点">
            <n-input v-model:value="pointsFrom[1]" placeholder="请输入终点"/>
          </n-form-item>
          <n-form-item label="操作">
            <n-button type="primary" @click="test_map.searchDriving(
                  [{
                    keyword: pointsFrom[0],
                    city: '重庆市'
                  },
                  {
                    keyword: pointsFrom[1],
                    city: '重庆市'
                  }]
              )">驾车导航</n-button>
          </n-form-item>
        </n-form>
      </n-el>
      <n-el tag="div" class="optionBox">
        <n-form
            ref="formRef"
            :label-width="120"
            :model="markers"
            label-placement="left"
        >
          <n-form-item label="lnt">
            <n-input v-model:value="markers.lnglat[0]" placeholder="请输入lnt"/>
          </n-form-item>
          <n-form-item label="lat">
            <n-input v-model:value="markers.lnglat[1]" placeholder="请输入lat"/>
          </n-form-item>
          <n-form-item label="content">
            <n-input v-model:value="markers.content" placeholder="请输入内容"/>
          </n-form-item>
          <n-form-item label="操作">
            <n-button type="primary" @click="test_map.addMarker(markers.lnglat[0],markers.lnglat[1],markers.content)">添加标记</n-button>
          </n-form-item>
        </n-form>
      </n-el>
    </n-el>
  </n-el>
</template>

<script lang="ts" setup>
import {onMounted, Ref, ref} from "vue";
import HzMapGaode from "/@com/echarts/map/Hz-Map-Gaode.vue";

const test_map = ref()

const lntlatForm = ref({
  start: [116.379028, 39.865042],
  end: [116.427281, 39.903719]
})

const pointsFrom = ref([
  '九龙坡',
  '沙坪坝'
])

const markers = ref(
    { lnglat: [116.379028, 39.865042], content: 'A' }
)

onMounted(() => {

});

</script>

<style scoped lang="scss">
.box{
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.gaode-map{
  width: 100%;
  height: 500px;
}
</style>