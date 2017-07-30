# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime, timedelta


class Journal(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)


class Section(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Article(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    teaser = models.TextField()
    href = models.CharField(max_length=300)
    image = models.TextField(default='void')
    article = models.TextField(default='void')
    cleand_article = models.TextField(default='void')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})


class User(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

"""
class Choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
"""

