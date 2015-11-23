# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(blank=True)),
                ('name_slug', models.SlugField(blank=True)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('rank_unique', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(blank=True)),
                ('name_slug', models.SlugField(blank=True)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('rarity', models.TextField(blank=True)),
                ('stack_amount', models.TextField(default=b'5000')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Potion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(blank=True)),
                ('name_slug', models.SlugField(blank=True)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
