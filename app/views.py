from flask import render_template,request
from app import app
from .request import get_sources,process_articles
from app import source

# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    sources = get_sources('sources')
    print(sources)

    return render_template('index.html',message=message,articles = articles)

    
   


