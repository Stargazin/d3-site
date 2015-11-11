# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscitems', '0003_crafting_mats'),
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
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
        migrations.AddField(
            model_name='amulet',
            name='affixes',
            field=models.ManyToManyField(to='legendaryitems.AmuletAffix', blank=True),
        ),
        migrations.AddField(
            model_name='amulet',
            name='mats',
            field=models.ManyToManyField(to='miscitems.Material', blank=True),
        ),
    ]
