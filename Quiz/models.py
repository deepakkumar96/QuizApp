from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from Quiz.managers import AccountManager
from django.conf import settings


class Account(AbstractBaseUser):
    # Choices
    USER_GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    # Fields
    email= models.EmailField(
        verbose_name='email address',
        max_length=25,
        unique=True
    )
    profile_picture = models.ImageField(
        upload_to='profile_images',
        blank=True
    )
    wallpaper = models.ImageField(
        upload_to='profile_wallpapers_images',
        blank=True
    )
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    gender = models.CharField(max_length=1, blank=True, choices=USER_GENDER)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.TextField(max_length=140, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    tagline = models.TextField(max_length=100, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Manager
    objects = AccountManager()

    # Methods
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Language(models.Model):
    # Choices
    LANGUAGE_TYPE = (
        ('C', 'Compiled'),
        ('I', 'Interpreted'),
        ('B', 'Both')
    )

    # Fields
    language_name = models.CharField(max_length=40)
    language_type = models.CharField(
        choices=LANGUAGE_TYPE,
        max_length=20,
        blank=True
    )
    play_count = models.PositiveIntegerField(verbose_name='play count')

    # Methods
    def __str__(self):
        return self.language_name

    def get_play_count(self):
        return self.play_count


class Level(models.Model):
    # Choices
    LEVELS_CHOICE = (
        ('Easy', 'EASY'),
        ('Medium', 'MEDIUM'),
        ('Hard', 'HARD')
    )

    # Relationship
    language = models.ForeignKey(
        Language,
        related_name='levels',
        related_query_name='level'
    )

    # Fields
    level_name = models.CharField(choices=LEVELS_CHOICE, max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    play_count = models.PositiveIntegerField(verbose_name='play count')

    # Methods
    def __str__(self):
        switch = {
            'Easy': 'Easy '+str(self.language),
            'Medium': 'Medium '+str(self.language),
            'Hard': 'Hard '+str(self.language),
        }
        return self.level_name + ' ' + str(self.language)
        # return switch.get(str(self.level_name))

    def get_language(self):
        return self.language

    def get_play_count(self):
        return self.play_count


class Question(models.Model):
    # Relationship
    language = models.ForeignKey(
        Language,
        related_name='questions',
        related_query_name='question'
    )
    level = models.ForeignKey(
        Level,
        related_name='questions',
        related_query_name='question'
    )

    # Fields
    question_text = models.TextField(max_length=400)
    code = models.TextField(max_length=400, blank=True)

    # Methods
    def __str__(self):
        return self.question_text


class Option(models.Model):
    # Relationship
    question = models.ForeignKey(
        Question,
        related_name='options',
        related_query_name='option'
    )

    # Fields
    option_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    # Methods
    def __str__(self):
        return self.option_text

    def is_it_correct(self):
        return self.is_correct

    def convert_to_json(self):
        return{
            'option_text': self.option_text,
            'is_correct': self.is_correct,
        }


class UserScore(models.Model):
    # Relationship
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='scores',
        related_query_name='score'
    )
    language = models.ForeignKey(
        Language,
        related_name='scores',
        related_query_name='score'
    )
    level = models.ForeignKey(
        Level,
        related_name='scores',
        related_query_name='score'
    )

    # Fields
    created_date = models.DateTimeField(auto_now_add=True)
    total_time = models.IntegerField()
    time_taken = models.IntegerField()
    total_question = models.IntegerField()
    total_correct = models.IntegerField()
    score = models.FloatField()

    # Methods
    def __str__(self):
        return str(self.score)

    def calculate_score(self):
        return self.score
