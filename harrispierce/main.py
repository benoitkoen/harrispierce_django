import psycopg2

from harrispierceDjango.settings.local import DATABASES

from harrispierce.inserting.insert_function import insert_article
from harrispierce.inserting.check_data import retrieve_data
from harrispierce.scrapping.scrap_urls import journals
from harrispierce.scrapping.scrap import scrap
from harrispierce.scrapping.scrap_articles import FTScrapingMachine
from harrispierce.util.config import ScrappingConfig

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

    ScrappingConfig.scrap_article_boolean = True

    for journal, urls in sorted(journals.items()):
        for section, url in urls.items():
            print('inserting for: ', '\n', journal, '\n', section, '\n', url, '\n', all_scrappers[journal])
            insert_article(myConnection, scrap(scrapper=all_scrappers[journal], journal=journal, section=section, url=url))
    """
    """
    """
    #retrieve_data(myConnection, 'journal')
    #retrieve_data(myConnection, 'section')
    retrieve_data(myConnection, 'article')
    """

    """
    for journal, urls in sorted(journals.items()):
        for section, url in urls.items():
            print('inserting for: ', '\n', journal, '\n', section, '\n', url, '\n', all_scrappers[journal])
            df = scrap(scrapper=all_scrappers[journal], journal=journal, section=section, url=url)
            print(df, '\n the len: ', len(df))
    """
    """
    scrapper = all_scrappers['Financial Times']
    t = scrap(scrapper, 'Financial Times', 'Companies', 'http://ft.com/companies')
    print('vfavfvf\n', t)
    """