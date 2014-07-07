import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin


class Poll(models.Model):

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):

    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text


#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):

    #fields = ['pub_date', 'question']
    fieldsets = [
        (None, {'fields':['question']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline,]
    list_display = ['question', 'pub_date', 'was_published_recently']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)