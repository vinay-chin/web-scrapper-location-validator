# Generated by Django 4.2.3 on 2023-07-16 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_location_id_alter_location_last_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 16, 8, 30, 24, 431327)),
        ),
        migrations.AlterField(
            model_name='scrapper',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 16, 8, 30, 24, 431716)),
        ),
    ]
