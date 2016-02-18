# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('email', models.EmailField(verbose_name='email address', max_length=255, unique=True)),
                ('profile_picture', models.ImageField(upload_to='profile_images', blank=True)),
                ('wallpaper', models.ImageField(upload_to='profile_wallpapers_images', blank=True)),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], blank=True, max_length=1)),
                ('date_of_birth', models.DateField(blank=True)),
                ('location', models.TextField(blank=True, max_length=140)),
                ('phone_no', models.CharField(blank=True, max_length=15)),
                ('tagline', models.TextField(blank=True, max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
