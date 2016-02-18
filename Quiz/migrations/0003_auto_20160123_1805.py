# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_remove_account_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('language_name', models.CharField(max_length=40)),
                ('language_type', models.CharField(blank=True, max_length=20, choices=[('C', 'Compiled'), ('I', 'Interpreted')])),
                ('play_count', models.PositiveIntegerField(verbose_name='play count')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('level_name', models.CharField(max_length=20, choices=[('E', 'EASY'), ('M', 'MEDIUM'), ('H', 'HARD')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('play_count', models.PositiveIntegerField(verbose_name='play count')),
                ('language', models.ForeignKey(related_query_name='level', related_name='levels', to='Quiz.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('option_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('question_text', models.TextField(max_length=400)),
                ('code', models.TextField(max_length=400)),
                ('language', models.ForeignKey(related_query_name='question', related_name='questions', to='Quiz.Language')),
                ('level', models.ForeignKey(related_query_name='question', related_name='questions', to='Quiz.Level')),
            ],
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('total_time', models.IntegerField()),
                ('total_question', models.IntegerField()),
                ('total_correct', models.IntegerField()),
                ('score', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
        migrations.AddField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=25, verbose_name='email address', unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='media/profile_images'),
        ),
        migrations.AddField(
            model_name='userscore',
            name='account',
            field=models.ForeignKey(related_name='scores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userscore',
            name='language',
            field=models.ForeignKey(related_name='scores', to='Quiz.Language'),
        ),
        migrations.AddField(
            model_name='userscore',
            name='level',
            field=models.ForeignKey(related_name='scores', to='Quiz.Level'),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(related_query_name='option', related_name='options', to='Quiz.Question'),
        ),
    ]
