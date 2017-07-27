from scrapping_functions import scrapwsj1, scrapwsj2, scrapwsj3, scrapwsj4, scrapft, scrapnyt1, scrapnyt2, scraple, scraparticle

import pandas as pd
pd.set_option('display.width', 320)


def scrap(journal, section, url):

    res = None

    if (journal == 'Wall Street Journal') & (section in ['World', 'Companies', 'Opinion']):
        res = pd.DataFrame(scrapwsj1(url))

    elif (journal == 'Wall Street Journal') & (section in ['Tech']):
        res = pd.DataFrame(scrapwsj2(url))

    elif (journal == 'Wall Street Journal') & (section in ['Economy']):
        res = pd.DataFrame(scrapwsj3(url))

    elif (journal == 'Wall Street Journal') & (section in ['Politics']):
        res = pd.DataFrame(scrapwsj4(url))

    elif journal == 'Financial Times':
        res = pd.DataFrame(scrapft(url))

    elif (journal == 'New York Times') & (section in ['Tech', 'World', 'Economy', 'Energy', 'Politics']):
        res = pd.DataFrame(scrapnyt1(url))

    elif (journal == 'New York Times') & (section in ['Dealbook']):
        res = pd.DataFrame(scrapnyt2(url))

    elif journal == 'Les Echos':
        res = pd.DataFrame(scraple(url))

    return res


#print('yo')
t = scrap('Financial Times', 'World', 'https://www.ft.com/world')

#t = scrap('New York Times', 'Dealbook', 'http://www.nytimes.com/pages/business/dealbook/index.html?src=busfn')
#t = scrap('Wall Street Journal', 'Tech', 'https://www.wsj.com/news/technology')
#t = scrap('Wall Street Journal', 'Economy', 'https://www.wsj.com/news/economy')
#t = scrap('Wall Street Journal', 'Tech', 'https://www.wsj.com/news/technology')


#print(t)
print(t.iloc[1]['hrefs'])


print(scraparticle(t.iloc[1]['hrefs']))

