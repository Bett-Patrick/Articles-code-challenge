from article import Article
from author import Author
from magazine import Magazine

# Test Cases
# Author class:
try:
    author1 = Author("Patrick Bett")
    print("***Author Class Test Cases***")
    print("\nAuthor name:", author1.name)
except ValueError as e:
    print("Could not create Author!!!", e)

# Check if the articles method returns all articles belonging to the author
author3 = Author("John Doe")
magazine1 = Magazine("Trending in Tech", "Technology")
# Adding articles:
article1 = author3.add_article(magazine1, "OOP in Python")
article2 = author3.add_article(magazine1, "Blockchain Applications")

print("\n**Checking Articles:**")
articles = author3.articles()
print(f"\t*{author3.name}'s Articles:*" )
if articles:
    for article in articles:
        print("- Title:", article.title)
else:
    print("Error: No articles found!!!")

# Check if the magazines method returns the list of magazines the author has contributed to
print("\n**Checking Magazines:**")
magazines = author3.magazines()
print(f"\t*{author3.name}'s Magazine contributions:*")
for magazine in magazines:
    print(f"- Magazine: {magazine.name}")

# Check if the topic_areas method returns a unique list of categories of magazines the author has contributed to
print("\n**Checking Topic Areas:**")
print(f"\t*Topic areas contributed to by {author3.name}*")
topic_areas = author3.topic_areas()
if topic_areas:
    for area in topic_areas:
        print("- Topic Area:", area)
else:
    print("No articles contributed yet.")


# Magazine class:
try:
    magazine1 = Magazine("People's Daily", "Politics")
    print("\n\n***Magazine class Test Cases***")
    print(f"Magazine: {magazine1.name}, Category: {magazine1.category}")
except ValueError as e:
    print("Could not create Magazine!!!",e)

# Add articles to magazine
magazine2 = Magazine("Building Traps", "Fitness")
author1 = Author("Patrick")
author2 = Author("Kiplangat")
author3 = Author("Bett")
article1 = Article(author1, magazine2, "Article 1")
article2 = Article(author1, magazine2, "Article 2")
article3 = Article(author2, magazine2, "Article 3")
article4 = Article(author3, magazine2, "Article 4")
article5 = Article(author3, magazine2, "Article 5")

magazine2.add_article(article1)
magazine2.add_article(article2)
magazine2.add_article(article3)
magazine2.add_article(article4)
magazine2.add_article(article5)

# Contributors to the magazine
try:
    print("\n\t**Contributors to a Magazine:**")
    contributor_names = [contributor.name for contributor in magazine2.contributors()]
    print(f"*Contributors to Magazine '{magazine2.name}'*: \n- {contributor_names}")
except ValueError as e:
    print("Could not get contributors for Magazine!!!", e)

# Check for Authors who have contributed more than 2 articles.
try:
    print("\n\t**Authors with more than 2 Article Contributions:**")
    print(f"*Authors with more than 2 articles for Magazine '{magazine2.name}'*: \n- {magazine2.contributing_authors()}")
except ValueError as e:
    print("Could not get contributing authors for Magazine!!!", e)

    
# Article class:
try:
    author2 = Author("Amos Clark")
    magazine2 = Magazine("Web 3", "Technology")
    article1 = Article(author2, magazine2, "What is web3")
    print("\n\n***Article class Test Cases***")
    print(f"Magazine: {article1.magazine.name}, Title: {article1.title}, Author: {article1.author.name}")
except ValueError as e:
    print("Could not create Article!!!", e)