from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect


from .models import Schedule, Event
from .forms import PortalForm


@login_required()
def schedule(request):
    user = request.user
    context = {}
    eventlist = Schedule.objects.filter(user=user).filter(
        revealed=True).select_related('event').order_by('event__time')
    context = {'eventlist': eventlist}
    return render(request, 'schedule.html', context)


@login_required()
def portal(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PortalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            dimmension = form.cleaned_data['dimmension']
            event = Event.objects.filter(password=dimmension)
            if event:
                schedule = Schedule.objects.filter(
                    event=event).filter(user=request.user).get()
                schedule.revealed = True
                schedule.save()
                return HttpResponseRedirect('/event/' + str(event.id))
            else:
                form.add_error('dimmension', 'That dimmension does not exist!')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PortalForm()

    return render(request, 'portal.html', {'form': form})


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        return context
