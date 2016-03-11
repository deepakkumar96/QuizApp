from django.contrib import admin
from Quiz.models import *

# Register your models here.

class LanguageInline(admin.TabularInline):
    model = Language

class LevelInline(admin.TabularInline):
    model = Level

class QuestionInline(admin.TabularInline):
    model = Question

class OptionInline(admin.TabularInline):
    model = Option

class LanguageAdmin(admin.ModelAdmin):
    inlines = [LevelInline, QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Account)
# admin.site.register(Language)
admin.site.register(Level)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(UserScore)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Challenge)


