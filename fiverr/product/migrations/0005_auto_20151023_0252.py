# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20151023_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproduct',
            name='photo',
            field=models.ImageField(upload_to='media/', null=True, blank=True),
        ),
    ]
