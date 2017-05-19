from datetime import datetime

import feedgenerator

from bs4 import BeautifulSoup

import requests

BASE_URL = 'https://www.nhl.com'
PAGE_URL = BASE_URL + '/islanders/news/'


def main():
    # Get the HTML page.
    response = requests.get(PAGE_URL)

    # Process the HTML using BeautifulSoup!
    soup = BeautifulSoup(response.content, 'html.parser')

    feed = feedgenerator.Rss201rev2Feed('Islanders News',
                                        PAGE_URL,
                                        'Islanders News')

    # Iterate over each article.
    for article in soup.find_all('article'):
        # Get the author element, this is used in a few places below.
        author = article.find_all(class_='article-item__contributor')[0]
        
        # Get the date element and parse it to a datetime.
        date = article.find_all(class_='article-item__date')[0]

        # The content is split into two pieces that must be re-assembled.
        preview = article.find_all('div', class_='article-item__preview')[0]

        feed.add_item(title=str(article.h1.string),
                      link=BASE_URL + article['data-url'],
                      description=str(preview),
                      author_name=author.contents[0].split('\n')[2].strip(),
                      author_link=author.a['href'],
                      pubdate=datetime.strptime(date['data-date'], "%Y-%m-%dT%H:%M:%S%z"))

    return feed.writeString('utf-8')


if __name__ == '__main__':
    main()
