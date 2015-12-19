# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_2h_axe_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(category='2H Axes',
		affix='mainStat',
		is_primary=True,
		desc='<span>+946 - 1,125</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+1,237 - 1,465</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	bleedChance = Affix(category='2H Axes',
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	sockets = Affix(category='2H Axes',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	lpk = Affix(category='2H Axes',
		affix='lpk',
		is_primary=False,
		desc='<span>+9,142 - 13,371</span> Life per Kill',
		ancient='<span>+14,708 - 17,385</span> Life per Kill')
	lpk.save()

	killExp = Affix(category='2H Axes',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()


def load_bow_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(category='Bows',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	percentDmg = Affix(category='Bows',
		affix='percentDmg',
		is_primary=True,
		desc='<span>+6 - 10%</span> Damage')
	percentDmg.save()

	ias = Affix(category='Bows',
		affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	eliteDmg = Affix(category='Bows',
		affix='eliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>9.0 - 10.0%</span>')
	eliteDmg.save()

	durability = Affix(category='Bows',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

#Etrayu
	etrayuColdDmg = Affix(category='Bows',
		affix='etrayuColdDmg',
		is_primary=True,
		desc='Cold skills do <span>15 - 20%</span> more damage')
	etrayuColdDmg.save()

#The Raven's Wing
	ravensExtraGold = Affix(category='Bows',
		affix='ravensExtraGold',
		is_primary=False,
		desc='<span>+71 - 80%</span> Extra Gold from Monsters')
	ravensExtraGold.save()

#Unbound Bolt
	unboundCHD = Affix(category='Bows',
		affix='unboundCHD',
		is_primary=True,
		desc='<span>+31.0 - 35.0%</span> Critical Hit Damage')
	unboundCHD.save()

#Uskang
	uskangLightDmg = Affix(category='Bows',
		affix='uskangLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	uskangLightDmg.save()

#Windforce
	windforceKnockbackChance = Affix(category='Bows',
		affix='windforceKnockbackChance',
		is_primary=False,
		desc='<span>+30.0 - 50.0%</span> chance to Knockback on Hit')
	windforceKnockbackChance.save()

#Yang's Recurve
	yangsRCR = Affix(category='Bows',
		affix='yangsRCR',
		is_primary=True,
		desc='<span>+40 - 50%</span> Resource Cost Reduction')
	yangsRCR.save()


def load_crossbow_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")


	mainStat = Affix(category='Crossbows',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	sockets = Affix(category='Crossbows',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Buriza-do Kyanon
	burizadoFreezeChance = Affix(category='Crossbows',
		affix='burizadoFreezeChance',
		is_primary=False,
		desc='<span>+7.5 - 10.0%</span> chance to Freeze on Hit')
	burizadoFreezeChance.save()

#Added in 2.4
#Manticore
	manticoreClusterArrow = Affix(category='Crossbows',
		affix='manticoreClusterArrow',
		is_primary=True,
		desc='Increase Cluster Arrow damag by <span>60 - 80%</span>')
	manticoreClusterArrow.save()

def load_daibo_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	dext = Affix(category='Daibos',
		affix='dext',
		is_primary=True,
		desc='<span>+946 - 1,125</span> Dexterity',
		ancient='<span>+1,237 - 1,465</span> Dexterity')
	dext.save()

	sockets = Affix(category='Daibos',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Added in 2.4
#Balance
	balanceTempestRush = Affix(category='Daibos',
		affix='balanceTempestRush',
		is_primary=True,
		desc='Increase Tempest Rush damage by <span>150 - 200%</span>')
	balanceTempestRush.save()

#Incense Torch of the Grand Temple
	incenseWaveOfLight = Affix(category='Daibos',
		affix='incenseWaveOfLight',
		is_primary=True,
		desc='Increase Wave of Light damage by <span>25 - 30%</span>')
	incenseWaveOfLight.save()

#Staff of Kyro
	staffDeadlyReach = Affix(category='Daibos',
		affix='staffDeadlyReach',
		is_primary=True,
		desc='Increase Deadly Reach damage by <span>40 - 50%</span>')
	staffDeadlyReach.save()


def load_2h_flail_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix(category='2H Flails',
		affix='stre',
		is_primary=True,
		desc='<span>+946 - 1,125</span> Strength',
		ancient='<span>+1,237 - 1,465</span> Strength')
	stre.save()

	sockets = Affix(category='2H Flails',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Added in 2.4
#Golden Flense
	goldenSweepAttack = Affix(category='2H Flails',
		affix='goldenSweepAttack',
		is_primary=True,
		desc='Increases Sweep Attack damage by <span>150 - 200%</span>')
	goldenSweepAttack.save()


def load_2h_mace_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix(category='2H Maces',
		affix='percentDmg',
		is_primary=True,
		desc='<span>+6 - 10%</span> Damage')
	percentDmg.save()

	mainStat = Affix(category='2H Maces',
		affix='mainStat',
		is_primary=True,
		desc='<span>+946 - 1,125</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+1,237 - 1,465</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	ccChance = Affix(category='2H Maces',
		affix='ccChance',
		is_primary=False,
		desc='<span>+1.0 - 5.1%</span> chance to {<span class="vary">Crowd Control</span>} on Hit<div class="extra"><div class="extra-x">X</div><span>Fear<br>Stun<br>Blind<br>Freeze<br>Chill<br>Slow<br>Immobilize<br>Knockback</span></div>')
	ccChance.save()

	lpk = Affix(category='2H Maces',
		affix='lpk',
		is_primary=False,
		desc='<span>+9,142 - 13,371</span> Life per Kill',
		ancient='<span>+14,708 - 17,385</span> Life per Kill')
	lpk.save()

#Schaefer's Hammer
	schaefersLightDmg = Affix(category='2H Maces',
		affix='schaefersLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>20 - 25%</span> more damage')
	schaefersLightDmg.save()

#Sledge of Athskeleng
	sledgeMovementSpeed = Affix(category='2H Maces',
		affix='sledgeMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	sledgeMovementSpeed.save()

#Wrath of the Bone King
	wrathColdDmg = Affix(category='2H Maces',
		affix='wrathColdDmg',
		is_primary=True,
		desc='Cold skills do <span>25 - 30%</span> more damage')
	wrathColdDmg.save()

def load_2h_mighty_weapon_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix(category='2H Mighty Weapons',
		affix='stre',
		is_primary=True,
		desc='<span>+946 - 1,125</span> Strength',
		ancient='<span>+1,237 - 1,465</span> Strength')
	stre.save()

	sockets = Affix(category='2H Mighty Weapons',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Fury of the Vanished Peak
	furySeismicSlam = Affix(category='2H Mighty Weapons',
		affix='furySeismicSlam',
		is_primary=True,
		desc='Increase Seismic Slam damage by <span>100 - 125%</span>')
	furySeismicSlam.save()

#The Gavel of Judgement
	gavelHammerOfTheAncients = Affix(category='2H Mighty Weapons',
		affix='gavelHammerOfTheAncients',
		is_primary=True,
		desc='Increase Hammer of the Ancients damage by <span>75 - 100%</span>')
	gavelHammerOfTheAncients.save()


def load_polearm_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(category='Polearms',
		affix='mainStat',
		is_primary=True,
		desc='<span>+946 - 1,125</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+1,237 - 1,465</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	lpk = Affix(category='Polearms',
		affix='lpk',
		is_primary=False,
		desc='<span>+9,142 - 13,371</span> Life per Kill',
		ancient='<span>+14,708 - 17,385</span> Life per Kill')
	lpk.save()

	sockets = Affix(category='Polearms',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Heart Slaughter
	heartPhysDmg = Affix(category='Polearms',
		affix='heartPhysDmg',
		is_primary=True,
		desc='Physical skills do <span>25 - 30%</span> more damage')
	heartPhysDmg.save()


def load_staff_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix(category='Staves',
		affix='percentDmg',
		is_primary=True,
		desc='<span>+6 - 10%</span> Damage')
	percentDmg.save()

	mainStat = Affix(category='Staves',
		affix='mainStat',
		is_primary=True,
		desc='<span>+946 - 1,125</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence</span></div>',
		ancient='<span>+1,237 - 1,465</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence</span></div>')
	mainStat.save()

	sockets = Affix(category='Staves',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	killExp = Affix(category='Staves',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	durability = Affix(category='Staves',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

#SuWong Diviner
	suwongAcidCloud = Affix(category='Staves',
		affix='suwongAcidCloud',
		is_primary=True,
		desc='Increase Acid Cloud damage by <span>75 - 100%</span>')
	suwongAcidCloud.save()

#The Grand Vizier
	grandMeteor = Affix(category='Staves',
		affix='grandMeteor',
		is_primary=True,
		desc='Increase Meteor damage by <span>25 - 30%</span>')
	grandMeteor.save()

#Wormwood
	wormwoodPoisDmg = Affix(category='Staves',
		affix='wormwoodPoisDmg',
		is_primary=True,
		desc='Poison skills do <span>20 - 25%</span> more damage')
	wormwoodPoisDmg.save()


def load_2h_sword_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix(category='2H Swords',
		affix='percentDmg',
		is_primary=True,
		desc='<span>+6 - 10%</span> Damage')
	percentDmg.save()

	mainStat = Affix(category='2H Swords',
		affix='mainStat',
		is_primary=True,
		desc='<span>+946 - 1,125</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+1,237 - 1,465</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	cdr = Affix(category='2H Swords',
		affix='cdr',
		is_primary=True,
		desc='<span>+6.0 - 10.0%</span> Cooldown Reduction')
	cdr.save()

	sockets = Affix(category='2H Swords',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	lpk = Affix(category='2H Swords',
		affix='lpk',
		is_primary=False,
		desc='<span>+9,142 - 13,371</span> Life per Kill',
		ancient='<span>+14,708 - 17,385</span> Life per Kill')
	lpk.save()

	killExp = Affix(category='2H Swords',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	durability = Affix(category='2H Swords',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

#Blackguard
	blackguardCCReduction = Affix(category='2H Swords',
		affix='blackguardCCReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	blackguardCCReduction.save()

#Added in 2.4
#Blade of Prophecy
	bladeCondemn = Affix(category='2H Swords',
		affix='bladeCondemn',
		is_primary=True,
		desc='Increases Condemn damage by <span>75 - 100%</span>')
	bladeCondemn.save()

#Corrupted Ashbringer
	corruptedUndeadDmg = Affix(category='2H Swords',
		affix='corruptedUndeadDmg',
		is_primary=False,
		desc='Increases damage against Undead by <span>9 - 15%</span>')
	corruptedUndeadDmg.save()

#Faithful Memory
	faithfulThorns = Affix(category='2H Swords',
		affix='faithfulThorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	faithfulThorns.save()

#Maximus
	maximusFireDmg = Affix(category='2H Swords',
		affix='maximusFireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	maximusFireDmg.save()

#The Grandfather
	grandfatherLife = Affix(category='2H Swords',
		affix='grandfatherLife',
		is_primary=True,
		desc='<span>+14 - 18%</span> Life')
	grandfatherLife.save()

#The Sultan of Blinding Sand
	sultanBlindChance = Affix(category='2H Swords',
		affix='sultanBlindChance',
		is_primary=False,
		desc='<span>+20.0 - 40.0%</span> chance to Blind on Hit')
	sultanBlindChance.save()


def load_ancient_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0002_1h_weapon_affixes'),
    ]

    operations = [
        migrations.RunPython(load_2h_axe_affixes),
        migrations.RunPython(load_bow_affixes),
        migrations.RunPython(load_crossbow_affixes),
        migrations.RunPython(load_daibo_affixes),
        migrations.RunPython(load_2h_flail_affixes),
        migrations.RunPython(load_2h_mace_affixes),
        migrations.RunPython(load_2h_mighty_weapon_affixes),
        migrations.RunPython(load_polearm_affixes),
        migrations.RunPython(load_staff_affixes),
        migrations.RunPython(load_2h_sword_affixes),
        migrations.RunPython(load_ancient_affixes)
    ]
