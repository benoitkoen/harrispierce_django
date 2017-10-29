from itertools import chain

from .models import Following, User


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

    #friends = Following.objects.filter(follower_id__in=following.values('user_followed_id'))
    #friends_name = User.objects.filter(id__in=friends.values('user_followed_id'))
    friends_name = followers_name & following_name

    args = {'followers': followers_name, 'following': following_name, 'friends': friends_name}

    return args
