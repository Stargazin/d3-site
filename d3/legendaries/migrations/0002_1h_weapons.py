# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_1h_axes(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(affix='mainStat',
		category='1H Axes')
	bleedChance = Affix.objects.get(affix='bleedChance',
		category='1H Axes')
	sockets = Affix.objects.get(affix='sockets',
		category='1H Axes')

	burningFireDmg = Affix.objects.get(affix='burningFireDmg',
		category='1H Axes')
	utarsColdDmg = Affix.objects.get(affix='utarsColdDmg',
		category='1H Axes')

	fleshTearer = Weapon(slot='1H Weapons',
		name='Flesh Tearer',
		pic='/assets/media/items/legendaries/weapons/1h/axes/flesh_tearer.png',
		category='1H Axes',
		random_primaries='2',
		random_secondaries='2')
	fleshTearer.save()
	fleshTearer.affixes.add(bleedChance)

	genzaniku = Weapon(slot='1H Weapons',
		name='Genzaniku',
		pic='/assets/media/items/legendaries/weapons/1h/axes/genzaniku.png',
		category='1H Axes',
		unique='Chance to summon a ghostly Fallen Champion when attacking.',
		random_primaries='3',
		random_secondaries='1')
	genzaniku.save()
	# genzaniku.affixes.add()

	hack = Weapon(slot='1H Weapons',
		name='Hack',
		pic='/assets/media/items/legendaries/weapons/1h/axes/hack.png',
		category='1H Axes',
		unique='<span>75 - 100%</span> of your Thorns damage is applied on every attack.',
		random_primaries='2',
		random_secondaries='1')
	hack.save()
	hack.affixes.add(sockets)

	skySplitter = Weapon(slot='1H Weapons',
		name='Sky Splitter',
		pic='/assets/media/items/legendaries/weapons/1h/axes/sky_splitter.png',
		category='1H Axes',
		unique='<span>15 - 20%</span> chance to Smite enemies for <span>600 - 750%</span> weapon damage as Lightning when you hit them.',
		random_primaries='2',
		random_secondaries='1')
	skySplitter.save()
	skySplitter.affixes.add(mainStat)

	theBurningAxeOfSankis = Weapon(slot='1H Weapons',
		name='The Burning Axe of Sankis',
		pic='/assets/media/items/legendaries/weapons/1h/axes/the_burning_axe_of_sankis.png',
		category='1H Axes',
		unique='Chance to fight through the pain when enemies hit you.',
		random_primaries='2',
		random_secondaries='1')
	theBurningAxeOfSankis.save()
	theBurningAxeOfSankis.affixes.add(burningFireDmg)

	theButchersSickle = Weapon(slot='1H Weapons',
		name='The Butcher\'s Sickle',
		pic='/assets/media/items/legendaries/weapons/1h/axes/the_butchers_sickle.png',
		category='1H Axes',
		unique='<span>20 - 25%</span> chance to drag enemies to you when attacking.',
		random_primaries='3',
		random_secondaries='1')
	theButchersSickle.save()
	# theButchersSickle.affixes.add()

	utarsRoar = Weapon(slot='1H Weapons',
		name='Utar\'s Roar',
		pic='/assets/media/items/legendaries/weapons/1h/axes/utars_roar.png',
		category='1H Axes',
		random_primaries='2',
		random_secondaries='2',
		notes='crafted')
	utarsRoar.save()
	utarsRoar.affixes.add(utarsColdDmg)

	for weapon in Weapon.objects.filter(category="1H Axes"):
		weapon.inherent = '<span class="inherent"><span>1.30</span> Attacks per Second</span>'
		weapon.save()


def load_ceremonial_knives(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	inte = Affix.objects.get(affix='inte',
		category='Ceremonial Knives')
	manaRegen = Affix.objects.get(affix='manaRegen',
		category='Ceremonial Knives')

	deadlyGraspOfTheDead = Affix.objects.get(affix='deadlyGraspOfTheDead',
		category='Ceremonial Knives')
	lastMassConfusionCDR = Affix.objects.get(affix='lastMassConfusionCDR',
		category='Ceremonial Knives')
	starmetalCHD = Affix.objects.get(affix='starmetalCHD',
		category='Ceremonial Knives')
	spiderCorpseSpiders = Affix.objects.get(affix='spiderCorpseSpiders',
		category='Ceremonial Knives')

	anessaziEdge = Weapon(slot='1H Weapons',
		name='Anessazi Edge',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/anessazi_edge.png',
		category='Ceremonial Knives',
		unique='Zombie Dogs stuns enemies around them for <span class="silver">1.5</span> seconds when summoned.',
		random_primaries='2',
		random_secondaries='1')
	anessaziEdge.save()
	anessaziEdge.affixes.add(inte)

	deadlyRebirth = Weapon(slot='1H Weapons',
		name='Deadly Rebirth',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/deadly_rebirth.png',
		category='Ceremonial Knives',
		unique='Grasp of the Dead gains the effect of the Rain of Corpses rune.',
		random_secondaries='1',
		notes='double check')
	deadlyRebirth.save()
	deadlyRebirth.affixes.add(inte, manaRegen, deadlyGraspOfTheDead)

	lastBreath = Weapon(slot='1H Weapons',
		name='Last Breath',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/last_breath.png',
		category='Ceremonial Knives',
		random_primaries='1',
		random_secondaries='2')
	lastBreath.save()
	lastBreath.affixes.add(inte, lastMassConfusionCDR)

	livingUmbralOath = Weapon(slot='1H Weapons',
		name='Living Umbral Oath',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/living_umbral_oath.png',
		category='Ceremonial Knives',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted')
	livingUmbralOath.save()
	# livingUmbralOath.affixes.add()

	rhenhoFlayer = Weapon(slot='1H Weapons',
		name='Rhen\'ho Flayer',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/rhenho_flayer.png',
		category='Ceremonial Knives',
		unique='Plague of Toads now seek out enemies and can explode twice.',
		random_primaries='2',
		random_secondaries='1')
	rhenhoFlayer.save()
	rhenhoFlayer.affixes.add(inte)

	sacredHarvester = Weapon(slot='1H Weapons',
		name='Sacred Harvester',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/sacred_harvester.png',
		category='Ceremonial Knives',
		unique='Soul Harvest now stacks up to <span class="silver">10</span> times.',
		random_primaries='2',
		random_secondaries='1')
	sacredHarvester.save()
	sacredHarvester.affixes.add(inte)

	starmetalKukri = Weapon(slot='1H Weapons',
		name='Starmetal Kukri',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/starmetal_kukri.png',
		category='Ceremonial Knives',
		unique='Reduce the cooldown of Fetish Army and Big Bad Voodoo by <span class="silver">1</span> second each time your fetishes deal damage.',
		random_primaries='1',
		random_secondaries='1')
	starmetalKukri.save()
	starmetalKukri.affixes.add(inte, starmetalCHD)

	theDaggerOfDarts = Weapon(slot='1H Weapons',
		name='The Dagger of Darts',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/the_dagger_of_darts.png',
		category='Ceremonial Knives',
		unique='Your Poison Darts and your Fetishes\' Poison Darts now pierce.',
		random_primaries='2',
		random_secondaries='1')
	theDaggerOfDarts.save()
	theDaggerOfDarts.affixes.add(inte)

	theGidbinn = Weapon(slot='1H Weapons',
		name='The Gidbinn',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/the_gidbinn.png',
		category='Ceremonial Knives',
		unique='Chance to summon a Fetish when attacking.',
		random_primaries='1',
		random_secondaries='1')
	theGidbinn.save()
	theGidbinn.affixes.add(inte, manaRegen)

	theSpiderQueensGrasp = Weapon(slot='1H Weapons',
		name='The Spider Queen\'s Grasp',
		pic='/assets/media/items/legendaries/weapons/1h/ceremonialknives/the_spider_queens_grasp.png',
		category='Ceremonial Knives',
		unique='Corpse Spiders releases a web on impact that Slows enemies by <span>60 - 80%</span>.',
		random_secondaries='1')
	theSpiderQueensGrasp.save()
	theSpiderQueensGrasp.affixes.add(inte, manaRegen, spiderCorpseSpiders)

	for weapon in Weapon.objects.filter(category="Ceremonial Knives"):
		weapon.inherent = '<span class="inherent"><span>1.40</span> Attacks per Second</span>'
		weapon.owner = 'wd'
		weapon.save()


def load_1h_daggers(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix.objects.get(affix='percentDmg', category='1H Daggers')
	mainStat = Affix.objects.get(affix='mainStat', category='1H Daggers')
	ias = Affix.objects.get(affix='ias', category='1H Daggers')

	pigBeastDmg = Affix.objects.get(affix='pigBeastDmg', category='1H Daggers')
	pigHumanDmg = Affix.objects.get(affix='pigHumanDmg', category='1H Daggers')
	barberCHD = Affix.objects.get(affix='barberCHD', category='1H Daggers')

	bloodMagicEdge = Weapon(slot='1H Weapons',
		name='Blood-Magic Edge',
		pic='/assets/media/items/legendaries/weapons/1h/daggers/bloodmagic_edge.png',
		category='1H Daggers',
		unique='Blood oozes from you.',
		random_primaries='2',
		random_secondaries='1',
		notes='crafted')
	bloodMagicEdge.save()
	bloodMagicEdge.affixes.add(ias)

	enviousBlade = Weapon(slot='1H Weapons',
		name='Envious Blade',
		pic='/assets/media/items/legendaries/weapons/1h/daggers/envious_blade.png',
		category='1H Daggers',
		unique='Gain <span class="silver">100%</span> Critical Hit Chance against enemies at full health.',
		random_primaries='2',
		random_secondaries='1')
	enviousBlade.save()
	enviousBlade.affixes.add(mainStat)

	eunjangdo = Weapon(slot='1H Weapons',
		name='Eun-jang-do',
		pic='/assets/media/items/legendaries/weapons/1h/daggers/eunjangdo.png',
		category='1H Daggers',
		unique='Attacking enemies below <span>17 - 20%</span> Life freezes them for <span class="silver">3</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	eunjangdo.save()
	eunjangdo.affixes.add(mainStat)

	kill = Weapon(slot='1H Weapons',
		name='Kill',
		pic='/assets/media/items/legendaries/weapons/1h/daggers/kill.png',
		category='1H Daggers',
		random_primaries='2',
		random_secondaries='2')
	kill.save()
	kill.affixes.add(ias)

	pigSticker = Weapon(slot='1H Weapons',
		name='Pig Sticker',
		pic='/assets/media/items/legendaries/weapons/1h/daggers/pig_sticker.png',
		category='1H Daggers',
		unique='Squeal!',
		random_primaries='3')
	pigSticker.save()
	pigSticker.affixes.add(mainStat, pigBeastDmg, pigHumanDmg)

	theBarber = Weapon(slot='1H Weapons',
		name='The Barber',
		pic='/assets/media/items/legendaries/weapons/1h/daggers/the_barber.png',
		category='1H Daggers',
		random_primaries='1',
		random_secondaries='1',
		notes='double check')
	theBarber.save()
	theBarber.affixes.add(mainStat, percentDmg, barberCHD)

	theHoradricHamburger = Weapon(slot='1H Weapons',
		name='The Horadric Hamburger',
		pic='/assets/media/items/legendaries/weapons/1h/daggers/the_horadric_hamburger.png',
		category='1H Daggers',
		random_primaries='2',
		random_secondaries='2')
	theHoradricHamburger.save()
	theHoradricHamburger.affixes.add(mainStat)

	wizardspike = Weapon(slot='1H Weapons',
		name='Wizardspike',
		pic='/assets/media/items/legendaries/weapons/1h/daggers/wizardspike.png',
		category='1H Daggers',
		unique='Performing an attack has a <span>20 - 25%</span> chance to hurl a Frozen Orb.',
		random_primaries='',
		random_secondaries='')
	wizardspike.save()
	wizardspike.affixes.add(mainStat)

	for weapon in Weapon.objects.filter(category="1H Daggers"):
		weapon.inherent = '<span class="inherent"><span>1.50</span> Attacks per Second</span>'
		weapon.save()


def load_fist_weapons(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix.objects.get(affix='percentDmg',
		category='Fist Weapons')
	dext = Affix.objects.get(affix='dext',
		category='Fist Weapons')
	bleedChance = Affix.objects.get(affix='bleedChance',
		category='Fist Weapons')
	lph = Affix.objects.get(affix='lph',
		category='Fist Weapons')
	lifePerSpirit = Affix.objects.get(affix='lifePerSpirit',
		category='Fist Weapons')
	spiritRegen = Affix.objects.get(affix='spiritRegen',
		category='Fist Weapons')

	durability = Affix.objects.get(affix='durability',
		category='Fist Weapons')

	rabidCHD = Affix.objects.get(affix='rabidCHD',
		category='Fist Weapons')
	rabidSlowChance = Affix.objects.get(affix='rabidSlowChance',
		category='Fist Weapons')
	sledgeStunChance = Affix.objects.get(affix='sledgeStunChance',
		category='Fist Weapons')
	wonLightDmg = Affix.objects.get(affix='wonLightDmg',
		category='Fist Weapons')

	crystalFist = Weapon(slot='1H Weapons',
		name='Crystal Fist',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/crystal_fist.png',
		category='Fist Weapons',
		random_primaries='1',
		random_secondaries='1')
	crystalFist.save()
	crystalFist.affixes.add(percentDmg, dext, durability)

	demonClaw = Weapon(slot='1H Weapons',
		name='Demon Claw',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/demon_claw.png',
		category='Fist Weapons',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted')
	demonClaw.save()
	demonClaw.affixes.add()

	fleshrake = Weapon(slot='1H Weapons',
		name='Fleshrake',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/fleshrake.png',
		category='Fist Weapons',
		random_primaries='1',
		random_secondaries='2')
	fleshrake.save()
	fleshrake.affixes.add(dext, lifePerSpirit)

	jawbreaker = Weapon(slot='1H Weapons',
		name='Jawbreaker',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/jawbreaker.png',
		category='Fist Weapons',
		unique='When Dashing Strike hits an enemy more than <span>30 - 35</span> yards away, its Charge cost is refunded.',
		random_primaries='2',
		random_secondaries='1')
	jawbreaker.save()
	jawbreaker.affixes.add(dext)

	lionsClaw = Weapon(slot='1H Weapons',
		name='Lion\'s Claw',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/lions_claw.png',
		category='Fist Weapons',
		unique='Seven-Sided Strike performs an additional <span class="silver">7</span> strikes.',
		random_primaries='2',
		random_secondaries='1')
	lionsClaw.save()
	lionsClaw.affixes.add(dext)

	logansClaw = Weapon(slot='1H Weapons',
		name='Logan\'s Claw',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/logans_claw.png',
		category='Fist Weapons',
		random_primaries='1',
		random_secondaries='2')
	logansClaw.save()
	logansClaw.affixes.add(dext, lph)

	rabidStrike = Weapon(slot='1H Weapons',
		name='Rabid Strike',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/rabid_strike.png',
		category='Fist Weapons',
		random_primaries='1',
		random_secondaries='1')
	rabidStrike.save()
	rabidStrike.affixes.add(dext, rabidCHD, rabidSlowChance)

	scarbringer = Weapon(slot='1H Weapons',
		name='Scarbringer',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/scarbringer.png',
		category='Fist Weapons',
		random_primaries='2',
		random_secondaries='2')
	scarbringer.save()
	scarbringer.affixes.add(bleedChance)

	sledgeFist = Weapon(slot='1H Weapons',
		name='Sledge Fist',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/sledge_fist.png',
		category='Fist Weapons',
		random_primaries='2',
		random_secondaries='1')
	sledgeFist.save()
	sledgeFist.affixes.add(dext, sledgeStunChance)

	theFistOfAzTurrasq = Weapon(slot='1H Weapons',
		name='The Fist of Az\'Turrasq',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/the_fist_of_azturrasq.png',
		category='Fist Weapons',
		unique='Exploding Palm\'s on-death explosion damage is increased by <span>75 - 100%</span>.',
		random_primaries='1',
		random_secondaries='1')
	theFistOfAzTurrasq.save()
	theFistOfAzTurrasq.affixes.add(dext, spiritRegen)

	vengefulWind = Weapon(slot='1H Weapons',
		name='Vengeful Wind',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/vengeful_wind.png',
		category='Fist Weapons',
		unique='Increases the maximum stack count of Sweeping Wind by <span class="silver">3</span>.',
		random_primaries='2',
		random_secondaries='1')
	vengefulWind.save()
	vengefulWind.affixes.add(dext)

	wonKhimLau = Weapon(slot='1H Weapons',
		name='Won Khim Lau',
		pic='/assets/media/items/legendaries/weapons/1h/fistweapons/won_khim_lau.png',
		category='Fist Weapons',
		random_primaries='2',
		random_secondaries='1')
	wonKhimLau.save()
	wonKhimLau.affixes.add(dext, wonLightDmg)

	for weapon in Weapon.objects.filter(category="Fist Weapons"):
		weapon.inherent = '<span class="inherent"><span>1.40</span> Attacks per Second</span>'
		weapon.owner = 'monk'
		weapon.save()


def load_1h_flails(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix.objects.get(affix='stre', category='1H Flails')
	sockets = Affix.objects.get(affix='sockets', category='1H Flails')

	goldenHolyDmg = Affix.objects.get(affix='goldenHolyDmg', category='1H Flails')

	darklight = Weapon(slot='1H Weapons',
		name='Darklight',
		pic='/assets/media/items/legendaries/weapons/1h/flails/darklight.png',
		category='1H Flails',
		unique='Fist of the Heavens has a <span>45 - 60%</span> chance to also be cast at your location.',
		random_primaries='2',
		random_secondaries='1')
	darklight.save()
	darklight.affixes.add(stre)

	goldenScourge = Weapon(slot='1H Weapons',
		name='Golden Scourge',
		pic='/assets/media/items/legendaries/weapons/1h/flails/golden_scourge.png',
		category='1H Flails',
		unique='Smite now jumps to <span class="silver">3</span> additional enemies.',
		random_primaries='2',
		random_secondaries='1')
	goldenScourge.save()
	goldenScourge.affixes.add(goldenHolyDmg)

	gyrfalconsFoote = Weapon(slot='1H Weapons',
		name='Gyrfalcon\'s Foote',
		pic='/assets/media/items/legendaries/weapons/1h/flails/gyrfalcons_foote.png',
		category='1H Flails',
		unique='Removes the resource cost of Blessed Shield.',
		random_primaries='2',
		random_secondaries='1')
	gyrfalconsFoote.save()
	gyrfalconsFoote.affixes.add(stre)

	inviolableFaith = Weapon(slot='1H Weapons',
		name='Inviolable Faith',
		pic='/assets/media/items/legendaries/weapons/1h/flails/inviolable_faith.png',
		category='1H Flails',
		unique='Casting Consecration also casts Consecration beneath all of your allies.',
		random_primaries='2',
		random_secondaries='1')
	inviolableFaith.save()
	inviolableFaith.affixes.add(sockets)

	johannasArgument = Weapon(slot='1H Weapons',
		name='Johanna\'s Argument',
		pic='/assets/media/items/legendaries/weapons/1h/flails/johannas_argument.png',
		category='1H Flails',
		unique='Increase the attack speed of Blessed Hammer by <span class="silver">100%</span>.',
		random_primaries='2',
		random_secondaries='1')
	johannasArgument.save()
	johannasArgument.affixes.add(stre)

	justiniansMercy = Weapon(slot='1H Weapons',
		name='Justinian\'s Mercy',
		pic='/assets/media/items/legendaries/weapons/1h/flails/justinians_mercy.png',
		category='1H Flails',
		unique='Blessed Hammer gains the effect of the Dominion rune.',
		random_primaries='2',
		random_secondaries='1')
	justiniansMercy.save()
	justiniansMercy.affixes.add(sockets)

	kassarsRetribution = Weapon(slot='1H Weapons',
		name='Kassar\'s Retribution',
		pic='/assets/media/items/legendaries/weapons/1h/flails/kassars_retribution.png',
		category='1H Flails',
		unique='Casting Justice increases your movement speed by <span>15 - 20%</span> for <span class="silver">2</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	kassarsRetribution.save()
	kassarsRetribution.affixes.add(stre)

	swiftmount = Weapon(slot='1H Weapons',
		name='Swiftmount',
		pic='/assets/media/items/legendaries/weapons/1h/flails/swiftmount.png',
		category='1H Flails',
		unique='Doubles the duration of Steed Charge.',
		random_primaries='2',
		random_secondaries='1')
	swiftmount.save()
	swiftmount.affixes.add(stre)

	for weapon in Weapon.objects.filter(category="1H Flails"):
		weapon.inherent = '<span class="inherent"><span>1.40</span> Attacks per Second</span>'
		weapon.owner = 'sader'
		weapon.save()


def load_hand_crossbows(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	dext = Affix.objects.get(affix='dext',
		category='Hand Crossbows')
	maxDisc = Affix.objects.get(affix='maxDisc',
		category='Hand Crossbows')
	sockets = Affix.objects.get(affix='sockets',
		category='Hand Crossbows')

	balefireFireDmg = Affix.objects.get(affix='balefireFireDmg',
		category='Hand Crossbows')
	dawnStunChance = Affix.objects.get(affix='dawnStunChance',
		category='Hand Crossbows')

	balefireCaster = Weapon(slot='1H Weapons',
		name='Balefire Caster',
		pic='/assets/media/items/legendaries/weapons/1h/handcrossbows/balefire_caster.png',
		category='Hand Crossbows',
		random_primaries='1',
		random_secondaries='2')
	balefireCaster.save()
	balefireCaster.affixes.add(dext, balefireFireDmg)

	blitzbolter = Weapon(slot='1H Weapons',
		name='Blitzbolter',
		pic='/assets/media/items/legendaries/weapons/1h/handcrossbows/blitzbolter.png',
		category='Hand Crossbows',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted')
	blitzbolter.save()
	# blitzbolter.affixes.add()

	calamity = Weapon(slot='1H Weapons',
		name='Calamity',
		pic='/assets/media/items/legendaries/weapons/1h/handcrossbows/calamity.png',
		category='Hand Crossbows',
		unique='Enemies you hit become Marked for Death.',
		random_primaries='2',
		random_secondaries='1')
	calamity.save()
	calamity.affixes.add(dext)

	dawn = Weapon(slot='1H Weapons',
		name='Dawn',
		pic='/assets/media/items/legendaries/weapons/1h/handcrossbows/dawn.png',
		category='Hand Crossbows',
		random_primaries='2',
		random_secondaries='1')
	dawn.save()
	dawn.affixes.add(dext, dawnStunChance)

	helltrapper = Weapon(slot='1H Weapons',
		name='Helltrapper',
		pic='/assets/media/items/legendaries/weapons/1h/handcrossbows/helltrapper.png',
		category='Hand Crossbows',
		unique='<span>7 - 10%</span> chance on hit to summon a Spike Trap, Caltrops or Sentry.',
		random_primaries='2',
		random_secondaries='1')
	helltrapper.save()
	helltrapper.affixes.add(dext)

	kmarTenclip = Weapon(slot='1H Weapons',
		name='K\'mar Tenclip',
		pic='/assets/media/items/legendaries/weapons/1h/handcrossbows/kmar_tenclip.png',
		category='Hand Crossbows',
		unique='Strafe gains the effect of the Drifting Shadow rune.',
		random_primaries='1',
		random_secondaries='1')
	kmarTenclip.save()
	kmarTenclip.affixes.add(dext, sockets)

	theDemonsDemise = Weapon(slot='1H Weapons',
		name='The Demon\'s Demise',
		pic='/assets/media/items/legendaries/weapons/1h/handcrossbows/the_demons_demise.png',
		category='Hand Crossbows',
		unique='Spike Trap - Sticky Trap spreads to nearby enemies when it explodes.',
		random_primaries='2',
		random_secondaries='1')
	theDemonsDemise.save()
	theDemonsDemise.affixes.add(dext)

	vallasBequest = Weapon(slot='1H Weapons',
		name='Valla\'s Bequest',
		pic='/assets/media/items/legendaries/weapons/1h/handcrossbows/vallas_bequest.png',
		category='Hand Crossbows',
		unique='Strafe projectiles pierce.',
		random_primaries='2')
	vallasBequest.save()
	vallasBequest.affixes.add(dext, maxDisc)

	for weapon in Weapon.objects.filter(category="Hand Crossbows"):
		weapon.inherent = '<span class="inherent"><span>1.60</span> Attacks per Second</span>'
		weapon.owner = 'dh'
		weapon.save()


def load_1h_maces(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix.objects.get(affix='percentDmg',
		category='1H Maces')
	mainStat = Affix.objects.get(affix='mainStat',
		category='1H Maces')
	ias = Affix.objects.get(affix='ias',
		category='1H Maces')
	sockets = Affix.objects.get(affix='sockets',
		category='1H Maces')

	killExp = Affix.objects.get(affix='killExp',
		category='1H Maces')

	devastatorFireDmg = Affix.objects.get(affix='devastatorFireDmg',
		category='1H Maces')
	echoingFearChance = Affix.objects.get(affix='echoingFearChance',
		category='1H Maces')
	jacesBlessedHammer = Affix.objects.get(affix='jacesBlessedHammer',
		category='1H Maces')
	nailbiterThorns = Affix.objects.get(affix='nailbiterThorns',
		category='1H Maces')
	neanderthalThorns = Affix.objects.get(affix='neanderthalThorns',
		category='1H Maces')
	nutcrackerCHD = Affix.objects.get(affix='nutcrackerCHD',
		category='1H Maces')
	nutcrackerStunChance = Affix.objects.get(affix='nutcrackerStunChance',
		category='1H Maces')
	odynLightDmg = Affix.objects.get(affix='odynLightDmg',
		category='1H Maces')
	sunEliteDmg = Affix.objects.get(affix='sunEliteDmg',
		category='1H Maces')
	sunExtraGold = Affix.objects.get(affix='sunExtraGold',
		category='1H Maces')


	devastator = Weapon(slot='1H Weapons',
		name='Devastator',
		pic='/assets/media/items/legendaries/weapons/1h/maces/devastator.png',
		category='1H Maces',
		random_primaries='2',
		random_secondaries='2',
		notes='crafted')
	devastator.save()
	devastator.affixes.add(devastatorFireDmg)

	echoingFury = Weapon(slot='1H Weapons',
		name='Echoing Fury',
		pic='/assets/media/items/legendaries/weapons/1h/maces/echoing_fury.png',
		category='1H Maces',
		random_secondaries='1')
	echoingFury.save()
	echoingFury.affixes.add(percentDmg, mainStat, ias, echoingFearChance)

	jacesHammerOfVigilance = Weapon(slot='1H Weapons',
		name='Jace\'s Hammer of Vigilance',
		pic='/assets/media/items/legendaries/weapons/1h/maces/jaces_hammer_of_vigilance.png',
		category='1H Maces',
		unique='Increase the size of your Blessed Hammers.',
		random_primaries='2',
		random_secondaries='1')
	jacesHammerOfVigilance.save()
	jacesHammerOfVigilance.affixes.add(jacesBlessedHammer)

	madMonarchsScepter = Weapon(slot='1H Weapons',
		name='Mad Monarch\'s Scepter',
		pic='/assets/media/items/legendaries/weapons/1h/maces/mad_monarchs_scepter.png',
		category='1H Maces',
		unique='After killing <span class="silver">10</span> enemies, you release a Poison Nova that deals <span>1050 - 1400%</span> weapon damage as Poison to enemies within <span class="silver">30</span> yards.',
		random_primaries='1',
		random_secondaries='1')
	madMonarchsScepter.save()
	madMonarchsScepter.affixes.add(percentDmg, mainStat)

	nailbiter = Weapon(slot='1H Weapons',
		name='Nailbiter',
		pic='/assets/media/items/legendaries/weapons/1h/maces/nailbiter.png',
		category='1H Maces',
		random_primaries='2',
		random_secondaries='1')
	nailbiter.save()
	nailbiter.affixes.add(percentDmg, nailbiterThorns)

	neanderthal = Weapon(slot='1H Weapons',
		name='Neanderthal',
		pic='/assets/media/items/legendaries/weapons/1h/maces/neanderthal.png',
		category='1H Maces',
		random_primaries='2')
	neanderthal.save()
	neanderthal.affixes.add(mainStat, neanderthalThorns, killExp)

	nutcracker = Weapon(slot='1H Weapons',
		name='Nutcracker',
		pic='/assets/media/items/legendaries/weapons/1h/maces/nutcracker.png',
		category='1H Maces',
		random_primaries='2',
		random_secondaries='1')
	nutcracker.save()
	nutcracker.affixes.add(nutcrackerCHD, nutcrackerStunChance)

	odynSon = Weapon(slot='1H Weapons',
		name='Odyn Son',
		pic='/assets/media/items/legendaries/weapons/1h/maces/odyn_son.png',
		category='1H Maces',
		unique='<span>20 - 40%</span> chance to Chain Lightning enemies when you hit them.',
		random_primaries='2',
		random_secondaries='1')
	odynSon.save()
	odynSon.affixes.add(odynLightDmg)

	solanium = Weapon(slot='1H Weapons',
		name='Solanium',
		pic='/assets/media/items/legendaries/weapons/1h/maces/solanium.png',
		category='1H Maces',
		unique='Critical Hits have a <span>3 - 4%</span> chance to spawn a health globe.',
		random_primaries='2',
		random_secondaries='1')
	solanium.save()
	solanium.affixes.add(sockets)

	sunKeeper = Weapon(slot='1H Weapons',
		name='Sun Keeper',
		pic='/assets/media/items/legendaries/weapons/1h/maces/sun_keeper.png',
		category='1H Maces',
		random_primaries='1',
		random_secondaries='1')
	sunKeeper.save()
	sunKeeper.affixes.add(mainStat, sunEliteDmg, sunExtraGold)

	telrandensHand = Weapon(slot='1H Weapons',
		name='Telranden\'s Hand',
		pic='/assets/media/items/legendaries/weapons/1h/maces/telrandens_hand.png',
		category='1H Maces',
		random_primaries='1',
		random_secondaries='2')
	telrandensHand.save()
	telrandensHand.affixes.add(mainStat, ias)

	for weapon in Weapon.objects.filter(category="1H Maces"):
		weapon.inherent = '<span class="inherent"><span>1.20</span> Attacks per Second</span>'
		weapon.save()

def load_1h_mighty_weapons(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix.objects.get(affix='stre',
		category='1H Mighty Weapons')
	bleedChance = Affix.objects.get(affix='bleedChance',
		category='1H Mighty Weapons')
	sockets = Affix.objects.get(affix='sockets',
		category='1H Mighty Weapons')

	fjordFreezeChance = Affix.objects.get(affix='fjordFreezeChance',
		category='1H Mighty Weapons')
	nightsLife = Affix.objects.get(affix='nightsLife',
		category='1H Mighty Weapons')

	ambosPride = Weapon(slot='1H Weapons',
		name='Ambo\'s Pride',
		pic='/assets/media/items/legendaries/weapons/1h/mightyweapons/ambos_pride.png',
		category='1H Mighty Weapons',
		random_primaries='1',
		random_secondaries='2')
	ambosPride.save()
	ambosPride.affixes.add(stre, bleedChance)

	bladeOfTheWarlord = Weapon(slot='1H Weapons',
		name='Blade of the Warlord',
		pic='/assets/media/items/legendaries/weapons/1h/mightyweapons/blade_of_the_warlord.png',
		category='1H Mighty Weapons',
		random_primaries='1',
		random_secondaries='2')
	bladeOfTheWarlord.save()
	bladeOfTheWarlord.affixes.add(stre, sockets)

	dishonoredLegacy = Weapon(slot='1H Weapons',
		name='Dishonored Legacy',
		pic='/assets/media/items/legendaries/weapons/1h/mightyweapons/dishonored_legacy.png',
		category='1H Mighty Weapons',
		unique='Cleave deals up to <span>300 - 400%</span> increased damage based on percentage of missing Fury.',
		random_primaries='2',
		random_secondaries='1')
	dishonoredLegacy.save()
	dishonoredLegacy.affixes.add(stre)

	fjordCutter = Weapon(slot='1H Weapons',
		name='Fjord Cutter',
		pic='/assets/media/items/legendaries/weapons/1h/mightyweapons/fjord_cutter.png',
		category='1H Mighty Weapons',
		unique='You are surrounded by a Chilling Aura when attacking.',
		random_primaries='2')
	fjordCutter.save()
	fjordCutter.affixes.add(stre, fjordFreezeChance)

	nightsReaping = Weapon(slot='1H Weapons',
		name='Night\'s Reaping',
		pic='/assets/media/items/legendaries/weapons/1h/mightyweapons/nights_reaping.png',
		category='1H Mighty Weapons',
		random_primaries='2',
		random_secondaries='2',
		notes='crafted')
	nightsReaping.save()
	nightsReaping.affixes.add(nightsLife)

	remorseless = Weapon(slot='1H Weapons',
		name='Remorseless',
		pic='/assets/media/items/legendaries/weapons/1h/mightyweapons/remorseless.png',
		category='1H Mighty Weapons',
		unique='Hammer of the Ancients has a <span>25 - 30%</span> chance to summon an Ancient for <span class="silver">20</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	remorseless.save()
	remorseless.affixes.add(stre)

	for weapon in Weapon.objects.filter(category="1H Mighty Weapons"):
		weapon.inherent = '<span class="inherent"><span>1.30</span> Attacks per Second</span>'
		weapon.owner = 'barb'
		weapon.save()


def load_1h_spears(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(affix='mainStat',
		category='1H Spears')
	eliteDmg = Affix.objects.get(affix='eliteDmg',
		category='1H Spears')

	akaneshHolyDmg = Affix.objects.get(affix='akaneshHolyDmg',
		category='1H Spears')
	scrimshawZombieCharger = Affix.objects.get(affix='scrimshawZombieCharger',
		category='1H Spears')
	threeWeaponThrow = Affix.objects.get(affix='threeWeaponThrow',
		category='1H Spears')
	threeAncientSpear = Affix.objects.get(affix='threeAncientSpear',
		category='1H Spears')

	akaneshTheHeraldOfRighteousness = Weapon(slot='1H Weapons',
		name='Akanesh, the Herald of Righteousness',
		pic='/assets/media/items/legendaries/weapons/1h/spears/akanesh_the_herald_of_righteousness.png',
		category='1H Spears',
		random_primaries='1',
		random_secondaries='2')
	akaneshTheHeraldOfRighteousness.save()
	akaneshTheHeraldOfRighteousness.affixes.add(mainStat, akaneshHolyDmg)

	arreatsLaw = Weapon(slot='1H Weapons',
		name='Arreat\'s Law',
		pic='/assets/media/items/legendaries/weapons/1h/spears/arreats_law.png',
		category='1H Spears',
		unique='Weapon Throw generates up to <span>15 - 20</span> additional Fury based on how far away the enemy hit is. Maximum benefit when the enemy hit is <span class="silver">20</span> or more yards away.',
		random_primaries='2',
		random_secondaries='1')
	arreatsLaw.save()
	arreatsLaw.affixes.add(mainStat)

	empyreanMessenger = Weapon(slot='1H Weapons',
		name='Empyrean Messenger',
		pic='/assets/media/items/legendaries/weapons/1h/spears/empyrean_messenger.png',
		category='1H Spears',
		random_primaries='1',
		random_secondaries='2')
	empyreanMessenger.save()
	empyreanMessenger.affixes.add(mainStat, eliteDmg)

	scrimshaw = Weapon(slot='1H Weapons',
		name='Scrimshaw',
		pic='/assets/media/items/legendaries/weapons/1h/spears/scrimshaw.png',
		category='1H Spears',
		unique='Reduces the Mana cost of Zombie Charger by <span>40 - 50%</span>.',
		random_primaries='1',
		random_secondaries='1')
	scrimshaw.save()
	scrimshaw.affixes.add(mainStat, scrimshawZombieCharger)

	theThreeHundredthSpear = Weapon(slot='1H Weapons',
		name='The Three Hundredth Spear',
		pic='/assets/media/items/legendaries/weapons/1h/spears/the_three_hundredth_spear.png',
		category='1H Spears',
		random_secondaries='2')
	theThreeHundredthSpear.save()
	theThreeHundredthSpear.affixes.add(mainStat, threeWeaponThrow, threeAncientSpear)

	for weapon in Weapon.objects.filter(category="1H Spears"):
		weapon.inherent = '<span class="inherent"><span>1.20</span> Attacks per Second</span>'
		weapon.save()


def load_1h_swords(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix.objects.get(affix='percentDmg',
		category='1H Swords')
	mainStat = Affix.objects.get(affix='mainStat',
		category='1H Swords')
	ias = Affix.objects.get(affix='ias',
		category='1H Swords')
	sockets = Affix.objects.get(affix='sockets',
		category='1H Swords')

	killExp = Affix.objects.get(affix='killExp',
		category='1H Swords')

	azurewrathColdDmg = Affix.objects.get(affix='azurewrathColdDmg',
		category='1H Swords')
	azurewrathFreezeChance = Affix.objects.get(affix='azurewrathFreezeChance',
		category='1H Swords')
	devilExtraGold = Affix.objects.get(affix='devilExtraGold',
		category='1H Swords')
	doombringerPhysDmg = Affix.objects.get(affix='doombringerPhysDmg',
		category='1H Swords')
	exarianCHD = Affix.objects.get(affix='exarianCHD',
		category='1H Swords')
	giftMovementSpeed = Affix.objects.get(affix='giftMovementSpeed',
		category='1H Swords')
	monsterBeastDmg = Affix.objects.get(affix='monsterBeastDmg',
		category='1H Swords')
	severDemonDmg = Affix.objects.get(affix='severDemonDmg',
		category='1H Swords')
	skycutterHolyDmg = Affix.objects.get(affix='skycutterHolyDmg',
		category='1H Swords')

	azurewrath = Weapon(slot='1H Weapons',
		name='Azurewrath',
		pic='/assets/media/items/legendaries/weapons/1h/swords/azurewrath.png',
		category='1H Swords',
		unique='Undead and Demon enemies within <span class="silver">25</span> yards take <span>500 - 650%</span> weapon damage as Holy every second and are sometimes knocked into the air.',
		random_primaries='2')
	azurewrath.save()
	azurewrath.affixes.add(azurewrathColdDmg, azurewrathFreezeChance)

	devilTongue = Weapon(slot='1H Weapons',
		name='Devil Tongue',
		pic='/assets/media/items/legendaries/weapons/1h/swords/devil_tongue.png',
		category='1H Swords',
		random_primaries='1',
		random_secondaries='1')
	devilTongue.save()
	devilTongue.affixes.add(percentDmg, mainStat, devilExtraGold)

	doombringer = Weapon(slot='1H Weapons',
		name='Doombringer',
		pic='/assets/media/items/legendaries/weapons/1h/swords/doombringer.png',
		category='1H Swords',
		random_primaries='1',
		random_secondaries='2')
	doombringer.save()
	doombringer.affixes.add(mainStat, doombringerPhysDmg)

	exarian = Weapon(slot='1H Weapons',
		name='Exarian',
		pic='/assets/media/items/legendaries/weapons/1h/swords/exarian.png',
		category='1H Swords',
		random_primaries='2',
		random_secondaries='2')
	exarian.save()
	exarian.affixes.add(exarianCHD)

	fulminator = Weapon(slot='1H Weapons',
		name='Fulminator',
		pic='/assets/media/items/legendaries/weapons/1h/swords/fulminator.png',
		category='1H Swords',
		unique='Lightning damage has a chance to turn enemies into lightning rods, causing them to pulse <span>444 - 555%</span> weapon damage as Lightning every second to nearby enemies for <span class="silver">6</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	fulminator.save()
	fulminator.affixes.add(mainStat)

	giftOfSilaria = Weapon(slot='1H Weapons',
		name='Gift of Silaria',
		pic='/assets/media/items/legendaries/weapons/1h/swords/gift_of_silaria.png',
		category='1H Swords',
		random_primaries='1',
		random_secondaries='2')
	giftOfSilaria.save()
	giftOfSilaria.affixes.add(mainStat, giftMovementSpeed)

	griswoldsPerfection = Weapon(slot='1H Weapons',
		name='Griswold\'s Perfection',
		pic='/assets/media/items/legendaries/weapons/1h/swords/griswolds_perfection.png',
		category='1H Swords',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted')
	griswoldsPerfection.save()
	# griswoldsPerfection.affixes.add()

	ingeom = Weapon(slot='1H Weapons',
		name='In-geom',
		pic='/assets/media/items/legendaries/weapons/1h/swords/in-geom.png',
		category='1H Swords',
		unique='Your skill cooldowns are reduced by <span>8 - 10</span> seconds for <span class="silver">15</span> seconds after killing an elite pack.',
		random_primaries='1',
		random_secondaries='1')
	ingeom.save()
	ingeom.affixes.add(percentDmg, mainStat)

	monsterHunter = Weapon(slot='1H Weapons',
		name='Monster Hunter',
		pic='/assets/media/items/legendaries/weapons/1h/swords/monster_hunter.png',
		category='1H Swords',
		random_primaries='2',
		random_secondaries='2')
	monsterHunter.save()
	monsterHunter.affixes.add(monsterBeastDmg)

	rimeheart = Weapon(slot='1H Weapons',
		name='Rimeheart',
		pic='/assets/media/items/legendaries/weapons/1h/swords/rimeheart.png',
		category='1H Swords',
		unique='<span class="silver">10%</span> chance on hit to instantly deal <span class="silver">10000%</span> weapon damage as Cold to enemies that are Frozen.',
		random_primaries='2',
		random_secondaries='1')
	rimeheart.save()
	rimeheart.affixes.add(mainStat)

	sever = Weapon(slot='1H Weapons',
		name='Sever',
		pic='/assets/media/items/legendaries/weapons/1h/swords/sever.png',
		category='1H Swords',
		unique='Slain enemies rest in pieces.',
		random_primaries='1')
	sever.save()
	sever.affixes.add(percentDmg, mainStat, severDemonDmg)

	shardOfHate = Weapon(slot='1H Weapons',
		name='Shard of Hate',
		pic='/assets/media/items/legendaries/weapons/1h/swords/shard_of_hate.png',
		category='1H Swords',
		unique='Elemental skills have a chance to trigger a powerful {<span class="vary">Attack</span>} that deals <span>200 - 250%</span> weapon damage',
		random_primaries='2',
		random_secondaries='1',
		notes='Cold skills trigger Freezing Skull<br>Poison skills trigger Poison Nova<br>Lightning Skills trigger Charged Bolt')
	shardOfHate.save()
	shardOfHate.affixes.add(mainStat)

	skycutter = Weapon(slot='1H Weapons',
		name='Skycutter',
		pic='/assets/media/items/legendaries/weapons/1h/swords/skycutter.png',
		category='1H Swords',
		unique='Chance to summon angelic assistance when attacking.',
		random_primaries='1',
		random_secondaries='1')
	skycutter.save()
	skycutter.affixes.add(mainStat, skycutterHolyDmg)

	spectrum = Weapon(slot='1H Weapons',
		name='spectrum',
		pic='/assets/media/items/legendaries/weapons/1h/swords/spectrum.png',
		category='1H Swords',
		random_primaries='?',
		random_secondaries='?')
	spectrum.save()
	spectrum.affixes.add(mainStat)

	theAncientBonesaberOfZumakalis = Weapon(slot='1H Weapons',
		name='The Ancient Bonesaber of Zumakalis',
		pic='/assets/media/items/legendaries/weapons/1h/swords/the_ancient_bonesaber_of_zumakalis.png',
		category='1H Swords',
		random_primaries='1',
		random_secondaries='2')
	theAncientBonesaberOfZumakalis.save()
	theAncientBonesaberOfZumakalis.affixes.add(mainStat, ias)

	thunderfuryBlessedBladeOfTheWindseeker = Weapon(slot='1H Weapons',
		name='Thunderfury, Blessed Blade of the Windseeker',
		pic='/assets/media/items/legendaries/weapons/1h/swords/thunderfury_blessed_blade_of_the_windseeker.png',
		category='1H Swords',
		unique='Chance on hit to blast your enemy with Lightning, dealing <span>279 - 372%</span> weapon damage as Lightning and then jumping to additional nearby enemies. Each enemy hit has their attack speed and movement speed reduced by <span class="silver">30%</span> for <span class="silver">3</span> seconds. Jumps up to <span class="silver">5</span> targets.',
		random_primaries='1',
		random_secondaries='1')
	thunderfuryBlessedBladeOfTheWindseeker.save()
	thunderfuryBlessedBladeOfTheWindseeker.affixes.add(mainStat, sockets)

	wildwood = Weapon(slot='1H Weapons',
		name='Wildwood',
		pic='/assets/media/items/legendaries/weapons/1h/swords/wildwood.png',
		category='1H Swords',
		random_primaries='1',
		random_secondaries='1')
	wildwood.save()
	wildwood.affixes.add(percentDmg, mainStat, killExp)


	for weapon in Weapon.objects.filter(category="1H Swords"):
		weapon.inherent = '<span class="inherent"><span>1.40</span> Attacks per Second</span>'
		weapon.save()


def load_wands(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	inte =  Affix.objects.get(affix='inte',
		category='Wands')

	maxAP =  Affix.objects.get(affix='maxAP',
		category='Wands')

	fragmentSpectralBlade =  Affix.objects.get(affix='fragmentSpectralBlade',
		category='Wands')
	gestureEleDmg =  Affix.objects.get(affix='gestureEleDmg',
		category='Wands')
	sloraksDisintegrate =  Affix.objects.get(affix='sloraksDisintegrate',
		category='Wands')

	aetherWalker = Weapon(slot='1H Weapons',
		name='Aether Walker',
		pic='/assets/media/items/legendaries/weapons/1h/wands/aether_walker.png',
		category='Wands',
		unique='Teleport no longer has a cooldown but costs <span class="silver">25</span> Arcane Power.',
		random_primaries='2',
		random_secondaries='1')
	aetherWalker.save()
	aetherWalker.affixes.add(inte)

	atrophy = Weapon(slot='1H Weapons',
		name='Atrophy',
		pic='/assets/media/items/legendaries/weapons/1h/wands/atrophy.png',
		category='Wands',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted')
	atrophy.save()
	# atrophy.affixes.add()

	blackhandKey = Weapon(slot='1H Weapons',
		name='Blackhand Key',
		pic='/assets/media/items/legendaries/weapons/1h/wands/blackhand_key.png',
		category='Wands',
		random_primaries='2',
		random_secondaries='1')
	blackhandKey.save()
	blackhandKey.affixes.add(inte, maxAP)

	fragmentOfDestiny = Weapon(slot='1H Weapons',
		name='Fragment of Destiny',
		pic='/assets/media/items/legendaries/weapons/1h/wands/fragment_of_destiny.png',
		category='Wands',
		random_primaries='1',
		random_secondaries='2')
	fragmentOfDestiny.save()
	fragmentOfDestiny.affixes.add(inte, fragmentSpectralBlade)

	gestureOfOrpheus = Weapon(slot='1H Weapons',
		name='Gesture of Orpheus',
		pic='/assets/media/items/legendaries/weapons/1h/wands/gesture_of_orpheus.png',
		category='Wands',
		unique='Reduces the cooldown of Slow Time by <span>30 - 40%</span>.',
		random_primaries='1',
		random_secondaries='1')
	gestureOfOrpheus.save()
	gestureOfOrpheus.affixes.add(inte, gestureEleDmg)

	serpentsSparker = Weapon(slot='1H Weapons',
		name='Serpent\'s Sparker',
		pic='/assets/media/items/legendaries/weapons/1h/wands/serpents_sparker.png',
		category='Wands',
		unique='You may have <span class="silver">1</span> extra Hydra active at a time.',
		random_primaries='2',
		random_secondaries='1')
	serpentsSparker.save()
	serpentsSparker.affixes.add(inte)

	sloraksMadness = Weapon(slot='1H Weapons',
		name='Slorak\'s Madness',
		pic='/assets/media/items/legendaries/weapons/1h/wands/sloraks_madness.png',
		category='Wands',
		unique='This wand finds your death humorous.',
		random_primaries='2',
		random_secondaries='1')
	sloraksMadness.save()
	sloraksMadness.affixes.add(inte, sloraksDisintegrate)

	starfire = Weapon(slot='1H Weapons',
		name='Starfire',
		pic='/assets/media/items/legendaries/weapons/1h/wands/starfire.png',
		category='Wands',
		random_primaries='2',
		random_secondaries='2')
	starfire.save()
	starfire.affixes.add(inte)

	wandOfWoh = Weapon(slot='1H Weapons',
		name='Wand of Woh',
		pic='/assets/media/items/legendaries/weapons/1h/wands/wand_of_woh.png',
		category='Wands',
		unique='<span class="silver">3</span> additional Explosive Blasts are triggered after casting Explosive Blast.',
		random_primaries='2',
		random_secondaries='1')
	wandOfWoh.save()
	wandOfWoh.affixes.add(inte)

	for weapon in Weapon.objects.filter(category="Wands"):
		weapon.inherent = '<span class="inherent"><span>1.40</span> Attacks per Second</span>'
		weapon.owner = 'wiz'
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
        ('legendaries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_1h_axes),
        migrations.RunPython(load_ceremonial_knives),
        migrations.RunPython(load_1h_daggers),
        migrations.RunPython(load_fist_weapons),
        migrations.RunPython(load_1h_flails),
        migrations.RunPython(load_hand_crossbows),
        migrations.RunPython(load_1h_maces),
        migrations.RunPython(load_1h_mighty_weapons),
        migrations.RunPython(load_1h_spears),
        migrations.RunPython(load_1h_swords),
        migrations.RunPython(load_wands),
        migrations.RunPython(load_slugs)
    ]
