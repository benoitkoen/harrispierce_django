# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime, timedelta


class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Journal(models.Model):
    sections = models.ManyToManyField(Section)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return "%s (%s)" % (
            self.name,
            ", ".join(section.name for section in self.sections.all()),
        )


class Article(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, unique=True)
    teaser = models.TextField(default='void', unique=True)
    href = models.CharField(max_length=300, null=False)
    image = models.TextField(default='void', unique=True)
    article = models.TextField(default='void')
    cleaned_article = models.TextField(default='void')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

"""
class Choice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    section = 
    journal = 
    article = 
    cleaned_article = 
    choice_date = models.DateTimeField(auto_now_add=True)
"""


