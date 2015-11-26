# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_helmet_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(category='Helmets',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	vita = Affix(category='Helmets',
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	chc = Affix(category='Helmets',
		affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()
	
	allRes = Affix(category='Helmets',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	sockets = Affix(category='Helmets',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Andariels Visage
	andarielsIAS = Affix(category='Helmets',
		affix='andarielsIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	andarielsIAS.save()

	andarielsFireDmgTaken = Affix(category='Helmets',
		affix='andarielsFireDmgTaken',
		is_primary=True,
		desc='Take <span>+5 - 10%</span> more Fire Damage')
	andarielsFireDmgTaken.save()

	andarielsEleDmg = Affix(category='Helmets',
		affix='andarielsEleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy')
	andarielsEleDmg.save()

	andarielsPoisRes = Affix(category='Helmets',
		affix='andarielsPoisRes',
		is_primary=False,
		desc='<span>+150 - 200</span> Poison Resistance')
	andarielsPoisRes.save()

#Blind Faith
	blindBlindchance = Affix(category='Helmets',
		affix='blindBlindchance',
		is_primary=False,
		desc='<span>+20.0 - 40.0%</span> chance to Blind on Hit')
	blindBlindchance.save()

#Mempo of Twilight
	mempoIAS = Affix(category='Helmets',
		affix='mempoIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	mempoIAS.save()

#The Helm of Rule
	helmBlockChance = Affix(category='Helmets',
		affix='helmBlockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	helmBlockChance.save()


def load_spirit_stone_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	dext = Affix(category='Spirit Stones',
		affix='dext',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000</span> Dexterity')
	dext.save()

	chc = Affix(category='Spirit Stones',
		affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()

	sockets = Affix(category='Spirit Stones',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	skillDmg = Affix(category='Spirit Stones',
		affix='skillDmg',
		is_primary=True,
		desc='Increases {<span class="vary">Skill Damage</span>} by <span>10 - 15%</span>',
		notes='Tempest Rush<br>Exploding Palm<br>Wave of Light<br>Lashing Tail Kick')
	skillDmg.save()

	ccReduction = Affix(category='Spirit Stones',
		affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	killExp = Affix(category='Spirit Stones',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

#The Eye of the Storm
	eyeLightDmg = Affix(category='Spirit Stones',
		affix='eyeLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 30%</span> more damage')
	eyeLightDmg.save()

#Tzo Krin's Gaze
	tzoWaveOfLight = Affix(category='Spirit Stones',
		affix='tzoWaveOfLight',
		is_primary=True,
		desc='Increase Wave of Light damage by <span>20 - 25%</span>')
	tzoWaveOfLight.save()


def load_voodoo_mask_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")


	inte = Affix(category='Voodoo Masks',
		affix='inte', 
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	chc = Affix(category='Voodoo Masks',
		affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()

	sockets = Affix(category='Voodoo Masks',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	maxMana = Affix(category='Voodoo Masks',
		affix='maxMana',
		is_primary=False,
		desc='<span>+120 - 150</span> Max Mana')
	maxMana.save()

	killExp = Affix(category='Voodoo Masks',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()


def load_wizard_hat_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	inte = Affix(category='Wizard Hats',
		affix='inte', 
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	apCrit = Affix(category='Wizard Hats',
		affix='apCrit',
		is_primary=True,
		desc='<span>+3 - 4</span> Arcane Power on Critical Hits')
	apCrit.save()

	sockets = Affix(category='Wizard Hats',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	maxAP = Affix(category='Wizard Hats',
		affix='maxAP',
		is_primary=False,
		desc='<span>+10 - 14</span> Max Arcane Power')
	maxAP.save()

#Storm Crow
	stormLightDmg = Affix(category='Wizard Hats',
		affix='stormLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	stormLightDmg.save()


def load_shoulders_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(slot='Shoulders',
		affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	vita = Affix(slot='Shoulders',
		affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	armor = Affix(slot='Shoulders',
		affix='armor',
		is_primary=True,
		desc='<span>+373 - 397</span> Armor',
		ancient='<span>+436 - 516</span> Armor')
	armor.save()

	itemHealing = Affix(slot='Shoulders',
		affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29,713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	extraGold = Affix(slot='Shoulders',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	profaneItemPickup = Affix(slot='Shoulders',
		affix='profaneItemPickup',
		is_primary=False,
		desc='<span>+4 - 6</span> Yards to Gold and Globe Pickup')
	profaneItemPickup.save()


def load_chest_armor_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(category='Chest Armors',
		affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	vita = Affix(category='Chest Armors',
		affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	allRes = Affix(category='Chest Armors',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	durability = Affix(category='Chest Armors',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

#CinderCoat
	cindercoatFireDmg = Affix(category='Chest Armors',
		affix='cindercoatFireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	cindercoatFireDmg.save()

#Goldskin
	goldskinExtraGold = Affix(category='Chest Armors',
		affix='goldskinExtraGold',
		is_primary=False,
		desc='<span>+100%</span> Extra Gold from Monsters')
	goldskinExtraGold.save()

#Tyrael's Might
	tyraelsDemonDmg = Affix(category='Chest Armors',
		affix='tyraelsDemonDmg',
		is_primary=False,
		desc='Increases damage against Demons by <span>10 - 20%</span>')
	tyraelsDemonDmg.save()


def load_cloak_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	dext = Affix(category='Cloaks',
		affix='dext',
		is_primary=True,
		desc='<span>+416 - 500</span> Dexterity',
		ancient='<span>+550 - 650</span> Dexterity')
	dext.save()

	vita = Affix(category='Cloaks',
		affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	armor = Affix(category='Cloaks',
		affix='armor',
		is_primary=True,
		desc='<span>+373 - 595</span> Armor',
		ancient='<span>+436 - 775</span> Armor')
	armor.save()

	sockets = Affix(category='Cloaks',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>3</span>)')
	sockets.save()


def load_bracers_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(slot='Bracers',
		affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	vita = Affix(slot='Bracers',
		affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	eleDmg = Affix(slot='Bracers',
		affix='eleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy')
	eleDmg.save()

	chc = Affix(slot='Bracers',
		affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()

	lps = Affix(slot='Bracers',
		affix='lps',
		is_primary=True,
		desc='<span>+6,448 - 7,678</span> Life Regeneration per Second',
		ancient='<span>+8,445 - 10,000</span> Life Regeneration per Second')
	lps.save()

	itemPickup = Affix(slot='Bracers',
		affix='itemPickup',
		is_primary=False,
		desc='<span>+1 - 2</span> Yards to Gold and Globe Pickup')
	itemPickup.save()

	extraGold = Affix(slot='Bracers',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	thorns = Affix(slot='Bracers',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,200 - 2,600</span> damage')
	thorns.save()

#Lacuni Prowlers
	lacuniIAS = Affix(slot='Bracers',
		affix='lacuniIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	lacuniIAS.save()

	lacuniMovementSpeed = Affix(slot='Bracers',
		affix='lacuniMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	lacuniMovementSpeed.save()

#Slave Bonds
	slaveMovementSpeed = Affix(slot='Bracers',
		affix='slaveMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	slaveMovementSpeed.save()

	slaveLPK = Affix(slot='Bracers',
		affix='slaveLPK',
		is_primary=False,
		desc='<span>+6,428 - 8,914</span> Life per Kill',
		ancient='<span>+9,805 - 11,590</span> Life per Kill')
	slaveLPK.save()

#Steady Strikers
	steadyIAS = Affix(slot='Bracers',
		affix='steadyIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	steadyIAS.save()


def load_gloves_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(slot='Gloves',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	ias = Affix(slot='Gloves',
		affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	chc = Affix(slot='Gloves',
		affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	chd = Affix(slot='Gloves',
		affix='chd',
		is_primary=True,
		desc='<span>+26.0 - 50.0%</span> Critical Hit Damage')
	chd.save()

	lph = Affix(slot='Gloves',
		affix='lph',
		is_primary=True,
		desc='<span>+7,737 - 9,214</span> Life per Hit',
		ancient='<span>+10,135 - 11,975</span> Life per Hit')
	lph.save()

#Frostburn
	frostburnColdDmg = Affix(slot='Gloves',
		affix='frostburnColdDmg',
		is_primary=True,
		desc='Cold skills do <span>10 - 15%</span> more damage')
	frostburnColdDmg.save()

#Magefist
	magefistFireDmg = Affix(slot='Gloves',
		affix='magefistFireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	magefistFireDmg.save()

#Stone Gauntlets
	stoneImmobilizeChance = Affix(slot='Gloves',
		affix='stoneImmobilizeChance',
		is_primary=False,
		desc='<span>+10.0 - 20.0%</span> chance to Immobilize on Hit')
	stoneImmobilizeChance.save()


def load_belt_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(category='Belts',
		affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	vita = Affix(category='Belts',
		affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	allRes = Affix(category='Belts',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	rcr = Affix(category='Belts',
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	itemPickup = Affix(category='Belts',
		affix='itemPickup',
		is_primary=False,
		desc='<span>+1 - 2</span> Yards to Gold and Globe Pickup')
	itemPickup.save()

	extraGold = Affix(category='Belts',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	durability = Affix(category='Belts',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

#Belt of the Trove
	troveReducedMeleeDmg = Affix(category='Belts',
		affix='troveReducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	troveReducedMeleeDmg.save()

#Fleeting Strap
	fleetingIAS = Affix(category='Belts',
		affix='fleetingIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	fleetingIAS.save()

#Hellcat Waistguard
	hellcatIAS = Affix(category='Belts',
		affix='hellcatIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	hellcatIAS.save()

#Saffron Wrap
	saffronCCReduction = Affix(category='Belts',
		affix='saffronCCReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	saffronCCReduction.save()

#String of Ears
	stringReducedMeleeDmg = Affix(category='Belts',
		affix='stringReducedMeleeDmg',
		is_primary=False,
		desc='<span>+25.0 - 30.0%</span> Melee Damage Reduction')
	stringReducedMeleeDmg.save()

#The Witching Hour
	witchingIAS = Affix(category='Belts',
		affix='witchingIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	witchingIAS.save()

	witchingCHD = Affix(category='Belts',
		affix='witchingCHD',
		is_primary=True,
		desc='<span>+26.0 - 50.0%</span> Critical Hit Damage')
	witchingCHD.save()

#Thundergod's Vigor
	thundergodsLightDmg = Affix(category='Belts',
		affix='thundergodsLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>10 - 15%</span> more damage')
	thundergodsLightDmg.save()

	thundergodsLightRes = Affix(category='Belts',
		affix='thundergodsLightRes',
		is_primary=False,
		desc='<span>+150 - 200</span> Lightning Resistance')
	thundergodsLightRes.save()

#Vigilante Belt
	vigilanteCDR = Affix(category='Belts',
		affix='vigilanteCDR',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	vigilanteCDR.save()


def load_mighty_belt_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix(category='Mighty Belts',
		affix='stre',
		is_primary=True,
		desc='<span>+416 - 500</span> Strength',
		ancient='<span>+550 - 650</span> Strength')
	stre.save()

	vita = Affix(category='Mighty Belts',
		affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	allRes = Affix(category='Mighty Belts',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	maxFury = Affix(category='Mighty Belts',
		affix='maxFury',
		is_primary=False,
		desc='<span>+10 - 12</span> Max Fury')
	maxFury.save()

#Girdle of Giants
	girdleIAS = Affix(category='Mighty Belts',
		affix='girdleIAS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	girdleIAS.save()

#Kotuur's Brace
	kotuursBlockChance = Affix(category='Mighty Belts',
		affix='kotuursBlockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	kotuursBlockChance.save()


def load_pants_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(slot='Pants',
		affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	lps = Affix(slot='Pants',
		affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	allRes = Affix(slot='Pants',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	extraGold = Affix(slot='Pants',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

#Hammer Jammers
	hammerMovementSpeed = Affix(slot='Pants',
		affix='hammerMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	hammerMovementSpeed.save()

#Swamp Land Waders
	swampPoisDmg = Affix(slot='Pants',
		affix='swampPoisDmg',
		is_primary=True,
		desc='Poison skills do <span>15 - 20%</span> more damage')
	swampPoisDmg.save()

	swampCCReduction = Affix(slot='Pants',
		affix='swampCCReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	swampCCReduction.save()


def load_boots_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")


	mainStat = Affix(slot='Boots',
		affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	vita = Affix(slot='Boots',
		affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	allRes = Affix(slot='Boots',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	armor = Affix(slot='Boots',
		affix='armor',
		is_primary=True,
		desc='<span>+373 - 397</span> Armor',
		ancient='<span>+436 - 516</span> Armor')
	armor.save()

	lps = Affix(slot='Boots',
		affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	movementSpeed = Affix(slot='Boots',
		affix='movementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	movementSpeed.save()

#Boj Anglers
	bojSkillDmg = Affix(slot='Boots',
		affix='bojSkillDmg',
		is_primary=True,
		desc='Increases {<span class="vary">Skill Damage</span>} by <span>10 - 15%</span>',
		notes='<strong>Barbarian: </strong>Ancient Spear | Hammer of the Ancients | Seismic Slam | Whirlwind<br><strong>Crusader: </strong>Blessed Hammer | Blessed Shield | Fist of the Heavens | Phalanx | Shield Bash | Sweep Attack<br><strong>Demon Hunter: </strong>Chakram | Cluster Arrow | Elemental Arrow | Impale | Multishot | Rapid Fire | Strafe<br><strong>Monk: </strong>Exploding Palm | Lashing Tail Kick | Tempest Rush | Wave of Light<br><strong>Witch Doctor: </strong>Acid Cloud | Firebats | Sacrifice | Spirit Barrage | Zombie Charger<br><strong>Wizard: </strong>Arcane Orb | Arcane Torrent | Disintegrate | Energy Twister | Meteor | Ray of Frost | Wave of Force')
	bojSkillDmg.save()

#Ice Climbers
	iceReducedColdDmg = Affix(slot='Boots',
		affix='iceReducedColdDmg',
		is_primary=True,
		desc='<span>+7 - 10%</span> Cold Damage Reduction')
	iceReducedColdDmg.save()


def load_ancient_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0005_accessory_affixes'),
    ]

    operations = [
        migrations.RunPython(load_helmet_affixes),
        migrations.RunPython(load_spirit_stone_affixes),
        migrations.RunPython(load_voodoo_mask_affixes),
        migrations.RunPython(load_wizard_hat_affixes),
        migrations.RunPython(load_shoulders_affixes),
        migrations.RunPython(load_chest_armor_affixes),
        migrations.RunPython(load_cloak_affixes),
        migrations.RunPython(load_bracers_affixes),
        migrations.RunPython(load_gloves_affixes),
        migrations.RunPython(load_belt_affixes),
        migrations.RunPython(load_mighty_belt_affixes),
        migrations.RunPython(load_pants_affixes),
        migrations.RunPython(load_boots_affixes),
        migrations.RunPython(load_ancient_affixes)
    ]
