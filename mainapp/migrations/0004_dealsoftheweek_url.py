# Generated by Django 2.2.16 on 2020-11-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_dealsoftheweek_hotoffers'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealsoftheweek',
            name='url',
            field=models.URLField(default='#', verbose_name='product url'),
        ),
    ]