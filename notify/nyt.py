import requests
from article import Article
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

articles = {}


def get_articles():
    r = requests.get(
        "https://api.nytimes.com/svc/topstories/v2/science.json?api-key=" +
        config['Keys']['NYT']
    )
    articles = []
    if r.status_code == 200:
        data = r.json()
        # print(data['results'][0]['multimedia'])
        articles = []
        for i in data['results']:
            articles.append(
                Article(i["title"], i["url"], i['multimedia'][4]['url'])
            )
    return articles


def get_new_articles():
    fresh_articles = get_articles()
    new_articles = []
    for a in fresh_articles:
        if a.get_link() not in articles:
            new_articles.append(a)
    articles.clear()
    for a in fresh_articles:
        articles[a.get_link()] = a
    return new_articles
