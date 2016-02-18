# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_auto_20160123_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
