import psycopg2

from harrispierceDjango.settings.local import DATABASES

from harrispierce.inserting.insert_function import insert_article
from harrispierce.inserting.check_data import retrieve_data
from harrispierce.scrapping.scrap_urls import journals
from harrispierce.scrapping.scrap import scrap
from harrispierce.scrapping.scrap_articles import FTScrapingMachine

hostname = ''
username = DATABASES['default']['USER']  # 'postgres'
password = ''
database = DATABASES['default']['NAME']  # 'postgres'

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

if __name__ == '__main__':

    all_scrappers = {}
    all_scrappers['Wall Street Journal'] = None
    all_scrappers['New York Times'] = None
    all_scrappers['Financial Times'] = FTScrapingMachine()
    all_scrappers['Les Echos'] = None

    """
    for journal, urls in journals.items():
        for section, url in urls.items():
            print('inserting for: ', '\n', journal, '\n', section, '\n', url)
            
            insert_article(myConnection, scrap(scrapper=all_scrappers[journal],
                                               journal=journal,
                                               section=section,
                                               url=url))
    """
    """
    #retrieve_data(myConnection, 'journal')
    #retrieve_data(myConnection, 'section')
    retrieve_data(myConnection, 'article')
    """
    """
    # t = scrap('Financial Times', 'World', 'https://www.ft.com/world')
    # t = scrap('New York Times', 'Tech', 'https://www.nytimes.com/section/technology')
    # t = scrap('New York Times', 'Economy', 'http://www.nytimes.com/pages/business/economy/index.html?src=busfn')
    # t = scrap('New York Times', 'Dealbook', 'http://www.nytimes.com/pages/business/dealbook/index.html?src=busfn')
    # t = scrap('Wall Street Journal', 'Tech', 'https://www.wsj.com/news/technology')

    # t = scrap('Les Echos', 'World', 'http://www.lesechos.fr/monde/index.php')
    # print('vfavfvf\n', t)
    # print(t['image'].iloc[2])
    """

    """
    l = [
    'https://www.ft.com/content/440dee7e-8654-11e7-bf50-e1c239b45787',
    'https://www.ft.com/content/b878361a-8673-11e7-8bb1-5ba57d47eff7',
    'https://www.ft.com/content/febf249e-866e-11e7-bf50-e1c239b45787',
    'https://www.ft.com/video/db0c4143-ba2e-4910-856a-0fd4e08a5093',
    'https://www.ft.com/content/979346ea-866b-11e7-bf50-e1c239b45787',
    'https://www.ft.com/content/a3b01274-865b-11e7-bf50-e1c239b45787',
    'https://www.ft.com/content/ec8757be-8633-11e7-bf50-e1c239b45787'
    ]
    """
    from time import sleep
    scrapper = FTScrapingMachine()
    t = scrap(scrapper, 'Financial Times', 'World', 'https://www.ft.com/world')
    print('vfavfvf\n', t)

    """
    #for arti in l:
    #    art = scrapper.scrap_ft_article(arti)
    #    if art is not None:
    #        print(art[:50])
    #    else:
    #        print(art)
    #    sleep(10)
    """