# utils/smart_search.py
import os

from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser

from apps.articles.models import Article


def create_search_index():
    schema = Schema(
        id=ID(stored=True),  # 确保 ID 字段被存储
        title=TEXT(stored=True),
        content=TEXT(stored=True)
    )
    indexdir = "indexdir"
    if not os.path.exists(indexdir):
        os.makedirs(indexdir)
    index = create_in(indexdir, schema)
    writer = index.writer()

    articles = Article.objects.all()
    for article in articles:
        writer.add_document(
            id=str(article.id),  # 将 ID 转换为字符串
            title=article.title,
            content=article.content
        )
    writer.commit()


def search(query_str):
    index = open_dir("indexdir")
    qp = QueryParser("content", schema=index.schema)
    query = qp.parse(query_str)

    with index.searcher() as searcher:
        results = searcher.search(query)
        article_ids = [int(result['id']) for result in results]  # 确保 ID 是整数

    articles = Article.objects.filter(id__in=article_ids)
    return articles