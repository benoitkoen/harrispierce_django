import urllib2
from bs4 import BeautifulSoup


def get_raw_data(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    return soup


def scrapwsj1(url):

    soup = get_raw_data(url)
    result = {'titles': [], 'hrefs': [], 'teasers': [], 'images': []}

    top_section = soup.find('div', {'class': 'buckets-bottom noImage-border-wrapper'})

    articles = top_section.find_all('article', {'class': 'hed-summ'})#'hed heading-2'})

    big = top_section.find('article', {'class': 'hed-summ no-image lead-headline'})

    articles.append(list(big)[0])
    articles = articles[:-1]
    print(articles[-1])

    for article in articles:

        if article.find('div', {'class': 'text-wrapper'}) is None:
            continue
        else:
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


def scrapwsj2(url):

    soup = get_raw_data(url)
    result = {'titles': [], 'hrefs': [], 'teasers': [], 'images': []}

    top_section = soup.find('div', {'class': 'cb-row'})

    articles = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-3 locked'})
    big = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-1 locked'})

    articles.append(list(big)[0])

    for article in articles:

        a = article.find('a', {'class': 'wsj-headline-link'})
        result['titles'].append(a.text)
        result['hrefs'].append(a.get('href'))

        image_div = article.findNext('div', {'class': 'right wsj-card-feature wsj-card-media Image'})
        image = image_div.find('img', {'class': 'wsj-img-content'})
        if image is not None:
            result['images'].append(image.get('src'))
        else:
            result['images'].append('void')

        div = image_div.findNext('div', {'class': 'wsj-card-body clearfix'}) # SIBLINGS oF H3 pour image et et teaser
        teaser = div.find('p', {'class': 'wsj-summary dj-sg wsj-card-feature'}).find('span').text
        if div is not None:
            result['teasers'].append(teaser)
        else:
            result['teasers'].append('no preview')

    return result


def scrapft(url):

    soup = get_raw_data(url)
    result = {'titles': [], 'hrefs': [], 'teasers': [], 'images': []}

    articles = soup.find_all('li', {'class': 'o-teaser-collection__item o-grid-row'})

    for article in articles:

        if (article.find('img') is None) | (article.find('p', {'class': 'o-teaser__standfirst'}) is None):
            continue
        else:
            a = article.find('a', {'class': 'js-teaser-heading-link'})
            title = a.text.strip()

            result['titles'].append(title)
            result['hrefs'].append('https://www.ft.com'+a.get('href'))

            p = article.find('p', {'class': 'o-teaser__standfirst'})
            result['teasers'].append(p.text)

            image = article.find('img')
            if image is not None:
                result['images'].append(image.get('data-srcset').split(' ')[0])
            else:
                result['images'].append('void')

    return result


def scrapnyt1(url):

    soup = get_raw_data(url)
    result = {'titles': [], 'hrefs': [], 'teasers': [], 'images': []}

    down_section = soup.find('ol', {'class': 'story-menu theme-stream initial-set'})
    articles = down_section.find_all('li')

    for article in articles:

        image = article.find('img')
        if image is not None:
            result['images'].append(image.get('src'))
            
            a = article.find('a', {'class': 'story-link'})
            if a is not None:
                result['hrefs'].append(a.get('href'))

                title = a.find('h2', {'class': 'headline'}).text.strip()
                result['titles'].append(title)

                p = article.find('p', {'class': 'summary'})
                result['teasers'].append(p.text)

    return result





















