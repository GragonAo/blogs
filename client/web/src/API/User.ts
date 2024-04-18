import Http from "@/G_FrameWork/Net/Http"
import SingletonFactory from "@/G_FrameWork/SingletonFactory"
import type { Result } from './API_Types/Base'
import type { UserInfo, ResponseUserLogin, UserRegister } from "./API_Types/User";
const http = SingletonFactory.getInstance(Http);

export const RegisterUserAPI = (data: UserRegister) => {
    return http.post<Result<UserRegister>>('api/users/register/', data);
}
export const LoginUserAPI = (username: string, password: string) => {
    return http.post<Result<ResponseUserLogin>>('api/users/login/', { username, password });
}
export const GetUserInfoAPI = (id: number) => {
    return http.get<Result<UserInfo>>('api/users/' + id);
}