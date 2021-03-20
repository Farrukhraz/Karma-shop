# Generated by Django 2.2.16 on 2020-11-21 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DealsOfTheWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='product name')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='product name')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='product image')),
                ('url', models.URLField(default='#', verbose_name='product url')),
            ],
        ),
        migrations.CreateModel(
            name='HotOffers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='product title')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='product description')),
                ('image', models.ImageField(blank=True, upload_to='hot_offers_images')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='product name')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('short_desc', models.CharField(blank=True, max_length=60, verbose_name='product short description')),
                ('description', models.TextField(blank=True, verbose_name='product description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='product price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='quantity in stock')),
                ('brand_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.ProductBrand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory')),
            ],
        ),
    ]