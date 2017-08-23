from .models import Article, Journal, Section


def index_get():
    journals = Journal.objects.prefetch_related('sections').all()
    args = {'journals': journals}

    return journals, args


def display_get(selection):
    selection_dict = {}

    for journal_section in selection:
        journal, section = journal_section.split('-')
        articles = Article.objects.filter(journal_id__name=journal, section_id__name=section)

        if journal not in selection_dict.keys():
            article_selection = {}
            article_selection[section] = articles
            selection_dict[journal] = article_selection
        else:
            article_selection[section] = articles
            selection_dict[journal] = article_selection

    args = {'selection_dict': selection_dict}

    return args


def insert_choices(conn, selection_dict):
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("deallocate all")

    cur.execute(
        "prepare insertion as "
        "INSERT INTO harrispierce_choice(user_id, journal_id, section_id, article_id, choice_date)"
        "VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)"
    )
