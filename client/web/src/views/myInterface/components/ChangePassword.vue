<template>
    <el-dialog v-model="dialogFormVisible" title="修改密码" width="500">
        <el-form :model="form" :rules="rules" ref="formRef" label-width="100px">
            <el-form-item label="当前密码" prop="currentPassword">
                <el-input type="password" v-model="form.currentPassword" autocomplete="off" />
            </el-form-item>
            <el-form-item label="新密码" prop="newPassword">
                <el-input type="password" v-model="form.newPassword" autocomplete="off" />
            </el-form-item>
            <el-form-item label="确认密码" prop="confirmPassword">
                <el-input type="password" v-model="form.confirmPassword" autocomplete="off" />
            </el-form-item>
        </el-form>
        <div class="dialog-footer">
            <el-button @click="dialogFormVisible = false">Cancel</el-button>
            <el-button type="primary" @click="handleSubmit">
                Confirm
            </el-button>
        </div>
    </el-dialog>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';
const dialogFormVisible = ref(false);

const showModal = () => {
    console.log("showModal Pwd");
    dialogFormVisible.value = true;
}
const formRef = ref();
const form = ref({
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
});
const rules = {
    currentPassword: [{ required: true, message: '请输入当前密码', trigger: 'blur' }],
    newPassword: [{ required: true, message: '请输入新密码', trigger: 'blur' }],
    confirmPassword: [
        { required: true, message: '请确认新密码', trigger: 'blur' },
        {
            validator: (rule, value, callback) => {
                if (value !== form.value.newPassword) {
                    callback(new Error('两次输入的新密码不一致'));
                } else {
                    callback();
                }
            }, trigger: 'blur'
        }
    ]
};

const handleSubmit = () => {
    formRef.value.validate((valid) => {
        if (valid) {
            ElMessage.success('密码修改成功');
            dialogFormVisible.value = false;
            // 提交表单逻辑
        } else {
            ElMessage.error('请检查表单内容');
        }
    });
};
defineExpose({
    showModal
});
</script>

<style scoped>
.el-card {
    margin-top: 20px;
}
</style>