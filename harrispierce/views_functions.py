from django.db.models import Q
from datetime import datetime
from collections import defaultdict
import psycopg2

from .models import Article, Journal, Section
from userprofile.models import Choice, PinnedArticles
from harrispierceDjango.settings.local import DATABASES

hostname = ''
username = DATABASES['default']['USER']  # 'postgres'
password = ''
database = DATABASES['default']['NAME']  # 'postgres'

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)


def index_get(user):
    """
    :param user: The session user.
    :return: A dict containing:
    - journals which is a queryset of Journal objects (with related Section objects)
    - choices which is a dict: {'journal': [1, 2], 'section': [1, 2, 7]}
    """
    journals = Journal.objects.prefetch_related('sections').all()

    choices = None

    if user is not None:
        choices = get_choices(myConnection, user)

    args = {'journals': journals, 'choices': choices}

    return args


def display_get(selection, user):
    """
    :param selection: A list containing 'journal_id-section_id' select by the user in index.
    :param user: The session user.
    :return: A dict containing:
    - selection_dict which is a dict: {Journal object: {Section object: Article queryset}}
    - pinned_articles which is a Article queryset
    """

    selection_dict = {}

    for journal_section in selection:
        journal_id, section_id = journal_section.split('-')

        journal = Journal.objects.get(pk=journal_id)
        section = Section.objects.get(pk=section_id)
        articles = Article.objects.filter(journal_id=journal_id, section_id=section_id).order_by('-pub_date')[:9]

        if journal not in selection_dict.keys():
            article_selection = {}
            article_selection[section] = articles
            selection_dict[journal] = article_selection
        else:

            article_selection[section] = articles
            selection_dict[journal] = article_selection

    if user is not None:
        insert_choices(selection, user)

    pinned_articles = Article.objects.filter(id__in=PinnedArticles.objects.values('article_id')).order_by('pub_date')

    args = {'selection_dict': selection_dict, 'pinned_articles': pinned_articles}

    return args


def display_search(keyword, sources, date, quantity):
    """
    :param keyword: A text input.
    :param sources: A checkbox for each journal.
    :param date: A date after which articles are retrieved.
    :param quantity: An integer input for the number of articles to retrieve per journal.
    :return: A dict containing:
    - selection_dict which is a dict with journal_name as key and Article queryset as value
    """
    selection_dict = {}

    for journal in sources:

        articles = Article.objects.filter(
            (Q(teaser__icontains=keyword) | Q(title__icontains=keyword)),
            pub_date__gte=date,
            journal_id__name=journal,
        ).order_by('pub_date')[:quantity]

        if len(articles) > 0:
            selection_dict[journal] = articles

    print('dsjnjns ', selection_dict)
    args = {'selection_dict': selection_dict}

    return args


def insert_choices(selection, user):
    """
    :param selection: A list containing 'journal_id-section_id' select by the user in index.
    :param user: The session user.
    :return: Creates a Choice object recording which journal and section a user has chosen in index.
    """

    for journal_section in selection:
        journal_id, section_id = journal_section.split('-')

        journal = Journal.objects.get(pk=journal_id)
        section = Section.objects.get(pk=section_id)

        Choice.objects.create(
            user=user,
            journal=journal,
            section=section,
        )


def get_choices(conn, user):
    """
    :param conn: A psycopg2 connection
    :param user: The session user.
    :return: A dict containing the latest user's choice: {'journal': [1, 2], 'section': [1, 2, 7]}.
    """

    choices = defaultdict(list)

    conn.autocommit = True
    cur = conn.cursor()

    cur.execute('SELECT id FROM auth_user WHERE username = {}{}{}'.format("'", user, "'"))
    user_id = cur.fetchone()[0]

    cur.execute("SELECT date_trunc('seconds', choice_date) FROM userprofile_choice WHERE user_id = {} ORDER BY date_trunc('seconds', choice_date) DESC limit 1".format(user_id))
    latest = cur.fetchone()
    if latest is None:
        return choices
    latest = latest[0]

    cur.execute("SELECT choice_date, journal_id, section_id FROM userprofile_choice WHERE user_id = %s and date_trunc('seconds', choice_date) = %s", [user_id, latest])

    result = cur.fetchall()

    for row in result:
        journal = row[1]
        section = row[2]

        if journal not in choices['journal']:
            choices['journal'].append(journal)
        if section not in choices['section']:
            choices['section'].append(section)

    return choices
