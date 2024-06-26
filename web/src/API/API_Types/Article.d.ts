export type ArticleBasicInfo = {
    id?: number,
    create_time?: string
    update_time?: string,
    title: string,
    content: string,
    likes?: number,
    views?: number,
    comments_count?: number,
    shares?: number,
    categories?: string,
    tags?: string,
    user?: number
}
export type ArticleDetailInfo = ArticleBasicInfo & {
    username: string,
    avatar: string
}