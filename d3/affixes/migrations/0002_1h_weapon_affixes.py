# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_1h_axe_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(category='1H Axes',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	bleedChance = Affix(category='1H Axes',
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	sockets = Affix(category='1H Axes',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#The Burning Axe of Sankis
	burningFireDmg = Affix(category='1H Axes',
		affix='burningFireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	burningFireDmg.save()

#Utar's Roar
	utarsColdDmg = Affix(category='1H Axes',
		affix='utarsColdDmg',
		is_primary=True,
		desc='Cold skills do <span>15 - 20%</span> more damage')
	utarsColdDmg.save()


def load_ceremonial_knife_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	inte = Affix(category='Ceremonial Knives',
		affix='inte', 
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	manaRegen = Affix(category='Ceremonial Knives',
		affix='manaRegen',
		is_primary=True,
		desc='<span>+12.00 - 14.00</span> Mana Regeneration per Second')
	manaRegen.save()


#Deadly Rebirth
	deadlyGraspOfTheDead = Affix(category='Ceremonial Knives',
		affix='deadlyGraspOfTheDead',
		is_primary=True,
		desc='Increase Grasp of the Dead damage by <span>45 - 60%</span>')
	deadlyGraspOfTheDead.save()

#Removed in 2.4
# #Last Breath
# 	lastMassConfusionCDR = Affix(category='Ceremonial Knives',
# 		affix='lastMassConfusionCDR',
# 		is_primary=True,
# 		desc='Reduce the cooldown of Mass Confusion by <span>15 - 20</span> seconds')
# 	lastMassConfusionCDR.save()

#Starmetal Kukri
	starmetalCHD = Affix(category='Ceremonial Knives',
		affix='starmetalCHD',
		is_primary=True,
		desc='<span>+31.0 - 35.0%</span> Critical Hit Damage')
	starmetalCHD.save()

#The Spider Queen's Grasp
	spiderCorpseSpiders = Affix(category='Ceremonial Knives',
		affix='spiderCorpseSpiders',
		is_primary=True,
		desc='Increase Corpse Spiders damage by <span>45 - 60%</span>')
	spiderCorpseSpiders.save()

def load_1h_dagger_affixes(apps, schema_edtior):
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix(category='1H Daggers',
		affix='percentDmg',
		is_primary=True,
		desc='<span>+6 - 10%</span> Damage')
	percentDmg.save()

	mainStat = Affix(category='1H Daggers',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	ias = Affix(category='1H Daggers',
		affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

#Pig Sticker
	pigBeastDmg = Affix(category='1H Daggers',
		affix='pigBeastDmg',
		is_primary=False,
		desc='Increase damage against Beasts by <span>15 - 30%</span>')
	pigBeastDmg.save()

	pigHumanDmg = Affix(category='1H Daggers',
		affix='pigHumanDmg',
		is_primary=False,
		desc='Increase damage against Humans by <span>15 - 30%</span>')
	pigHumanDmg.save()

#The Barber
	barberCHD = Affix(category='1H Daggers',
		affix='barberCHD',
		is_primary=True,
		desc='<span>+31.0 - 35.0%</span> Critical Hit Damage')
	barberCHD.save()

#2.4 new
#Voo's Juicer
	voosGraspOfTheDead = Affix(category='1H Daggers',
		affix='voosGraspOfTheDead',
		is_primary=True,
		desc='Increase damage of Spirit Barrage by <span>45 - 60%</span>')
	voosGraspOfTheDead.save()


def load_fist_weapon_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix(category='Fist Weapons',
		affix='percentDmg',
		is_primary=True,
		desc='<span>+6 - 10%</span> Damage')
	percentDmg.save()

	dext = Affix(category='Fist Weapons',
		affix='dext',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000</span> Dexterity')
	dext.save()

	bleedChance = Affix(category='Fist Weapons',
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	lph = Affix(category='Fist Weapons',
		affix='lph',
		is_primary=True,
		desc='<span>+15,474 - 18,429</span> Life per Hit',
		ancient='<span>+20,271 - 23,950</span> Life per Hit')
	lph.save()

	lifePerSpirit = Affix(category='Fist Weapons',
		affix='lifePerSpirit',
		is_primary=True,
		desc='<span>+353 - 415</span> Life per Spirit spent',
		ancient='<span>+456 - 540</span> Life per Spirit spent')
	lifePerSpirit.save()

	spiritRegen = Affix(category='Fist Weapons',
		affix='spiritRegen',
		is_primary=True,
		desc='<span>+2.17 - 3.00</span> Spirit Regeneration per Second')
	spiritRegen.save()


	durability = Affix(category='Fist Weapons',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

#Rabid Strike
	rabidCHD = Affix(category='Fist Weapons',
		affix='rabidCHD',
		is_primary=True,
		desc='<span>+31.0 - 35.0%</span> Critical Hit Damage')
	rabidCHD.save()

	rabidSlowChance = Affix(category='Fist Weapons',
		affix='rabidSlowChance',
		is_primary=False,
		desc='<span>+15.0 - 25.0%</span> chance to Slow on Hit')
	rabidSlowChance.save()

#Sledge Fist
	sledgeStunChance = Affix(category='Fist Weapons',
		affix='sledgeStunChance',
		is_primary=False,
		desc='<span>+30.0 - 50.0%</span> chance to Stun on Hit')
	sledgeStunChance.save()

#Won Khim Lau
	wonLightDmg = Affix(category='Fist Weapons',
		affix='wonLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 25%</span> more damage')
	wonLightDmg.save()

def load_1h_flail_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix(category='1H Flails',
		affix='stre',
		is_primary=True,
		desc='<span>+626 - 750</span> Strength',
		ancient='<span>+825 - 1,000</span> Strength')
	stre.save()

	sockets = Affix(category='1H Flails',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Golden Scourge
	goldenHolyDmg = Affix(category='1H Flails',
		affix='goldenHolyDmg',
		is_primary=True,
		desc='Holy skills do <span>15 - 20%</span> more damage')
	goldenHolyDmg.save()

def load_hand_crossbow_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	dext = Affix(category='Hand Crossbows',
		affix='dext',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000</span> Dexterity')
	dext.save()

	maxDisc = Affix(category='Hand Crossbows',
		affix='maxDisc',
		is_primary=False,
		desc='<span>+9 - 12</span> Max Discipline')
	maxDisc.save()

	sockets = Affix(category='Hand Crossbows',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Balefire Caster
	balefireFireDmg = Affix(category='Hand Crossbows',
		affix='balefireFireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	balefireFireDmg.save()

#Dawn
	dawnStunChance = Affix(category='Hand Crossbows',
		affix='dawnStunChance',
		is_primary=False,
		desc='<span>+1.0 - 5.0%</span> chance to Stun on Hit')
	dawnStunChance.save()

#Added in 2.4
#K'mar Tenclip
	kmarStrafe = Affix(category='Hand Crossbows',
		affix='kmarStrafe',
		is_primary=True,
		desc='Increase Strafe damage by <span>75 - 100%</span>')
	kmarStrafe.save()

#Added in 2.4
#Valla's Bequest
	vallasStrafe = Affix(category='Hand Crossbows',
		affix='vallasStrafe',
		is_primary=True,
		desc='Increase Strafe damage by <span>75 - 100%</span>')
	vallasStrafe.save()


def load_1h_mace_affixes(apps,schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix(category='1H Maces',
		affix='percentDmg',
		is_primary=True,
		desc='<span>+6 - 10%</span> Damage')
	percentDmg.save()

	mainStat = Affix(category='1H Maces',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	ias = Affix(category='1H Maces',
		affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	sockets = Affix(category='1H Maces',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	thorns = Affix(category='1H Maces',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()

	killExp = Affix(category='1H Maces',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

#Devastator
	devastatorFireDmg = Affix(category='1H Maces',
		affix='devastatorFireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	devastatorFireDmg.save()

#Echoing Fury
	echoingFearChance = Affix(category='1H Maces',
		affix='echoingFearChance',
		is_primary=False,
		desc='<span>+10.0 - 20.0%</span> chance to Fear on Hit')
	echoingFearChance.save()

#Jace's Hammer of Vigilence
	jacesBlessedHammer = Affix(category='1H Maces',
		affix='jacesBlessedHammer',
		is_primary=True,
		desc='Increase Blessed Hammer damage by <span>15 - 20%</span>')
	jacesBlessedHammer.save()

#Nailbiter
	nailbiterThorns = Affix(category='1H Maces',
		affix='nailbiterThorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	nailbiterThorns.save()

#Neanderthal
	neanderthalThorns = Affix(category='1H Maces',
		affix='neanderthalThorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	neanderthalThorns.save()

#Nutcracker
	nutcrackerCHD = Affix(category='1H Maces',
		affix='nutcrackerCHD',
		is_primary=True,
		desc='<span>+31.0 - 35.0%</span> Critical Hit Damage')
	nutcrackerCHD.save()

	nutcrackerStunChance = Affix(category='1H Maces',
		affix='nutcrackerStunChance',
		is_primary=False,
		desc='<span>+5.0 - 10.0%</span> chance to Stun on Hit')
	nutcrackerStunChance.save()

#Odyn Son
	odynLightDmg = Affix(category='1H Maces',
		affix='odynLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	odynLightDmg.save()

#Sun Keeper
	sunEliteDmg = Affix(category='1H Maces',
		affix='sunEliteDmg',
		is_primary=True,
		desc='Increase damage against Elites by <span>15 - 30%</span>')
	sunEliteDmg.save()

	sunExtraGold = Affix(category='1H Maces',
		affix='sunExtraGold',
		is_primary=False,
		desc='<span>+71 - 80%</span> Extra Gold from Monsters')
	sunExtraGold.save()


def load_1h_mighty_weapon_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix(category='1H Mighty Weapons',
		affix='stre',
		is_primary=True,
		desc='<span>+626 - 750</span> Strength',
		ancient='<span>+825 - 1,000</span> Strength')
	stre.save()

	bleedChance = Affix(category='1H Mighty Weapons',
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	sockets = Affix(category='1H Mighty Weapons',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Fjord Cutter
	fjordFreezeChance = Affix(category='1H Mighty Weapons',
		affix='fjordFreezeChance',
		is_primary=False,
		desc='<span>+7.5 - 10.0%</span> chance to Freeze on Hit')
	fjordFreezeChance.save()

#Night's Reaping
	nightsLife = Affix(category='1H Mighty Weapons',
		affix='nightsLife',
		is_primary=True,
		desc='<span>+14 - 18%</span> Life')
	nightsLife.save()

def load_1h_spear_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(category='1H Spears',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	eliteDmg = Affix(category='1H Spears',
		affix='eliteDmg',
		is_primary=True,
		desc='Increase damage against Elites by <span>5.0 - 8.0%</span>')
	eliteDmg.save()

#Akanesh, the Herald of Righteousness
	akaneshHolyDmg = Affix(category='1H Spears',
		affix='akaneshHolyDmg',
		is_primary=True,
		desc='Holy skills do <span>15 - 25%</span> more damage')
	akaneshHolyDmg.save()

#Scrimshaw
	scrimshawZombieCharger = Affix(category='1H Spears',
		affix='scrimshawZombieCharger',
		is_primary=True,
		desc='Increase Zombie Charger damage by <span>60 - 80%</span>')
	scrimshawZombieCharger.save()

#The Three Hundredth Spear
	threeWeaponThrow = Affix(category='1H Spears',
		affix='threeWeaponThrow',
		is_primary=True,
		desc='Increase Weapon Throw damage by <span>35 - 50%</span>')
	threeWeaponThrow.save()

	threeAncientSpear = Affix(category='1H Spears',
		affix='threeAncientSpear',
		is_primary=True,
		desc='Increase Zombie Charger damage by <span>35 - 50%</span>')
	threeAncientSpear.save()


def load_1h_sword_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")


	percentDmg = Affix(category='1H Swords',
		affix='percentDmg',
		is_primary=True,
		desc='<span>+6 - 10%</span> Damage')
	percentDmg.save()

	mainStat = Affix(category='1H Swords',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	ias = Affix(category='1H Swords',
		affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	sockets = Affix(category='1H Swords',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	killExp = Affix(category='1H Swords',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()


#Azurewrath
	azurewrathColdDmg = Affix(category='1H Swords',
		affix='azurewrathColdDmg',
		is_primary=True,
		desc='Cold skills do <span>15 - 20%</span> more damage')
	azurewrathColdDmg.save()

	azurewrathFreezeChance = Affix(category='1H Swords',
		affix='azurewrathFreezeChance',
		is_primary=False,
		desc='<span>+20.0 - 25.0%</span> chance to Freeze on Hit')
	azurewrathFreezeChance.save()

#Devil Tongue
	devilExtraGold = Affix(category='1H Swords',
		affix='devilExtraGold',
		is_primary=False,
		desc='<span>+71 - 80%</span> Extra Gold from Monsters')
	devilExtraGold.save()

#Doombringer
	doombringerPhysDmg = Affix(category='1H Swords',
		affix='doombringerPhysDmg',
		is_primary=True,
		desc='Physical skills do <span>15 - 20%</span> more damage')
	doombringerPhysDmg.save()

#Exarian
	exarianCHD = Affix(category='1H Swords',
		affix='exarianCHD',
		is_primary=True,
		desc='<span>+31.0 - 35.0%</span> Critical Hit Damage')
	exarianCHD.save()

#Gift of Silaria
	giftMovementSpeed = Affix(category='1H Swords',
		affix='giftMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	giftMovementSpeed.save()

#Monster Hunter
	monsterBeastDmg = Affix(category='1H Swords',
		affix='monsterBeastDmg',
		is_primary=False,
		desc='Increase damage against Beasts by <span>9 - 15%</span>')
	monsterBeastDmg.save()

#Sever
	severDemonDmg = Affix(category='1H Swords',
		affix='severDemonDmg',
		is_primary=False,
		desc='Increase damage against Demons by <span>5 - 10%</span>')
	severDemonDmg.save()

#Skycutter
	skycutterHolyDmg = Affix(category='1H Swords',
		affix='skycutterHolyDmg',
		is_primary=True,
		desc='Holy skills do <span>15 - 20%</span> more damage')
	skycutterHolyDmg.save()


def load_wand_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	inte = Affix(category='Wands',
		affix='inte', 
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	maxAP = Affix(category='Wands',
		affix='maxAP',
		is_primary=False,
		desc='<span>+10 - 14</span> Max Arcane Power')
	maxAP.save()

#Fragment of Destiny
	fragmentSpectralBlade = Affix(category='Wands',
		affix='fragmentSpectralBlade',
		is_primary=True,
		desc='Increase Spectral Blade damage by <span>15 - 30%</span>')
	fragmentSpectralBlade.save()

#Gesture of Orpheus
	gestureEleDmg = Affix(category='Wands',
		affix='gestureEleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage<div class="extra"><div class="extra-x">X</div><span>Cold<br>Fire<br>Lightning<br>Arcane</div>')
	gestureEleDmg.save()

#Slorak's Madness
	sloraksDisintegrate = Affix(category='Wands',
		affix='sloraksDisintegrate',
		is_primary=True,
		desc='Increase Disintegrate damage by <span>15 - 30%</span>')
	sloraksDisintegrate.save()

#2.4 new
#Unstable Sceptor
	unstableArcaneOrb = Affix(category='Wands',
		affix='unstableArcaneOrb',
		is_primary=True,
		desc='Increase Arcane Orb damage by <span>50 - 65%</span>')
	unstableArcaneOrb.save()

#Added in 2.4
#Wand of Woh
	wandExplosiveBlast = Affix(category='Wands',
		affix='wandExplosiveBlast',
		is_primary=True,
		desc='Increase Explosive Blast damage by <span>75 - 100%</span>')
	wandExplosiveBlast.save()

def load_ancient_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_1h_axe_affixes),
        migrations.RunPython(load_ceremonial_knife_affixes),
        migrations.RunPython(load_1h_dagger_affixes),
        migrations.RunPython(load_fist_weapon_affixes),
        migrations.RunPython(load_1h_flail_affixes),
        migrations.RunPython(load_hand_crossbow_affixes),
        migrations.RunPython(load_1h_mace_affixes),
        migrations.RunPython(load_1h_mighty_weapon_affixes),
        migrations.RunPython(load_1h_spear_affixes),
        migrations.RunPython(load_1h_sword_affixes),
        migrations.RunPython(load_wand_affixes),
        migrations.RunPython(load_ancient_affixes),
    ]
