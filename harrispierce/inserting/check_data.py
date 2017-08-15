
def retrieve_data(conn, table):
    conn.autocommit = True
    cur = conn.cursor()

    if table == 'journal':
        cur.execute('SELECT * FROM harrispierce_journal LIMIT 15;')
        journals = cur.fetchall()
        for journal in journals:
            print(journal)

    elif table == 'section':
        cur.execute('SELECT * FROM harrispierce_section LIMIT 15;')
        sections = cur.fetchall()
        for section in sections:
            print(section)

    elif table == 'article':
        cur.execute('SELECT * FROM harrispierce_article LIMIT 15;')
        articles = cur.fetchall()
        for article in articles:
            print(article)
