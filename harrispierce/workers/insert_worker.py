import psycopg2

from harrispierce.scrapping.scrap_urls import journals
from harrispierce.scrapping.scrap import scrap
from harrispierce.articles_db_insertion.insert_function import insert_article

from harrispierceDjango.settings.local import DATABASES

hostname = ''
username = DATABASES['default']['USER']  # 'postgres'
password = ''
database = DATABASES['default']['NAME']  # 'postgres'

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

for journal, urls in journals.items():
    for section, url in urls.items():
        print('INSERTING FOR: ', journal, section, url)
        insert_article(scrap(journal, section, url))

#myConnection.close()
