# Generated by Django 3.0.2 on 2020-03-03 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol', '0004_auto_20200303_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='com_order_mapper',
            name='requestedStartDate',
            field=models.DateField(default=datetime.datetime(2020, 3, 3, 17, 25, 51, 557498)),
        ),
    ]