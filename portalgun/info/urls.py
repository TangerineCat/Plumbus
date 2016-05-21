from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

app_name = 'info'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='welcome'), name='welcome'),
    url(r'^help/', views.welcome, name='help'),
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^index/', views.index, name='index'),
]
