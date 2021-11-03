from django.shortcuts import render
from django.http import Http404
from .models import *

# def api_poll(request):
#     try:
#         pass
#     except api_poll.DoesNotExist:
#         raise Http404("Question does not exist")
#
#     return render(request, 'polls/detail.images', {'question': question})


def user_cards(request):
    users = PersonalData.objects.all()
    return render(request, 'TalkTalk.html', context={'users': users})


def for_companies(request):
    return render(request, 'TalkTalkForCompanies.html')
