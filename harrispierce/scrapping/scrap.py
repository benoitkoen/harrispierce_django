from harrispierce.scrapping.scrapping_functions import scrapwsj1, scrapwsj2, scrapwsj3, scrapwsj4, scrapft, scrapnyt1, scrapnyt2, scraple

import pandas as pd
pd.set_option('display.width', 320)


def scrap(scrapper, journal, section, url):

    res = None

    if (journal == 'Wall Street Journal') & (section in ['World', 'Companies', 'Opinion']):
        res = exception_handler(scrapwsj1(scrapper, journal, section, url))

    elif (journal == 'Wall Street Journal') & (section in ['Tech']):
        res = exception_handler(scrapwsj2(scrapper, journal, section, url))

    elif (journal == 'Wall Street Journal') & (section in ['Economy']):
        res = exception_handler(scrapwsj3(scrapper, journal, section, url))

    elif (journal == 'Wall Street Journal') & (section in ['Politics']):
        res = exception_handler(scrapwsj4(scrapper, journal, section, url))

    elif journal == 'Financial Times':
        res = exception_handler(scrapft(scrapper, journal, section, url))

    elif (journal == 'New York Times') & (section in ['Tech', 'World', 'Politics']):
        res = exception_handler(scrapnyt1(scrapper, journal, section, url))

    elif (journal == 'New York Times') & (section in ['Dealbook', 'Economy', 'Energy']):
        res = exception_handler(scrapnyt2(scrapper, journal, section, url))

    elif journal == 'Les Echos':
        res = exception_handler(scraple(scrapper, journal, section, url))

    return res


def exception_handler(res_dict):

    res_df = None

    try:
        res_df = pd.DataFrame(res_dict)
    except ValueError:
        print('could not build the dataframe')

    return res_df

"""
t = scrap(scrapper, 'Financial Times', 'World', 'https://www.ft.com/world')
print('vfavfvf\n', t)
"""