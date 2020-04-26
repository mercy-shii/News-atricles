from flask import render_template
from app import app
from .request import get_sources

#views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting popular source
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('enterainment')
    business_sources = get_sources('business')
    health_sources = get_sources('health')
    science_sources = get_sources('science')

    title = 'News-articles'
    return render_template('index.html',title = title,business = business_sources,health = health_sources,science = science_sources,sports = sports_sources,technology = technology_sources,entertainment = enterainment_sources,general = general_sources)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)    