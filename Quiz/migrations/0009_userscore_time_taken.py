# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0008_auto_20160125_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='time_taken',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
