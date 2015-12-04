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
                ('category', models.TextField(default=b'Legendary Gem')),
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
                ('rarity', models.TextField(default=b'L')),
                ('stack_amount', models.TextField(default=b'5000')),
                ('category', models.TextField(blank=True)),
                ('category_slug', models.SlugField(blank=True)),
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
                ('category', models.TextField(default=b'Legendary Potion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
