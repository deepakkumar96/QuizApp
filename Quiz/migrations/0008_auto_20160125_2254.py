# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0007_option_is_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscore',
            name='account',
            field=models.ForeignKey(related_name='scores', related_query_name='score', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='language',
            field=models.ForeignKey(related_name='scores', related_query_name='score', to='Quiz.Language'),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='level',
            field=models.ForeignKey(related_name='scores', related_query_name='score', to='Quiz.Level'),
        ),
    ]
