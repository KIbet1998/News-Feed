from flask import render_template 
from app import app

# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    message = 'Welcome to News Feed,Stay updated'
    return render_template('index.html',message=message)
@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    returns news details page and its data
    '''
    return render_template('news.html',id = news_id)
