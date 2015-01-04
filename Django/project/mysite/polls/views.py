from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from django.shortcuts import render, get_object_or_404

from models import Question

def index(request, **kwargs):
    # return HttpResponse('Poll Index Page'+str(kwargs)) # 1

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ','.join([question.question_text for question in latest_question_list]) # 2
    # return HttpResponse(output)

    # template = loader.get_template("polls/index.html") # 3
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))

    context = {'latest_quesion_list': latest_question_list}
    return render(request, "polls/index.html", context)



def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id) # 1

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)