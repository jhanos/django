# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('combat', '0005_auto_20150627_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pathfinderarmor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pathfindercreatures',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pathfinderweapon',
            name='id',
        ),
        migrations.AlterField(
            model_name='pathfinderarmor',
            name='name',
            field=models.CharField(blank=True, serialize=False, primary_key=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pathfindercreatures',
            name='name',
            field=models.CharField(blank=True, serialize=False, primary_key=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pathfinderweapon',
            name='name',
            field=models.CharField(blank=True, serialize=False, primary_key=True, max_length=100),
        ),
    ]
