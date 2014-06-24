# -*- coding: utf-8 -*-
from django.db import models


class MyCache(models.Model):

    def __unicode__(self):
        return str(self.counter)

    counter = models.IntegerField()
