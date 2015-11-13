# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscitems', '0003_crafting_mats'),
        ('affixes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amulet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField()),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField()),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField()),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('affixes', models.ManyToManyField(to='affixes.AmuletAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ring',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField()),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField()),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField()),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('affixes', models.ManyToManyField(to='affixes.RingAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField()),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField()),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField()),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('affixes', models.ManyToManyField(to='affixes.SourceAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
