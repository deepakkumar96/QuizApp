# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0010_auto_20160210_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level_name',
            field=models.CharField(max_length=20, choices=[('Easy', 'EASY'), ('Medium', 'MEDIUM'), ('Hard', 'HARD')]),
        ),
    ]
