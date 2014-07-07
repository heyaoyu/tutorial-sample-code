from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from models import Poll
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    ##output = ', '.join([poll.question for poll in latest_poll_list])
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {'latest_poll_list':latest_poll_list})

    #return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    #try:
    #   poll = Poll.objects.get(pk=poll_id)
    #except Poll.DoesNotExist, e:
    #    raise Http404
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)