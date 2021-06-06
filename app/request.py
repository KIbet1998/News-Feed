from app import app
import urllib.request,json
from .models import Articles

Articles = articles.Articles
#getting api key
api_key = app.config['NEWS_API_KEY']
#getting the nes base url
base_url = app.config['NEWS_ARTICLES_API_BASE_URL']

def get_articles(articles)