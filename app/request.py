import urllib.request
import json
from .models import Source,Article





#getting api key
api_key = None

#getting news base url
base_url = None
articles_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key=app.config['NEWS_API_KEY']

    base_url=app.config['SOURCE_API_BASE_URL']
    print('***base source url***')
    print(base_url)

    article_url=app.config['ARTICLE_NEWS_URL']
    print('***base article***')
    print(articles_url)

def get_source(category):
    '''
    Function that gets json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
    print('***get_source_url***')
    print(get_source_url)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_source(source_results_list)
    return source_results

def process_source(source_list):
    '''
    function that processes the news results and transform them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain news details
    Returns:
        sources_results: Alist of news source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        urlToImage = source_item.get('urlToImage')

        if id:
            source_object = Source(id,name,description,url,category,language,country,urlToImage)

            source_results.append(source_object)
    return source_results

def get_articles(id):
    '''
    Function that gets the json response to url request
    '''
    get_articles_url = articles_url.format(id,api_key)

    print(f'***{get_articles_url}***')
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())
        articles_object = None

        

        if articles_results['articles']:
            article_object = process_articles(article_results['articles'])

    return articles_object

def process_articles(article_list):
    article_object=[]

    for article_item in article_list:
        article_id = article_item.get('id')
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        image=article_item.get('urlToImage')
        date=article_item.get('publishedAt')
        article_result=Article(article_id,author,title,description,url,image,date)
        
        article_object.append(article_result)

    return article_object