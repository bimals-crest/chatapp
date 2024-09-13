# Generated by Django 5.1 on 2024-09-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_remove_subscriber_email_remove_subscriber_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='email_subscription',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
