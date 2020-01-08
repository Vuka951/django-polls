from django.contrib import admin

# Register your models here.
from .models import Question, Choice


admin.site.site_header = 'Poller Admin'
admin.site.site_Title = 'Poller Admin'
admin.site.index_title = 'Welcome to Poller Admin'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    filedsets = [
        (None, {'fields': ['question_text']}),
        (
            'Date Info',
            {
                'fields': ['pub_date'],
                'classes': ['collapse']
            }
        ),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
