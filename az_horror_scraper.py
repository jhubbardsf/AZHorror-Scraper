import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "http://a-zhorror.com/more-horror/horror-release-roundup-april-2020")
soup = BeautifulSoup(page.content, 'html.parser')

# Create list for upcoming movie titles
movie_titles = []
sqs_block_contents = soup.select('.sqs-block-content')

# Extract the movie_titles
for elem in sqs_block_contents:
    title = elem.select('h1 > strong')
    if (len(title) > 0):
        movie_titles.append(title[0].text)

# Remove last element from array which is an issue with their site
movie_titles.pop()

# Print list
print(movie_titles)
