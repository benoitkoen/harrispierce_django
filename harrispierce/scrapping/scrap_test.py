import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import html


payload = {
    "email": "benoit.koenig@hec.edu",
    "password": "attention"#,
    #"csrfmiddlewaretoken": "<CSRF_TOKEN>"
}

session_requests = requests.session()

login_url = 'https://accounts.ft.com/login?location=https%3A%2F%2Fwww.ft.com%2Fcontent%2F6f2f8b0e-73d9-11e7-aca6-c6bd07df1a3c'

result = session_requests.get(login_url)

tree = html.fromstring(result.text)
#authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

result = session_requests.post(
    login_url,
    data=payload,
    headers=dict(referer=login_url)
)


url = 'https://www.ft.com/content/87d644fc-73a4-11e7-aca6-c6bd07df1a3c'
#url = "http://www.reuters.com/article/2014/03/06/us-syria-crisis-assad-insight-idUSBREA250SD20140306"

result = session_requests.get(
    url,
    headers=dict(referer=url)
)

tree = html.fromstring(result.content)
bucket_names = tree.xpath("//div[@class='article__body n-content-body']/p/text()")

print(bucket_names)

"""
soup = BeautifulSoup(urllib2.urlopen(url), 'lxml')

with open('ctp_output.txt', 'w') as f:
    for tag in soup.find_all('p'):
        f.write(tag.text.encode('utf-8') + '\n')


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


        


