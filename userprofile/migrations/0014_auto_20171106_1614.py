# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-06 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_sentarticles_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedarticles',
            name='journal',
        ),
        migrations.RemoveField(
            model_name='likedarticles',
            name='section',
        ),
        migrations.RemoveField(
            model_name='pinnedarticles',
            name='journal',
        ),
        migrations.RemoveField(
            model_name='pinnedarticles',
            name='section',
        ),
        migrations.RemoveField(
            model_name='sentarticles',
            name='journal',
        ),
        migrations.RemoveField(
            model_name='sentarticles',
            name='section',
        ),
    ]
