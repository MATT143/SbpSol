# Generated by Django 2.2.11 on 2020-03-29 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol', '0008_auto_20200316_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='com_order_mapper',
            name='prov_email',
            field=models.EmailField(default='na@na.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='com_order_mapper',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 17, 21, 20, 68627)),
        ),
    ]