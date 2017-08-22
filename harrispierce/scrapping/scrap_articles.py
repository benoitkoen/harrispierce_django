import requests
from lxml import html


class FTScrapingMachine:

    def __init__(self,
                 email="benoit.koenig@hec.edu",
                 password="attention",
                 login_url='https://accounts.ft.com/login?location=https%3A%2F%2Fwww.ft.com%2Fcontent%2F6f2f8b0e-73d9-11e7-aca6-c6bd07df1a3c',
                 ):         #https://accounts.ft.com/login?location=https%3A%2F%2Fwww.ft.com%2Fcontent%2Fd5119962-868f-11e7-8bb1-5ba57d47eff7

        self.payload = {
            "email": email,
            "password": password
        }
        self.login_url = login_url
        self.logged_in = False
        self.session_requests = None

    def scrap_ft_article(self, article_url):

        print('loggedin already? ', self.logged_in, '\n', article_url)
        # if not logged in yet
        if self.logged_in is False:
            self.session_requests = requests.session()

            result = self.session_requests.get(self.login_url)
            tree = html.fromstring(result.text)
            result = self.session_requests.post(
                self.login_url,
                data=self.payload,
                headers=dict(referer=self.login_url)
            )
            print('login successful: ', "My Account" in result.text)
            print('login failed: ', "Sign in" in result.text)

            self.logged_in = True

        # Scrapping
        result = self.session_requests.get(
            article_url,
            headers=dict(referer=article_url)
        )

        tree = html.fromstring(result.content)

        paragraphes = tree.xpath("//div[@class='article__body n-content-body']/p/text()")

        article = ''

        for p in paragraphes:
            article += p

        if len(article) == 0:
            return 'void'
        return article
