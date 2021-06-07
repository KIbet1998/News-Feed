from flask import render_template,request
from app import app
from .request import get_articles,process_articles
from .articles import Articles

# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''

    message = 'Welcome to News Feed,Stay updated'
    articles = get_articles('sports')
    print(articles)
    return render_template('index.html',message=message,articles = articles)

    
   


