# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0009_userscore_time_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_images', blank=True),
        ),
    ]
