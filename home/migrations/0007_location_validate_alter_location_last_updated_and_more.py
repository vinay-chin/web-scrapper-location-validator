# Generated by Django 4.2.3 on 2023-07-16 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_location_last_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='validate',
            field=models.CharField(default='not yet validated', max_length=999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 16, 8, 37, 8, 643619)),
        ),
        migrations.AlterField(
            model_name='scrapper',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 16, 8, 37, 8, 643904)),
        ),
    ]
