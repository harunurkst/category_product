# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20151022_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', null=True),
        ),
        migrations.AlterField(
            model_name='mainproduct',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', null=True),
        ),
    ]
