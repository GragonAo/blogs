<template>
    <el-container>
        <el-header>
            <h2>编辑个人资料</h2>
        </el-header>
        <el-main>
            <el-row :gutter="20">
                <el-col :span="16">
                    <el-card>
                        <UserForm :user="user" @updateUser="updateUser" />
                    </el-card>
                </el-col>
                <el-col :span="8">
                    <el-card>
                        <UserInfo :user="user" />
                    </el-card>
                </el-col>
            </el-row>
        </el-main>
    </el-container>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import UserForm from './components/UserForm.vue';
import UserInfo from './components/UserInfo.vue';
import type { UserProfile } from '@/API/API_Types/User';

const user = ref<UserProfile>();

function updateUser(updatedUser: UserProfile) {
    Object.assign(user, updatedUser);
}

</script>

<style scoped>
.el-header {
    background-color: #f0f2f5;
    padding: 20px;
    text-align: center;
}

.el-main {
    padding: 20px;
}
</style>