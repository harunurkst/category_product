# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20151026_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(upload_to='media/', blank=True, null=True),
        ),
    ]
