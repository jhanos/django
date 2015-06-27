# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('combat', '0004_auto_20150626_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pathfindercreatures',
            name='weapon',
        ),
        migrations.AddField(
            model_name='pathfindercreatures',
            name='defaultWeapon1',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pathfindercreatures',
            name='defaultWeapon2',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
