from ..models import Article, Journal, Section


def insert_article(df):

    if df is None:
        return

    for i in range(len(df)):

        print('Inserting...')

        article = df.ix[i, 'article']
        cleaned_article = df.ix[i, 'cleaned_article']
        href = df.ix[i, 'href']
        image = df.ix[i, 'image']
        journal = df.ix[i, 'journal']
        section = df.ix[i, 'section']
        teaser = df.ix[i, 'teaser']
        title = df.ix[i, 'title']

    journal = Journal.objects.get(name=journal)
    section = Section.objects.get(name=section)

    Article.objects.create(
        article=article,
        cleaned_article=cleaned_article,
        href=href,
        image=image,
        teaser=teaser,
        title=title,
        journal=journal.id,
        section=section.id,
    )

    """
from datetime import datetime
import psycopg2
 
def insert_article(conn, df):

    if df is None:
        return
        
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("deallocate all")

    try:
        cur.execute(
            "prepare insertion as "
            "INSERT INTO harrispierce_article(title, teaser, href, image, article, cleaned_article, pub_date, journal_id, section_id)"
            "VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9) "
            "ON CONFLICT DO NOTHING"
        )
    except psycopg2.ProgrammingError:
        print('error prog')
        pass

    for i in range(len(df)):

        print('Inserting...')

        article = df.ix[i, 'article']
        cleaned_article = df.ix[i, 'cleaned_article']
        href = df.ix[i, 'href']
        image = df.ix[i, 'image']
        journal = df.ix[i, 'journal']
        section = df.ix[i, 'section']
        teaser = df.ix[i, 'teaser']
        title = df.ix[i, 'title']

        cur.execute('SELECT id FROM harrispierce_journal WHERE name = {}{}{}'.format("'", journal, "'"))
        journal_id = cur.fetchone()[0]
        cur.execute('SELECT id FROM harrispierce_section WHERE name = {}{}{}'.format("'", section, "'"))
        section_id = cur.fetchone()[0]

        cur.execute("execute insertion (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (title,
                     teaser,
                     href,
                     image,
                     article,
                     cleaned_article,
                     datetime.utcnow(),
                     journal_id,
                     section_id
                     ))
    """