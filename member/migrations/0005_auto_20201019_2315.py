# Generated by Django 3.1.1 on 2020-10-19 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20201019_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 23, 15, 12, 206568)),
        ),
    ]
