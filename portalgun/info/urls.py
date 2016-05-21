from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

app_name = 'info'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='welcome')),
    url(r'^help/', views.help, name='help'),
    url(r'^welcome/', views.help, name='welcome'),
    url(r'^index/', views.index, name='index'),
    url(r'^teams/', views.teams, name='teams'),
    url(r'^badge/', views.badge, name='badge'),
    url(r'^about/', views.about, name='about'),
]
