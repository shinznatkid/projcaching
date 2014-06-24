# -*- coding: utf-8 -*-
from caching.models import *
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_page
import random


def gen_data():
    caches = MyCache.objects.all()
    return {'caches': caches, 'random': random.random()}


@cache_page(15)
def perview_page(request):
    return render(request, 'display_list.html', gen_data())


def persite_page(request):
    return render(request, 'display_list.html', gen_data())


@never_cache
def nocache(request):
    return render(request, 'display_list.html', gen_data())
