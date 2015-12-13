# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_amulet_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

#Amulet primaries
#==============================================================================
#==============================================================================
	dmg = Affix(slot='Amulets',
		affix='dmg',
		is_primary=True,
		desc='<span>+60 - 80</span> -- <span>120 - 160</span> Damage',
		ancient='<span>+88 - 105</span> -- <span>168 - 210</span> Damage')
	dmg.save()

	mainStat = Affix(slot='Amulets',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	dext = Affix(slot='Amulets',
		affix='dext',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000</span> Dexterity')
	dext.save()

	inte = Affix(slot='Amulets',
		affix='inte',
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	stre = Affix(slot='Amulets',
		affix='stre',
		is_primary=True,
		desc='<span>+626 - 750</span> Strength',
		ancient='<span>+825 - 1,000</span> Strength')
	stre.save()

	vita = Affix(slot='Amulets',
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	eleDmg = Affix(slot='Amulets',
		affix='eleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy</span></div>')
	eleDmg.save()

	physDmg = Affix(slot='Amulets',
		affix='physDmg',
		is_primary=True,
		desc='Physical skills do <span>15 - 20%</span> more damage')
	physDmg.save()

	coldDmg = Affix(slot='Amulets',
		affix='coldDmg',
		is_primary=True,
		desc='Cold skills do <span>15 - 20%</span> more damage')
	coldDmg.save()

	fireDmg = Affix(slot='Amulets',
		affix='fireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	fireDmg.save()

	lightDmg = Affix(slot='Amulets',
		affix='lightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	lightDmg.save()

	poisDmg = Affix(slot='Amulets',
		affix='poisDmg',
		is_primary=True,
		desc='Poison skills do <span>15 - 20%</span> more damage')
	poisDmg.save()

	arcaneDmg = Affix(slot='Amulets',
		affix='arcaneDmg',
		is_primary=True,
		desc='Arcane skills do <span>15 - 20%</span> more damage')
	arcaneDmg.save()

	holyDmg = Affix(slot='Amulets',
		affix='holyDmg',
		is_primary=True,
		desc='Holy skills do <span>15 - 20%</span> more damage')
	holyDmg.save()

	ias = Affix(slot='Amulets',
		affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	chc = Affix(slot='Amulets',
		affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	chd = Affix(slot='Amulets',
		affix='chd',
		is_primary=True,
		desc='<span>+51.0 - 100.0%</span> Critical Hit Damage')
	chd.save()

	cdr = Affix(slot='Amulets',
		affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	life = Affix(slot='Amulets',
		affix='life',
		is_primary=True,
		desc='<span>+14 - 18%</span> Life')
	life.save()

	armor = Affix(slot='Amulets',
		affix='armor',
		is_primary=True,
		desc='<span>+559 - 595</span> Armor',
		ancient='<span>+654 - 775</span> Armor')
	armor.save()

	allRes = Affix(slot='Amulets',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	lps = Affix(slot='Amulets',
		affix='lps',
		is_primary=True,
		desc='<span>+6,448 - 7,678</span> Life Regeneration per Second',
		ancient='<span>+8,845 - 10,000</span> Life Regeneration per Second')
	lps.save()

	lph = Affix(slot='Amulets',
		affix='lph',
		is_primary=True,
		desc='<span>+15,474 - 18,429</span> Life per Hit',
		ancient='<span>+20,271 - 23,950</span> Life per Hit')
	lph.save()

	rcr = Affix(slot='Amulets',
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	sockets = Affix(slot='Amulets',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Amulet secondaries
#==============================================================================
#==============================================================================
	eleRes = Affix(slot='Amulets',
		affix='eleRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Resistance to {<span class="vary">One Element</span>}<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane</span></div>',
		ancient='<span>+176 - 210</span> Resistance to {<span class="vary">One Element</span>}<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane</span></div>')
	eleRes.save()

	physRes = Affix(slot='Amulets',
		affix='physRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Physical Resistance',
		ancient='<span>+176 - 210</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(slot='Amulets',
		affix='coldRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Cold Resistance',
		ancient='<span>+176 - 210</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(slot='Amulets',
		affix='fireRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Fire Resistance',
		ancient='<span>+176 - 210</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(slot='Amulets',
		affix='lightRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Lightning Resistance',
		ancient='<span>+176 - 210</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(slot='Amulets',
		affix='poisRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Poison Resistance',
		ancient='<span>+176 - 210</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(slot='Amulets',
		affix='arcaneRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Arcane Resistance',
		ancient='<span>+176 - 210</span> Arcane Resistance')
	arcaneRes.save()


	reducedRangedDmg = Affix(slot='Amulets',
		affix='reducedRangedDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Ranged Damage Reduction')
	reducedRangedDmg.save()

	reducedMeleeDmg = Affix(slot='Amulets',
		affix='reducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	reducedMeleeDmg.save()


	blindChance = Affix(slot='Amulets',
		affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 5.1%</span> chance to Blind on Hit')
	blindChance.save()


	ccReduction = Affix(slot='Amulets',
		affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	thorns = Affix(slot='Amulets',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()

	itemHealing = Affix(slot='Amulets',
		affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29.713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	lpk = Affix(slot='Amulets',
		affix='lpk',
		is_primary=False,
		desc='<span>+6,428 - 8,914</span> Life per Kill',
		ancient='<span>+9,805 - 11,590</span> Life per Kill')
	lpk.save()


	killExp = Affix(slot='Amulets',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(slot='Amulets',
		affix='extraGold',
		is_primary=False,
		desc='<span>+71 - 80%</span> Extra Gold from Monsters')
	extraGold.save()

#Eye of Elitch
	eyeReducedRangedDmg = Affix(slot='Amulets',
		affix='eyeReducedRangedDmg',
		is_primary=False,
		desc='Reduces damage from ranged attacks by <span>27.7 - 32.9%</span>.')
	eyeReducedRangedDmg.save()

#Holy Beacon
	holySpiritRegen = Affix(slot='Amulets',
		affix='holySpiritRegen',
		desc='<span>+2.2 - 3.0</span> Spirit Regeneration per Second',
		is_primary=True)
	holySpiritRegen.save()

#Kymbo's Gold
	kymbosExtraGold = Affix(slot='Amulets',
		affix='kymbosExtraGold',
		desc='<span>+75 - 100%</span> Extra Gold from Monsters',
		is_primary=False)
	kymbosExtraGold.save()

#Moonlight Ward
	moonlightArcaneDmg = Affix(slot='Amulets',
		affix='moonlightArcaneDmg',
		desc='Arcane skills do <span>+20 - 25%</span> more damage.',
		is_primary=True)
	moonlightArcaneDmg.save()

#Rondal's Locket
	rondalsItemPickup = Affix(slot='Amulets',
		affix='rondalsItemPickup',
		desc='<span>+4 - 6</span> Yards to Gold and Globe Pickup',
		is_primary=False)
	rondalsItemPickup.save()

#The Flavor of Time
	flavorMovementSpeed = Affix(slot='Amulets',
		affix='flavorMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	flavorMovementSpeed.save()


def load_ring_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

#Ring Primaries
#==============================================================================
#==============================================================================
	dmg = Affix(slot='Rings',
		affix='dmg',
		is_primary=True,
		desc='<span>+60 - 80</span> -- <span>120 - 160</span> Damage',
		ancient='<span>+88 - 105</span> -- <span>168 - 210</span> Damage')
	dmg.save()

	mainStat = Affix(slot='Rings',
		affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	dext = Affix(slot='Rings',
		affix='dext',
		is_primary=True,
		desc='<span>+416 - 500</span> Dexterity',
		ancient='<span>+550 - 650</span> Dexterity')
	dext.save()

	inte = Affix(slot='Rings',
		affix='inte',
		is_primary=True,
		desc='<span>+416 - 500</span> Intelligence',
		ancient='<span>+550 - 650</span> Intelligence')
	inte.save()

	stre = Affix(slot='Rings',
		affix='stre',
		is_primary=True,
		desc='<span>+416 - 500</span> Strength',
		ancient='<span>+550 - 650</span> Strength')
	stre.save()

	vita = Affix(slot='Rings',
		affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	ias = Affix(slot='Rings',
		affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	chc = Affix(slot='Rings',
		affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()

	chd = Affix(slot='Rings',
		affix='chd',
		is_primary=True,
		desc='<span>+26.0 - 50.0%</span> Critical Hit Damage')
	chd.save()

	cdr = Affix(slot='Rings',
		affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	areaDmg = Affix(slot='Rings',
		affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20%</span> Area Damage')
	areaDmg.save()

	life = Affix(slot='Rings',
		affix='life',
		is_primary=True,
		desc='<span>+10 - 15%</span> Life')
	life.save()

	armor = Affix(slot='Rings',
		affix='armor',
		is_primary=True,
		desc='<span>+373 - 397</span> Armor',
		ancient='<span>+436 - 516</span> Armor')
	armor.save()

	allRes = Affix(slot='Rings',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	lps = Affix(slot='Rings',
		affix='lps',
		is_primary=True,
		desc='<span>+6,448 - 7,678</span> Life Regeneration per Second',
		ancient='<span>+8,845 - 10,000</span> Life Regeneration per Second')
	lps.save()

	lph = Affix(slot='Rings',
		affix='lph',
		is_primary=True,
		desc='<span>+7,737 - 9,214</span> Life per Hit',
		ancient='<span>+10,135 - 11,975</span> Life per Hit')
	lph.save()

	rcr = Affix(slot='Rings',
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	sockets = Affix(slot='Rings',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Ring secondaries
#==============================================================================
#==============================================================================
	eleRes = Affix(slot='Rings',
		affix='eleRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Resistance to {<span class="vary">One Element</span>}<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane</span></div>',
		ancient='<span>+176 - 210</span> Resistance to {<span class="vary">One Element</span>}<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane</span></div>')
	eleRes.save()

	physRes = Affix(slot='Rings',
		affix='physRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Physical Resistance',
		ancient='<span>+176 - 210</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(slot='Rings',
		affix='coldRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Cold Resistance',
		ancient='<span>+176 - 210</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(slot='Rings',
		affix='fireRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Fire Resistance',
		ancient='<span>+176 - 210</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(slot='Rings',
		affix='lightRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Lightning Resistance',
		ancient='<span>+176 - 210</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(slot='Rings',
		affix='poisRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Poison Resistance',
		ancient='<span>+176 - 210</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(slot='Rings',
		affix='arcaneRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Arcane Resistance',
		ancient='<span>+176 - 210</span> Arcane Resistance')
	arcaneRes.save()


	ccReduction = Affix(slot='Rings',
		affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	thorns = Affix(slot='Rings',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,220 - 2,600</span> damage')
	thorns.save()

	itemHealing = Affix(slot='Rings',
		affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29.713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	lpk = Affix(slot='Rings',
		affix='lpk',
		is_primary=False,
		desc='<span>+6,428 - 8,914</span> Life per Kill',
		ancient='<span>+9,805 - 11,590</span> Life per Kill')
	lpk.save()


	killExp = Affix(slot='Rings',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(slot='Rings',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

#Hellfire Ring (70)
	hellfireBonusExp = Affix(slot='Rings',
		affix='hellfireBonusExp',
		is_primary=False,
		desc='Increases Bonus Experience by <span class="silver">45%</span>')
	hellfireBonusExp.save()

#Justice Lantern
	justiceBlockChance = Affix(slot='Rings',
		affix='justiceBlockChance',
		is_primary=True,
		desc='<span class="silver">+12%</span> Chance to Block')
	justiceBlockChance.save()

	justiceCCReduction = Affix(slot='Rings',
		affix='justiceCCReduction',
		is_primary=False,
		desc='<span>+35 - 50%</span> Crowd Control Duration Reduction')
	justiceCCReduction.save()

#Leoric's Ring
	leoricsBonusExp = Affix(slot='Rings',
		affix='leoricsBonusExp',
		is_primary=False,
		desc='Increases Bonus Experience by <span>20 - 30%</span>')
	leoricsBonusExp.save()

#Manald Heal
	manaldMaxResource = Affix(slot='Rings',
		affix='manaldMaxResource',
		is_primary=False,
		desc='+Max {<span class="vary">Resource</span>}<div class="extra"><div class="extra-x">X</div><span>+10-12 Fury<br>+8-10 Wrath<br>+9-12 Discipline<br>+13-15 Spirit<br>+120-150 Mana<br>+10-14 Arcane Power</span></div>')
	manaldMaxResource.save()

#Nagelring
	nagelringMagicFind = Affix(slot='Rings',
		affix='nagelringMagicFind',
		is_primary=False,
		desc='<span>25 - 50%</span> Better Chance of Finding Magical Items')
	nagelringMagicFind.save()

#Obsidian Ring
	obsidianDurability = Affix(slot='Rings',
		affix='obsidianDurability',
		is_primary=False,
		desc='Ignores Durability Loss')
	obsidianDurability.save()

#Oculus Ring
	oculusEliteDmg = Affix(slot='Rings',
		affix='oculusEliteDmg',
		is_primary=True,
		desc='<span>+12.0 - 16.0%</span> Elite Damage Reduction')
	oculusEliteDmg.save()

#Pandemonium Loop
	pandemoniumFearChance = Affix(slot='Rings',
		affix='pandemoniumFearChance',
		is_primary=False,
		desc='<span>+10.0 - 15.0%</span> chance to Fear on Hit')
	pandemoniumFearChance.save()

#Rechel's Ring of Larceny
	rechelsFearChance = Affix(slot='Rings',
		affix='rechelsFearChance',
		is_primary=False,
		desc='<span>+1.0 - 5.1%</span> chance to Fear on Hit')
	rechelsFearChance.save()

#Stolen Ring
	stolenItemPickup = Affix(slot='Rings',
		affix='stolenItemPickup',
		is_primary=False,
		desc='<span>+1 - 2</span> Yards to Gold and Globe Pickup')
	stolenItemPickup.save()

#Stone of Jordan
	stoneEleDmg = Affix(slot='Rings',
		affix='stoneEleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy</span></div>')
	stoneEleDmg.save()

	stoneEliteDmg = Affix(slot='Rings',
		affix='stoneEliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>25.0 - 30.0%</span>')
	stoneEliteDmg.save()

	stoneMaxResource = Affix(slot='Rings',
		affix='stoneMaxResource',
		is_primary=False,
		desc='+Max {<span class="vary">Resource</span>}<div class="extra"><div class="extra-x">X</div><span>+10-12 Fury<br>+8-10 Wrath<br>+9-12 Discipline<br>+13-15 Spirit<br>+120-150 Mana<br>+10-14 Arcane Power</span></div>')
	stoneMaxResource.save()

#Unity
	unityEliteDmg = Affix(slot='Rings',
		affix='unityEliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>12.0 - 15.0%</span>')
	unityEliteDmg.save()


def load_ancient_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0004_offhand_affixes'),
    ]

    operations = [
        migrations.RunPython(load_amulet_affixes),
        migrations.RunPython(load_ring_affixes),
        migrations.RunPython(load_ancient_affixes)
    ]