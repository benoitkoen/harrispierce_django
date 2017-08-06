from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep

from harrispierce.scrapping.scrap_articles import scrap_ft_article
#from harrispierce.processing.clean_articles import clean_article


def get_raw_data(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    return soup


def scrapwsj1(journal, section, url):

    soup = get_raw_data(url)
    result = {'journal': [], 'section': [], 'titles': [], 'hrefs': [],
              'teasers': [], 'images': [], 'article': [], 'cleaned_article': []}

    top_section = soup.find('div', {'class': 'buckets-bottom noImage-border-wrapper'})

    articles = top_section.find_all('article', {'class': 'hed-summ'})

    big = top_section.find('article', {'class': 'hed-summ no-image lead-headline'})

    articles.append(list(big)[0])
    articles = articles[:-1]

    for article in articles:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

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


def scrapwsj2(journal, section, url):

    soup = get_raw_data(url)
    result = {'journal': [], 'section': [], 'titles': [], 'hrefs': [], 'teasers': [],
              'images': [], 'article': [], 'cleaned_article': []}

    top_section = soup.find('div', {'class': 'cb-row'})

    articles = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-3 locked'})
    big = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-1 locked'})

    try:
        articles.append(list(big)[0])
    except IndexError:
        pass

    for article in articles:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

        a = article.find('a', {'class': 'wsj-headline-link'})
        result['titles'].append(a.text)
        result['hrefs'].append(a.get('href'))

        image_div = article.findNext('div', {'class': 'right wsj-card-feature wsj-card-media Image'})
        image = image_div.find('img', {'class': 'wsj-img-content'})
        if image is not None:
            result['images'].append(image.get('src'))
        else:
            image = image_div.find('meta')
            if image is not None:
                result['images'].append(image.get('content'))
            else:
                result['images'].append('void')

        div = image_div.findNext('div', {'class': 'wsj-card-body clearfix'}) # SIBLINGS oF H3 pour image et et teaser
        teaser = div.find('p', {'class': 'wsj-summary dj-sg wsj-card-feature'}).find('span').text
        if div is not None:
            result['teasers'].append(teaser)
        else:
            result['teasers'].append('no preview')

    return result


def scrapwsj3(journal, section, url):

    soup = get_raw_data(url)
    result = {'journal': [], 'section': [], 'titles': [], 'hrefs': [],
              'teasers': [], 'images': [], 'article': [], 'cleaned_article': []}

    top_section = soup.find('div', {'class': 'buckets-bottom noImage-border-wrapper'})

    articles = top_section.find_all('article', {'class': 'hed-summ'})
    big = top_section.find_all('article', {'class': 'lead-headline hed-summ'})

    articles.append(list(big)[0])

    articles = articles[0:5]

    for article in articles:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

        if article.find('div', {'class': 'text-wrapper'}) is None:
            continue

        else:

            a = article.find('a', {'class': 'subPrev headline'})

            if a is None:
                a = article.find('a', {'class': 'headline'})

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


def scrapwsj4(journal, section, url):

    soup = get_raw_data(url)
    result = {'journal': [], 'section': [], 'titles': [], 'hrefs': [], 'teasers': [],
              'images': [], 'article': [], 'cleaned_article': []}

    top_section = soup.find('div', {'class': 'cb-row'})

    articles = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-3 locked'})
    big = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-1 locked'})

    articles.append(list(big)[0])

    for article in articles:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

        a = article.find('a', {'class': 'wsj-headline-link'})
        result['titles'].append(a.text)
        result['hrefs'].append(a.get('href'))

        image_div = article.find_next_sibling('div', {'class': 'right wsj-card-feature wsj-card-media Image'})

        if image_div is not None:
            image = image_div.find('img', {'class': 'wsj-img-content'})

            div = article.find_next_sibling().find_next_sibling('div', {'class': 'wsj-card-body clearfix'}) # SIBLINGS oF H3 pour image et teaser
            teaser = div.find('p', {'class': 'wsj-summary dj-sg wsj-card-feature'}).find('span').text
            result['teasers'].append(teaser)

            result['images'].append(image.get('src'))
        else:
            div = article.find_next_sibling('p', {'class': 'wsj-summary dj-sg wsj-card-feature'}) # SIBLINGS oF H3 pour image et teaser

            if div is None:
                div = article.find_next_sibling().find('p', {'class': 'wsj-summary dj-sg wsj-card-feature'})

            teaser = div.find('span').text
            result['teasers'].append(teaser)

            result['images'].append('void')

    return result


def scrapft(journal, section, url):

    soup = get_raw_data(url)
    result = {'journal': [], 'section': [], 'titles': [], 'hrefs': [], 'teasers': [],
              'images': [], 'article': [], 'cleaned_article': []}

    articles = soup.find_all('li', {'class': 'o-teaser-collection__item o-grid-row'})

    for article in articles:

        result['journal'].append(journal)
        result['section'].append(section)

        result['cleaned_article'].append('void')

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

    login_url = \
        'https://accounts.ft.com/login?location=https%3A%2F%2Fwww.ft.com%2Fcontent%2F6f2f8b0e-73d9-11e7-aca6-c6bd07df1a3c'

    for href in result['hrefs']:
        result['article'].append(scrap_ft_article(login_url, href))
        sleep(15)

    #for article in result['article']:
    #    result['cleaned_content'].append(clean_article(article))

    return result


def scrapnyt1(journal, section, url):

    soup = get_raw_data(url)
    result = {'journal': [], 'section': [], 'titles': [], 'hrefs': [], 'teasers': [],
              'images': [], 'article': [], 'cleaned_article': []}

    down_section = soup.find('ol', {'class': 'story-menu theme-stream initial-set'})
    articles = down_section.find_all('li')

    for article in articles:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

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


def scrapnyt2(journal, section, url):

    soup = get_raw_data(url)
    result = {'journal': [], 'section': [], 'titles': [], 'hrefs': [], 'teasers': [],
              'images': [], 'article': [], 'cleaned_article': []}

    col = soup.find('div', {'class': 'columnGroup last'})
    articles = col.find_all('div', {'class': 'story'})

    for article in articles:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

        h3 = article.find('h3')
        title = h3.find('a').text.strip()
        href = h3.find('a').get('href')

        result['titles'].append(title)
        result['hrefs'].append(href)

        p = article.find('p', {'class': 'summary'})
        result['teasers'].append(p.text.strip())

        image = article.find('img')
        if image is not None:
            result['images'].append(image.get('src'))
        else:
            result['images'].append('void')

    return result


def scraple(journal, section, url):
    soup = get_raw_data(url)
    result = {'journal': [], 'section': [], 'titles': [], 'hrefs': [], 'teasers': [],
              'images': [], 'article': [], 'cleaned_article': []}

    col = soup.find('div', {'class': 'article-secondaire'})
    articles = col.find_all('article', {'class': 'article-small article-medium'})

    big = soup.find('article', {'class': 'article-large'})

    titre = big.find('h2', {'class': 'titre'})
    title = titre.find('a').text.strip()
    href = titre.find('a').get('href')

    result['titles'].append(title)
    result['hrefs'].append(href)

    p = big.find('p', {'class': 'chapo'})
    result['teasers'].append(p.text.strip())

    image = big.find('picture')
    if image is not None:
        result['images'].append('https://www.lesechos.fr'+image.find('source').get('srcset'))
    else:
        result['images'].append('void')

    for article in articles:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

        titre = article.find('div', {'class': 'titre'})
        title = titre.find('a').text.strip()
        href = titre.find('a').get('href')

        result['titles'].append(title)
        result['hrefs'].append(href)

        p = article.find('p', {'class': 'chapo'})
        result['teasers'].append(p.text.strip())

        image = article.find('picture')
        if image is not None:
            result['images'].append('https://www.lesechos.fr'+image.find('source').get('srcset'))
        else:
            result['images'].append('void')

    return result



















