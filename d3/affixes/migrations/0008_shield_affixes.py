# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_shield_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "ShieldAffix")


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


#Lidless Wall
	lidlessEleDmg = Affix(affix='lidlessEleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy')
	lidlessEleDmg.save()

	lidlessMaxResource = Affix(affix='lidlessMaxResource',
		is_primary=False,
		desc='Increase Max {<span class="vary">Resource</span>}',
		notes='Fury<br>Wrath<br>Discipline<br>Spirit<br>Mana<br>Arcane Power')
	lidlessMaxResource.save()

#Storm Shield
	stormReducedMeleeDmg = Affix(affix='stormReducedMeleeDmg',
		is_primary=False,
		desc='Reduces damage from melee attacks by <span>25.0 - 30.0%</span>')
	stormReducedMeleeDmg.save()


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
