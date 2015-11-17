# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_mighty_belt_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "MightyBeltAffix")


	stre = Affix(affix='stre',
		is_primary=True,
		desc='<span>+416 - 500</span> Strength',
		ancient='<span>+550 - 650</span> Strength')
	stre.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	allRes = Affix(affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()


	maxFury = Affix(affix='maxFury',
		is_primary=False,
		desc='<span>+10 - 12</span> Max Fury')
	maxFury.save()


#Girdle of Giants
	girdleIAS = Affix(affix='girdleIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	girdleIAS.save()

#Kotuur's Brace
	kotuursBlockChance = Affix(affix='kotuursBlockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	kotuursBlockChance.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0018_belt_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_mighty_belt_affixes)
    ]
