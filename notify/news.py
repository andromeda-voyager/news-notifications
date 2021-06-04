import guardian
import nyt

news_sources = [guardian.get_new_articles, nyt.get_new_articles]


def get_new_articles():
    articles = []
    for source in news_sources:
        articles += source()
    return articles
