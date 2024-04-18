import Http from "@/G_FrameWork/Net/Http"
import SingletonFactory from "@/G_FrameWork/SingletonFactory"
import type { Result } from './API_Types/Base'
import type { ArticleInfo } from "./API_Types/Article";
const http = SingletonFactory.getInstance(Http);
export const GetArtiecleListAPI = () => {
    return http.get<Result<ArticleInfo[]>>('api/articles/');
}
export const GetArticleAPI = (id: number) => {
    return http.get<Result<ArticleInfo>>('api/articles/' + id);
}
export const CreateArticleAPI = (title: string, content: string) => {
    return http.post<Result<ArticleInfo>>('api/articles/', { title, content });
}
export const UpdateArticleAPI = (title: string, content: string) => {
    return http.put<Result<ArticleInfo>>('api/articles/', { title, content });
}
export const DeleteArticleAPI = (id: number) => {
    return http.delete<Result<null>>('api/articles/' + id);
}