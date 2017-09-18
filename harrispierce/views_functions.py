from django.db.models import Q
from datetime import datetime
import psycopg2

from .models import Article, Journal, Section
from harrispierceDjango.settings.local import DATABASES

hostname = ''
username = DATABASES['default']['USER']  # 'postgres'
password = ''
database = DATABASES['default']['NAME']  # 'postgres'

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)


def index_get():
    journals = Journal.objects.prefetch_related('sections').all()
    args = {'journals': journals}

    return journals, args


def display_get(selection, user):
    selection_dict = {}

    for journal_section in selection:
        journal, section = journal_section.split('-')

        articles = Article.objects.filter(journal_id__name=journal, section_id__name=section).order_by('pub_date')[:9]

        if journal not in selection_dict.keys():
            article_selection = {}
            article_selection[section] = articles
            selection_dict[journal] = article_selection
        else:
            article_selection[section] = articles
            selection_dict[journal] = article_selection

    if user is not None:
        insert_choices(myConnection, selection_dict, user)

    args = {'selection_dict': selection_dict}

    return args


def display_search(keyword, sources, date, quantity):
    selection_dict = {}

    for journal in sources:

        articles = Article.objects.filter(
            (Q(teaser__icontains=keyword) | Q(title__icontains=keyword)),
            pub_date__gte=date,
            journal_id__name=journal,
        ).order_by('pub_date')[:quantity]

        selection_dict[journal] = articles

    args = {'selection_dict': selection_dict}

    return args


def insert_choices(conn, selection_dict, user):
    print('user: ', user)
    choices = {}
    for journal in selection_dict.keys():
        choices[journal] = list(selection_dict[journal].keys())

    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("deallocate all")

    cur.execute(
        "prepare choice_insertion as "
        "INSERT INTO userprofile_choice(user_id, journal_id, section_id, choice_date)"
        "VALUES ($1, $2, $3, $4)"
    )

    for journal in selection_dict.keys():
        for section in selection_dict[journal]:

            cur.execute('SELECT id FROM harrispierce_journal WHERE name = {}{}{}'.format("'", journal, "'"))
            journal_id = cur.fetchone()[0]
            cur.execute('SELECT id FROM harrispierce_section WHERE name = {}{}{}'.format("'", section, "'"))
            section_id = cur.fetchone()[0]
            cur.execute('SELECT id FROM auth_user WHERE username = {}{}{}'.format("'", user, "'"))
            user_id = cur.fetchone()[0]

            cur.execute("execute choice_insertion (%s, %s, %s, %s)",
                        (user_id,
                         journal_id,
                         section_id,
                         datetime.utcnow(),
                         ))
