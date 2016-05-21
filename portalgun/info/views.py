from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Team, Alignment, Identity

class IndexView(generic.ListView):
    template_name = 'index.html'


def index(request):
    return render(request, 'index.html')

@login_required()
def teams(request):
    user = request.user

    context={}
    return render(request, 'teams.html', context)

@login_required()
def help(request):
    return render(request, 'help.html')

@login_required()
def badge(request):
    return render(request, 'badge.html')

def about(request):
    return render(request, 'about.html')