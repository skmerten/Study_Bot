"""
Definition of urls for Study_Bot.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.newQuestion, name='newQuestion'),
    url(r'^settings$', app.views.settings, name='settings'),
    url(r'^question$', app.views.newQuestion, name='newQuestion'),
    url(r'^score$', app.views.score, name='score'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
]
