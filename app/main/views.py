from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles

#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting popular source
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    health_sources = get_sources('health')
    science_sources = get_sources('science')

    title = 'News-articles'
    return render_template('index.html',title = title,business = business_sources,health = health_sources,science = science_sources,sports = sports_sources,technology = technology_sources,entertainment = entertainment_sources,general = general_sources)

@main.route('/source_id>')
def source(id):

    '''
    View news page function that returns the news details page and its data
    '''
    articles = get_articles(id)
    title = 'News-articles'
    return render_template('source.html',articles = articles,title = title)    