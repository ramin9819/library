# Generated by Django 3.1.1 on 2020-10-12 09:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 15, 9, 44, 5, 188085, tzinfo=utc)),
        ),
    ]