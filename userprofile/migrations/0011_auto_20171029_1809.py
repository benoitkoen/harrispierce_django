# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 18:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('harrispierce', '0002_auto_20170918_1319'),
        ('userprofile', '0010_sentarticles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentarticles',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harrispierce.Article'),
        ),
        migrations.AlterUniqueTogether(
            name='sentarticles',
            unique_together=set([('sender', 'article')]),
        ),
    ]
