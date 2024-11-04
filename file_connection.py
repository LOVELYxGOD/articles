import json
def get_articles():
    with open("articles.json",'r', encoding='utf-8') as articles:
        articles_data = json.load(articles)
    return articles_data

def save_articles(name, text):
    with open("articles.json", 'r', encoding='utf-8') as file:
        articles = json.load(file)

    articles[name] = text

    with open("articles.json", 'w', encoding='utf-8') as file:
        json.dump(articles, file, ensure_ascii=False)

