import SingletonFactory from "@/G_FrameWork/SingletonFactory";
import type { Result } from "./API_Types/Base";
import type { UserInfo } from "./API_Types/User";
import Http from "@/G_FrameWork/Net/Http";

const http = SingletonFactory.getInstance(Http);
export const UploadImgAPI = (data: FormData) => {
    return http.post<Result<{ imgs: string }>>('api/files/upload/img/', data);
}