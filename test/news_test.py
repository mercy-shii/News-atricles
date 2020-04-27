import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test case to test the behaviour of the article class
    '''
    def setUp(self):
        '''
        Setup method that will run before every test
        '''
        self.new_article = Article('bbc','bbc','silah koskei','Trump','Trump takes on swearing in of Kenya oposition leader',
                                    'www.bbc.com/kenya','www.bbc.com/kenya/image.jpg',"28-01-2018T10.00.00EAT")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()