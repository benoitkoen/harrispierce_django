#from harrispierce.scrapping.scrap import scrap
#from harrispierce.models import Article

from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres@localhost:5432/harrispiercedb')
df.to_sql('harrispierce_article', engine, if_exists="replace")

"""
def insert_into_pg(journal, section, url):

    df = scrap(journal, section, url)
    df_records = df.to_dict('records')

    model_instances = [Article(
        field_1=record['field_1'],
        field_2=record['field_2'],
    ) for record in df_records]

    Article.objects.bulk_create(model_instances)
"""

t = insert_into_pg('Wall Street Journal', 'Politics', 'https://www.wsj.com/news/politics')


#t = scrap('Financial Times', 'World', 'https://www.ft.com/world')

#t = scrap('New York Times', 'Dealbook', 'http://www.nytimes.com/pages/business/dealbook/index.html?src=busfn')
#t = scrap('Wall Street Journal', 'Politics', 'https://www.wsj.com/news/politics')
#t = scrap('Wall Street Journal', 'Economy', 'https://www.wsj.com/news/economy')
#t = scrap('Wall Street Journal', 'Tech', 'https://www.wsj.com/news/technology')

print('vfavfvf')
#print('vfavfvf\n', t.iloc[0]['articles'])
#print('vfavfvf\n', t.iloc[1]['articles'])
#print('url: ', t.iloc[1]['hrefs'])