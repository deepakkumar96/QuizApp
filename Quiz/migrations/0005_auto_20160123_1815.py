# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_auto_20160123_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_type',
            field=models.CharField(choices=[('C', 'Compiled'), ('I', 'Interpreted'), ('B', 'Both')], max_length=20, blank=True),
        ),
    ]
