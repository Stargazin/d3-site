# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_shield_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "ShieldAffix")


	mainStat = Affix(affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span>Main Stat</span>}',
		ancient='<span>+825 - 1,000</span> {<span>Main Stat</span>}')
	mainStat.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	allRes = Affix(affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	blockChance = Affix(affix='blockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	blockChance.save()


	thorns = Affix(affix='thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0007_crusader_shield_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_shield_affixes)
    ]
