# Generated by Django 5.0.4 on 2024-04-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightresv', '0003_alter_flight_departurecity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]