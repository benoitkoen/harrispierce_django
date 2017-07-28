import urllib2
from bs4 import BeautifulSoup
from scrap import scrap
from journal_instances import journal_list

url = 'https://www.ft.com/content/87d644fc-73a4-11e7-aca6-c6bd07df1a3c'
#url = "http://www.reuters.com/article/2014/03/06/us-syria-crisis-assad-insight-idUSBREA250SD20140306"

soup = BeautifulSoup(urllib2.urlopen(url), 'lxml')

with open('ctp_output.txt', 'w') as f:
    for tag in soup.find_all('p'):
        f.write(tag.text.encode('utf-8') + '\n')



"""
def get_raw_data(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    return soup

print(get_raw_data(t.iloc[1]['hrefs']))


for i in journal_list:

    for section, url in (i.urls).items():
        print(i.name, section, url)

        print(scrap(i.name, section, url))
"""


        


