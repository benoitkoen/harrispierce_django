from harrispierce.scrapping.scrapping_functions import scrapwsj1, scrapwsj2, scrapwsj3, scrapwsj4, scrapft, scrapnyt1, scrapnyt2, scraple

import pandas as pd
pd.set_option('display.width', 320)


def scrap(scrapper, journal, section, url):

    res = None

    if (journal == 'Wall Street Journal') & (section in ['World', 'Companies', 'Opinion']):
        res = pd.DataFrame(scrapwsj1(scrapper, journal, section, url))

    elif (journal == 'Wall Street Journal') & (section in ['Tech']):
        res = pd.DataFrame(scrapwsj2(scrapper, journal, section, url))

    elif (journal == 'Wall Street Journal') & (section in ['Economy']):
        res = pd.DataFrame(scrapwsj3(scrapper, journal, section, url))

    elif (journal == 'Wall Street Journal') & (section in ['Politics']):
        res = pd.DataFrame(scrapwsj4(scrapper, journal, section, url))

    elif journal == 'Financial Times':
        res = pd.DataFrame(scrapft(scrapper, journal, section, url))

    elif (journal == 'New York Times') & (section in ['Tech', 'World', 'Politics']):
        res = pd.DataFrame(scrapnyt1(scrapper, journal, section, url))

    elif (journal == 'New York Times') & (section in ['Dealbook', 'Economy', 'Energy']):
        res = pd.DataFrame(scrapnyt2(scrapper, journal, section, url))

    elif journal == 'Les Echos':
        res = pd.DataFrame(scraple(scrapper, journal, section, url))

    return res

"""
t = scrap(scrapper, 'Financial Times', 'World', 'https://www.ft.com/world')
print('vfavfvf\n', t)
"""