# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_bracers_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "BracersAffix")


	mainStat = Affix(affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	eleDmg = Affix(affix='eleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy')
	eleDmg.save()

	chc = Affix(affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()

	lps = Affix(affix='lps',
		is_primary=True,
		desc='<span>+6,448 - 7,678</span> Life Regeneration per Second',
		ancient='<span>+8,445 - 10,000</span> Life Regeneration per Second')
	lps.save()


	itemPickup = Affix(affix='itemPickup',
		is_primary=False,
		desc='<span>+1 - 2</span> Yards to Gold and Globe Pickup')
	itemPickup.save()

	extraGold = Affix(affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	thorns = Affix(affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,200 - 2,600</span> damage')
	thorns.save()


#Lacuni Prowlers
	lacuniIAS = Affix(affix='lacuniIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	lacuniIAS.save()

	lacuniMovementSpeed = Affix(affix='lacuniMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	lacuniMovementSpeed.save()

#Slave Bonds
	slaveMovementSpeed = Affix(affix='slaveMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	slaveMovementSpeed.save()

	slaveLPK = Affix(affix='slaveLPK',
		is_primary=False,
		desc='<span>+6,428 - 8,914</span> Life per Kill',
		ancient='<span>+9,805 - 11,590</span> Life per Kill')
	slaveLPK.save()

#Steady Strikers
	steadyIAS = Affix(affix='steadyIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	steadyIAS.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0015_cloak_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_bracers_affixes)
    ]
