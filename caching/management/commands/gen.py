#!/usr/bin/python
# -*- coding: utf-8

from django.core.management.base import BaseCommand
from caching.models import *


class Command(BaseCommand):
    args = ''
    help = 'Generate caching object'

    def handle(self, *args, **options):
        limited = 100
        counting = 1
        bulk = []
        mycache_count = MyCache.objects.count()
        if mycache_count < limited:
            counting = mycache_count
        for i in range(counting, limited+1):
            bulk.append(MyCache(counter=i))
        if bulk:
            MyCache.objects.bulk_create(bulk)
        self.stdout.write('Successfully generated for %s items.' % (limited-counting))
