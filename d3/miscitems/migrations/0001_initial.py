# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('rarity', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('stack_amount', models.IntegerField(default=5000)),
            ],
        ),
    ]
