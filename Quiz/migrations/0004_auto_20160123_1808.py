# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_auto_20160123_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, verbose_name='last login', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default=datetime.datetime(2016, 1, 24, 2, 8, 50, 815253, tzinfo=utc), verbose_name='password', max_length=128),
            preserve_default=False,
        ),
    ]
