# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_gloves_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "GlovesAffix")


	mainStat = Affix(affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	ias = Affix(affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	chc = Affix(affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	chd = Affix(affix='chd',
		is_primary=True,
		desc='<span>+26.0 - 50.0%</span> Critical Hit Damage')
	chd.save()

	lph = Affix(affix='lph',
		is_primary=True,
		desc='<span>+7,737 - 9,214</span> Life per Hit',
		ancient='<span>+10,135 - 11,975</span> Life per Hit')
	lph.save()


#Frostburn
	frostburnColdDmg = Affix(affix='frostburnColdDmg',
		is_primary=True,
		desc='Cold skills do <span>10 - 15%</span> more damage')
	frostburnColdDmg.save()

#Magefist
	magefistFireDmg = Affix(affix='magefistFireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	magefistFireDmg.save()

#Stone Gauntlets
	stoneImmobilizeChance = Affix(affix='stoneImmobilizeChance',
		is_primary=False,
		desc='<span>+10.0 - 20.0%</span> chance to Immobilize on Hit')
	stoneImmobilizeChance.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0016_bracers_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_gloves_affixes)
    ]
