# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoryAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot', models.TextField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('affix', models.TextField()),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Accessory Affixes',
            },
        ),
        migrations.CreateModel(
            name='ArmorAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot', models.TextField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('affix', models.TextField()),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Armor Affixes',
            },
        ),
        migrations.CreateModel(
            name='WeaponAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot', models.TextField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('affix', models.TextField()),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Weapon Affixes',
            },
        ),
    ]
