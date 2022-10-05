import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    # Django’s database API
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # Alternatively, you can use the render() method instead of
    # return HttpResponse(template.render(context, request))
    # We can also remove the dependency from django.template import loader
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
    response = "Your're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)