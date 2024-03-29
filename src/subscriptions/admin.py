# -*- coding: utf-8 -*-

import datetime
from django.contrib import admin
from models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','created_at','subscribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('name','email','phone','created_at')
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.date.today()

    subscribed_today.short_description = u'Inscrição hoje?'
    subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionAdmin)
