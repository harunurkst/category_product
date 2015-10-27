# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=125, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description')),
                ('photo', models.ImageField(null=True, upload_to='media/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=125)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('description', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to='media/', blank=True)),
                ('categories', models.ForeignKey(blank=True, to='product.Category', null=True)),
            ],
        ),
    ]
