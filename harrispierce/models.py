# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime


class Journal(models.Model):
    name = models.CharField(max_length=200)


class Section(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Article(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name
