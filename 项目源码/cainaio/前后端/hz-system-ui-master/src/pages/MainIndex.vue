<template>
  <n-config-provider :theme="getThemeConfig.theme? darkTheme : null" class="wh100">
    <n-el tag="div" class="wh100">
      <n-layout position="absolute">
        <n-layout-header style="height: 64px;" bordered>
          <n-el tag="div" class="top-box">
            <n-el tag="div" class="top-box-logo">
              <n-gradient-text :size="24" type="success">
                HZ
              </n-gradient-text>
            </n-el>
            <n-el tag="div" class="top-box-main">
              <n-menu
                  :collapsed-width="64"
                  :collapsed-icon-size="22"
                  :options="mainMenuOptions"
                  :collapsed="collapsed"
                  mode="horizontal"
                  v-if="getThemeConfig.menuPosition === 'top'"
              />
            </n-el>
            <n-el tag="div" class="top-box-user">
              <n-space>
                <n-button
                    size="small"
                    icon="ri:logout-box-r-line"
                    text
                    @click="showDrawer = true"
                >
                  <n-icon :component="ColorFilterOutline" size="24"/>
                </n-button>
                <n-dropdown
                    :options="shortcutMenuOptions"
                    trigger="click"
                    @select="handleSelect"
                >
                  <n-icon :component="Apps" size="24"/>
                </n-dropdown>
              </n-space>
            </n-el>
          </n-el>
        </n-layout-header>
        <n-layout has-sider position="absolute" style="top: 64px; bottom: 32px;" >
          <n-layout-sider
              bordered
              collapse-mode="width"
              :collapsed-width="64"
              :width="240"
              :collapsed="collapsed"
              show-trigger
              @collapse="collapsed = true"
              @expand="collapsed = false"
              v-if="getThemeConfig.menuPosition === 'left'"
              :native-scrollbar="false"
          >
            <n-menu
                :collapsed-width="64"
                :collapsed-icon-size="22"
                :options="mainMenuOptions"
                :collapsed="collapsed"
            />
          </n-layout-sider>
          <n-layout content-style="padding: 24px;"
                    :native-scrollbar="false"
          >
            <router-view></router-view>
          </n-layout>
        </n-layout>
        <n-layout-footer
            bordered
            position="absolute"
            style="height: 32px;justify-content: center;display: flex;align-items: center;"
        >
          <n-ellipsis :line-clamp="1">
            ©2023 This System Created by HZ Team 2023 All Rights Reserved
          </n-ellipsis>
        </n-layout-footer>
      </n-layout>
    </n-el>
    <n-drawer v-model:show="showDrawer" placement="right" :width="240" :native-scrollbar="false">
      <n-space justify="center" vertical>
        <n-space justify="center">
          <n-gradient-text :size="24" type="success">
            系统设置
          </n-gradient-text>
        </n-space>
        <n-space justify="center">
          <n-gradient-text type="warning">
            开发模式
          </n-gradient-text>
          <n-switch
              v-model:value="getThemeConfig.isDemo"
          >
          </n-switch>
        </n-space>
        <n-space justify="center">
          <n-gradient-text type="warning">
            主题设置
          </n-gradient-text>
            <n-switch
              v-model:value="getThemeConfig.theme"
            >
            <template #checked-icon>
              <n-icon :component="Moon"/>
            </template>
            <template #unchecked-icon>
              <n-icon :component="Sunny"/>
            </template>
          </n-switch>
        </n-space>
        <n-space justify="center">
          <n-gradient-text type="warning">
            菜单位置
          </n-gradient-text>
          <n-radio-group v-model:value="getThemeConfig.menuPosition">
            <n-radio value="left">左侧</n-radio>
            <n-radio value="top">顶部</n-radio>
          </n-radio-group>
        </n-space>
        <n-space justify="center">
          <n-button
              size="small"
              type="primary"
              @click="saveThemeConfig"
          >保存配置</n-button>
        </n-space>
      </n-space>
    </n-drawer>
  </n-config-provider>
</template>

<script lang="ts" setup>
import {darkTheme} from 'naive-ui';
import {Apps, Moon, Sunny,ColorFilterOutline} from '@vicons/ionicons5'
import {mainMenuOptions, shortcutMenuOptions} from "/@/bean/MenuConfig";
import {useThemeConfig} from "/@bean/GlobalConfig";
import {Local, Session} from "/@utils/StorageTools";
import router from "/@/router";

const collapsed = ref(false)
const showDrawer = ref(false)

const storesThemeConfig = useThemeConfig();
const { themeConfig } = storeToRefs(storesThemeConfig);

const getThemeConfig = computed(() => {
  return themeConfig.value;
});

const saveThemeConfig = () => {
  Local.set('themeConfig',getThemeConfig.value)
  router.go(0)
}

const handleSelect = (key: string) => {
  if (key === 'logout') {
    Session.remove('token')
    router.push({
      path: '/login'
    })
  }else if (key === 'bigScreen') {
    router.push({
      path: '/bigScreen'
    })
  }
}

</script>

<style scoped lang="scss">
@import "/@/assets/styles/MainIndex.css";
</style>