from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from harrispierce.models import Article, Journal, Section


class Profile(models.Model):
    """
    A model that records the profile for a user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)


class Choice(models.Model):
    """
    A model that records the sections chosen by the user in index.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    choice_date = models.DateTimeField(auto_now_add=True)

class PinnedArticles(models.Model):
    """
    A model that records the articles that have been pinned by the user for later reading.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    #article = models.ForeignKey(Article, on_delete=models.CASCADE, unique=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    pinned_date = models.DateTimeField(auto_now_add=True)


class LikedArticles(models.Model):
    """
    A model that records the articles that have been liked by the user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    #article = models.ForeignKey(Article, on_delete=models.CASCADE, unique=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now_add=True)


class SentArticles(models.Model):
    """
    A model that records the articles that have been sent by the user to a friend.
    """
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipient')
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(auto_now_add=True)


class Following(models.Model):
    """
    A model that records the follow-followed relationships between users.
    """
    user_followed = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_followed')
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follower')

    class Meta:
        unique_together = ('user_followed', 'follower')


