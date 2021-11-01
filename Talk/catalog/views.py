from django.shortcuts import render
from django.http import Http404



def api_poll(request, ):
    try:

    except api_poll.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})
# Create your views here.
