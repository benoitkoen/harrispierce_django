import urllib2
from bs4 import BeautifulSoup
from scrap import scrap
from journal_instances import journal_list

for i in journal_list:

    for section, url in (i.urls).items():
        print(i.name, section, url)

        print(scrap(i.name, section, url))


        


