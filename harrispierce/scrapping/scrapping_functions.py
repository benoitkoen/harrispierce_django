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


def scrapwsj3(url):

    soup = get_raw_data(url)
    result = {'titles': [], 'hrefs': [], 'teasers': [], 'images': []}

    top_section = soup.find('div', {'class': 'buckets-bottom noImage-border-wrapper'})

    articles = top_section.find_all('article', {'class': 'hed-summ'})
    big = top_section.find_all('article', {'class': 'lead-headline hed-summ'})

    articles.append(list(big)[0])

    articles = articles[0:5]

    for article in articles:

        if article.find('div', {'class': 'text-wrapper'}) is None:
            continue

        else:

            a = article.find('a', {'class': 'subPrev headline'})

            if a is None:
                a = article.find('a', {'class': 'headline'})

            #print(article, a)

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


def scrapwsj4(url):

    soup = get_raw_data(url)
    result = {'titles': [], 'hrefs': [], 'teasers': [], 'images': []}

    top_section = soup.find('div', {'class': 'cb-row'})

    articles = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-3 locked'})
    big = top_section.find_all('h3', {'class': 'wsj-headline dj-sg wsj-card-feature heading-1 locked'})

    #articles.append(list(big)[0])

    for article in articles:

        a = article.find('a', {'class': 'wsj-headline-link'})
        result['titles'].append(a.text)
        result['hrefs'].append(a.get('href'))

        #print(article)

        image_div = article.find_next_sibling('div', {'class': 'right wsj-card-feature wsj-card-media Image'})

        #image = image_div.find('meta')
        if image_div is not None:
            image = image_div.find('img', {'class': 'wsj-img-content'})

            div = article.find_next_sibling().find_next_sibling('div', {'class': 'wsj-card-body clearfix'}) # SIBLINGS oF H3 pour image et teaser
            teaser = div.find('p', {'class': 'wsj-summary dj-sg wsj-card-feature'}).find('span').text
            result['teasers'].append(teaser)

            #result['images'].append(image.get('content'))
            result['images'].append(image.get('src'))
        else:
            div = article.find_next_sibling('p', {'class': 'wsj-summary dj-sg wsj-card-feature'}) # SIBLINGS oF H3 pour image et teaser

            if div is None:
                div = article.find_next_sibling().find('p', {'class': 'wsj-summary dj-sg wsj-card-feature'})

            teaser = div.find('span').text
            result['teasers'].append(teaser)

            #print(article.parent.findChildren())
                  #find('div', {'class': 'right wsj-card-feature wsj-card-media Image'}))
            #image =
            result['images'].append('void')

            #image = image_div.find('img', {'class': 'wsj-img-content'})
            #result['images'].append(image.get('src'))


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


def scrapnyt2(url):

    soup = get_raw_data(url)
    result = {'titles': [], 'hrefs': [], 'teasers': [], 'images': []}

    col = soup.find('div', {'class': 'columnGroup last'})
    articles = col.find_all('div', {'class': 'story'})

    for article in articles:

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


def scraple(url):
    soup = get_raw_data(url)
    result = {'titles': [], 'hrefs': [], 'teasers': [], 'images': []}

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


def scraparticle(url):

    soup = get_raw_data(url)
    #result = {'article': []}

    article = ''

    cont = soup.find('div')#, {'class': 'article__main o-grid-row'})
    print(soup.find('div'))
    p = cont.find_all('p')
    for pa in p:
        article += p.text

    return article


















