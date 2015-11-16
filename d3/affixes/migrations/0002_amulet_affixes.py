# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_amulet_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "AmuletAffix")

	dmg = Affix(affix='dmg',
		is_primary=True,
		desc='<span>+60 - 80</span> -- <span>120 - 160</span> Damage',
		ancient='<span>+88 - 105</span> -- <span>168 - 210</span> Damage')
	dmg.save()

	mainStat = Affix(affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	dext = Affix(affix='dext',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000</span> Dexterity')
	dext.save()

	inte = Affix(affix='inte',
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	stre = Affix(affix='stre',
		is_primary=True,
		desc='<span>+626 - 750</span> Strength',
		ancient='<span>+825 - 1,000</span> Strength')
	stre.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	eleDmg = Affix(affix='eleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy')
	eleDmg.save()

	physDmg = Affix(affix='physDmg',
		is_primary=True,
		desc='Physical skills do <span>15 - 20%</span> more damage')
	physDmg.save()

	coldDmg = Affix(affix='coldDmg',
		is_primary=True,
		desc='Cold skills do <span>15 - 20%</span> more damage')
	coldDmg.save()

	fireDmg = Affix(affix='fireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	fireDmg.save()

	lightDmg = Affix(affix='lightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	lightDmg.save()

	poisDmg = Affix(affix='poisDmg',
		is_primary=True,
		desc='Poison skills do <span>15 - 20%</span> more damage')
	poisDmg.save()

	arcaneDmg = Affix(affix='arcaneDmg',
		is_primary=True,
		desc='Arcane skills do <span>15 - 20%</span> more damage')
	arcaneDmg.save()

	holyDmg = Affix(affix='holyDmg',
		is_primary=True,
		desc='Holy skills do <span>15 - 20%</span> more damage')
	holyDmg.save()

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
		desc='<span>+51.0 - 100.0%</span> Critical Hit Damage')
	chd.save()

	cdr = Affix(affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	life = Affix(affix='life',
		is_primary=True,
		desc='<span>+14 - 18%</span> Life')
	life.save()

	armor = Affix(affix='armor',
		is_primary=True,
		desc='<span>+559 - 595</span> Armor',
		ancient='<span>+654 - 775</span> Armor')
	armor.save()

	allRes = Affix(affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	lps = Affix(affix='lps',
		is_primary=True,
		desc='<span>+6,448 - 7,678</span> Life Regeneration per Second',
		ancient='<span>+8,845 - 10,000</span> Life Regeneration per Second')
	lps.save()

	lph = Affix(affix='lph',
		is_primary=True,
		desc='<span>+15,474 - 18,429</span> Life per Hit',
		ancient='<span>+20,271 - 23,950</span> Life per Hit')
	lph.save()

	rcr = Affix(affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	sockets = Affix(affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Secondaries
#==============================================================================
#==============================================================================
	eleRes = Affix(affix='eleRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Resistance to {<span class="vary">One Element</span>}',
		ancient='<span>+176 - 210</span> Resistance to {<span class="vary">One Element</span>}',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane')
	eleRes.save()

	physRes = Affix(affix='physRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Physical Resistance',
		ancient='<span>+176 - 210</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(affix='coldRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Cold Resistance',
		ancient='<span>+176 - 210</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(affix='fireRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Fire Resistance',
		ancient='<span>+176 - 210</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(affix='lightRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Lightning Resistance',
		ancient='<span>+176 - 210</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(affix='poisRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Poison Resistance',
		ancient='<span>+176 - 210</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(affix='arcaneRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Arcane Resistance',
		ancient='<span>+176 - 210</span> Arcane Resistance')
	arcaneRes.save()


	reducedRangedDmg = Affix(affix='reducedRangedDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Ranged Damage Reduction')
	reducedRangedDmg.save()

	reducedMeleeDmg = Affix(affix='reducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	reducedMeleeDmg.save()


	blindChance = Affix(affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 5.1%</span> chance to Blind on Hit')
	blindChance.save()


	ccReduction = Affix(affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	thorns = Affix(affix='thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()

	itemHealing = Affix(affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29.713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	lpk = Affix(affix='lpk',
		is_primary=False,
		desc='<span>+6,428 - 8,914</span> Life per Kill',
		ancient='<span>+9,805 - 11,590</span> Life per Kill')
	lpk.save()


	killExp = Affix(affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(affix='extraGold',
		is_primary=False,
		desc='<span>+71 - 80%</span> Extra Gold from Monsters')
	extraGold.save()

#Eye of Elitch
	eyeReducedRangedDmg = Affix(affix='eyeReducedRangedDmg',
		is_primary=False,
		desc='Reduces damage from ranged attacks by <span>27.7 - 32.9%</span>.')
	eyeReducedRangedDmg.save()

#Holy Beacon
	holySpiritRegen = Affix(affix='holySpiritRegen',
		desc='<span>+2.2 - 3.0</span> Spirit Regeneration per Second',
		is_primary=True)
	holySpiritRegen.save()

#Kymbo's Gold
	kymbosExtraGold = Affix(affix='kymbosExtraGold',
		desc='<span>+75 - 100%</span> Extra Gold from Monsters',
		is_primary=False)
	kymbosExtraGold.save()

#Moonlight Ward
	moonlightArcaneDmg = Affix(affix='moonlightArcaneDmg',
		desc='Arcane skills do <span>+20 - 25%</span> more damage.',
		is_primary=True)
	moonlightArcaneDmg.save()

#Rondal's Locket
	rondalsItemPickup = Affix(affix='rondalsItemPickup',
		desc='<span>+4 - 6</span> Yards to Gold and Globe Pickup',
		is_primary=False)
	rondalsItemPickup.save()

#The Flavor of Time
	flavorMovementSpeed = Affix(affix='flavorMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	flavorMovementSpeed.save()

	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()
		else:
			pass


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(load_amulet_affixes),
    ]