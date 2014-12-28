#coding=utf-8
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(verbose_name='question content', max_length=200)
    pub_date = models.DateTimeField(verbose_name='timestamp published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = pub_date
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name="related question")
    choice_text = models.CharField(verbose_name='choice content', max_length=200)
    votes = models.IntegerField(verbose_name='total vote number', default=0)

    def __unicode__(self):
        return self.choice_text