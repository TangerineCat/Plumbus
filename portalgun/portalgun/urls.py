"""plumbus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from revproxy.views import ProxyView

urlpatterns = [
    url(r'^$', auth_views.login),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('info.urls')),
    url(r'^', include('schedule.urls')),
    url(r'^info/', include('info.urls')),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^(?P<path>.*)$', ProxyView.as_view(upstream='http://getschwifty2016.com/')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)