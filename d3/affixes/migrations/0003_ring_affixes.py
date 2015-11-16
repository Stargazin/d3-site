# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_ring_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "RingAffix")

	dmg = Affix(affix='dmg',
		is_primary=True,
		desc='<span>+60 - 80</span> -- <span>120 - 160</span> Damage',
		ancient='<span>+88 - 105</span> -- <span>168 - 210</span> Damage')
	dmg.save()

	mainStat = Affix(affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	dext = Affix(affix='dext',
		is_primary=True,
		desc='<span>+416 - 500</span> Dexterity',
		ancient='<span>+550 - 650</span> Dexterity')
	dext.save()

	inte = Affix(affix='inte',
		is_primary=True,
		desc='<span>+416 - 500</span> Intelligence',
		ancient='<span>+550 - 650</span> Intelligence')
	inte.save()

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

	ias = Affix(affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	chc = Affix(affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()

	chd = Affix(affix='chd',
		is_primary=True,
		desc='<span>+26.0 - 50.0%</span> Critical Hit Damage')
	chd.save()

	cdr = Affix(affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	areaDmg = Affix(affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20%</span> Area Damage')
	areaDmg.save()

	life = Affix(affix='life',
		is_primary=True,
		desc='<span>+10 - 15%</span> Life')
	life.save()

	armor = Affix(affix='armor',
		is_primary=True,
		desc='<span>+373 - 397</span> Armor',
		ancient='<span>+436 - 516</span> Armor')
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
		desc='<span>+7,737 - 9,214</span> Life per Hit',
		ancient='<span>+10,135 - 11,975</span> Life per Hit')
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


	ccReduction = Affix(affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	thorns = Affix(affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,220 - 2,600</span> damage')
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
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

#Hellfire Ring (70)
	hellfireBonusExp = Affix(affix='hellfireBonusExp',
		is_primary=False,
		desc='Increases Bonus Experience by <span class="silver">45%</span>')
	hellfireBonusExp.save()

#Justice Lantern
	justiceBlockChance = Affix(affix='justiceBlockChance',
		is_primary=True,
		desc='<span class="silver">+12%</span> Chance to Block')
	justiceBlockChance.save()

	justiceCCReduction = Affix(affix='justiceCCReduction',
		is_primary=False,
		desc='<span>+35 - 50%</span> Crowd Control Duration Reduction')
	justiceCCReduction.save()

#Leoric's Ring
	leoricsBonusExp = Affix(affix='leoricsBonusExp',
		is_primary=False,
		desc='Increases Bonus Experience by <span>20 - 30%</span>')
	leoricsBonusExp.save()

#Manald Heal
	manaldMaxResource = Affix(affix='manaldMaxResource',
		is_primary=False,
		desc='+Max {<span class="vary">Resource</span>}',
		notes='Fury<br>Wrath<br>Discipline<br>Spirit<br>Mana<br>Arcane Power')
	manaldMaxResource.save()

#Obsidian Ring
	obsidianDurability = Affix(affix='obsidianDurability',
		is_primary=False,
		desc='Ignores Durability Loss')
	obsidianDurability.save()

#Oculus Ring
	oculusEliteDmg = Affix(affix='oculusEliteDmg',
		is_primary=True,
		desc='<span>+12.0 - 16.0%</span> Elite Damage Reduction')
	oculusEliteDmg.save()

#Pandemonium Loop
	pandemoniumFearChance = Affix(affix='pandemoniumFearChance',
		is_primary=False,
		desc='<span>+10.0 - 15.0%</span> chance to Fear on Hit')
	pandemoniumFearChance.save()

#Rechel's Ring of Larceny
	rechelsFearChance = Affix(affix='rechelsFearChance',
		is_primary=False,
		desc='<span>+1.0 - 5.1%</span> chance to Fear on Hit')
	rechelsFearChance.save()

#Stolen Ring
	stolenItemPickup = Affix(affix='stolenItemPickup',
		is_primary=False,
		desc='<span>+1 - 2</span> Yards to Gold and Globe Pickup')
	stolenItemPickup.save()

#Stone of Jordan
	stoneEleDmg = Affix(affix='stoneEleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy')
	stoneEleDmg.save()

	stoneEliteDmg = Affix(affix='stoneEliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>25.0 - 30.0%</span>')
	stoneEliteDmg.save()

	stoneMaxResource = Affix(affix='stoneMaxResource',
		is_primary=False,
		desc='+Max {<span class="vary">Resource</span>}',
		notes='Fury<br>Wrath<br>Discipline<br>Spirit<br>Mana<br>Arcane Power')
	stoneMaxResource.save()

#Unity
	unityEliteDmg = Affix(affix='unityEliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>12.0 - 15.0%</span>')
	unityEliteDmg.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()
		else:
			pass


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0002_amulet_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_ring_affixes)
    ]
