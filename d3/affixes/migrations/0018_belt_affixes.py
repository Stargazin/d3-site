# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_belt_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "BeltAffix")


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

	allRes = Affix(affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	rcr = Affix(affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()


	itemPickup = Affix(affix='itemPickup',
		is_primary=False,
		desc='<span>+1 - 2</span> Yards to Gold and Globe Pickup')
	itemPickup.save()

	extraGold = Affix(affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	durability = Affix(affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

#Belt of the Trove
	troveReducedMeleeDmg = Affix(affix='troveReducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	troveReducedMeleeDmg.save()

#Fleeting Strap
	fleetingIAS = Affix(affix='fleetingIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	fleetingIAS.save()

#Hellcat Waistguard
	hellcatIAS = Affix(affix='hellcatIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	hellcatIAS.save()

#Saffron Wrap
	saffronCCReduction = Affix(affix='saffronCCReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	saffronCCReduction.save()

#String of Ears
	stringReducedMeleeDmg = Affix(affix='stringReducedMeleeDmg',
		is_primary=False,
		desc='<span>+25.0 - 30.0%</span> Melee Damage Reduction')
	stringReducedMeleeDmg.save()

#The Witching Hour
	witchingIAS = Affix(affix='witchingIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	witchingIAS.save()

	witchingCHD = Affix(affix='witchingCHD',
		is_primary=True,
		desc='<span>+26.0 - 50.0%</span> Critical Hit Damage')
	witchingCHD.save()

#Thundergod's Vigor
	thundergodsLightDmg = Affix(affix='thundergodsLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>10 - 15%</span> more damage')
	thundergodsLightDmg.save()

	thundergodsLightRes = Affix(affix='thundergodsLightRes',
		is_primary=False,
		desc='<span>+150 - 200</span> Lightning Resistance')
	thundergodsLightRes.save()

#Vigilante Belt
	vigilanteCDR = Affix(affix='vigilanteCDR',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	vigilanteCDR.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0017_gloves_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_belt_affixes)
    ]
