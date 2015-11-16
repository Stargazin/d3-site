# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_helmet_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "HelmetAffix")


	mainStat = Affix(affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	chc = Affix(affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()
	
	allRes = Affix(affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	sockets = Affix(affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()


#Andariels Visage
	andarielsIAS = Affix(affix='andarielsIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	andarielsIAS.save()

	andarielsFireDmgTaken = Affix(affix='andarielsFireDmgTaken',
		is_primary=True,
		desc='Take <span>+5 - 10%</span> more Fire Damage')
	andarielsFireDmgTaken.save()

	andarielsEleDmg = Affix(affix='andarielsEleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy')
	andarielsEleDmg.save()

	andarielsPoisRes = Affix(affix='andarielsPoisRes',
		is_primary=False,
		desc='<span>+150 - 200</span> Poison Resistance')
	andarielsPoisRes.save()

#Blind Faith
	blindBlindchance = Affix(affix='blindBlindchance',
		is_primary=False,
		desc='<span>+20.0 - 40.0%</span> chance to Blind on Hit')
	blindBlindchance.save()

#Mempo of Twilight
	mempoIAS = Affix(affix='mempoIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	mempoIAS.save()

#The Helm of Rule
	helmBlockChance = Affix(affix='helmBlockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	helmBlockChance.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0008_shield_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_helmet_affixes)
    ]
