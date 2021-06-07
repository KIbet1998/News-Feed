from flask import render_template,request
from app import app
from .request import get_sources,get_articles
from .models import source

# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    sources = get_sources('sources')
    print(sources)

    return render_template('index.html',sources = sources)

@app.route('/articles')
def articles():
    articles = get_articles('sports')
    return render_template('articles.html',articles = articles)

    
   


