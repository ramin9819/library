# Generated by Django 3.1.1 on 2020-10-19 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20201019_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateTimeField(),
        ),
    ]