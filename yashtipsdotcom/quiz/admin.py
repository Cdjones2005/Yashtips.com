from django.contrib import admin
from . import models
# Register your models here.

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer',
        'is_correct',
    ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'difficulty',
    ]
    list_display = [
        'title'
    ]
    inlines = [
        AnswerInlineModel,
    ]

@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer',
        'is_correct',
        'question'
    ]
