export type UserRegister = {
    username: string,
    password: string,
    password_confirm?: string,
    email: string,
    mobile?: string,
    avatar?: string
    verificatory?: number
}
export type ResponseUserLogin = {
    token: string,
    refresh_token: string,
    user_id: number
}
export type UserInfo = {
    username: string,
    email: string,
    mobile: number,
    avatar: string,
    id: number
}

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
export type Repo = {
    name: string;
    description: string | null;
    html_url: string;
    language: string | null;
}