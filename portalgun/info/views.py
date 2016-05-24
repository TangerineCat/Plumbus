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
    context = {}
    identitylist = Identity.objects.filter(user=user)
    if not identitylist:
        # user does not have identity
        print 'no identity'
        pass
    elif len(identitylist) > 1:
        # non-unique user
        print 'non-unique user\n'
        pass
    else:
        identity = identitylist.select_related('team', 'alignment').get()
        showhidden = identity.alignment.alignment != 'N'
        context = {'identity': identity, 'showhidden': showhidden}

    return render(request, 'teams.html', context)


@login_required()
def help(request):
    return render(request, 'help.html')


@login_required()
def badge(request):
    user = request.user
    context = {}
    identitylist = Identity.objects.filter(user=user)
    identity = identitylist.select_related('alignment').get()
    context = {'identity': identity}
    return render(request, 'badge.html', context)

def about(request):
    return render(request, 'about.html')
