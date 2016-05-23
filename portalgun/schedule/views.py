from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Event, Schedule


@login_required()
def schedule(request):
    user = request.user
    context = {}
    eventlist = Schedule.objects.filter(user=user).filter(revealed=True).order_by('time')
    context = {'eventlist': eventlist}
    return render(request, 'schedule.html')


@login_required()
def portal(request):
    return render(request, 'portal.html')
