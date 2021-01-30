# Generated by Django 3.1.5 on 2021-01-27 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20210127_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default='job', max_length=50),
        ),
        migrations.AddField(
            model_name='job',
            name='requirements',
            field=models.CharField(default='not specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 27, 17, 52, 27, 827559)),
        ),
    ]
