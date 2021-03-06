# Generated by Django 2.2.11 on 2020-03-29 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol', '0009_auto_20200329_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='com_order_mapper',
            name='quantity',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='com_order_mapper',
            name='renewalTerm',
            field=models.IntegerField(blank=True, default=12),
        ),
        migrations.AlterField(
            model_name='com_order_mapper',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 20, 51, 22, 784983)),
        ),
    ]
