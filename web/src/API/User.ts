import Http from "@/G_FrameWork/Net/Http"
import SingletonFactory from "@/G_FrameWork/SingletonFactory"
import type { Result } from './API_Types/Base'
import type { UserInfo, ResponseUserLogin, UserRegister, UserProfile } from "./API_Types/User";
import useUserStore from "@/stores/User";
const http = SingletonFactory.getInstance(Http);

export const RegisterUserAPI = (data: UserRegister) => {
    return http.post<Result<UserRegister>>('api/users/register/', data);
}
export const LoginUserAPI = (username: string, password: string, imgBase64?: ['']) => {
    return http.post<Result<ResponseUserLogin>>('api/users/login/', { username, password, imgBase64 });
}
export const GetUserInfoAPI = () => {
    return http.get<Result<UserInfo>>('api/users/userinfo/');
}
export const GetUserProfile = () => {
    return http.get<Result<UserProfile>>('api/users/userProfile/');
}
export const UploadUserAvatarAPI = (data: FormData) => {
    return http.post<Result<UserInfo>>('api/users/upload/avatar/', data);
}
export const UploadUserPhotoAPI = (data: FormData) => {
    return http.post<Result<{}>>('api/users/upload/face/', data);
}