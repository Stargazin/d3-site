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
            name='BeltAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Belt Affixes',
            },
        ),
        migrations.CreateModel(
            name='BootsAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Boots Affixes',
            },
        ),
        migrations.CreateModel(
            name='BracersAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Bracers Affixes',
            },
        ),
        migrations.CreateModel(
            name='ChestArmorAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Chest Armor Affixes',
            },
        ),
        migrations.CreateModel(
            name='CloakAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Cloak Affixes',
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
            name='GlovesAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Gloves Affixes',
            },
        ),
        migrations.CreateModel(
            name='HelmetAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Helmet Affixes',
            },
        ),
        migrations.CreateModel(
            name='MightyBeltAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Mighty Belt Affixes',
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
            name='PantsAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Pants Affixes',
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
            name='ShouldersAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Shoulders Affixes',
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
        migrations.CreateModel(
            name='SpiritStoneAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Spirit Stone Affixes',
            },
        ),
        migrations.CreateModel(
            name='VoodooMaskAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Voodoo Mask Affixes',
            },
        ),
        migrations.CreateModel(
            name='WizardHatAffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affix', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField()),
                ('desc', models.TextField()),
                ('ancient', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Wizard Hat Affixes',
            },
        ),
    ]
