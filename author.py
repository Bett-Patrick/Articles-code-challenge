from article import Article

class Author:
    def __init__(self,name):
        if not isinstance(name,str) and len(name) == 0:
            raise TypeError("Name must be of type str")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    # return all articles belonging to an author.
    def articles(self):
        return self._articles
    
    # return lists of magazines the author has contributed to.
    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    # Creates and returns a new Article instance and associates the magazine provided with the author.
    def add_article(self,magazine,title):
        article = Article(self,magazine,title)
        if not isinstance(article,Article):
            raise ValueError("Article must be of type Article!!!")
        self._articles.append(article)
        return article

    # returns a unique list with the categories of the magazines the author has contributed to.
    def topic_areas(self):
        if len(self._articles) == 0:
            return None
        return list(set(article.magazine.category for article in self._articles))
    
    

