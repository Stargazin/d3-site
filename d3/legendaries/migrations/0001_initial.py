# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscitems', '0001_initial'),
        ('affixes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('name_slug', models.SlugField(blank=True)),
                ('pic', models.ImageField(upload_to=b'')),
                ('slot', models.TextField(blank=True)),
                ('slot_slug', models.SlugField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('category_slug', models.SlugField(blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.TextField(blank=True)),
                ('random_secondaries', models.TextField(blank=True)),
                ('owner', models.TextField(blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('group', models.TextField(default=b'accessory')),
                ('affixes', models.ManyToManyField(to='affixes.Affix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Accessories',
            },
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('name_slug', models.SlugField(blank=True)),
                ('pic', models.ImageField(upload_to=b'')),
                ('slot', models.TextField(blank=True)),
                ('slot_slug', models.SlugField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('category_slug', models.SlugField(blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.TextField(blank=True)),
                ('random_secondaries', models.TextField(blank=True)),
                ('owner', models.TextField(blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('inherent', models.TextField(blank=True)),
                ('group', models.TextField(default=b'armor')),
                ('affixes', models.ManyToManyField(to='affixes.Affix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Armor',
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('name_slug', models.SlugField(blank=True)),
                ('pic', models.ImageField(upload_to=b'')),
                ('slot', models.TextField(blank=True)),
                ('slot_slug', models.SlugField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('category_slug', models.SlugField(blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.TextField(blank=True)),
                ('random_secondaries', models.TextField(blank=True)),
                ('owner', models.TextField(blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('inherent', models.TextField(blank=True)),
                ('group', models.TextField(default=b'weapon')),
                ('affixes', models.ManyToManyField(to='affixes.Affix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
