import Http from "@/G_FrameWork/Net/Http"
import SingletonFactory from "@/G_FrameWork/SingletonFactory"
import type { Result } from './API_Types/Base'
import type { ArticleInfo } from "./API_Types/Article";
const http = SingletonFactory.getInstance(Http);
export const GetArtiecleListAPI = () => {
    return http.get<Result<ArticleInfo[]>>('api/articles/list/');
}
export const GetArticleAPI = (id: number) => {
    return http.get<Result<ArticleInfo>>('api/articles/' + id);
}
export const GetUserArticlesAPI = () => {
    return http.get<Result<ArticleInfo[]>>('api/articles/userArticles/');
}
export const CreateArticleAPI = (title: string, content: string) => {
    return http.post<Result<ArticleInfo>>('api/articles/create/', { title, content });
}
export const UpdateArticleAPI = (id: number, data: ArticleInfo) => {
    return http.put<Result<ArticleInfo>>('api/articles/update/' + id, data);
}
export const DeleteArticleAPI = (id: number) => {
    return http.delete<Result<null>>('/api/articles/delete/' + id);
}