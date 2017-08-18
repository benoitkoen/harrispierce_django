import unittest
import pytest
import pandas as pd
from pandas.util.testing import assert_frame_equal
from datetime import datetime
from django.db import connection


from harrispierce.inserting.insert_function import insert_article


class TestInsertFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = connection
        cls.image1 = 'https://si.wsj.net/public/resources/images/BN-UQ698_alibab_Z120_20170811132345.jpg'
        cls.image2 = 'https://www.lesechos.fr/medias/2017/08/16/2108060_kpmg-et-pwc-condamnes-a-de-lourdes-amendes-web-010182356164_290x152.jpg'
        cls.image3 = 'https://www.lesechos.fr/industrie-services/immobilier-btp/030497622430-le-gouvernement-veut-assouplir-lobligation-du-quota-de-25-dhlm-2108308.php'
        cls.image4 = 'https://www.lesechos.fr/medias/2017/08/09/2107077_palm-islands-un-symbole-qui-a-pris-leau-web-030462356035_290x152.jpg'
        cls.ref_date = datetime.utcnow()

    @pytest.mark.django_db(transaction=True)
    def test_insert_article(self):

        df_to_insert = pd.DataFrame(
            columns=
                ['article', 'cleaned_article', 'href', 'image', 'journal', 'section', 'teaser', 'title', 'pub_date'],
            data=[
                ['voidart', 'voidcle', 'href1', self.image1, 'Wall Street Journal', 'World', 'teaser1', 'title1', self.ref_date],
                ['voidart', 'voidcle', 'href2', self.image2, 'New York Times', 'World', 'teaser2', 'title2', self.ref_date],
                ['voidart', 'voidcle', 'href3', self.image3, 'Financial Times', 'Companies', 'teaser3', 'title3', self.ref_date],
                ['voidart', 'voidcle', 'href4', self.image4, 'Les Echos', 'World', 'teaser4', 'title4', self.ref_date]
            ]
        )

        cur = self.connection.cursor()

        cur.execute('TRUNCATE harrispierce_article;')
        cur.execute('TRUNCATE harrispierce_journal CASCADE;')
        cur.execute('TRUNCATE harrispierce_section CASCADE;')

        cur.execute("INSERT INTO harrispierce_journal(name, country) VALUES"
                    "('Wall Street Journal', 'US'),"
                    "('New York Times', 'US'),"
                    "('Financial Times', 'US'),"
                    "('Les Echos', 'France')")

        cur.execute("INSERT INTO harrispierce_section(name) VALUES"
                    "('World'), ('Companies')"
                    )

        insert_article(self.connection, df_to_insert)

        cur.execute('SELECT * FROM harrispierce_article;')
        articles_extracted = cur.fetchall()

        data = [elem[1:] for elem in articles_extracted]

        print('data\n', data)

        columns = ['title', 'teaser', 'href', 'image', 'article', 'cleaned_article', 'pub_date', 'journal', 'section']

        articles_extracted = pd.DataFrame(
            data=data,
            columns=columns
        )
        articles_extracted = articles_extracted[['article', 'cleaned_article', 'href', 'image', 'journal',
                                                 'section', 'teaser', 'title']]#, 'pub_date']]

        articles_expected = pd.DataFrame(
            columns=
                ['article', 'cleaned_article', 'href', 'image', 'journal', 'section', 'teaser', 'title'],# 'pub_date'],
            data=[
                ['voidart', 'voidcle', 'href1', self.image1, 1, 1, 'teaser1', 'title1'], #self.ref_date],
                ['voidart', 'voidcle', 'href2', self.image2, 2, 1, 'teaser2', 'title2'], #self.ref_date],
                ['voidart', 'voidcle', 'href3', self.image3, 3, 2, 'teaser3', 'title3'], #self.ref_date],
                ['voidart', 'voidcle', 'href4', self.image4, 4, 1, 'teaser4', 'title4'], #self.ref_date]
            ]
        )

        print('articles_extracted\n', articles_extracted, '\n', articles_expected)

        assert_frame_equal(articles_extracted, articles_expected)

    @pytest.mark.django_db(transaction=True)
    def test_insert_duplicate_article(self):
        df_to_insert = pd.DataFrame(
            columns=
            ['article', 'cleaned_article', 'href', 'image', 'journal', 'section', 'teaser', 'title', 'pub_date'],
            data=[
                ['voidart', 'voidcle', 'href1', self.image1, 'Wall Street Journal', 'World', 'teaser1', 'title1',
                 self.ref_date],
                ['voidart', 'voidcle', 'href2', self.image2, 'New York Times', 'World', 'teaser2', 'title2',
                 self.ref_date],
                ['voidart', 'voidcle', 'href3', self.image3, 'Financial Times', 'Companies', 'teaser3', 'title3',
                 self.ref_date],
                ['voidart', 'voidcle', 'href4', self.image4, 'Les Echos', 'World', 'teaser4', 'title4',
                 self.ref_date]
            ]
        )

        cur = self.connection.cursor()

        cur.execute('TRUNCATE harrispierce_article;')
        cur.execute('TRUNCATE harrispierce_journal CASCADE;')
        cur.execute('TRUNCATE harrispierce_section CASCADE;')

        cur.execute("INSERT INTO harrispierce_journal(name, country) VALUES"
                    "('Wall Street Journal', 'US'),"
                    "('New York Times', 'US'),"
                    "('Financial Times', 'US'),"
                    "('Les Echos', 'France')")

        cur.execute("INSERT INTO harrispierce_section(name) VALUES"
                    "('World'), ('Companies')"
                    )

        # insert first articles
        insert_article(self.connection, df_to_insert)

        df_of_duplicates_to_insert = pd.DataFrame(
            columns=
            ['article', 'cleaned_article', 'href', 'image', 'journal', 'section', 'teaser', 'title', 'pub_date'],
            data=[
                ['voidart', 'voidcle', 'href1', self.image1, 'Wall Street Journal', 'World', 'teaser1', 'title1',
                 self.ref_date],
                ['voidart', 'voidcle', 'href2', self.image2, 'New York Times', 'World', 'teaser2', 'title2',
                 self.ref_date],
                ['voidart', 'voidcle', 'href3', self.image3, 'Financial Times', 'Companies', 'teaser3', 'title3',
                 self.ref_date],
                ['voidart', 'voidcle', 'href4', self.image4, 'Les Echos', 'World', 'teaser4', 'title4',
                 self.ref_date]
            ]
        )

        # insert duplicates
        insert_article(self.connection, df_of_duplicates_to_insert)

        cur.execute('SELECT * FROM harrispierce_article;')
        articles_extracted = cur.fetchall()

        data = [elem[1:] for elem in articles_extracted]

        columns = ['title', 'teaser', 'href', 'image', 'article', 'cleaned_article', 'pub_date', 'journal', 'section']

        articles_extracted = pd.DataFrame(
            data=data,
            columns=columns
        )
        articles_extracted = articles_extracted[['article', 'cleaned_article', 'href', 'image', 'journal',
                                                 'section', 'teaser', 'title']]  # , 'pub_date']]

        articles_expected = pd.DataFrame(
            columns=
            ['article', 'cleaned_article', 'href', 'image', 'journal', 'section', 'teaser', 'title'],  # 'pub_date'],
            data=[
                ['voidart', 'voidcle', 'href1', self.image1, 1, 1, 'teaser1', 'title1'],  # self.ref_date],
                ['voidart', 'voidcle', 'href2', self.image2, 2, 1, 'teaser2', 'title2'],  # self.ref_date],
                ['voidart', 'voidcle', 'href3', self.image3, 3, 2, 'teaser3', 'title3'],  # self.ref_date],
                ['voidart', 'voidcle', 'href4', self.image4, 4, 1, 'teaser4', 'title4'],  # self.ref_date]
            ]
        )

        assert_frame_equal(articles_extracted, articles_expected)


"""
from harrispierceDjango.settings.local import DATABASES
import psycopg2
class TestInsertFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hostname = ''
        cls.username = DATABASES['default']['USER']  # 'postgres'
        cls.password = ''
        cls.database = DATABASES['default']['NAME']  # 'postgres'

        cls.myConnection = psycopg2.connect(host=cls.hostname,
                                            user=cls.username,
                                            password=cls.password,
                                            dbname=cls.database)
        cls.image = 'https://si.wsj.net/public/resources/images/BN-UQ698_alibab_Z120_20170811132345.jpg'

    def test_insert_article(self):

        df_to_insert = pd.DataFrame(
            columns=
                ['article', 'cleaned_article', 'href', 'image', 'journal', 'section', 'teaser', 'title'],
            data=[
                ['voidart', 'voidcle', 'href1', self.image, 'Wall Street Journal', 'World', 'teaser1', 'title1'],
                ['voidart', 'voidcle', 'href2', self.image, 'New York Times', 'World', 'teaser2', 'title2'],
                ['voidart', 'voidcle', 'href3', self.image, 'Financial Times', 'Companies', 'teaser3', 'title3'],
                ['voidart', 'voidcle', 'href4', self.image, 'Les Echos', 'World', 'teaser4', 'title4']
            ]
        )

        self.myConnection.autocommit = True
        cur = self.myConnection.cursor()

        cur.execute('TRUNCATE harrispierce_article;')
        cur.execute('TRUNCATE harrispierce_journal CASCADE;')
        cur.execute('TRUNCATE harrispierce_section CASCADE;')
        #cur.execute("DBCC CHECKIDENT('harrispierce_section', RESEED, 1);")

        cur.execute("INSERT INTO harrispierce_journal(name, country) VALUES"
                    "('Wall Street Journal', 'US'),"
                    "('New York Times', 'US'),"
                    "('Financial Times', 'US'),"
                    "('Les Echos', 'France')")
        

        insert_article(self.myConnection, df_to_insert)

        cur.execute('TRUNCATE harrispierce_article;')
        insert_article(self.myConnection, df_to_insert)

        cur.execute('TRUNCATE harrispierce_journal CASCADE;')
        cur.execute("INSERT INTO harrispierce_journal(name, country) VALUES"
                    "('Wall Street Journal', 'US'),"
                    "('New York Times', 'US'),"
                    "('Financial Times', 'US'),"
                    "('Les Echos', 'France')")

        cur.execute('SELECT * FROM harrispierce_article;')
        articles_extracted = cur.fetchall()
        print(len(articles_extracted[0]), articles_extracted[0])
        data = [elem[1:] for elem in articles_extracted]
        print(data)
        columns = ['title', 'teaser', 'href', 'image', 'article', 'cleaned_article', 'pub_date', 'journal', 'section']

        articles_extracted = pd.DataFrame(
            data=data,
            columns=columns
        )

        print(articles_extracted)
        
        assert_frame_equal(df_to_insert, articles_extracted)
"""
