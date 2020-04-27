class Source:
    '''
    Source class to define source Objects
    '''

    def __init__(self,id,name,description,url,category,language,country,urlToImage):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        self.urlToImage = urlToImage



class Article:
    '''
    Article class to define article objects
    '''
    
    def __init__(self,id,author,title,description,image,url,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.image = image
        self.url = url
        self.date = date        