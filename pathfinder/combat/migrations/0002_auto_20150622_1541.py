# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('combat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PathfinderArmor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('AC', models.IntegerField(null=True, blank=True)),
                ('dexLimit', models.IntegerField(null=True, blank=True)),
                ('magic', models.IntegerField(null=True, blank=True)),
                ('master', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pathfindercreatures',
            name='weapon',
            field=models.ManyToManyField(null=True, to='combat.PathfinderWeapon', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pathfinderweapon',
            name='magic',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pathfinderweapon',
            name='master',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pathfinderweapon',
            name='weaponRange',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
