from django.conf.urls import url
from . import views
from django.urls import path, re_path
import re

urlpatterns = [
    path("", views.index, name='index'),
    re_path( r'^details/(?P<id>\[0,50]{1})/$', views.details)
  #  re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
]
