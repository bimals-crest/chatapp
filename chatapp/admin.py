from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'is_subscribed', 'email_subscription')
    search_fields = ('name', 'phone_number', 'email')
    list_filter = ('is_subscribed', 'email_subscription')

admin.site.register(Subscriber, SubscriberAdmin)
