# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('combat', '0002_auto_20150622_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderweapon',
            name='name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
