# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0006_armor_affixes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('name_slug', models.SlugField()),
                ('owner', models.TextField()),
                ('owner_slug', models.SlugField()),
                ('patch', models.TextField()),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Item Sets',
            },
        ),
        migrations.CreateModel(
            name='SetEffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('effect', models.TextField()),
                ('pieces', models.TextField()),
                ('notes', models.TextField(blank=True)),
                ('itemSet', models.ForeignKey(related_name='effects', to='itemsets.ItemSet')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Set Effects',
            },
        ),
        migrations.CreateModel(
            name='SetPiece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('name_slug', models.SlugField(blank=True)),
                ('pic', models.ImageField(upload_to=b'')),
                ('category', models.TextField(blank=True)),
                ('random_affixes', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('affixes', models.ManyToManyField(to='affixes.Affix', blank=True)),
                ('itemSet', models.ForeignKey(related_name='pieces', to='itemsets.ItemSet')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Set Pieces',
            },
        ),
    ]
