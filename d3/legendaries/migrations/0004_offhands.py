'''
Needed affixes and item-specific affixes are defined first.
Items of category/slot defined after.
'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_sources(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	dmg = Affix.objects.get(category='Sources',
		affix='dmg')
	inte = Affix.objects.get(category='Sources',
		affix='inte')
	chc = Affix.objects.get(category='Sources',
		affix='chc')
	apCrit = Affix.objects.get(category='Sources',
		affix='apCrit')

	winterColdDmg = Affix.objects.get(category='Sources',
		affix='winterColdDmg')

	cosmicStrand = Weapon(slot='Offhands',
		category='Sources',
		name='Cosmic Strand',
		pic='media/items/legendaries/offhands/sources/cosmic_strand.png',
		unique='Teleport gains the effect of the Wormhole rune',
		random_primaries='4',
		random_secondaries='1',
		notes='crafted',
		patch='23')
	cosmicStrand.save()
	cosmicStrand.affixes.add(dmg)

#2.4 new
	etchedSigil = Weapon(slot='Offhands',
		category='Sources',
		name='Etched Sigil',
		pic='media/items/legendaries/2.4/weapons/etched_sigil.png',
		unique='Your Arcane Torrent, Disintegrate, and Ray of Frost also cast your other damaging Arcane Power Spenders every second',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	etchedSigil.save()
	etchedSigil.affixes.add(dmg, inte, chc)

	lightOfGrace = Weapon(slot='Offhands',
		category='Sources',
		name='Light of Grace',
		pic='media/items/legendaries/offhands/sources/light_of_grace.png',
		unique='Ray of Frost now pierces',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	lightOfGrace.save()
	lightOfGrace.affixes.add(dmg, inte, chc)

	mirrorball = Weapon(slot='Offhands',
		category='Sources',
		name='Mirrorball',
		pic='media/items/legendaries/offhands/sources/mirrorball.png',
		unique='Magic Missile fires <span>1 - 2</span> extra missiles',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	mirrorball.save()
	mirrorball.affixes.add(dmg, inte, chc)

	mykensBallOfHate = Weapon(slot='Offhands',
		category='Sources',
		name='Myken\'s Ball of Hate',
		pic='media/items/legendaries/offhands/sources/mykens_ball_of_hate.png',
		unique='Electrocute can chain to enemies that have already been hit',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	mykensBallOfHate.save()
	mykensBallOfHate.affixes.add(dmg, inte, chc)

#2.4 new
	orbOfInfiniteDepth = Weapon(slot='Offhands',
		category='Sources',
		name='Orb of Infinite Depth',
		pic='media/items/legendaries/2.4/weapons/orb_of_infinite_depth.png',
		unique='Each time you hit an enemy with Explosive Blast your damage is increased by <span>4 - 5%</span> and your damage reduction is increased by <span class="silver">15%</span> for <span class="silver">6</span> seconds. This effect can stack up to <span class="silver">4</span> times',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	orbOfInfiniteDepth.save()
	orbOfInfiniteDepth.affixes.add(dmg, inte, chc)

#2.4 new
	primordialSoul = Weapon(slot='Offhands',
		category='Sources',
		name='Primordial Soul',
		pic='media/items/legendaries/2.4/weapons/primordial_soul.png',
		unique='Elemental Exposure\'s damage bonus per stack is increased to <span class="silver">10%</span>',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	primordialSoul.save()
	primordialSoul.affixes.add(dmg, inte, chc)

	theOculus = Weapon(slot='Offhands',
		category='Sources',
		name='The Oculus',
		pic='media/items/legendaries/offhands/sources/the_oculus.png',
		unique='Taking damage has up to a <span>15 - 20%</span> chance to reset the cooldown on Teleport',
		random_primaries='',
		random_secondaries='',
		patch='23')
	theOculus.save()
	theOculus.affixes.add(dmg, inte, chc, apCrit)

	triumvirate = Weapon(slot='Offhands',
		category='Sources',
		name='Triumvirate',
		pic='media/items/legendaries/offhands/sources/triumvirate.png',
		unique='Your Signature Spells increase the damage of Arcane Orb by <span>150 - 200%</span> for <span class="silver">6</span> seconds, stacking up to <span class="silver">3</span> times',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	triumvirate.save()
	triumvirate.affixes.add(dmg, inte, chc)

	winterFlurry = Weapon(slot='Offhands',
		category='Sources',
		name='Winter Flurry',
		pic='media/items/legendaries/offhands/sources/winter_flurry.png',
		unique='Enemies killed by Cold damage have a <span>15 - 20%</span> chance to release a Frost Nova',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	winterFlurry.save()
	winterFlurry.affixes.add(dmg, inte, chc, winterColdDmg)

	for weapon in Weapon.objects.filter(category="Sources"):
		weapon.owner = 'wz'
		weapon.save()


def load_quivers(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	dext = Affix.objects.get(category='Quivers', affix='dext')
	ias = Affix.objects.get(category='Quivers', affix='ias')
	chc = Affix.objects.get(category='Quivers', affix='chc')
	eliteDmg = Affix.objects.get(category='Quivers', affix='eliteDmg')
	rcr = Affix.objects.get(category='Quivers', affix='rcr')

	holyEleDmg = Affix.objects.get(category='Quivers', affix='holyEleDmg')
	bombadiersSentry = Affix.objects.get(category='Quivers',
		affix='bombadiersSentry')
	deadMultishot = Affix.objects.get(category='Quivers',
		affix='deadMultishot')
	sinRapidFire = Affix.objects.get(category='Quivers',
		affix='sinRapidFire')


	archfiendArrows = Weapon(slot='Offhands',
		category='Quivers',
		name='Archfiend Arrows',
		pic='media/items/legendaries/offhands/quivers/archfiend_arrows.png',
		random_primaries='2',
		random_secondaries='2',
		patch='23')
	archfiendArrows.save()
	archfiendArrows.affixes.add(ias, chc, eliteDmg)

#2.4
	bombadiersRucksack = Weapon(slot='Offhands',
		category='Quivers',
		name='Bombadier\'s Rucksack',
		pic='media/items/legendaries/offhands/quivers/bombardiers_rucksack.png',
		unique='You may have <span class="silver">2</span> additional Sentries',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	bombadiersRucksack.save()
	bombadiersRucksack.affixes.add(dext, ias, chc, bombadiersSentry)

	deadMansLegacy = Weapon(slot='Offhands',
		category='Quivers',
		name='Dead Man\'s Legacy',
		pic='media/items/legendaries/offhands/quivers/dead_mans_legacy.png',
		unique='Multishot hits enemies below <span>50 - 60%</span> health twice',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	deadMansLegacy.save()
	deadMansLegacy.affixes.add(dext, ias, chc, deadMultishot)

	emimeisDuffel = Weapon(slot='Offhands',
		category='Quivers',
		name='Emimei\'s Duffel',
		pic='media/items/legendaries/offhands/quivers/emimeis_duffel.png',
		unique='Bolas now explode instantly',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	emimeisDuffel.save()
	emimeisDuffel.affixes.add(dext, ias)

	fletchersPride = Weapon(slot='Offhands',
		category='Quivers',
		name='Fletcher\'s Pride',
		pic='media/items/legendaries/offhands/quivers/fletchers_pride.png',
		random_primaries='2',
		random_secondaries='2',
		patch='23')
	fletchersPride.save()
	fletchersPride.affixes.add(dext, ias, rcr)

	holyPointShot = Weapon(slot='Offhands',
		category='Quivers',
		name='Holy Point Shot',
		pic='media/items/legendaries/offhands/quivers/holy_point_shot.png',
		random_primaries='2',
		random_secondaries='2',
		patch='23')
	holyPointShot.save()
	holyPointShot.affixes.add(dext, ias, holyEleDmg)

	meticulousBolts = Weapon(slot='Offhands',
		category='Quivers',
		name='Meticulous Bolts',
		pic='media/items/legendaries/offhands/quivers/meticulous_bolts.png',
		unique='Elemental Arrow - Ball Lightning now travels at <span>30 - 40%</span> speed',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	meticulousBolts.save()
	meticulousBolts.affixes.add(dext, ias)

#2.4
	sinSeekers = Weapon(slot='Offhands',
		category='Quivers',
		name='Sin Seekers',
		pic='media/items/legendaries/offhands/quivers/sin_seekers.png',
		unique='Rapid Fire no longer has a channel cost',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	sinSeekers.save()
	sinSeekers.affixes.add(dext, ias, chc, sinRapidFire)

	spinesOfSeethingHatred = Weapon(slot='Offhands',
		category='Quivers',
		name='Spines of Seething Hatred',
		pic='media/items/legendaries/offhands/quivers/spines_of_seething_hatred.png',
		unique='Chakram now generates <span>3 - 4</span> Hatred',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	spinesOfSeethingHatred.save()
	spinesOfSeethingHatred.affixes.add(dext, ias)

	theNinthCirriSatchel = Weapon(slot='Offhands',
		category='Quivers',
		name='The Ninth Cirri Satchel',
		pic='media/items/legendaries/offhands/quivers/the_ninth_cirri_satchel.png',
		unique='Hungering Arrow has <span>20 - 25%</span> additional chance to pierce',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	theNinthCirriSatchel.save()
	theNinthCirriSatchel.affixes.add(dext, ias)

	for weapon in Weapon.objects.filter(category='Quivers'):
		weapon.owner = 'dh'
		weapon.save()


def load_mojos(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	dmg = Affix.objects.get(category='Mojos',
		affix='dmg')
	inte = Affix.objects.get(category='Mojos',
		affix='inte')
	chc = Affix.objects.get(category='Mojos',
		affix='chc')
	lps = Affix.objects.get(category='Mojos',
		affix='lps')
	manaRegen = Affix.objects.get(category='Mojos',
		affix='manaRegen')
	sacrifice = Affix.objects.get(category='Mojos',
		affix='sacrifice')
	maxMana = Affix.objects.get(category='Mojos',
		affix='maxMana')
	durability = Affix.objects.get(category='Mojos',
		affix='durability')

	# thingItemPickup = Affix.objects.get(category='Mojos',
	# 	affix='thingItemPickup')
	wilkensGraspOfTheDead = Affix.objects.get(category='Mojos',
		affix='wilkensGraspOfTheDead')

	gazingDemise = Weapon(slot='Offhands',
		category='Mojos',
		name='Gazing Demise',
		pic='media/items/legendaries/offhands/mojos/gazing_demise.png',
		random_primaries='1',
		random_secondaries='2',
		patch='23')
	gazingDemise.save()
	gazingDemise.affixes.add(dmg, inte, lps, manaRegen)

	henrisPerquisition = Weapon(slot='Offhands',
		category='Mojos',
		name='Henri\'s Perquisition',
		pic='media/items/legendaries/offhands/mojos/henris_perquisition.png',
		unique='The first time an enemy deals damage to you, reduce that damage by <span>60 - 80%</span> and Charm the enemy for <span class="silver">3</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	henrisPerquisition.save()
	henrisPerquisition.affixes.add(dmg, inte, chc, durability)

	homunculus = Weapon(slot='Offhands',
		category='Mojos',
		name='Homunculus',
		pic='media/items/legendaries/offhands/mojos/homunculus.png',
		unique='A Zombie Dog is automatically summoned to your side every <span class="silver">2</span> seconds',
		random_primaries='2',
		patch='23')
	homunculus.save()
	homunculus.affixes.add(dmg, inte, chc, sacrifice, maxMana)

	shukranisTriumph = Weapon(slot='Offhands',
		category='Mojos',
		name='Shukrani\'s Triumph',
		pic='media/items/legendaries/offhands/mojos/shukranis_triumph.png',
		unique='Spirit Walk lasts until you attack or until an enemy is within <span class="silver">30</span> yards of you',
		random_primaries='1',
		random_secondaries='1',
		patch='23')
	shukranisTriumph.save()
	shukranisTriumph.affixes.add(dmg, inte, chc, manaRegen)

	spite = Weapon(slot='Offhands',
		category='Mojos',
		name='Spite',
		pic='media/items/legendaries/offhands/mojos/spite.png',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	spite.save()
	spite.affixes.add(dmg, chc, maxMana)

#2.4
	thingOfTheDeep = Weapon(slot='Offhands',
		category='Mojos',
		name='Thing of the Deep',
		pic='media/items/legendaries/offhands/mojos/thing_of_the_deep.png',
		unique='<span class="silver">+20</span> Yards to Gold and Globe Pickup',
		random_primaries='2',
		patch='24')
	thingOfTheDeep.save()
	thingOfTheDeep.affixes.add(dmg, inte, chc, maxMana)

	uhkapianSerpent = Weapon(slot='Offhands',
		category='Mojos',
		name='Uhkapian Serpent',
		pic='media/items/legendaries/offhands/mojos/uhkapian_serpent.png',
		unique='<span>25 - 30%</span> of the damage you take is redirected to your Zombie Dogs',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	uhkapianSerpent.save()
	uhkapianSerpent.affixes.add(dmg, inte, chc)

#2.4 new
	vileHive = Weapon(slot='Offhands',
		category='Mojos',
		name='Vile Hive',
		pic='media/items/legendaries/2.4/weapons/vile_hive.png',
		unique='Locust Swarm gains the effect of the Pestilence rune and deals <span>45 - 60%</span> increased damage',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	vileHive.save()
	vileHive.affixes.add(dmg, inte, chc)

#2.4 new
	wilkensReach = Weapon(slot='Offhands',
		category='Mojos',
		name='Wilken\'s Reach',
		pic='media/items/legendaries/2.4/weapons/wilkens_reach.png',
		unique='Removes the cooldown of Grasp of the Dead',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	wilkensReach.save()
	wilkensReach.affixes.add(dmg, inte, chc, wilkensGraspOfTheDead)


	for weapon in Weapon.objects.filter(category='Mojos'):
		weapon.owner = 'wd'
		weapon.save()


def load_crusader_shields(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix.objects.get(category='Crusader Shields',
		affix='stre')
	blockChance = Affix.objects.get(category='Crusader Shields',
		affix='blockChance')

	frydehrsCondemn = Affix.objects.get(category='Crusader Shields',
		affix='frydehrsCondemn')

	jekangbordBlessedShield = Affix.objects.get(category='Crusader Shields',
		affix='jekangbordBlessedShield')

	unrelentingPhalanxDmg = Affix.objects.get(category='Crusader Shields',
		affix='unrelentingPhalanxDmg')

	akaratsAwakening = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Akarat\'s Awakening',
		pic='media/items/legendaries/offhands/crusadershields/akarats_awakening.png',
		unique='Every successful Block has a <span>20 - 25%</span> chance to reduce all cooldowns by <span class="silver">1</span> second',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>',
		patch='23')
	akaratsAwakening.save()
	akaratsAwakening.affixes.add(stre, blockChance)

#2.4
	frydehrsWrath = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Frydehr\'s Wrath',
		pic='media/items/legendaries/offhands/crusadershields/frydehrs_wrath.png',
		unique='Condemn has no cooldown but instead costs <span class="silver">40</span> Wrath',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		patch='24')
	frydehrsWrath.save()
	frydehrsWrath.affixes.add(stre, frydehrsCondemn)

	guardOfJohanna = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Guard Of Johanna',
		pic='media/items/legendaries/offhands/crusadershields/guard_of_johanna.png',
		unique='Blessed Hammer damage is increased by <span>200 - 250%</span> for the first <span class="silver">3</span> enemies it hits',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		patch='23')
	guardOfJohanna.save()
	guardOfJohanna.affixes.add(stre)

	hallowedBulwark = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Hallowed Bulwark',
		pic='media/items/legendaries/offhands/crusadershields/hallowed_bulwark.png',
		unique='Iron Skin also increases your Block Amount by <span>45 - 60%</span>',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		patch='23')
	hallowedBulwark.save()
	hallowedBulwark.affixes.add(stre)

	hellskull = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Hellskull',
		pic='media/items/legendaries/offhands/crusadershields/hellskull.png',
		unique='Gain <span class="silver">10%</span> increased damage while wielding a Two-Handed Weapon',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		patch='23')
	hellskull.save()
	hellskull.affixes.add(stre)

#2.4
	jekangbord = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Jekangbord',
		pic='media/items/legendaries/offhands/crusadershields/jekangbord.png',
		unique='Blessed Shield ricochets to <span>4 - 6</span> additional enemies',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		patch='24')
	jekangbord.save()
	jekangbord.affixes.add(stre, jekangbordBlessedShield)

	piroMarella = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Piro Marella',
		pic='media/items/legendaries/offhands/crusadershields/piro_marella.png',
		unique='Reduces the Wrath cost of Shield Bash by <span>40 - 50%</span>',
		random_primaries='4',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		patch='23')
	piroMarella.save()
	# piroMarella.affixes.add()

	salvation = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Salvation',
		pic='media/items/legendaries/offhands/crusadershields/salvation.png',
		unique='Blocked attacks heal you and your allies for <span>20 - 30%</span> of the amount blocked',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>',
		patch='23')
	salvation.save()
	salvation.affixes.add(stre, blockChance)

	#2.4 new
	shieldOfFury = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Shield of Fury',
		pic='media/items/legendaries/2.4/weapons/shield_of_fury.png',
		unique='Each time an enemy takes damage from your Heaven\'s Fury, it increases the damage they take from your Heaven\'s Fury by <span>15 - 20%</span>',
		random_primaries='3',
		random_secondaries='1',
		patch='24')
	shieldOfFury.save()
	shieldOfFury.affixes.add(stre)

	sublimeConviction = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Sublime Conviction',
		pic='media/items/legendaries/offhands/crusadershields/sublime_conviction.png',
		unique='When you Block, you have up to a <span>15 - 20%</span> chance to Stun the attacker for <span class="silver">1.5</span> seconds based on your current Wrath',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>',
		patch='23')
	sublimeConviction.save()
	sublimeConviction.affixes.add(stre, blockChance)

	theFinalWitness = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='The Final Witness',
		pic='media/items/legendaries/offhands/crusadershields/the_final_witness.png',
		unique='Shield Glare now hits all enemies around you',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		patch='23')
	theFinalWitness.save()
	theFinalWitness.affixes.add(stre)

#2.4
	unrelentingPhalanx = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Unrelenting Phalanx',
		pic='media/items/legendaries/offhands/crusadershields/unrelenting_phalanx.png',
		unique='Phalanx now casts twice',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		patch='24')
	unrelentingPhalanx.save()
	unrelentingPhalanx.affixes.add(stre, unrelentingPhalanxDmg)

	for weapon in Weapon.objects.filter(category='Crusader Shields'):
		weapon.owner = 'cs'
		weapon.save()


def load_shields(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(category='Shields',
		affix='mainStat')
	vita = Affix.objects.get(category='Shields',
		affix='vita')
	allRes = Affix.objects.get(category='Shields',
		affix='allRes')
	blockChance = Affix.objects.get(category='Shields',
		affix='blockChance')
	thorns = Affix.objects.get(category='Shields',
		affix='thorns')

	lidlessEleDmg = Affix.objects.get(category='Shields',
		affix='lidlessEleDmg')
	lidlessMaxResource = Affix.objects.get(category='Shields',
		affix='lidlessMaxResource')
	stormReducedMeleeDmg = Affix.objects.get(category='Shields',
		affix='stormReducedMeleeDmg')


	covensCriterion = Weapon(slot='Offhands',
		category='Shields',
		name='Coven\'s Criterion',
		pic='media/items/legendaries/offhands/shields/covens_criterion.png',
		unique='You take <span>45 - 60%</span> less damage from blocked attacks',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>',
		owner='all',
		patch='23')
	covensCriterion.save()
	covensCriterion.affixes.add(vita, blockChance)

	defenderOfWestmarch = Weapon(slot='Offhands',
		category='Shields',
		name='Defender of Westmarch',
		pic='media/items/legendaries/offhands/shields/defender_of_westmarch.png',
		unique='Blocks have a chance of summoning a charging wolf that deals <span>800 - 1000%</span> weapon damage to all enemies it passes through',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>',
		owner='all',
		patch='23')
	defenderOfWestmarch.save()
	defenderOfWestmarch.affixes.add(mainStat, blockChance)

	denial = Weapon(slot='Offhands',
		category='Shields',
		name='Denial',
		pic='media/items/legendaries/offhands/shields/denial.png',
		unique='Each enemy hit by your Sweep Attack increases the damage of your next Sweep Attack by <span class="silver">30 - 40%</span>, stacking up to <span>5</span> times',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		owner='cs',
		patch='23')
	denial.save()
	denial.affixes.add(mainStat)

	eberliCharo = Weapon(slot='Offhands',
		category='Shields',
		name='Eberli Charo',
		pic='media/items/legendaries/offhands/shields/eberli_charo.png',
		unique='Reduces the cooldown of Heaven\'s Fury by <span>45 - 50%</span>',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		owner='cs',
		patch='23')
	eberliCharo.save()
	eberliCharo.affixes.add(mainStat)

	freezeOfDeflection = Weapon(slot='Offhands',
		category='Shields',
		name='Freeze of Deflection',
		pic='media/items/legendaries/offhands/shields/freeze_of_deflection.png',
		unique='Blocking an attack has a chance to Freeze the attacker for <span>0.5 - 1.5</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		owner='all',
		patch='23')
	freezeOfDeflection.save()
	freezeOfDeflection.affixes.add(mainStat)

	ivoryTower = Weapon(slot='Offhands',
		category='Shields',
		name='Ivory Tower',
		pic='media/items/legendaries/offhands/shields/ivory_tower.png',
		unique='Blocks release forward a Fires of Heaven',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		owner='cs',
		patch='23')
	ivoryTower.save()
	ivoryTower.affixes.add(mainStat, vita)

	lidlessWall = Weapon(slot='Offhands',
		category='Shields',
		name='Lidless Wall',
		pic='media/items/legendaries/offhands/shields/lidless_wall.png',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		owner='all',
		patch='23')
	lidlessWall.save()
	lidlessWall.affixes.add(mainStat, lidlessEleDmg, lidlessMaxResource)

	stormshield = Weapon(slot='Offhands',
		category='Shields',
		name='Stormshield',
		pic='media/items/legendaries/offhands/shields/stormshield.png',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>19.0 - 24.0%</span> Block Chance</span>',
		owner='all',
		patch='23')
	stormshield.save()
	stormshield.affixes.add(mainStat, stormReducedMeleeDmg)

	votoyiasSpiker = Weapon(slot='Offhands',
		category='Shields',
		name='Vo\'Toyias Spiker',
		pic='media/items/legendaries/offhands/shields/votoyias_spiker.png',
		unique='Enemies affected by Provoke take double damage from Thorns',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		owner='cs',
		patch='23')
	votoyiasSpiker.save()
	votoyiasSpiker.affixes.add(mainStat, thorns)

	wallOfBone = Weapon(slot='Offhands',
		category='Shields',
		name='Wall of Bone',
		pic='media/items/legendaries/offhands/shields/wall_of_man.png',
		unique='<span>20 - 30%</span> chance to be protected by a Shield of Bones when you are hit',
		random_primaries='4',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>',
		owner='all',
		patch='23')
	wallOfBone.save()
	# wallOfBone.affixes.add()


def load_slugs(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")

	for weapon in Weapon.objects.all():
		weapon.name_slug = slugify(weapon.name)
		weapon.slot_slug = slugify(weapon.slot)
		weapon.category_slug = slugify(weapon.category)
		weapon.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0003_2h_weapons'),
    ]

    operations = [
        migrations.RunPython(load_sources),
        migrations.RunPython(load_quivers),
        migrations.RunPython(load_mojos),
        migrations.RunPython(load_crusader_shields),
        migrations.RunPython(load_shields),
        migrations.RunPython(load_slugs)
    ]
