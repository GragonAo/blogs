<template>
    <el-form :model="form" label-width="100px">
        <el-form-item label="用户名">
            <el-input v-model="form.username" />
        </el-form-item>
        <el-form-item label="电子邮件地址">
            <el-input v-model="form.email" />
        </el-form-item>
        <el-form-item label="名">
            <el-input v-model="form.firstName" />
        </el-form-item>
        <el-form-item label="姓">
            <el-input v-model="form.lastName" />
        </el-form-item>
        <el-divider />
        <el-form-item label="地址">
            <el-input v-model="form.address" />
        </el-form-item>
        <el-form-item label="城市">
            <el-input v-model="form.city" />
        </el-form-item>
        <el-form-item label="国家">
            <el-input v-model="form.country" />
        </el-form-item>
        <el-form-item label="邮政编码">
            <el-input v-model="form.postalCode" />
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="handleSubmit">保存</el-button>
        </el-form-item>
    </el-form>
</template>

<script lang="ts" setup>
import { defineProps, defineEmits, reactive } from 'vue';

const props = defineProps<{ user: any }>();
const emits = defineEmits(['updateUser']);
const form = reactive({ ...props.user });

function handleSubmit() {
    emits('updateUser', form);
}
</script>

<style scoped>
.el-form-item {
    margin-bottom: 20px;
}
</style>