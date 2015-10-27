# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_mainproduct_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproduct',
            name='categories',
            field=models.ForeignKey(null=True, to='product.Category'),
        ),
    ]
