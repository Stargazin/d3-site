# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affix',
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
                'verbose_name_plural': 'Affixes',
            },
        ),
    ]
