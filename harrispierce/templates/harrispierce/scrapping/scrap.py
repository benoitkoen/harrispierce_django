from scrapping_functions import scrapwsj1

import pandas as pd
pd.set_option('display.width', 320)


def scrap(journal, section, url):

    if (journal == 'Wall Street Journal') & (section in ['World', 'Business', 'Opinion', 'Economy']):
        #for i in scrapwsj1(url).keys():
        #    print(i, len(i))
        #print(scrapwsj1(url))
        res = pd.DataFrame(scrapwsj1(url))

        return res


print('yo')
#print(scrap('Wall Street Journal', 'World', 'https://www.wsj.com/news/world'))
print(scrap('Wall Street Journal', 'Economy', 'https://www.wsj.com/news/economy'))

