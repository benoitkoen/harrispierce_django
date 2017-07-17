import urllib2
from bs4 import BeautifulSoup


def get_raw_data(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    return soup


def scrapwsj1(url):

    soup = get_raw_data(url)
    result = {'titles': [], 'hrefs': [], 'teasers': [], 'images': []}

    articles = soup.find_all('article', {'class': 'hed-summ'})

    for article in articles:

        a = article.find('a', {'class': 'subPrev headline'})
        result['titles'].append(a.text)
        result['hrefs'].append(a.get('href'))

        div = article.find('div', {'class': 'text-wrapper'})
        if div is not None:
            result['teasers'].append(div.find('p', {'class': 'summary'}).text)
        else:
            result['teasers'].append('no preview')

        image = article.find('img')
        if image is not None:
            result['images'].append(image.get('data-src'))
        else:
            result['images'].append('void')

    return result
