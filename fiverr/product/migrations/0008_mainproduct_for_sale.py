# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20151026_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainproduct',
            name='for_sale',
            field=models.CharField(default='N', choices=[('Y', 'Yes'), ('N', 'No')], max_length=2),
        ),
    ]
