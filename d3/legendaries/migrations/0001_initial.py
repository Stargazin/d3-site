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
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
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
            name='Belt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'440 - 506')),
                ('affixes', models.ManyToManyField(to='affixes.BeltAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Boots',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'513 - 590')),
                ('affixes', models.ManyToManyField(to='affixes.BootsAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bracers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'366 - 421')),
                ('affixes', models.ManyToManyField(to='affixes.BracersAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChestArmor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'660 - 759')),
                ('affixes', models.ManyToManyField(to='affixes.ChestArmorAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cloak',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'660 - 759')),
                ('owner', models.TextField(default=b'Demon Hunter')),
                ('affixes', models.ManyToManyField(to='affixes.CloakAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CrusaderShield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('block_chance', models.TextField(blank=True)),
                ('block_amount', models.TextField(default=b'17000-19000 -- 21000-25000')),
                ('ancient_block_amount', models.TextField(default=b'20900-25000 -- 27500-32800')),
                ('base_armor', models.TextField(default=b'1,980 - 2,277')),
                ('owner', models.TextField(default=b'Crusader')),
                ('affixes', models.ManyToManyField(to='affixes.CrusaderShieldAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gloves',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'513 - 590')),
                ('affixes', models.ManyToManyField(to='affixes.GlovesAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Helmet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'660 - 759')),
                ('affixes', models.ManyToManyField(to='affixes.HelmetAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MightyBelt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'516 - 675')),
                ('owner', models.TextField(default=b'Barbarian')),
                ('affixes', models.ManyToManyField(to='affixes.MightyBeltAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mojo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('owner', models.TextField(default=b'Witch Doctor')),
                ('affixes', models.ManyToManyField(to='affixes.MojoAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pants',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'660 - 759')),
                ('affixes', models.ManyToManyField(to='affixes.PantsAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('owner', models.TextField(default=b'Demon Hunter')),
                ('affixes', models.ManyToManyField(to='affixes.QuiverAffix', blank=True)),
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
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
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
            name='Shield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('block_chance', models.TextField(blank=True)),
                ('block_amount', models.TextField(default=b'17000-19000 -- 21000-25000')),
                ('ancient_block_amount', models.TextField(default=b'20900-25000 -- 27500-32800')),
                ('base_armor', models.TextField(default=b'1,760 - 2,024')),
                ('affixes', models.ManyToManyField(to='affixes.ShieldAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shoulders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'586 - 674')),
                ('affixes', models.ManyToManyField(to='affixes.ShouldersAffix', blank=True)),
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
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('owner', models.TextField(default=b'Wizard')),
                ('affixes', models.ManyToManyField(to='affixes.SourceAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpiritStone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'660 - 759')),
                ('owner', models.TextField(default=b'Monk')),
                ('affixes', models.ManyToManyField(to='affixes.SpiritStoneAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoodooMask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'660 - 759')),
                ('owner', models.TextField(default=b'Witch Doctor')),
                ('affixes', models.ManyToManyField(to='affixes.VoodooMaskAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WizardHat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to=b'', blank=True)),
                ('unique', models.TextField(blank=True)),
                ('unique_is_primary', models.NullBooleanField(default=False)),
                ('unique2', models.TextField(blank=True)),
                ('unique2_is_primary', models.NullBooleanField(default=False)),
                ('unique3', models.TextField(blank=True)),
                ('unique3_is_primary', models.NullBooleanField(default=False)),
                ('random_primaries', models.CharField(max_length=1, blank=True)),
                ('random_secondaries', models.CharField(max_length=1, blank=True)),
                ('number_of_mats', models.CommaSeparatedIntegerField(max_length=32, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('base_armor', models.TextField(default=b'660 - 759')),
                ('owner', models.TextField(default=b'Wizard')),
                ('affixes', models.ManyToManyField(to='affixes.WizardHatAffix', blank=True)),
                ('mats', models.ManyToManyField(to='miscitems.Material', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
