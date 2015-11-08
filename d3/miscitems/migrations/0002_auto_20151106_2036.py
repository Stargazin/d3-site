# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscitems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
