from .models import Following


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

    print('FOLLWO: ', followers)
    print('fofofo: ', following)

    args = {'followers': followers, 'following': following}

    return args
