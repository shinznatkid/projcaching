#!/usr/bin/python
# -*- coding: utf-8

from django.db.models.signals import post_syncdb
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Permission

# custom user related permissions
def add_user_permissions(sender, **kwargs):
	ct = ContentType.objects.get(app_label='auth', model='user')
	perm, created = Permission.objects.get_or_create(codename='can_view', name='Can View Users', content_type=ct)
post_syncdb.connect(add_user_permissions, sender=auth_models)