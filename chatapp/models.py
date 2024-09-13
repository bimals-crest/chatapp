from django.db import models

class Subscriber(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    is_subscribed = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    email_subscription = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.phone_number})'
