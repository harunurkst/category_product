# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20151023_0252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainproduct',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='mainproduct',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
