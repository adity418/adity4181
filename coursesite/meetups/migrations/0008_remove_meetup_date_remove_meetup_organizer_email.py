# Generated by Django 5.0.4 on 2024-04-15 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0007_alter_meetup_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='date',
        ),
        migrations.RemoveField(
            model_name='meetup',
            name='organizer_email',
        ),
    ]
