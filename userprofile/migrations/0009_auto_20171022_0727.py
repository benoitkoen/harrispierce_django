# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 07:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0008_auto_20170921_1809'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='following',
            unique_together=set([('user_followed', 'follower')]),
        ),
    ]
