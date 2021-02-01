# Generated by Django 2.2.16 on 2021-02-01 19:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20210201_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuserprofile',
            name='tagline',
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 19, 7, 20, 794545, tzinfo=utc)),
        ),
    ]
