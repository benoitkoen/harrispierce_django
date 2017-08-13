#!/usr/bin/python

import psycopg2
from datetime import datetime

hostname = ''
username = 'postgres'
password = ''
database = 'postgres'

"""
# https://www.a2hosting.com/kb/developer-corner/postgresql/connecting-to-postgresql-using-python
def insert_article_local(conn, journal, section, size):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(
        "prepare insertion as "
        
        "INSERT INTO harrispierce_article(title, teaser, href, image, article, cleaned_article, pub_date, journal_id, section_id)"
        "VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)"
    )

    for i in range(size):
        cur.execute('SELECT id FROM harrispierce_journal WHERE name = {}{}{}'.format("'", journal, "'"))
        journal_id = cur.fetchone()[0]
        cur.execute('SELECT id FROM harrispierce_section WHERE name = {}{}{}'.format("'", section, "'"))
        section_id = cur.fetchone()[0]

        cur.execute("execute insertion (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    ('titlePSY'+str(i),
                     'teaserPSY'+str(i),
                     'hrefPSY'+str(i),
                     'imagePSY'+str(i),
                     'articlePSY'+str(i),
                     'cleaned_articlePSY'+str(i),
                     datetime.utcnow(),
                     journal_id,
                     section_id
                     ))

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
#insert_article_local(myConnection, 1, 1, 1)
insert_article_local(myConnection, 'Wall Street Journal', 'World', 3)
myConnection.close()
"""
