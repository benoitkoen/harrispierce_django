import pytest
import pandas as pd
from datetime import datetime, timedelta
from django.db import connection
from django.test.client import RequestFactory

from harrispierce.inserting.insert_function import insert_article

@pytest.mark.django_db
class TestDisplay:
    @classmethod
    def setUpClass(cls):
        cls.connection = connection
        cls.ref_date = datetime.utcnow()
        cls.factory = RequestFactory()

    def test_display_view(self, client):
        response = client.get('/display.html/')
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_get(self):
        df_to_insert = pd.DataFrame(
            columns=
            ['article', 'cleaned_article', 'href', 'image', 'journal', 'section', 'teaser', 'title', 'pub_date'],
            data=[
                ['voidart', 'voidcle', 'href1', self.image, 'Financial Times', 'Companies', 'teaser1', 'title1',
                 self.ref_date + timedelta(days=1)],
                ['voidart', 'voidcle', 'href2', self.image, 'Financial Times', 'Companies', 'teaser2', 'title2',
                 self.ref_date + timedelta(days=2)],
                ['voidart', 'voidcle', 'href3', self.image, 'Financial Times', 'Companies', 'teaser3', 'title3',
                 self.ref_date + timedelta(days=3)],
                ['voidart', 'voidcle', 'href4', self.image, 'Financial Times', 'Companies', 'teaser4', 'title4',
                 self.ref_date + timedelta(days=4)],
                ['voidart', 'voidcle', 'href3', self.image, 'Financial Times', 'Companies', 'teaser3', 'title3',
                 self.ref_date + timedelta(days=5)],
                ['voidart', 'voidcle', 'href3', self.image, 'Financial Times', 'Companies', 'teaser3', 'title3',
                 self.ref_date + timedelta(days=6)],
                ['voidart', 'voidcle', 'href3', self.image, 'Financial Times', 'Companies', 'teaser3', 'title3',
                 self.ref_date + timedelta(days=7)],
                ['voidart', 'voidcle', 'href3', self.image, 'Financial Times', 'Companies', 'teaser3', 'title3',
                 self.ref_date + timedelta(days=8)],
                ['voidart', 'voidcle', 'href3', self.image, 'Financial Times', 'Companies', 'teaser3', 'title3',
                 self.ref_date + timedelta(days=9)]
            ]
        )

        cur = self.connection.cursor()

        #cur.execute('TRUNCATE harrispierce_article;')
        #cur.execute('TRUNCATE harrispierce_journal CASCADE;')
        #cur.execute('TRUNCATE harrispierce_section CASCADE;')

        cur.execute("INSERT INTO harrispierce_journal(name, country) VALUES"
                    "('Wall Street Journal', 'US'),"
                    "('New York Times', 'US'),"
                    "('Financial Times', 'US'),"
                    "('Les Echos', 'France')")

        cur.execute("INSERT INTO harrispierce_section(name) VALUES"
                    "('World'), ('Companies')"
                    )

        insert_article(self.connection, df_to_insert)

        request = self.factory.get('/display')
