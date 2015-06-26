# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PathfinderCreatures',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('AC', models.IntegerField(null=True, blank=True)),
                ('ACtouch', models.IntegerField(null=True, blank=True)),
                ('ACflat', models.IntegerField(null=True, blank=True)),
                ('hp', models.IntegerField(null=True, blank=True)),
                ('init', models.IntegerField(null=True, blank=True)),
                ('fort', models.IntegerField(null=True, blank=True)),
                ('ref', models.IntegerField(null=True, blank=True)),
                ('will', models.IntegerField(null=True, blank=True)),
                ('speed', models.IntegerField(null=True, blank=True)),
                ('str', models.IntegerField(null=True, blank=True)),
                ('dex', models.IntegerField(null=True, blank=True)),
                ('con', models.IntegerField(null=True, blank=True)),
                ('int', models.IntegerField(null=True, blank=True)),
                ('wis', models.IntegerField(null=True, blank=True)),
                ('cha', models.IntegerField(null=True, blank=True)),
                ('baseAtk', models.IntegerField(null=True, blank=True)),
                ('CMB', models.IntegerField(null=True, blank=True)),
                ('CMD', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PathfinderWeapon',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('lightWeapon', models.BooleanField(default=True)),
                ('damage', models.CharField(blank=True, max_length=100)),
                ('crit', models.IntegerField(null=True, blank=True)),
                ('critMulti', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
