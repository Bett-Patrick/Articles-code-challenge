class Article:
    def __init__(self,author,magazine,title):
        if not isinstance(title,str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a non-empty string and of lenght between 5 and 50!!!")
        self._title = title
        self._author = author
        self._magazine = magazine

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author!!!")
        self._author = author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        if not isinstance(magazine,Magazine):
            raise ValueError("Magzine must be of type Magazine!!!")
        self._magazine = magazine
    

