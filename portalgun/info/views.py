from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'index.html'

@login_required()
def index(request):
    return render(request, 'index.html')
