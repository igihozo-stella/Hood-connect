# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import neighbourhood,healthservices,notifications,Business,Health,Authorities,BlogPost,Profile


class HealthAdmin(admin.ModelAdmin):
    filter_horizontal =['healthservices']


admin.site.register(neighbourhood)
admin.site.register(Health,HealthAdmin)
admin.site.register(Business)
admin.site.register(healthservices)
admin.site.register(Authorities)
admin.site.register(BlogPost)
admin.site.register(Profile)
admin.site.register(notifications)