import requests
from notify.article import Article
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
articles = {}


def get_articles():
    r = requests.get(
        "https://content.guardianapis.com/search?section=science&page=3&show-fields=thumbnail&api-key=" + config['Keys']['Guardian']
    )
    articles = []
    if r.status_code == 200:
        data = r.json()
        results = data["response"]["results"]
        articles = []
        for i in results:
            articles.append(
                Article(i["webTitle"], i["webUrl"], i["fields"]["thumbnail"])
            )
    return articles


def check_for_new():
    fresh_articles = get_articles()
    new_articles = []
    for a in fresh_articles:
        if a.get_link() not in articles:
            new_articles.append(a)
    articles.clear()
    for a in fresh_articles:
        articles[a.get_link()] = a
    return new_articles
