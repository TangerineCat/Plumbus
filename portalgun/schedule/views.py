from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def schedule(request):
    return render(request, 'schedule.html')

@login_required()
def portal(request):
    return render(request, 'portal.html')