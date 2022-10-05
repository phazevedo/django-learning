import http
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Question
from django.template import loader

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
    # We can also remove the dependency
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk= question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    
    # can also be written as when adding 'from django.shortcuts import get_object_or_404'
    question = get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "Your're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)