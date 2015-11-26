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
		pic='/assets/media/items/legendaries/offhands/sources/cosmic_strand.png',
		unique='Teleport gains the effect of the Wormhole rune.',
		random_primaries='4',
		random_secondaries='1',
		notes='crafted')
	cosmicStrand.save()
	cosmicStrand.affixes.add(dmg)

	lightOfGrace = Weapon(slot='Offhands',
		category='Sources',
		name='Light of Grace',
		pic='/assets/media/items/legendaries/offhands/sources/light_of_grace.png',
		unique='Ray of Frost now pierces.',
		random_primaries='2',
		random_secondaries='1')
	lightOfGrace.save()
	lightOfGrace.affixes.add(dmg, inte, chc)

	mirrorball = Weapon(slot='Offhands',
		category='Sources',
		name='Mirrorball',
		pic='/assets/media/items/legendaries/offhands/sources/mirrorball.png',
		unique='Magic Missile fires <span>1 - 2</span> extra missiles.',
		random_primaries='2',
		random_secondaries='1')
	mirrorball.save()
	mirrorball.affixes.add(dmg, inte, chc)

	mykensBallOfHate = Weapon(slot='Offhands',
		category='Sources',
		name='Myken\'s Ball of Hate',
		pic='/assets/media/items/legendaries/offhands/sources/mykens_ball_of_hate.png',
		unique='Electrocute can chain to enemies that have already been hit.',
		random_primaries='2',
		random_secondaries='1')
	mykensBallOfHate.save()
	mykensBallOfHate.affixes.add(dmg, inte, chc)

	theOculus = Weapon(slot='Offhands',
		category='Sources',
		name='The Oculus',
		pic='/assets/media/items/legendaries/offhands/sources/the_oculus.png',
		unique='Taking damage has up to a <span>15 - 20%</span> chance to reset the cooldown on Teleport.',
		random_primaries='',
		random_secondaries='')
	theOculus.save()
	theOculus.affixes.add(dmg, inte, chc, apCrit)

	triumvirate = Weapon(slot='Offhands',
		category='Sources',
		name='Triumvirate',
		pic='/assets/media/items/legendaries/offhands/sources/triumvirate.png',
		unique='Your Signature Spells increase the damage of Arcane Orb by <span>75 - 100%</span> for <span class="silver">6</span> seconds, stacking up to <span class="silver">3</span> times.',
		random_primaries='2',
		random_secondaries='1')
	triumvirate.save()
	triumvirate.affixes.add(dmg, inte, chc)

	winterFlurry = Weapon(slot='Offhands',
		category='Sources',
		name='Winter Flurry',
		pic='/assets/media/items/legendaries/offhands/sources/winter_flurry.png',
		unique='Enemies killed by Cold damage have a <span>15 - 20%</span> chance to release a Frost Nova.',
		random_primaries='2',
		random_secondaries='1')
	winterFlurry.save()
	winterFlurry.affixes.add(dmg, inte, chc, winterColdDmg)

	for weapon in Weapon.objects.filter(category="Sources"):
		weapon.owner = 'wiz'
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


	archfiendArrows = Weapon(slot='Offhands',
		category='Quivers',
		name='Archfiend Arrows',
		pic='/assets/media/items/legendaries/offhands/quivers/archfiend_arrows.png',
		random_primaries='2',
		random_secondaries='2')
	archfiendArrows.save()
	archfiendArrows.affixes.add(ias, chc, eliteDmg)

	bombadiersRucksack = Weapon(slot='Offhands',
		category='Quivers',
		name='Bombadier\'s Rucksack',
		pic='/assets/media/items/legendaries/offhands/quivers/bombardiers_rucksack.png',
		unique='You may have <span class="silver">2</span> additional Sentries.',
		random_primaries='2',
		random_secondaries='1')
	bombadiersRucksack.save()
	bombadiersRucksack.affixes.add(dext, ias, chc)

	deadMansLegacy = Weapon(slot='Offhands',
		category='Quivers',
		name='DeadMan\'s Legacy',
		pic='/assets/media/items/legendaries/offhands/quivers/dead_mans_legacy.png',
		unique='Multishot hits enemies below <span>50 - 60%</span> health twice.',
		random_primaries='2',
		random_secondaries='1')
	deadMansLegacy.save()
	deadMansLegacy.affixes.add(dext, ias, chc)

	emimeisDuffel = Weapon(slot='Offhands',
		category='Quivers',
		name='Emimei\'s Duffel',
		pic='/assets/media/items/legendaries/offhands/quivers/emimeis_duffel.png',
		unique='Bolas now explode instantly.',
		random_primaries='3',
		random_secondaries='1')
	emimeisDuffel.save()
	emimeisDuffel.affixes.add(dext, ias)

	fletchersPride = Weapon(slot='Offhands',
		category='Quivers',
		name='Fletcher\'s Pride',
		pic='/assets/media/items/legendaries/offhands/quivers/fletchers_pride.png',
		random_primaries='2',
		random_secondaries='2')
	fletchersPride.save()
	fletchersPride.affixes.add(dext, ias, rcr)

	holyPointShot = Weapon(slot='Offhands',
		category='Quivers',
		name='Holy Point Shot',
		pic='/assets/media/items/legendaries/offhands/quivers/holy_point_shot.png',
		random_primaries='2',
		random_secondaries='2')
	holyPointShot.save()
	holyPointShot.affixes.add(dext, ias, holyEleDmg)

	meticulousBolts = Weapon(slot='Offhands',
		category='Quivers',
		name='Meticulous Bolts',
		pic='/assets/media/items/legendaries/offhands/quivers/meticulous_bolts.png',
		unique='Elemental Arrow - Ball Lightning now travels at <span>30 - 40%</span> speed.',
		random_primaries='3',
		random_secondaries='1')
	meticulousBolts.save()
	meticulousBolts.affixes.add(dext, ias)

	sinSeekers = Weapon(slot='Offhands',
		category='Quivers',
		name='Sin Seekers',
		pic='/assets/media/items/legendaries/offhands/quivers/sin_seekers.png',
		random_primaries='2',
		random_secondaries='2')
	sinSeekers.save()
	sinSeekers.affixes.add(dext, ias, chc)

	spinesOfSeethingHatred = Weapon(slot='Offhands',
		category='Quivers',
		name='Spines of Seeth ingHatred',
		pic='/assets/media/items/legendaries/offhands/quivers/spines_of_seething_hatred.png',
		unique='Chakram now generates <span>3 - 4</span> Hatred.',
		random_primaries='3',
		random_secondaries='1')
	spinesOfSeethingHatred.save()
	spinesOfSeethingHatred.affixes.add(dext, ias)

	theNinthCirriSatchel = Weapon(slot='Offhands',
		category='Quivers',
		name='The Ninth Cirri Satchel',
		pic='/assets/media/items/legendaries/offhands/quivers/the_ninth_cirri_satchel.png',
		unique='Hungering Arrow has <span>20 - 25%</span> additional chance to pierce.',
		random_primaries='3',
		random_secondaries='1')
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

	thingItemPickup = Affix.objects.get(category='Mojos',
		affix='thingItemPickup')


	gazingDemise = Weapon(slot='Offhands',
		category='Mojos',
		name='Gazing Demise',
		pic='/assets/media/items/legendaries/offhands/mojos/gazing_demise.png',
		random_primaries='1',
		random_secondaries='2')
	gazingDemise.save()
	gazingDemise.affixes.add(dmg, inte, lps, manaRegen)

	henrisPerquisition = Weapon(slot='Offhands',
		category='Mojos',
		name='Henri\'s Perquisition',
		pic='/assets/media/items/legendaries/offhands/mojos/henris_perquisition.png',
		unique='The first time an enemy deals damage to you, reduce that damage by <span>60 - 80%</span> and Charm the enemy for <span class="silver">3</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	henrisPerquisition.save()
	henrisPerquisition.affixes.add(dmg, inte, chc, durability)

	homunculus = Weapon(slot='Offhands',
		category='Mojos',
		name='homunculus',
		pic='/assets/media/items/legendaries/offhands/mojos/homunculus.png',
		unique='A Zombie Dog is automatically summoned to your side every <span class="silver">2</span> seconds.',
		random_primaries='2')
	homunculus.save()
	homunculus.affixes.add(dmg, inte, chc, sacrifice, maxMana)

	shukranisTriumph = Weapon(slot='Offhands',
		category='Mojos',
		name='Shukrani\'s Triumph',
		pic='/assets/media/items/legendaries/offhands/mojos/shukranis_triumph.png',
		unique='Spirit Walk lasts until you attack or until an enemy is within <span class="silver">30</span> yards of you.',
		random_primaries='1',
		random_secondaries='1')
	shukranisTriumph.save()
	shukranisTriumph.affixes.add(dmg, inte, chc, manaRegen)

	spite = Weapon(slot='Offhands',
		category='Mojos',
		name='spite',
		pic='/assets/media/items/legendaries/offhands/mojos/spite.png',
		random_primaries='3',
		random_secondaries='1')
	spite.save()
	spite.affixes.add(dmg, chc, maxMana)

	thingOfTheDeep = Weapon(slot='Offhands',
		category='Mojos',
		name='Thing Of The Deep',
		pic='/assets/media/items/legendaries/offhands/mojos/thing_of_the_deep.png',
		random_primaries='1')
	thingOfTheDeep.save()
	thingOfTheDeep.affixes.add(dmg, inte, chc, manaRegen, maxMana, thingItemPickup)

	uhkapianSerpent = Weapon(slot='Offhands',
		category='Mojos',
		name='Uhkapian Serpent',
		pic='/assets/media/items/legendaries/offhands/mojos/uhkapian_serpent.png',
		unique='<span>25 - 30%</span> of the damage you take is redirected to your Zombie Dogs.',
		random_primaries='2',
		random_secondaries='1')
	uhkapianSerpent.save()
	uhkapianSerpent.affixes.add(dmg, inte, chc)

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

	akaratsAwakening = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Akarat\'s Awakening',
		pic='/assets/media/items/legendaries/offhands/crusadershields/akarats_awakening.png',
		unique='Every successful block has a <span>20 - 25%</span> chance to reduce all cooldowns by <span class="silver">1</span> second.',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>')
	akaratsAwakening.save()
	akaratsAwakening.affixes.add(stre, blockChance)

	frydehrsWrath = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Frydehr\'s Wrath',
		pic='/assets/media/items/legendaries/offhands/crusadershields/frydehrs_wrath.png',
		unique='Condemn has no cooldown but instead costs <span class="silver">40</span> Wrath.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	frydehrsWrath.save()
	frydehrsWrath.affixes.add(stre)

	guardOfJohanna = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Guard Of Johanna',
		pic='/assets/media/items/legendaries/offhands/crusadershields/guard_of_johanna.png',
		unique='Blessed Hammer damage is increased by <span>200 - 250%</span> for the first <span class="silver">3</span> enemies it hits.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	guardOfJohanna.save()
	guardOfJohanna.affixes.add(stre)

	hallowedBulwark = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Hallowed Bulwark',
		pic='/assets/media/items/legendaries/offhands/crusadershields/hallowed_bulwark.png',
		unique='Iron Skin also increases your Block Amount by <span>45 - 60%</span>.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	hallowedBulwark.save()
	hallowedBulwark.affixes.add(stre)

	hellskull = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='hellskull',
		pic='/assets/media/items/legendaries/offhands/crusadershields/hellskull.png',
		unique='Gain <span class="silver">10%</span> increased damage while wielding a two-handed weapon.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	hellskull.save()
	hellskull.affixes.add(stre)

	jekangbord = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='jekangbord',
		pic='/assets/media/items/legendaries/offhands/crusadershields/jekangbord.png',
		unique='Blessed Shield ricochets to <span>4 - 6</span> additional enemies.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	jekangbord.save()
	jekangbord.affixes.add(stre)

	piroMarella = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Piro Marella',
		pic='/assets/media/items/legendaries/offhands/crusadershields/piro_marella.png',
		unique='Reduces the Wrath cost of Shield Bash by <span>40 - 50%</span>.',
		random_primaries='4',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	piroMarella.save()
	piroMarella.affixes.add()

	salvation = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='salvation',
		pic='/assets/media/items/legendaries/offhands/crusadershields/salvation.png',
		unique='Blocked attacks heal you and your allies for <span>20 - 30%</span> of the amount blocked.',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>')
	salvation.save()
	salvation.affixes.add(stre, blockChance)

	sublimeConviction = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Sublime Conviction',
		pic='/assets/media/items/legendaries/offhands/crusadershields/sublime_conviction.png',
		unique='When you block, you have up to a <span>15 - 20%</span> chance to Stun the attacker for <span class="silver">1.5</span> seconds based on your current Wrath.',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>')
	sublimeConviction.save()
	sublimeConviction.affixes.add(stre, blockChance)

	theFinalWitness = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='The Final Witness',
		pic='/assets/media/items/legendaries/offhands/crusadershields/the_final_witness.png',
		unique='Shield Glare now hits all enemies around you.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	theFinalWitness.save()
	theFinalWitness.affixes.add(stre)

	unrelentingPhalanx = Weapon(slot='Offhands',
		category='Crusader Shields',
		name='Unrelenting Phalanx',
		pic='/assets/media/items/legendaries/offhands/crusadershields/unrelenting_phalanx.png',
		unique='Phalanx now casts twice.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	unrelentingPhalanx.save()
	unrelentingPhalanx.affixes.add(stre)

	for weapon in Weapon.objects.filter(category='Crusader Shields'):
		weapon.owner = 'sader'
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
		pic='/assets/media/items/legendaries/offhands/shields/covens_criterion.png',
		unique='You take <span>45 - 60%</span> less damage from blocked attacks.',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>')
	covensCriterion.save()
	covensCriterion.affixes.add(vita, blockChance)

	defenderOfWestmarch = Weapon(slot='Offhands',
		category='Shields',
		name='Defender Of Westmarch',
		pic='/assets/media/items/legendaries/offhands/shields/defender_of_westmarch.png',
		unique='Blocks have a chance of summoning a charging wolf that deals <span>800 - 1000%</span> weapon damage to all enemies it passes through.',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>21.0 - 31.0%</span> Block Chance</span>')
	defenderOfWestmarch.save()
	defenderOfWestmarch.affixes.add(mainStat, blockChance)

	denial = Weapon(slot='Offhands',
		category='Shields',
		name='denial',
		pic='/assets/media/items/legendaries/offhands/shields/denial.png',
		unique='Each enemy hit by your Sweep Attack increases the damage of your next Sweep Attack by <span class="silver">30 - 40%</span>, stacking up to <span>5</span> times.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	denial.save()
	denial.affixes.add(mainStat)

	eberliCharo = Weapon(slot='Offhands',
		category='Shields',
		name='Eberli Charo',
		pic='/assets/media/items/legendaries/offhands/shields/eberli_charo.png',
		unique='Reduces the cooldown of Heaven\'s Fury by <span>45 - 50%</span>.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	eberliCharo.save()
	eberliCharo.affixes.add(mainStat)

	freezeOfDeflection = Weapon(slot='Offhands',
		category='Shields',
		name='Freeze Of Deflection',
		pic='/assets/media/items/legendaries/offhands/shields/freeze_of_deflection.png',
		unique='Blocking an attack has a chance to Freeze the attacker for <span>0.5 - 1.5</span> seconds.',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	freezeOfDeflection.save()
	freezeOfDeflection.affixes.add(mainStat)

	ivoryTower = Weapon(slot='Offhands',
		category='Shields',
		name='Ivory Tower',
		pic='/assets/media/items/legendaries/offhands/shields/ivory_tower.png',
		unique='Blocks release forward a Fires of Heaven.',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	ivoryTower.save()
	ivoryTower.affixes.add(mainStat, vita)

	lidlessWall = Weapon(slot='Offhands',
		category='Shields',
		name='Lidless Wall',
		pic='/assets/media/items/legendaries/offhands/shields/lidless_wall.png',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	lidlessWall.save()
	lidlessWall.affixes.add(mainStat, lidlessEleDmg, lidlessMaxResource)

	stormshield = Weapon(slot='Offhands',
		category='Shields',
		name='stormshield',
		pic='/assets/media/items/legendaries/offhands/shields/stormshield.png',
		random_primaries='3',
		random_secondaries='1',
		inherent='<span class="inherent"><span>19.0 - 24.0%</span> Block Chance</span>')
	stormshield.save()
	stormshield.affixes.add(mainStat, stormReducedMeleeDmg)

	votoyiasSpiker = Weapon(slot='Offhands',
		category='Shields',
		name='Vo\'Toyias Spiker',
		pic='/assets/media/items/legendaries/offhands/shields/votoyias_spiker.png',
		unique='Enemies affected by Provoke take double damage from Thorns.',
		random_primaries='2',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	votoyiasSpiker.save()
	votoyiasSpiker.affixes.add(mainStat, thorns)

	wallOfBone = Weapon(slot='Offhands',
		category='Shields',
		name='Wall Of Bone',
		pic='/assets/media/items/legendaries/offhands/shields/wall_of_man.png',
		unique='<span>20 - 30%</span> chance to be protected by a shield of bones when you are hit.',
		random_primaries='4',
		random_secondaries='1',
		inherent='<span class="inherent"><span>10.0 - 20.0%</span> Block Chance</span>')
	wallOfBone.save()
	# wallOfBone.affixes.add()

	for weapon in Weapon.objects.filter(category='Shields'):
		weapon.owner = 'all'
		weapon.save()


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
