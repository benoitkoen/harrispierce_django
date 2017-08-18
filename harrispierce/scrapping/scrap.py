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
