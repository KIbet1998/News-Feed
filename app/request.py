from app import app
import urllib.request,json
from .articles import Articles
from app import articles

Articles = articles.Articles
Source = source.Source
#getting api key
api_key = app.config['NEWS_API_KEY']
#getting the news base url
articles_url = app.config['NEWS_ARTICLES_API_BASE_URL']
#getting the source base url
base_url=app.config['NEWS_SOURCES_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        source_results = None
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
    return source_results
    
def get_articles(id):
    '''
    process the articles and returns a list of objects
    '''
    get_articles_url = articles_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data= url.read()
        get_articles_response=json.loads(get_articles_data)
        articles_result=None
        if get_articles_response['articles']:
            articles_result_list=get_articles_response['articles']
            articles_result = process_articles(articles_result_list)
    
    return articles_result   


def process_articles(articles_list):
    articles_object=[]
    for article_item in articles_list:
        id= article_item.get('id')
        title =article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        image=article_item.get('image')
        date = article_item.get('date')

        if image:
            articles_result=Articles(id,title,description,url,image,date)
            articles_object.append(articles_result)
       

    print(articles_object)
    return articles_object

