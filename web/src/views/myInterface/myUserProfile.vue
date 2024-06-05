<template>
    <div class="profile-container">
        <el-card shadow="hover">
            <h2>用户资料</h2>
            <el-form :model="editableUserProfile" label-width="120px" class="profile-form">
                <el-row :gutter="20">
                    <el-col :span="12">
                        <el-form-item label="学校">
                            <el-input v-model="editableUserProfile.school" />
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="地址">
                            <el-input v-model="editableUserProfile.address" />
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="12">
                        <el-form-item label="城市">
                            <el-input v-model="editableUserProfile.city" />
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="州/省">
                            <el-input v-model="editableUserProfile.state" />
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="12">
                        <el-form-item label="邮政编码">
                            <el-input v-model="editableUserProfile.zip" />
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="年龄">
                            <el-input v-model="editableUserProfile.age" type="number" />
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="12">
                        <el-form-item label="爱好">
                            <el-input v-model="editableUserProfile.hobbies" />
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="LinkedIn">
                            <el-input v-model="editableUserProfile.linkedin" />
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="12">
                        <el-form-item label="GitHub">
                            <el-input v-model="editableUserProfile.github" />
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="学历">
                            <el-input v-model="editableUserProfile.degree" />
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="12">
                        <el-form-item label="专业">
                            <el-input v-model="editableUserProfile.major" />
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="毕业年份">
                            <el-input v-model="editableUserProfile.graduation_year" type="number" />
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="12">
                        <el-form-item label="公司名称">
                            <el-input v-model="editableUserProfile.company_name" />
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="职位">
                            <el-input v-model="editableUserProfile.job_title" />
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-form-item label="职位描述">
                    <el-input type="textarea" v-model="editableUserProfile.job_description" />
                </el-form-item>
                <el-form-item label="技能">
                    <el-input type="textarea" v-model="editableUserProfile.skills" />
                </el-form-item>
                <el-form-item label="证书">
                    <el-input type="textarea" v-model="editableUserProfile.certificates" />
                </el-form-item>
                <el-form-item label="语言">
                    <el-input type="textarea" v-model="editableUserProfile.languages" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="saveProfile">保存</el-button>
                    <el-button @click="resetProfile">重置</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import { ElMessage } from 'element-plus';
import type { UserProfile } from '@/API/API_Types/User';
import { GetUserProfile, UpdateUserProfile } from '@/API/User';
const props = defineProps<{
    userProfile: UserProfile;
}>();

const editableUserProfile = ref({ ...props.userProfile });

const saveProfile = async () => {
    await UpdateUserProfile(editableUserProfile.value).then((res) => {
        if (res?.code == 200) ElMessage.success('用户资料已保存');
        else ElMessage.error(res?.message);
    }).catch((err) => {
        ElMessage.error(err);
    });

};
const getProfile = async () => {
    await GetUserProfile().then(res => {
        if (res?.code == 200) editableUserProfile.value = res.data;
        else ElMessage.error(res?.message);
    }).catch((err) => {
        ElMessage.error(err);
    })
}
onMounted(() => {
    getProfile();
})

const resetProfile = () => {
    Object.assign(editableUserProfile, props.userProfile);
    ElMessage.info('用户资料已重置');
};
</script>

<style scoped>
.profile-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.el-card {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
}

h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
}

.el-row {
    margin-bottom: 10px;
}

.el-form-item {
    margin-bottom: 20px;
}

.el-input {
    width: 100%;
}

.el-button {
    margin-right: 10px;
}
</style>