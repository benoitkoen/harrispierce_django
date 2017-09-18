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


def index_get(user):
    journals = Journal.objects.prefetch_related('sections').all()

    choices = None

    if user is not None:
        choices = get_choices(myConnection, user)

    args = {'journals': journals, 'choices': choices}

    return args


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


def get_choices(conn, user):

    choices = {}

    conn.autocommit = True
    cur = conn.cursor()

    cur.execute('SELECT id FROM auth_user WHERE username = {}{}{}'.format("'", user, "'"))
    user_id = cur.fetchone()[0]
    cur.execute("SELECT date_trunc('seconds', choice_date) FROM userprofile_choice WHERE user_id = {} ORDER BY date_trunc('seconds', choice_date) DESC limit 1".format(user_id))
    latest = cur.fetchone()[0]
    print('kfjsdfksskdjhf', latest)

    cur.execute("SELECT choice_date, journal_id, section_id FROM userprofile_choice WHERE user_id = %s and date_trunc('seconds', choice_date) = %s", [user_id, latest])

    result = cur.fetchall()

    print('WOOOOOOOOO', result)

    for row in result:
        journal = row[1]
        section = row[2]

        if journal not in choices.keys():
            choices[journal] = []
            choices[journal].append(section)
        else:
            choices[journal].append(section)

        print(choices)

    return choices