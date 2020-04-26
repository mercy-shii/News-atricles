from app import app
import urllib.request,json
from .models import Source

Source = source.Source

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the source base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_result_list = get_source_response['sources']
            source_results = process_source(sources_result_list)


    return source_results

def process_sources(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_sources = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        

        if poster:
            source_object = Source(id,name,description)
            source_results.append(source_object)

    return source_sources   