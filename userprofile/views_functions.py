from itertools import chain

from .models import Following, User, SentArticles, Article


def profile_get(user):
    """
    :param user: The session user.
    :return: A dict containing:
    - journals which is a queryset of Journal objects (with related Section objects)
    - choices which is a dict: {'journal': [1, 2], 'section': [1, 2, 7]}
    """

    user_id = user.id

    try:
        followers = Following.objects.filter(user_followed_id=user_id)
    except Following.DoesNotExist:
        followers = None

    try:
        following = Following.objects.filter(follower_id=user_id)
    except Following.DoesNotExist:
        following = None

    followers_name = User.objects.filter(id__in=followers.values('follower_id')).values('username')
    following_name = User.objects.filter(id__in=following.values('user_followed_id')).values('username')

    friends_name = followers_name & following_name

    args = {'followers': followers_name, 'following': following_name, 'friends': friends_name}

    return args


def recommended_get(user):
    """
    :param user: The session user.
    :return: A dict containing:
    - journals which is a queryset of Journal objects (with related Section objects)
    - choices which is a dict: {'journal': [1, 2], 'section': [1, 2, 7]}
    """

    user_id = user.id

    sent_article_objects = SentArticles.objects.filter(recipient_id=user_id).order_by('-sent_date')
    article_objects = Article.objects.filter(id__in=sent_article_objects.values('article_id'))
    sender_objects = [User.objects.get(id=sent_article_object.sender_id) for sent_article_object in sent_article_objects]

    print(article_objects[0].image)

    sent_articles = zip(sent_article_objects, article_objects, sender_objects)

    args = {'sent_articles': sent_articles}

    return args