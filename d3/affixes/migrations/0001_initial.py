# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmuletAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Amulet Affixes',
            },
        ),
        migrations.CreateModel(
            name='CrusaderShieldAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Crusader Shield Affixes',
            },
        ),
        migrations.CreateModel(
            name='MojoAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Mojo Affixes',
            },
        ),
        migrations.CreateModel(
            name='QuiverAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Quiver Affixes',
            },
        ),
        migrations.CreateModel(
            name='RingAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Ring Affixes',
            },
        ),
        migrations.CreateModel(
            name='ShieldAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Shield Affixes',
            },
        ),
        migrations.CreateModel(
            name='SourceAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Source Affixes',
            },
        ),
    ]
