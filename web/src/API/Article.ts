import Http from "@/G_FrameWork/Net/Http"
import SingletonFactory from "@/G_FrameWork/SingletonFactory"
import type { Result } from './API_Types/Base'
import type { ArticleBasicInfo, ArticleDetailInfo, } from "./API_Types/Article";
const http = SingletonFactory.getInstance(Http);
export const GetArtiecleListAPI = () => {
    return http.get<Result<ArticleBasicInfo[]>>('api/articles/list/');
}
export const GetArticleAPI = (id: number) => {
    return http.get<Result<ArticleDetailInfo>>('api/articles/' + id);
}
export const GetUserArticlesAPI = () => {
    return http.get<Result<ArticleBasicInfo[]>>('api/articles/userArticles/');
}
export const searchAPI = (searchContent: string) => {
    return http.get<Result<ArticleBasicInfo[]>>('api/articles/search/' + searchContent);
}
export const CreateArticleAPI = (title: string, content: string) => {
    return http.post<Result<ArticleBasicInfo>>('api/articles/create/', { title, content });
}
export const UpdateArticleAPI = (id: number, data: ArticleBasicInfo) => {
    return http.put<Result<ArticleBasicInfo>>('api/articles/update/' + id + '/', data);
}
export const DeleteArticleAPI = (id: number) => {
    return http.delete<Result<null>>('/api/articles/delete/' + id);
}