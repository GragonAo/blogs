<template>
  <el-row>
    <el-col :span="24">
      <el-card style="padding-right: 12px" shadow="always">
        <Page_Header />
      </el-card>
    </el-col>
  </el-row>
  <el-divider border-style="double" />
  <CardItem />
</template>

<script setup lang='ts'>
import Page_Header from './components/Page_Header.vue';
import CardItem from './components/CardItem.vue'

</script>

<style scoped></style>