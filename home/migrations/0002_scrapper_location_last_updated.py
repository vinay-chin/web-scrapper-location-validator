# Generated by Django 4.2.3 on 2023-07-16 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='scrapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 16, 5, 31, 49, 781532))),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 16, 5, 31, 49, 781262)),
        ),
    ]
