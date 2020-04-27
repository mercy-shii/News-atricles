import os

class Config:
    '''
    General configuration parent class
    '''
   
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=b50dd86155244655ab3cb391841bd78a'
    ARTICLE_NEWS_URL = 'https://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=b50dd86155244655ab3cb391841bd78a'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
    
  

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}    