from article import Article
from author import Author

class Magazine:
    def __init__(self,name,category):
        if not isinstance(name,str) and len(name) >= 2 and len(name) <= 16:
            raise ValueError("Name must be a string of lenght between 2 and 16.")
        self._name = name

        if not isinstance(category,str) and len(category) > 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not isinstance(name,str) and len(name) >= 2 and len(name) <= 16:
            raise ValueError("Name must be a string of lenght between 2 and 16.")
        self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,category):
        if not isinstance(category,str) and len(category) > 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = category

    # return a list of all the articles the magazine has published.
    def articles(self):
        return self._articles
    

    #returns a unique list of authors who have written for the magazine 
    def contributors(self):
        return list(set(article.author for article in self._articles if isinstance(article.author, Author)))


     # returning a list of article titles 
    def article_titles(self):
        if len(self._articles) == 0:
            return None
        return [article.title for article in self._articles]

    def add_article(self,article):
        if not isinstance(article,Article):
            raise ValueError("Article must be of type Article")
        self._articles.append(article)
        return article
    
    # returns a list of authors who have written more than 2 articles for the magazine
    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        
        for author in author_counts:
            if author_counts[author] > 2:
                return author
