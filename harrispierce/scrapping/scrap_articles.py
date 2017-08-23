import requests
from lxml import html


def scrap_ft_article(login_url, article_url):
    payload = {
        "email": "benoit.koenig@hec.edu",
        "password": "attention"
    }

    session_requests = requests.session()

    result = session_requests.get(login_url)

    tree = html.fromstring(result.text)

    result = session_requests.post(
        login_url,
        data=payload,
        headers=dict(referer=login_url)
    )

    result = session_requests.get(
        article_url,
        headers=dict(referer=article_url)
    )

    tree = html.fromstring(result.content)

    paragraphes = tree.xpath("//div[@class='article__body n-content-body']/p/text()")

    article = ''

    for p in paragraphes:
        article += p

    return article


#art = scrap_ft_article(
#    'https://accounts.ft.com/login?location=https%3A%2F%2Fwww.ft.com%2Fcontent%2F6f2f8b0e-73d9-11e7-aca6-c6bd07df1a3c',
#    'https://www.ft.com/content/87d644fc-73a4-11e7-aca6-c6bd07df1a3c')

art = scrap_ft_article('https://accounts.ft.com/login?location=https%3A%2F%2Fwww.ft.com%2Fcontent%2F6f2f8b0e-73d9-11e7-aca6-c6bd07df1a3c',
                       'https://www.ft.com/content/a48c4aec-859c-11e7-8bb1-5ba57d47eff7')

print(art)

