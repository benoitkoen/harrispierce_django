import urllib2
from bs4 import BeautifulSoup

url = 'https://www.wsj.com/news/opinion'

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'lxml')

#a = soup.find_all('a', {'class': 'subPrev headline'})
art = soup.find_all('article', {'class': 'hed-summ'})

print(art[0])

"""
for el in art:
    li = el.find_all('a', {'class': 'subPrev headline'})
    for a in li:
        print(a.text)
        print(a.get('href'))

    div = el.find_all('div', {'class': 'text-wrapper'})
    for d in div:
        print(d.find('p', {'class': 'summary'}).text)

    image = el.find('img')
    if el.find('img') is not None:
        print(image.get('data-src'))
    else:
        print('void')
        
"""


