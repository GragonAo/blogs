export type UserRegister = {
    username: string,
    password: string,
    password_confirm?: string,
    email: string,
    mobile?: number,
    avatar?: string
    verificatory?: number
}
export type ResponseUserLogin = {
    token: string,
    refresh: string,
    id: number,
}
export type UserInfo = {
    username: string,
    email: string,
    mobile: number,
    avatar: string,
    id: number
}
export type UserLoginInfo = UserInfo & ResponseUserLogin