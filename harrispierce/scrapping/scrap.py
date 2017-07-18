from scrapping_functions import scrapwsj1, scrapwsj2, scrapft, scrapnyt1

import pandas as pd
pd.set_option('display.width', 320)


def scrap(journal, section, url):

    if (journal == 'Wall Street Journal') & (section in ['World', 'Business', 'Opinion', 'Economy']):
        res = pd.DataFrame(scrapwsj1(url))

    elif (journal == 'Wall Street Journal') & (section in ['Politics', 'Technology']):
        res = pd.DataFrame(scrapwsj2(url))

    elif journal == 'Financial Times':
        res = pd.DataFrame(scrapft(url))

    elif (journal == 'New York Times') & (section in ['Technology', 'World']):
        res = pd.DataFrame(scrapnyt1(url))

    return res


print('yo')
t = scrap('Financial Times', 'World', 'https://www.ft.com/world')

#t = scrap('Wall Street Journal', 'Politics', 'https://www.wsj.com/news/politics')
t = scrap('New York Times', 'Technology', 'https://www.nytimes.com/section/technology')


print(t)
print(t.iloc[2]['hrefs'])

