# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_auto_20160123_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='code',
            field=models.TextField(max_length=400, blank=True),
        ),
    ]
