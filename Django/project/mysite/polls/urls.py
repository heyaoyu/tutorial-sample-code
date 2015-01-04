from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from views import *

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', vote, name='vote'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)