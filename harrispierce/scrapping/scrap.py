from harrispierce.scrapping.scrapping_functions import scrapwsj1, scrapwsj2, scrapwsj3, scrapwsj4, scrapft, scrapnyt1, scrapnyt2, scraple

import pandas as pd
pd.set_option('display.width', 320)


def scrap(journal, section, url):

    res = None

    if (journal == 'Wall Street Journal') & (section in ['World', 'Companies', 'Opinion']):
        res = pd.DataFrame(scrapwsj1(journal, section, url))

    elif (journal == 'Wall Street Journal') & (section in ['Tech']):
        res = pd.DataFrame(scrapwsj2(journal, section, url))

    elif (journal == 'Wall Street Journal') & (section in ['Economy']):
        res = pd.DataFrame(scrapwsj3(journal, section, url))

    elif (journal == 'Wall Street Journal') & (section in ['Politics']):
        res = pd.DataFrame(scrapwsj4(journal, section, url))

    elif journal == 'Financial Times':
        res = pd.DataFrame(scrapft(journal, section, url))

    elif (journal == 'New York Times') & (section in ['Tech', 'World', 'Politics']):
        res = pd.DataFrame(scrapnyt1(journal, section, url))

    elif (journal == 'New York Times') & (section in ['Dealbook', 'Economy', 'Energy']):
        res = pd.DataFrame(scrapnyt2(journal, section, url))

    elif journal == 'Les Echos':
        res = pd.DataFrame(scraple(journal, section, url))

    return res



#t = scrap('Financial Times', 'World', 'https://www.ft.com/world')
#t = scrap('New York Times', 'Tech', 'https://www.nytimes.com/section/technology')
#t = scrap('New York Times', 'Economy', 'http://www.nytimes.com/pages/business/economy/index.html?src=busfn')
#t = scrap('New York Times', 'Dealbook', 'http://www.nytimes.com/pages/business/dealbook/index.html?src=busfn')
t = scrap('Wall Street Journal', 'Tech', 'https://www.wsj.com/news/technology')

#t = scrap('Les Echos', 'World', 'http://www.lesechos.fr/monde/index.php')
print('vfavfvf\n', t)
print(t['image'].iloc[2])



