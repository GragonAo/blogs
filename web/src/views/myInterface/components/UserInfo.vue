<template>
    <div class="profile-container">
        <el-card>
            <h2>用户资料</h2>
            <el-form :model="editableUserProfile" label-width="120px">
                <el-row>
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
                <el-row>
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
                <el-row>
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
                <el-row>
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
                <el-row>
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
                <el-row>
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
                <el-row>
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
import { reactive } from 'vue';
import { ElMessage } from 'element-plus';

export type UserProfile = {
    school?: string | null;
    address?: string | null;
    city?: string | null;
    state?: string | null;
    zip?: string | null;
    age?: number | null;
    hobbies?: string | null;
    linkedin?: string | null;
    github?: string | null;
    degree?: string | null;
    major?: string | null;
    graduation_year?: number | null;
    company_name?: string | null;
    job_title?: string | null;
    job_description?: string | null;
    skills?: string | null;
    certificates?: string | null;
    languages?: string | null;
}

const props = defineProps<{
    userProfile: UserProfile;
}>();

const editableUserProfile = reactive({ ...props.userProfile });

const saveProfile = () => {
    // 这里可以添加保存逻辑，例如发送到服务器
    ElMessage.success('用户资料已保存');
};

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
}

.el-row {
    margin-bottom: 10px;
}
</style>