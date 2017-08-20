import psycopg2

from harrispierceDjango.settings.local import DATABASES

from harrispierce.inserting.insert_function import insert_article
from harrispierce.inserting.check_data import retrieve_data
from harrispierce.scrapping.scrap_urls import journals
from harrispierce.scrapping.scrap import scrap

hostname = ''
username = DATABASES['default']['USER']  # 'postgres'
password = ''
database = DATABASES['default']['NAME']  # 'postgres'

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

if __name__ == '__main__':

    for journal, urls in journals.items():
        for section, url in urls.items():
            print('inserting for: ', '\n', journal, '\n', section, '\n', url)
            
            insert_article(myConnection, scrap(journal, section, url))

    """
    #retrieve_data(myConnection, 'journal')
    #retrieve_data(myConnection, 'section')
    retrieve_data(myConnection, 'article')
    """
    # t = scrap('Financial Times', 'World', 'https://www.ft.com/world')
    # t = scrap('New York Times', 'Tech', 'https://www.nytimes.com/section/technology')
    # t = scrap('New York Times', 'Economy', 'http://www.nytimes.com/pages/business/economy/index.html?src=busfn')
    # t = scrap('New York Times', 'Dealbook', 'http://www.nytimes.com/pages/business/dealbook/index.html?src=busfn')
    # t = scrap('Wall Street Journal', 'Tech', 'https://www.wsj.com/news/technology')
    """
    t = scrap('Wall Street Journal', 'World', 'https://www.wsj.com/news/world')
    print('vfavfvf\n', t)
    # print(t['image'].iloc[2])
    """