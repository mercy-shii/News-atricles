from app import app
import urllib.request,json
from .models import source, article

Source = source.Source
Article = article.Article

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the source base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)


    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')


        if id:
             sources_object = Source(id,name,description,url)
             sources_results.append(sources_object)

    return sources_results  


def get_articles(id):
    '''
    Function that gets the json response to url request
    '''
    get_article_news_url = article_url.format(id,api_key)
    with urllib.request.urlopen(get_article_news_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(articles_list):
    '''
    process the dictionary and output a list of objects
    '''
    article_results = []
    source_dictionary = {}
    for result in articles_list:
        source_id = result ['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']

        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        image = result.get('image')
        date = result.get('date')

        if urlToImage:
            print (id)
            article_object = Article(id,name,author,title,description,url,urlToImage,date)

            article_results.append(article_object)

    return article_results    