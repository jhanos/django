# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('combat', '0003_pathfinderweapon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderarmor',
            name='compMalus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pathfinderarmor',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
