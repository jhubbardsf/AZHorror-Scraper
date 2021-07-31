import requests
import time
from bs4 import BeautifulSoup

# Needed variables for later
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
years = ["2018", "2019", "2020", "2021"]

# Create list for upcoming movie titles
movie_titles = []

for year in years:
    for month in months:
        # Make a request
        page = requests.get(f'http://a-zhorror.com/more-horror/horror-release-roundup-{month}-{year}')
        time.sleep(5)
        this_month = 0


        soup = BeautifulSoup(page.content, 'html.parser')
        sqs_block_contents = soup.select('.sqs-block-content')

        # Extract the movie_titles
        for elem in sqs_block_contents:
            title = elem.select('h1 > strong')
            if (len(title) > 0):
                movie_title = title[0].text
                movie_titles.append(movie_title)
                this_month += 1

        # Remove last element from array which is an issue with their site
        if (len(movie_titles) > 0):
            movie_titles.pop()
        print(f'{month} of {year} is done... {"error" if ((this_month - 1) == -1) else (this_month - 1)}')



# Print list
print(movie_titles)
print(f'Total movies: {len(movie_titles)}')
