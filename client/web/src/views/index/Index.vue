<template>
  <el-scrollbar height="400px">
    <el-row>
      <el-col :span="24">
        <el-card style="padding-right: 12px" shadow="always">
          <Page_Header />
        </el-card>
      </el-col>
    </el-row>
    <el-divider border-style="double" />
    <el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row>
    <el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row>
    <el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row><el-row>
      <el-col :span="12">hguighiuahuig</el-col>
    </el-row>
  </el-scrollbar>

</template>

<script setup lang='ts'>
import Http from '@/G_FrameWork/Net/Http';
import Page_Header from './components/Page_Header.vue';
import SingletonFactory from '@/G_FrameWork/SingletonFactory'
import type { User } from '@/utils/types/User';
import WebSocketClient from '@/G_FrameWork/Net/WebSocket';
</script>

<style scoped></style>