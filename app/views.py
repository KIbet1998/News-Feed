from flask import render_template 
from app import app

# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    message = 'Welcome to News Feed,stay updated'
    return render_template('index.html',message=message)