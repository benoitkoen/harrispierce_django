from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
import ssl

from harrispierce.util.config import ScrappingConfig

context = ssl._create_unverified_context()
result_dict = {'journal': [], 'section': [], 'title': [], 'href': [],
               'teaser': [], 'image': [], 'article': [], 'cleaned_article': []}


def get_raw_data(url):
    page = urlopen(url, context=context)
    soup = BeautifulSoup(page, 'lxml')
    return soup


def clean_result(dict):
    for key, val in dict.items():
        for index, item in enumerate(val):
            if item is None:
                val[index] = 'void'


def scrapwsj1(scrapper, journal, section, url):

    soup = get_raw_data(url)
    result = result_dict

    top_section = soup.find('div', {'class': 'buckets-bottom noImage-border-wrapper'})

    articles = top_section.find_all('article', {'class': 'hed-summ'})

    big = top_section.find('article', {'class': 'hed-summ no-image lead-headline'})


    if big is not None:
        articles.append(list(big)[0])
        articles = articles[:-1]

    for article in articles[:ScrappingConfig.scrapping_limit]:

        if article.find('div', {'class': 'text-wrapper'}) is None:
            continue
        else:
            result['journal'].append(journal)
            result['section'].append(section)
            result['article'].append('void')
            result['cleaned_article'].append('void')

            a = article.find('a', {'class': 'subPrev headline'})

            result['title'].append(a.text)
            result['href'].append(a.get('href'))

            div = article.find('div', {'class': 'text-wrapper'})
            if div is not None:
                result['teaser'].append(div.find('p', {'class': 'summary'}).text)
            else:
                result['teaser'].append('no preview')

            image = article.find('img')
            if image is not None:
                result['image'].append(image.get('data-src'))
            else:
                result['image'].append('void')

    clean_result(result)

    return result


def scrapwsj2(scrapper, journal, section, url):

    soup = get_raw_data(url)
    result = result_dict

    top_section = soup.find('div', {'class': 'cb-row'})

    articles = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-3 locked'})
    big = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-1 locked'})

    try:
        articles.append(list(big)[0])
    except IndexError:
        pass

    for article in articles[:ScrappingConfig.scrapping_limit]:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

        a = article.find('a', {'class': 'wsj-headline-link'})
        result['title'].append(a.text)
        result['href'].append(a.get('href'))

        image_div = article.findNext('div', {'class': 'right wsj-card-feature wsj-card-media Image'})
        image = image_div.find('img', {'class': 'wsj-img-content'})
        if image is not None:
            result['image'].append(image.get('src'))
        else:
            image = image_div.find('meta')
            if image is not None:
                result['image'].append(image.get('content'))
            else:
                result['image'].append('void')

        div = image_div.findNext('div', {'class': 'wsj-card-body clearfix'}) # SIBLINGS oF H3 pour image et et teaser
        teaser = div.find('p', {'class': 'wsj-summary dj-sg wsj-card-feature'}).find('span').text
        if div is not None:
            result['teaser'].append(teaser)
        else:
            result['teaser'].append('no preview')

    clean_result(result)

    return result


def scrapwsj3(scrapper, journal, section, url):

    soup = get_raw_data(url)
    result = result_dict

    top_section = soup.find('div', {'class': 'buckets-bottom noImage-border-wrapper'})

    articles = top_section.find_all('article', {'class': 'hed-summ'})
    big = top_section.find_all('article', {'class': 'lead-headline hed-summ'})

    articles.append(list(big))

    articles = articles[0:5]

    for article in articles[:ScrappingConfig.scrapping_limit]:

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

            result['title'].append(a.text)
            result['href'].append(a.get('href'))

            div = article.find('div', {'class': 'text-wrapper'})
            if div is not None:
                result['teaser'].append(div.find('p', {'class': 'summary'}).text)
            else:
                result['teaser'].append('no preview')

            image = article.find('img')
            if image is not None:
                result['image'].append(image.get('data-src'))
            else:
                result['image'].append('void')

    clean_result(result)

    return result


def scrapwsj4(scrapper, journal, section, url):

    soup = get_raw_data(url)
    result = result_dict

    top_section = soup.find('div', {'class': 'cb-row'})

    articles = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-3 locked'})
    big = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-1 locked'})

    articles.append(list(big)[0])

    for article in articles[:ScrappingConfig.scrapping_limit]:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

        a = article.find('a', {'class': 'wsj-headline-link'})
        result['title'].append(a.text)
        result['href'].append(a.get('href'))

        image_div = article.find_next_sibling('div', {'class': 'right wsj-card-feature wsj-card-media Image'})

        if image_div is not None:
            image = image_div.find('img', {'class': 'wsj-img-content'})

            div = article.find_next_sibling().find_next_sibling('div', {'class': 'wsj-card-body clearfix'}) # SIBLINGS oF H3 pour image et teaser
            teaser = div.find('p', {'class': 'wsj-summary dj-sg wsj-card-feature'}).find('span').text
            result['teaser'].append(teaser)

            result['image'].append(image.get('src'))
        else:
            div = article.find_next_sibling('p', {'class': 'wsj-summary dj-sg wsj-card-feature'}) # SIBLINGS oF H3 pour image et teaser

            if div is None:
                div = article.find_next_sibling().find('p', {'class': 'wsj-summary dj-sg wsj-card-feature'})

            teaser = div.find('span').text
            result['teaser'].append(teaser)

            result['image'].append('void')

    clean_result(result)

    return result


def scrapft(scrapper, journal, section, url):

    soup = get_raw_data(url)
    result = result_dict

    articles = soup.find_all('li', {'class': 'o-teaser-collection__item o-grid-row'})

    for article in articles[:ScrappingConfig.scrapping_limit]:

        if (article.find('img') is None) | (article.find('p', {'class': 'o-teaser__standfirst'}) is None):
            continue

        else:

            result['journal'].append(journal)
            result['section'].append(section)

            result['cleaned_article'].append('void')

            a = article.find('a', {'class': 'js-teaser-heading-link'})

            title = a.text.strip()
            result['title'].append(title)

            href = 'https://www.ft.com'+a.get('href')
            result['href'].append(href)

            p = article.find('p', {'class': 'o-teaser__standfirst'})
            result['teaser'].append(p.text)

            image = article.find('img')
            if image is not None:
                result['image'].append(image.get('data-srcset').split(' ')[0])
            else:
                result['image'].append('void')

            if ScrappingConfig.scrap_article_boolean is True:
                # Article scrapping requiring login
                article = scrapper.scrap_ft_article(href)
                result['article'].append(article)
                print('scraped: ', article[:50])
                sleep(ScrappingConfig.sleep_time)
            else:
                result['article'].append('void')

    clean_result(result)

    return result


def scrapnyt1(scrapper, journal, section, url):

    soup = get_raw_data(url)
    result = result_dict

    down_section = soup.find('div', {'class': 'stream'}).find('ol')
    articles = down_section.find_all('li')

    for article in articles[:ScrappingConfig.scrapping_limit]:

        image = article.find('img')
        if image is not None:
            result['journal'].append(journal)
            result['section'].append(section)
            result['article'].append('void')
            result['cleaned_article'].append('void')

            result['image'].append(image.get('src'))
            
            a = article.find('a', {'class': 'story-link'})
            if a is not None:
                result['href'].append(a.get('href'))

                title = a.find('h2', {'class': 'headline'}).text.strip()
                result['title'].append(title)

                p = article.find('p', {'class': 'summary'})
                result['teaser'].append(p.text)

    clean_result(result)

    return result


def scrapnyt2(scrapper, journal, section, url):

    soup = get_raw_data(url)
    result = result_dict

    col = soup.find('div', {'class': 'columnGroup last'})
    articles = col.find_all('div', {'class': 'story'})

    for article in articles[:ScrappingConfig.scrapping_limit]:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

        h3 = article.find('h3')
        title = h3.find('a').text.strip()
        href = h3.find('a').get('href')

        result['title'].append(title)
        result['href'].append(href)

        p = article.find('p', {'class': 'summary'})
        result['teaser'].append(p.text.strip())

        image = article.find('img')
        if image is not None:
            result['image'].append(image.get('src'))
        else:
            result['image'].append('void')

    clean_result(result)

    return result


def scraple(scrapper, journal, section, url):
    soup = get_raw_data(url)
    result = result_dict

    col = soup.find('div', {'class': 'article-secondaire'})
    articles = col.find_all('article', {'class': 'article-small article-medium'})

    big = soup.find('article', {'class': 'article-large'})

    titre = big.find('h2', {'class': 'titre'})
    title = titre.find('a').text.strip()
    href = titre.find('a').get('href')

    result['title'].append(title)
    result['href'].append(href)

    result['journal'].append(journal)
    result['section'].append(section)
    result['article'].append('void')
    result['cleaned_article'].append('void')

    p = big.find('p', {'class': 'chapo'})
    result['teaser'].append(p.text.strip())

    image = big.find('picture')
    if image is not None:
        result['image'].append('https://www.lesechos.fr'+image.find('source').get('srcset'))
    else:
        result['image'].append('void')

    for article in articles[:ScrappingConfig.scrapping_limit]:

        result['journal'].append(journal)
        result['section'].append(section)
        result['article'].append('void')
        result['cleaned_article'].append('void')

        titre = article.find('div', {'class': 'titre'})
        title = titre.find('a').text.strip()
        href = titre.find('a').get('href')

        result['title'].append(title)
        result['href'].append(href)

        p = article.find('p', {'class': 'chapo'})
        result['teaser'].append(p.text.strip())

        image = article.find('picture')
        if image is not None:
            result['image'].append('https://www.lesechos.fr'+image.find('source').get('srcset'))
        else:
            result['image'].append('void')

    clean_result(result)

    return result
