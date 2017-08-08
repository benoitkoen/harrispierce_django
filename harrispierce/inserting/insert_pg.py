#!/usr/bin/python

import psycopg2

hostname = ''
username = 'postgres'
password = ''
database = 'postgres'


# https://www.a2hosting.com/kb/developer-corner/postgresql/connecting-to-postgresql-using-python
def insert_article_local(conn, journal, section, size):
    cur = conn.cursor()
    cur.execute(
        "prepare insertion as "
        
        "INSERT INTO harrispierce_article(title, teaser, href, image, article, cleaned_article, journal_id, section_id)"
        "VALUES ($1, $2, $3, $4, $5, $6, SELECT id FROM harrispierce_journal WHERE name = $7, "
        "SELECT id FROM harrispierce_section WHERE name = $8"
    )

    for i in range(size):
        cur.execute("execute insertion (%s, %s, %s, %s, %s, %s, %s, %s)",
                    ('title'+str(i),
                     'teaser'+str(i),
                     'href'+str(i),
                     'image'+str(i),
                     'article'+str(i),
                     'cleaned_article'+str(i),
                     journal,
                     section
                     ))

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
insert_article_local(myConnection, 'Wall Street Journal', 'Economy', 5)
myConnection.close()


#t = insert_into_pg('Wall Street Journal', 'Politics', 'https://www.wsj.com/news/politics')


#t = scrap('Financial Times', 'World', 'https://www.ft.com/world')

#t = scrap('New York Times', 'Dealbook', 'http://www.nytimes.com/pages/business/dealbook/index.html?src=busfn')
#t = scrap('Wall Street Journal', 'Politics', 'https://www.wsj.com/news/politics')
#t = scrap('Wall Street Journal', 'Economy', 'https://www.wsj.com/news/economy')
#t = scrap('Wall Street Journal', 'Tech', 'https://www.wsj.com/news/technology')

print('vfavfvf')
#print('vfavfvf\n', t.iloc[0]['articles'])
#print('vfavfvf\n', t.iloc[1]['articles'])
#print('url: ', t.iloc[1]['hrefs'])