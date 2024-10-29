import json
def get_articles():
    with open("articles.json",'r',encoding='utf-8') as articles:
    	articles_data = json.load(articles)
    return articles_data
