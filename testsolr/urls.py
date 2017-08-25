#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from views import *

urlpatterns = [
        url(r'^index/$', indexes_search, name='search_view'),
]
'''
urlpatterns = [
        url(r'^$', api_root, name='search'),
]
'''
