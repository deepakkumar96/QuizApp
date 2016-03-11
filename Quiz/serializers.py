from rest_framework import serializers
from Quiz.models import *


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = (
            'email', 'first_name', 'last_name', 'gender', 'location',
            'phone_no', 'tagline', 'profile_picture', 'wallpaper'
        )
        write_only_field = ('password',)
        #lookup_field = 'email'


class SimpleAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'first_name')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('option_text', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    language = serializers.StringRelatedField()
    level = serializers.StringRelatedField()

    class Meta:
        model = Question
        fields = ('language', 'level', 'question_text', 'code', 'options')


class UserScoreSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = UserScore
        fields = ('account', 'language', 'level', 'created_date', 'total_time', 'time_taken',
                  'total_question', 'total_correct', 'score')


class ShortUserScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserScore
        fields = ('total_time', 'time_taken', 'total_question', 'total_correct', 'score')


class LevelSerializer(serializers.ModelSerializer):
    scores = UserScoreSerializer(many=True, read_only=True)
    level_name = serializers.StringRelatedField()

    class Meta:
        model = Level
        fields = ('pk', 'level_name', 'play_count', 'scores')


class LanguageSerializer(serializers.ModelSerializer):
    levels = LevelSerializer(many=True, read_only=True)

    class Meta:
        model = Language
        fields = ('pk', 'language_name', 'language_type', 'play_count', 'levels')


class ChallengeSerializer(serializers.ModelSerializer):
    user_from = serializers.StringRelatedField()
    user_to = serializers.StringRelatedField()
    # language = serializers.SlugRelatedField(slug_field='language_name', read_only=True)
    score = ShortUserScoreSerializer()

    class Meta:
        model = Challenge
        fields = (
            'pk', 'user_from', 'user_to', 'language', 'level',
            'is_accepted', 'message', 'score'
        )


class LanguageWithQuestion(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Language
        fields = ('pk', 'language_name', 'questions')


class LevelWithQuestion(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    #questions = QuestionSerializer()

    class Meta:
        model = Level
        fields = ('language', 'level_name', 'questions')
