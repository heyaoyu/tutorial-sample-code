# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200, verbose_name=b'choice content')),
                ('votes', models.IntegerField(default=0, verbose_name=b'total vote number')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200, verbose_name=b'question content')),
                ('pub_date', models.DateTimeField(verbose_name=b'timestamp published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(verbose_name=b'related question', to='polls.Question'),
            preserve_default=True,
        ),
    ]
