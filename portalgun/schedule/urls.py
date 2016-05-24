from django.conf.urls import url

from . import views

app_name = 'schedule'

urlpatterns = [
    url(r'^portal/?$', views.portal, name='portal'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^event/(?P<pk>[\w.@+-]+)/$',
        views.EventDetailView.as_view(), name='event-detail'),
]
