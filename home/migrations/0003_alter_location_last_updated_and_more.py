# Generated by Django 4.2.3 on 2023-07-16 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_scrapper_location_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 16, 5, 34, 10, 871593, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='scrapper',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 16, 5, 34, 10, 871847, tzinfo=datetime.timezone.utc)),
        ),
    ]