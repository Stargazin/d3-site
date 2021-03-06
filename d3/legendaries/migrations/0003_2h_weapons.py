'''
Needed affixes and item-specific affixes are defined first.
Items of category/slot defined after.
Owners are placed before loading (ex. #2H Axe bb-cs-mk-wd-wz)
'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


#2H Axe  bb-cs-mk-wd-wz
def load_2h_axes(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(affix='mainStat', category='2H Axes')
	bleedChance = Affix.objects.get(affix='bleedChance', category='2H Axes')
	sockets = Affix.objects.get(affix='sockets', category='2H Axes')

	lpk = Affix.objects.get(affix='lpk', category='2H Axes')
	killExp = Affix.objects.get(affix='killExp', category='2H Axes')

	burstOfWrath = Weapon(slot='2H Weapons',
		name='Burst of Wrath',
		pic='media/items/legendaries/weapons/2h/axes/burst_of_wrath.png',
		category='2H Axes',
		random_primaries='1',
		random_secondaries='1',
		patch='23')
	burstOfWrath.save()
	burstOfWrath.affixes.add(mainStat, sockets)

	butchersCarver = Weapon(slot='2H Weapons',
		name='Butcher\'s Carver',
		pic='media/items/legendaries/weapons/2h/axes/butchers_carver.png',
		category='2H Axes',
		unique='The Butcher still inhabits his carver',
		random_primaries='2',
		random_secondaries='2',
		patch='23')
	butchersCarver.save()
	butchersCarver.affixes.add(mainStat)

	cinderSwitch = Weapon(slot='2H Weapons',
		name='Cinder Switch',
		pic='media/items/legendaries/weapons/2h/axes/cinder_switch.png',
		category='2H Axes',
		unique='<span>25 - 50%</span> chance to cast a Fireball when attacking',
		random_primaries='3',
		random_secondaries='1',
		notes='crafted',
		patch='23')
	cinderSwitch.save()
	# cinderSwitch.affixes.add()

	messerschmidtsReaver = Weapon(slot='2H Weapons',
		name='Messerschmidt\'s Reaver',
		pic='media/items/legendaries/weapons/2h/axes/messerschmidts_reaver.png',
		category='2H Axes',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	messerschmidtsReaver.save()
	messerschmidtsReaver.affixes.add(mainStat, lpk)

	skorn = Weapon(slot='2H Weapons',
		name='Skorn',
		pic='media/items/legendaries/weapons/2h/axes/skorn.png',
		category='2H Axes',
		random_secondaries='2',
		patch='23')
	skorn.save()
	skorn.affixes.add(mainStat, bleedChance, sockets)

	theExecutioner = Weapon(slot='2H Weapons',
		name='The Executioner',
		pic='media/items/legendaries/weapons/2h/axes/the_executioner.png',
		category='2H Axes',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	theExecutioner.save()
	theExecutioner.affixes.add(mainStat, killExp)

	for weapon in Weapon.objects.filter(category="2H Axes"):
		weapon.inherent = '<span class="inherent"><span>1.00</span> Attacks per Second</span>'
		weapon.owner = 'bb-cs-mk-wd-wz'
		weapon.save()


#Bow  dh-wd-wz
def load_bows(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(affix='mainStat',
		category='Bows')
	percentDmg = Affix.objects.get(affix='percentDmg',
		category='Bows')
	ias = Affix.objects.get(affix='ias',
		category='Bows')
	eliteDmg = Affix.objects.get(affix='eliteDmg',
		category='Bows')

	durability = Affix.objects.get(affix='durability',
		category='Bows')

	etrayuColdDmg = Affix.objects.get(affix='etrayuColdDmg',
		category='Bows')
	ravensExtraGold = Affix.objects.get(affix='ravensExtraGold',
		category='Bows')
	unboundCHD = Affix.objects.get(affix='unboundCHD',
		category='Bows')
	uskangLightDmg = Affix.objects.get(affix='uskangLightDmg',
		category='Bows')
	windforceKnockbackChance = Affix.objects.get(affix='windforceKnockbackChance',
		category='Bows')
	yangsRCR = Affix.objects.get(affix='yangsRCR',
		category='Bows')

	cluckeye = Weapon(slot='2H Weapons',
		name='Cluckeye',
		pic='media/items/legendaries/weapons/2h/bows/cluckeye.png',
		category='Bows',
		unique='<span>25 - 50%</span> chance to Cluck when attacking',
		random_primaries='2',
		random_secondaries='1',
		owner='dh-wd-wz',
		patch='23')
	cluckeye.save()
	cluckeye.affixes.add(mainStat)

	etrayu = Weapon(slot='2H Weapons',
		name='Etrayu',
		pic='media/items/legendaries/weapons/2h/bows/etrayu.png',
		category='Bows',
		random_primaries='1',
		random_secondaries='1',
		notes='double check',
		owner='dh-wd-wz',
		patch='23')
	etrayu.save()
	etrayu.affixes.add(mainStat, etrayuColdDmg, durability)

	kridershot = Weapon(slot='2H Weapons',
		name='Kridershot',
		pic='media/items/legendaries/weapons/2h/bows/kridershot.png',
		category='Bows',
		unique='Elemental Arrow now generates <span>3 - 4</span> Hatred',
		random_primaries='1',
		random_secondaries='1',
		owner='dh',
		patch='23')
	kridershot.save()
	kridershot.affixes.add(mainStat, percentDmg)

	leonineBowOfHashir = Weapon(slot='2H Weapons',
		name='Leonine Bow of Hashir',
		pic='media/items/legendaries/weapons/2h/bows/leonine_bow_of_hashir.png',
		category='Bows',
		unique='Bola Shot has a <span>15 - 20%</span> chance on explosion to pull in all enemies within <span class="silver">24</span> yards',
		random_primaries='2',
		random_secondaries='1',
		owner='dh',
		patch='23')
	leonineBowOfHashir.save()
	leonineBowOfHashir.affixes.add(mainStat)

	odysseysEnd = Weapon(slot='2H Weapons',
		name='Odyssey\'s End',
		pic='media/items/legendaries/weapons/2h/bows/odysseys_end.png',
		category='Bows',
		unique='Enemies snared by your Entangling Shot take <span>20 - 25%</span> increased damage from all sources',
		random_primaries='2',
		random_secondaries='1',
		owner='dh',
		patch='23')
	odysseysEnd.save()
	odysseysEnd.affixes.add(mainStat)

	sydyruCrust = Weapon(slot='2H Weapons',
		name='Sydyru Crust',
		pic='media/items/legendaries/weapons/2h/bows/sydyru_crust.png',
		category='Bows',
		random_primaries='1',
		random_secondaries='2',
		notes='crafted',
		owner='dh-wd-wz',
		patch='23')
	sydyruCrust.save()
	sydyruCrust.affixes.add(ias, eliteDmg)

	theRavensWing = Weapon(slot='2H Weapons',
		name='The Raven\'s Wing',
		pic='media/items/legendaries/weapons/2h/bows/the_ravens_wing.png',
		category='Bows',
		unique='A Raven flies to your side',
		random_primaries='2',
		random_secondaries='1',
		owner='dh-wd-wz',
		patch='23')
	theRavensWing.save()
	theRavensWing.affixes.add(mainStat, ravensExtraGold)

	unboundBolt = Weapon(slot='2H Weapons',
		name='Unbound Bolt',
		pic='media/items/legendaries/weapons/2h/bows/unbound_bolt.png',
		category='Bows',
		random_primaries='1',
		random_secondaries='2',
		notes='crafted',
		owner='dh-wd-wz',
		patch='23')
	unboundBolt.save()
	unboundBolt.affixes.add(ias, unboundCHD)

	uskang = Weapon(slot='2H Weapons',
		name='Uskang',
		pic='media/items/legendaries/weapons/2h/bows/uskang.png',
		category='Bows',
		random_primaries='1',
		random_secondaries='2',
		owner='dh-wd-wz',
		patch='23')
	uskang.save()
	uskang.affixes.add(mainStat, uskangLightDmg)

	windforce = Weapon(slot='2H Weapons',
		name='Windforce',
		pic='media/items/legendaries/weapons/2h/bows/windforce.png',
		category='Bows',
		random_primaries='2',
		random_secondaries='1',
		owner='dh-wd-wz',
		patch='23')
	windforce.save()
	windforce.affixes.add(mainStat, windforceKnockbackChance)

	yangsRecurve = Weapon(slot='2H Weapons',
		name='Yang\'s Recurve',
		pic='media/items/legendaries/weapons/2h/bows/yangs_recurve.png',
		category='Bows',
		unique='Multishot attacks <span class="silver">50%</span> faster',
		random_primaries='1',
		random_secondaries='1',
		owner='dh',
		patch='23')
	yangsRecurve.save()
	yangsRecurve.affixes.add(percentDmg, mainStat, yangsRCR)

	for weapon in Weapon.objects.filter(category="Bows"):
		weapon.inherent = '<span class="inherent"><span>1.40</span> Attacks per Second</span>'
		weapon.save()


#Crossbow  dh-wd-wz
def load_crossbows(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(affix='mainStat',
		category='Crossbows')
	sockets = Affix.objects.get(affix='sockets',
		category='Crossbows')

	burizadoFreezeChance = Affix.objects.get(affix='burizadoFreezeChance',
		category='Crossbows')
	manticoreClusterArrow = Affix.objects.get(affix='manticoreClusterArrow',
		category='Crossbows')

	arcaneBarb = Weapon(slot='2H Weapons',
		name='Arcane Barb',
		pic='media/items/legendaries/weapons/2h/crossbows/arcane_barb.png',
		category='Crossbows',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted',
		owner='dh-wd-wz',
		patch='23')
	arcaneBarb.save()
	# arcaneBarb.affixes.add()

	bakkanCaster = Weapon(slot='2H Weapons',
		name='Bakkan Caster',
		pic='media/items/legendaries/weapons/2h/crossbows/bakkan_caster.png',
		category='Crossbows',
		random_primaries='2',
		random_secondaries='2',
		owner='dh-wd-wz',
		patch='23')
	bakkanCaster.save()
	bakkanCaster.affixes.add(mainStat)

	burizadoKyanon = Weapon(slot='2H Weapons',
		name='Buriza-Do Kyanon',
		pic='media/items/legendaries/weapons/2h/crossbows/burizado_kyanon.png',
		category='Crossbows',
		unique='Your Projectiles pierce <span>1 - 2</span> additional times',
		random_primaries='2',
		owner='dh',
		patch='23')
	burizadoKyanon.save()
	burizadoKyanon.affixes.add(mainStat, burizadoFreezeChance)

	chanonBolter = Weapon(slot='2H Weapons',
		name='Chanon Bolter',
		pic='media/items/legendaries/weapons/2h/crossbows/chanon_bolter.png',
		category='Crossbows',
		unique='Your Spike Traps lure enemies to them. Enemies may be Taunted once every <span>12 - 16</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		owner='dh',
		patch='23')
	chanonBolter.save()
	chanonBolter.affixes.add(mainStat)

	demonMachine = Weapon(slot='2H Weapons',
		name='Demon Machine',
		pic='media/items/legendaries/weapons/2h/crossbows/demon_machine.png',
		category='Crossbows',
		unique='<span>35 - 65%</span> chance to shoot Explosive Bolts when attacking',
		random_primaries='2',
		random_secondaries='1',
		owner='dh-wd-wz',
		patch='23')
	demonMachine.save()
	demonMachine.affixes.add(mainStat)

#2.4
	hellrack = Weapon(slot='2H Weapons',
		name='Hellrack',
		pic='media/items/legendaries/weapons/2h/crossbows/hellrack.png',
		category='Crossbows',
		unique='Chance to Root enemies to the ground when you hit them',
		random_primaries='2',
		random_secondaries='1',
		owner='dh-wd-wz',
		patch='24')
	hellrack.save()
	hellrack.affixes.add(mainStat, sockets)

#2.4
	manticore = Weapon(slot='2H Weapons',
		name='Manticore',
		pic='media/items/legendaries/weapons/2h/crossbows/manticore.png',
		category='Crossbows',
		unique='Reduces the Hatred cost of Cluster Arrow by <span>40 - 50%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='dh',
		patch='24')
	manticore.save()
	manticore.affixes.add(mainStat, manticoreClusterArrow)

	pusSpitter = Weapon(slot='2H Weapons',
		name='Pus Spitter',
		pic='media/items/legendaries/weapons/2h/crossbows/pus_spitter.png',
		category='Crossbows',
		unique='<span>25 - 50%</span> chance to lob an Acid Blob when attacking',
		random_primaries='2',
		random_secondaries='1',
		owner='dh-wd-wz',
		patch='23')
	pusSpitter.save()
	pusSpitter.affixes.add(mainStat)

#2.4
	wojahnniAssaulter = Weapon(slot='2H Weapons',
		name='Wojahnni Assaulter',
		pic='media/items/legendaries/weapons/2h/crossbows/wojahnni_assaulter.png',
		category='Crossbows',
		unique='Rapid Fire deals <span>30 - 40%</span> more damage for every second that you channel. Stacks up to <span class="silver">4</span> times',
		random_primaries='2',
		random_secondaries='1',
		owner='dh',
		patch='24')
	wojahnniAssaulter.save()
	wojahnniAssaulter.affixes.add(mainStat, sockets)

	for weapon in Weapon.objects.filter(category="Crossbows"):
		weapon.inherent = '<span class="inherent"><span>1.10</span> Attacks per Second</span>'
		weapon.save()


#Daibo  mk
def load_daibos(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	dext = Affix.objects.get(affix='dext',
		category='Daibos')
	sockets = Affix.objects.get(affix='sockets',
		category='Daibos')

	balanceTempestRush = Affix.objects.get(affix='balanceTempestRush',
		category='Daibos')
	incenseWaveOfLight = Affix.objects.get(affix='incenseWaveOfLight',
		category='Daibos')
	staffDeadlyReach = Affix.objects.get(affix='staffDeadlyReach',
		category='Daibos')

#2.4
	balance = Weapon(slot='2H Weapons',
		name='Balance',
		pic='media/items/legendaries/weapons/2h/daibos/balance.png',
		category='Daibos',
		unique='When your Tempest Rush hits <span class="silver">3</span> or fewer enemies, it gains <span class="silver">100%</span> Critical Hit Chance',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	balance.save()
	balance.affixes.add(dext, balanceTempestRush)

	flyingDragon = Weapon(slot='2H Weapons',
		name='Flying Dragon',
		pic='media/items/legendaries/weapons/2h/daibos/flying_dragon.png',
		category='Daibos',
		unique='Chance to double your Attack Speed when attacking',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	flyingDragon.save()
	flyingDragon.affixes.add(dext)

	incenseTorchOfTheGrandTemple = Weapon(slot='2H Weapons',
		name='Incense Torch of the Grand Temple',
		pic='media/items/legendaries/weapons/2h/daibos/incense_torch_of_the_grand_temple.png',
		category='Daibos',
		unique='Reduces the Spirit cost of Wave of Light by <span>40 - 50%</span>',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	incenseTorchOfTheGrandTemple.save()
	incenseTorchOfTheGrandTemple.affixes.add(dext, incenseWaveOfLight)

	laiYuisPersuader = Weapon(slot='2H Weapons',
		name='Lai Yui\'s Persuader',
		pic='media/items/legendaries/weapons/2h/daibos/lai_yuis_persuader.png',
		category='Daibos',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted',
		patch='23')
	laiYuisPersuader.save()
	# laiYuisPersuader.affixes.add()

	rozpedinsForce = Weapon(slot='2H Weapons',
		name='Rozpedin\'s Force',
		pic='media/items/legendaries/weapons/2h/daibos/rozpedins_force.png',
		category='Daibos',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted',
		patch='23')
	rozpedinsForce.save()
	# rozpedinsForce.affixes.add()

	staffOfKyro = Weapon(slot='2H Weapons',
		name='Staff of Kyro',
		pic='media/items/legendaries/weapons/2h/daibos/staff_of_kyro.png',
		category='Daibos',
		random_secondaries='2',
		patch='23')
	staffOfKyro.save()
	staffOfKyro.affixes.add(dext, sockets, staffDeadlyReach)

	theFlowOfEternity = Weapon(slot='2H Weapons',
		name='The Flow of Eternity',
		pic='media/items/legendaries/weapons/2h/daibos/the_flow_of_eternity.png',
		category='Daibos',
		unique='Reduces the cooldown of Seven-Sided Strike by <span>45 - 60%</span>',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	theFlowOfEternity.save()
	theFlowOfEternity.affixes.add(dext)

	thePaddle = Weapon(slot='2H Weapons',
		name='The Paddle',
		pic='media/items/legendaries/weapons/2h/daibos/the_paddle.png',
		category='Daibos',
		unique='Slap!',
		random_primaries='2',
		random_secondaries='2',
		patch='23')
	thePaddle.save()
	thePaddle.affixes.add(dext)

	warstaffOfGeneralQuang = Weapon(slot='2H Weapons',
		name='Warstaff of General Quang',
		pic='media/items/legendaries/weapons/2h/daibos/warstaff_of_general_quang.png',
		category='Daibos',
		unique='Tempest Rush gains the effect of the Tailwind rune',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	warstaffOfGeneralQuang.save()
	warstaffOfGeneralQuang.affixes.add(dext)

	for weapon in Weapon.objects.filter(category="Daibos"):
		weapon.inherent = '<span class="inherent"><span>1.10</span> Attacks per Second</span>'
		weapon.owner = 'mk'
		weapon.save()


#2H Flail  cs
def load_2h_flails(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix.objects.get(affix='stre', category='2H Flails')
	sockets = Affix.objects.get(affix='sockets', category='2H Flails')

	goldenSweepAttack = Affix.objects.get(affix='goldenSweepAttack', category='2H Flails')

#2.4 new
	akkhansAddendum = Weapon(slot='2H Weapons',
		name='Akkhan\'s Addendum',
		pic='media/items/legendaries/2.4/weapons/akkhans_addendum.png',
		category='2H Flails',
		unique='Akarat\'s Champion gains the effects of the Prophet rune and the Embodiment of Power rune',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	akkhansAddendum.save()
	akkhansAddendum.affixes.add(stre)

#2.4 new
	akkhansLeniency = Weapon(slot='2H Weapons',
		name='Akkhan\'s Leniency',
		pic='media/items/legendaries/2.4/weapons/akkhans_leniency.png',
		category='2H Flails',
		unique='Each enemy hit by your Blessed Shield increases the damage of your Blessed Shield by <span>15 - 20%</span> for <span class="silver">3</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	akkhansLeniency.save()
	akkhansLeniency.affixes.add(stre)

	balefulRemnant = Weapon(slot='2H Weapons',
		name='Baleful Remnant',
		pic='media/items/legendaries/weapons/2h/flails/baleful_remnant.png',
		category='2H Flails',
		unique='Enemies killed while Akarat\'s Champion is active turn into Phalanx Avatars for <span class="silver">10</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	balefulRemnant.save()
	balefulRemnant.affixes.add(sockets)

	fateOfTheFell = Weapon(slot='2H Weapons',
		name='Fate of the Fell',
		pic='media/items/legendaries/weapons/2h/flails/fate_of_the_fell.png',
		category='2H Flails',
		unique='Gain <span class="silver">2</span> additional rays of Heaven\'s Fury',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	fateOfTheFell.save()
	fateOfTheFell.affixes.add(stre)

#2.4
	goldenFlense = Weapon(slot='2H Weapons',
		name='Golden Flense',
		pic='media/items/legendaries/weapons/2h/flails/golden_flense.png',
		category='2H Flails',
		unique='Sweep Attack restores <span>4 - 6</span> Wrath for each enemy hit',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	goldenFlense.save()
	goldenFlense.affixes.add(stre, goldenSweepAttack)

	theMortalDrama = Weapon(slot='2H Weapons',
		name='The Mortal Drama',
		pic='media/items/legendaries/weapons/2h/flails/the_mortal_drama.png',
		category='2H Flails',
		unique='Double the number of Bombardment impacts',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	theMortalDrama.save()
	theMortalDrama.affixes.add(stre)

	for weapon in Weapon.objects.filter(category="2H Flails"):
		weapon.inherent = '<span class="inherent"><span>1.15</span> Attacks per Second</span>'
		weapon.owner = 'cs'
		weapon.save()


#2H Mace  bb-cs-mk-wd-wz
def load_2h_maces(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix.objects.get(affix='percentDmg',
		category='2H Maces')
	mainStat = Affix.objects.get(affix='mainStat',
		category='2H Maces')

	ccChance = Affix.objects.get(affix='ccChance',
		category='2H Maces')
	lpk = Affix.objects.get(affix='lpk',
		category='2H Maces')

	schaefersLightDmg = Affix.objects.get(affix='schaefersLightDmg',
		category='2H Maces')
	sledgeMovementSpeed = Affix.objects.get(affix='sledgeMovementSpeed',
		category='2H Maces')
	wrathColdDmg = Affix.objects.get(affix='wrathColdDmg',
		category='2H Maces')

	arthefsSparkOfLife = Weapon(slot='2H Weapons',
		name='Arthef\'s Spark of Life',
		pic='media/items/legendaries/weapons/2h/maces/arthefs_spark_of_life.png',
		category='2H Maces',
		unique='Heal for <span>3 - 4%</span> of your missing Life when you kill an Undead enemy',
		random_primaries='2',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	arthefsSparkOfLife.save()
	arthefsSparkOfLife.affixes.add(mainStat)

	crushbane = Weapon(slot='2H Weapons',
		name='Crushbane',
		pic='media/items/legendaries/weapons/2h/maces/crushbane.png',
		category='2H Maces',
		random_primaries='2',
		random_secondaries='2',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	crushbane.save()
	crushbane.affixes.add(mainStat)

	schaefersHammer = Weapon(slot='2H Weapons',
		name='Schaefer\'s Hammer',
		pic='media/items/legendaries/weapons/2h/maces/schaefers_hammer.png',
		category='2H Maces',
		unique='Casting a Lightning skill charges you with Lightning, causing you to deal <span>650 - 850%</span> weapon damage as Lightning every second for <span class="silver">5</span> seconds to nearby enemies',
		random_primaries='2',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	schaefersHammer.save()
	schaefersHammer.affixes.add(schaefersLightDmg)

	skywarden = Weapon(slot='2H Weapons',
		name='Skywarden',
		pic='media/items/legendaries/weapons/2h/maces/skywarden.png',
		category='2H Maces',
		unique='Every <span class="silver">60</span> seconds, gain a random Law for <span class="silver">60</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='23')
	skywarden.save()
	skywarden.affixes.add(mainStat)

	sledgeOfAthskeleng = Weapon(slot='2H Weapons',
		name='Sledge of Athskeleng',
		pic='media/items/legendaries/weapons/2h/maces/sledge_of_athskeleng.png',
		category='2H Maces',
		random_secondaries='2',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	sledgeOfAthskeleng.save()
	sledgeOfAthskeleng.affixes.add(percentDmg, mainStat, sledgeMovementSpeed)

	soulsmasher = Weapon(slot='2H Weapons',
		name='Soulsmasher',
		pic='media/items/legendaries/weapons/2h/maces/soulsmasher.png',
		category='2H Maces',
		unique='When you kill an enemy, it explodes for <span>450 - 600%</span> of your Life per Kill as damage to all enemies within <span class="silver">20</span> yards. You no longer benefit from your Life per Kill',
		random_primaries='2',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	soulsmasher.save()
	soulsmasher.affixes.add(mainStat, lpk)

	sunder = Weapon(slot='2H Weapons',
		name='Sunder',
		pic='media/items/legendaries/weapons/2h/maces/sunder.png',
		category='2H Maces',
		unique='<span>25 - 50%</span> chance to Sunder the ground your enemies walk on when you attack',
		random_primaries='3',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	sunder.save()
	# sunder.affixes.add()

	theFurnace = Weapon(slot='2H Weapons',
		name='The Furnace',
		pic='media/items/legendaries/weapons/2h/maces/the_furnace.png',
		category='2H Maces',
		unique='Increases damage against Elites by <span>40 - 50%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	theFurnace.save()
	theFurnace.affixes.add(mainStat)

	wrathOfTheBoneKing = Weapon(slot='2H Weapons',
		name='Wrath of the Bone King',
		pic='media/items/legendaries/weapons/2h/maces/wrath_of_the_bone_king.png',
		category='2H Maces',
		random_primaries='2',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	wrathOfTheBoneKing.save()
	wrathOfTheBoneKing.affixes.add(wrathColdDmg, lpk, ccChance)

	for weapon in Weapon.objects.filter(category="2H Maces"):
		weapon.inherent = '<span class="inherent"><span>0.90</span> Attacks per Second</span>'
		weapon.owner = 'all'
		weapon.save()


#2H Mighty Weapon  bb
def load_2h_mighty_weapons(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	stre = Affix.objects.get(affix='stre',
		category='2H Mighty Weapons')
	sockets = Affix.objects.get(affix='sockets',
		category='2H Mighty Weapons')

	bladeEarthquake = Affix.objects.get(affix='bladeEarthquake',
		category='2H Mighty Weapons')
	furyLifePerFury = Affix.objects.get(affix='furyLifePerFury',
		category='2H Mighty Weapons')
	furySeismicSlam = Affix.objects.get(affix='furySeismicSlam',
		category='2H Mighty Weapons')
	gavelHammerOfTheAncients = Affix.objects.get(affix='gavelHammerOfTheAncients',
		category='2H Mighty Weapons')


	bastionsRevered = Weapon(slot='2H Weapons',
		name='Bastion\'s Revered',
		pic='media/items/legendaries/weapons/2h/mightyweapons/bastions_revered.png',
		category='2H Mighty Weapons',
		unique='Frenzy now stacks up to <span class="silver">10</span> times',
		random_primaries='1',
		random_secondaries='1',
		patch='23')
	bastionsRevered.save()
	bastionsRevered.affixes.add(stre, sockets)

#2.4 new
	bladeOfTheTribes = Weapon(slot='2H Weapons',
		name='Blade of the Tribes',
		pic='media/items/legendaries/2.4/weapons/blade_of_the_tribes.png',
		category='2H Mighty Weapons',
		unique='War Cry and Threatening Shout cause an Avalanche and Earthquake',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	bladeOfTheTribes.save()
	bladeOfTheTribes.affixes.add(stre, bladeEarthquake)

	furyOfTheVanishedPeak = Weapon(slot='2H Weapons',
		name='Fury of the Vanished Peak',
		pic='media/items/legendaries/weapons/2h/mightyweapons/fury_of_the_vanished_peak.png',
		category='2H Mighty Weapons',
		unique='Reduces the Fury cost of Seismic Slam by <span>40 - 50%</span>',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	furyOfTheVanishedPeak.save()
	furyOfTheVanishedPeak.affixes.add(stre, furyLifePerFury, furySeismicSlam)

	mawdawcsSorrow = Weapon(slot='2H Weapons',
		name='Mawdawc\'s Sorrow',
		pic='media/items/legendaries/weapons/2h/mightyweapons/madawcs_sorrow.png',
		category='2H Mighty Weapons',
		unique='Stun enemies for <span class="silver">2</span> seconds the first time you hit them',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	mawdawcsSorrow.save()
	mawdawcsSorrow.affixes.add(stre)

	theGavelOfJudgement = Weapon(slot='2H Weapons',
		name='The Gavel of Judgement',
		pic='media/items/legendaries/weapons/2h/mightyweapons/the_gavel_of_judgement.png',
		category='2H Mighty Weapons',
		unique='Hammer of the Ancients returns <span>20 - 25</span> Fury if it hits <span class="silver">3</span> or fewer enemies',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	theGavelOfJudgement.save()
	theGavelOfJudgement.affixes.add(stre, gavelHammerOfTheAncients)

	warOfTheDead = Weapon(slot='2H Weapons',
		name='War of the Dead',
		pic='media/items/legendaries/weapons/2h/mightyweapons/war_of_the_dead.png',
		category='2H Mighty Weapons',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted',
		patch='23')
	warOfTheDead.save()
	# warOfTheDead.affixes.add()

	for weapon in Weapon.objects.filter(category="2H Mighty Weapons"):
		weapon.inherent = '<span class="inherent"><span>1.10</span> Attacks per Second</span>'
		weapon.owner = 'bb'
		weapon.save()


#Polearm  bb-cs-mk-wd
def load_polearms(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(affix='mainStat', category='Polearms')
	sockets = Affix.objects.get(affix='sockets', category='Polearms')

	lpk = Affix.objects.get(affix='lpk', category='Polearms')

	heartPhysDmg = Affix.objects.get(affix='heartPhysDmg', category='Polearms')

	bovineBardiche = Weapon(slot='2H Weapons',
		name='Bovine Bardiche',
		pic='media/items/legendaries/weapons/2h/polearms/bovine_bardiche.png',
		category='Polearms',
		unique='Chance on hit to summon a herd of murderous cows',
		random_primaries='2',
		random_secondaries='1',
		owner='bb-cs-mk-wd',
		patch='23')
	bovineBardiche.save()
	bovineBardiche.affixes.add(mainStat)

	heartSlaughter = Weapon(slot='2H Weapons',
		name='Heart Slaughter',
		pic='media/items/legendaries/weapons/2h/polearms/heart_slaughter.png',
		category='Polearms',
		random_primaries='1',
		random_secondaries='1',
		owner='bb-cs-mk-wd',
		patch='23')
	heartSlaughter.save()
	heartSlaughter.affixes.add(mainStat, heartPhysDmg, lpk)

	pledgeOfCaldeum = Weapon(slot='2H Weapons',
		name='Pledge of Caldeum',
		pic='media/items/legendaries/weapons/2h/polearms/pledge_of_caldeum.png',
		category='Polearms',
		random_primaries='2',
		random_secondaries='2',
		owner='bb-cs-mk-wd',
		patch='23')
	pledgeOfCaldeum.save()
	pledgeOfCaldeum.affixes.add(mainStat)

#2.4
	standoff = Weapon(slot='2H Weapons',
		name='Standoff',
		pic='media/items/legendaries/weapons/2h/polearms/standoff.png',
		category='Polearms',
		unique='Furious Charge gains increased damage equal to <span>200 - 250%</span> of your bonus Movement Speed',
		random_primaries='2',
		random_secondaries='1',
		owner='bb',
		patch='24')
	standoff.save()
	standoff.affixes.add(mainStat)

	vigilance = Weapon(slot='2H Weapons',
		name='Vigilance',
		pic='media/items/legendaries/weapons/2h/polearms/vigilance.png',
		category='Polearms',
		unique='Getting hit has a chance to automatically cast Inner Sanctuary',
		random_primaries='2',
		random_secondaries='1',
		owner='mk',
		patch='23')
	vigilance.save()
	vigilance.affixes.add(mainStat)

	for weapon in Weapon.objects.filter(category="Polearms"):
		weapon.inherent = '<span class="inherent"><span>0.95</span> Attacks per Second</span>'
		weapon.save()


#Staff  mk-wd-wz
def load_staves(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix.objects.get(affix='percentDmg',
		category='Staves')
	mainStat = Affix.objects.get(affix='mainStat',
		category='Staves')
	sockets = Affix.objects.get(affix='sockets',
		category='Staves')

	killExp = Affix.objects.get(affix='killExp',
		category='Staves')
	durability = Affix.objects.get(affix='durability',
		category='Staves')

	staffFirebats = Affix.objects.get(affix='staffFirebats',
		category='Staves')
	suwongAcidCloud = Affix.objects.get(affix='suwongAcidCloud',
		category='Staves')
	grandMeteor = Affix.objects.get(affix='grandMeteor',
		category='Staves')
	wormwoodPoisDmg = Affix.objects.get(affix='wormwoodPoisDmg',
		category='Staves')


	ahvarionSpearOfLycander = Weapon(slot='2H Weapons',
		name='Ahvarion, Spear of Lycander',
		pic='media/items/legendaries/weapons/2h/staves/ahavarion_spear_of_lycander.png',
		category='Staves',
		unique='Chance on killing a Demon to gain a random Shrine effect',
		random_primaries='2',
		random_secondaries='1',
		owner='mk-wd-wz',
		patch='23')
	ahvarionSpearOfLycander.save()
	ahvarionSpearOfLycander.affixes.add(sockets)

	autumnsCall = Weapon(slot='2H Weapons',
		name='Autumn\'s Call',
		pic='media/items/legendaries/weapons/2h/staves/autumns_call.png',
		category='Staves',
		random_primaries='2',
		random_secondaries='1',
		owner='mk-wd-wz',
		patch='23')
	autumnsCall.save()
	autumnsCall.affixes.add(mainStat, killExp)

	malothsFocus = Weapon(slot='2H Weapons',
		name='Maloth\'s Focus',
		pic='media/items/legendaries/weapons/2h/staves/maloths_focus.png',
		category='Staves',
		unique='Enemies occasionally Flee at the sight of this staff',
		random_primaries='2',
		random_secondaries='1',
		owner='mk-wd-wz',
		patch='23')
	malothsFocus.save()
	malothsFocus.affixes.add(mainStat)

	markOfTheMagi = Weapon(slot='2H Weapons',
		name='Mark of the Magi',
		pic='media/items/legendaries/weapons/2h/staves/mark_of_the_magi.png',
		category='Staves',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted',
		owner='mk-wd-wz',
		patch='23')
	markOfTheMagi.save()
	# markOfTheMagi.affixes.add()

#2.4 new
	staffOfChiroptera = Weapon(slot='2H Weapons',
		name='Staff of Chiroptera',
		pic='media/items/legendaries/2.4/weapons/staff_of_chiroptera.png',
		category='Staves',
		unique='Firebats attacks <span class="silver">100%</span> faster and costs <span>70 - 75%</span> less Mana',
		random_primaries='2',
		random_secondaries='1',
		owner='wd',
		patch='24')
	staffOfChiroptera.save()
	staffOfChiroptera.affixes.add(mainStat, staffFirebats)

	suwongDiviner = Weapon(slot='2H Weapons',
		name='SuWong Diviner',
		pic='media/items/legendaries/weapons/2h/staves/suwong_diviner.png',
		category='Staves',
		unique='Acid Cloud gains the effect of the Lob Blob Bomb rune',
		random_primaries='1',
		random_secondaries='1',
		owner='wd',
		patch='23')
	suwongDiviner.save()
	suwongDiviner.affixes.add(percentDmg, mainStat, suwongAcidCloud)

	theBrokenStaff = Weapon(slot='2H Weapons',
		name='The Broken Staff',
		pic='media/items/legendaries/weapons/2h/staves/the_broken_staff.png',
		category='Staves',
		random_primaries='1',
		random_secondaries='1',
		owner='mk-wd-wz',
		patch='23')
	theBrokenStaff.save()
	theBrokenStaff.affixes.add(mainStat, sockets, durability)

	theGrandVizier = Weapon(slot='2H Weapons',
		name='The Grand Vizier',
		pic='media/items/legendaries/weapons/2h/staves/the_grand_vizier.png',
		category='Staves',
		unique='Reduces the Arcane Power cost of Meteor by <span>40 - 50%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='wz',
		patch='23')
	theGrandVizier.save()
	theGrandVizier.affixes.add(mainStat, grandMeteor)

	theSmolderingCore = Weapon(slot='2H Weapons',
		name='The Smoldering Core',
		pic='media/items/legendaries/weapons/2h/staves/the_smoldering_core.png',
		category='Staves',
		unique='Lesser enemies are now lured to your Meteor impact areas',
		random_primaries='1',
		random_secondaries='1',
		owner='wz',
		patch='23')
	theSmolderingCore.save()
	theSmolderingCore.affixes.add(mainStat, sockets)

	theTormentor = Weapon(slot='2H Weapons',
		name='The Tormentor',
		pic='media/items/legendaries/weapons/2h/staves/the_tormentor.png',
		category='Staves',
		unique='Chance to Charm enemies when you hit them',
		random_primaries='2',
		random_secondaries='1',
		owner='mk-wd-wz',
		patch='23')
	theTormentor.save()
	theTormentor.affixes.add(mainStat)

	valtheksRebuke = Weapon(slot='2H Weapons',
		name='Valthek\'s Rebuke',
		pic='media/items/legendaries/weapons/2h/staves/valtheks_rebuke.png',
		category='Staves',
		unique='Energy Twister now travels in a straight path',
		random_primaries='1',
		random_secondaries='1',
		owner='wz',
		patch='23')
	valtheksRebuke.save()
	valtheksRebuke.affixes.add(mainStat, sockets)

	wormwood = Weapon(slot='2H Weapons',
		name='Wormwood',
		pic='media/items/legendaries/weapons/2h/staves/wormwood.png',
		category='Staves',
		unique='Locust Swarm continuously plagues enemies around you',
		random_primaries='1',
		random_secondaries='1',
		owner='wd',
		patch='23')
	wormwood.save()
	wormwood.affixes.add(mainStat, wormwoodPoisDmg)

	for weapon in Weapon.objects.filter(category="Staves"):
		weapon.inherent = '<span class="inherent"><span>1.00</span> Attacks per Second</span>'
		weapon.save()


#2H Sword  bb-cs-mk-wd-wz
def load_2h_swords(apps, schema_editor):
	Weapon = apps.get_model("legendaries", "Weapon")
	Affix = apps.get_model("affixes", "Affix")

	percentDmg = Affix.objects.get(affix='percentDmg',
		category='2H Swords')
	mainStat = Affix.objects.get(affix='mainStat',
		category='2H Swords')
	cdr = Affix.objects.get(affix='cdr',
		category='2H Swords')
	sockets = Affix.objects.get(affix='sockets',
		category='2H Swords')

	lpk = Affix.objects.get(affix='lpk',
		category='2H Swords')
	killExp = Affix.objects.get(affix='killExp',
		category='2H Swords')
	durability = Affix.objects.get(affix='durability',
		category='2H Swords')

	blackguardCCReduction = Affix.objects.get(affix='blackguardCCReduction',
		category='2H Swords')
	bladeCondemn = Affix.objects.get(affix='bladeCondemn',
		category='2H Swords')
	corruptedUndeadDmg = Affix.objects.get(affix='corruptedUndeadDmg',
		category='2H Swords')
	faithfulThorns = Affix.objects.get(affix='faithfulThorns',
		category='2H Swords')
	maximusFireDmg = Affix.objects.get(affix='maximusFireDmg',
		category='2H Swords')
	grandfatherLife = Affix.objects.get(affix='grandfatherLife',
		category='2H Swords')
	sultanBlindChance = Affix.objects.get(affix='sultanBlindChance',
		category='2H Swords')

	blackguard = Weapon(slot='2H Weapons',
		name='Blackguard',
		pic='media/items/legendaries/weapons/2h/swords/blackguard.png',
		category='2H Swords',
		random_primaries='1',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	blackguard.save()
	blackguard.affixes.add(percentDmg, mainStat, blackguardCCReduction)

#2.4
	bladeOfProphecy = Weapon(slot='2H Weapons',
		name='Blade of Prophecy',
		pic='media/items/legendaries/weapons/2h/swords/blade_of_prophecy.png',
		category='2H Swords',
		unique='<span class="silver">2</span> Condemned enemies also trigger Condemn\'s explosion',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='24')
	bladeOfProphecy.save()
	bladeOfProphecy.affixes.add(mainStat, cdr, bladeCondemn)

	bloodBrother = Weapon(slot='2H Weapons',
		name='Blood Brother',
		pic='media/items/legendaries/weapons/2h/swords/blood_brother.png',
		category='2H Swords',
		unique='Grants a <span>15 - 20%</span> chance to block attacks. Blocked attacks inflict <span class="silver">30%</span> less damage. After blocking an attack, your next attack inflicts <span class="silver">30%</span> additional damage',
		random_primaries='1',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	bloodBrother.save()
	bloodBrother.affixes.add(percentDmg, mainStat)

	camsRebuttal = Weapon(slot='2H Weapons',
		name='Cam\'s Rebuttal',
		pic='media/items/legendaries/weapons/2h/swords/cams_rebuttal.png',
		category='2H Swords',
		unique='Falling Sword can be used again within <span class="silver">4</span> seconds before the cooldown is triggered',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='23')
	camsRebuttal.save()
	camsRebuttal.affixes.add(mainStat)

	corruptedAshbringer = Weapon(slot='2H Weapons',
		name='Corrupted Ashbringer',
		pic='media/items/legendaries/weapons/2h/swords/corrupted_ashbringer.png',
		category='2H Swords',
		unique='Chance on kill to raise a skeleton to fight for you. Upon accumulating <span class="silver">5</span> skeletons, they each explode for <span class="silver">1000%</span> weapon damage and the sword transforms into Ashbringer for a short time. Attacking with Ashbringer burns your enemy for <span>5000 - 6000%</span> weapon damage as Holy',
		random_primaries='2',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	corruptedAshbringer.save()
	corruptedAshbringer.affixes.add(mainStat, corruptedUndeadDmg, lpk)

	faithfulMemory = Weapon(slot='2H Weapons',
		name='Faithful Memory',
		pic='media/items/legendaries/weapons/2h/swords/faithful_memory.png',
		category='2H Swords',
		random_primaries='2',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	faithfulMemory.save()
	faithfulMemory.affixes.add(mainStat, faithfulThorns)

	maximus = Weapon(slot='2H Weapons',
		name='Maximus',
		pic='media/items/legendaries/weapons/2h/swords/maximus.png',
		category='2H Swords',
		unique='Chance on hit to summon a Demonic Slave',
		random_primaries='1',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	maximus.save()
	maximus.affixes.add(mainStat, maximusFireDmg)

	scourge = Weapon(slot='2H Weapons',
		name='Scourge',
		pic='media/items/legendaries/weapons/2h/swords/scourge.png',
		category='2H Swords',
		unique='<span>20 - 45%</span> chance when attacking to explode with demonic fury for <span>1800 - 2000%</span> weapon damage as Fire',
		random_primaries='2',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	scourge.save()
	scourge.affixes.add(sockets)

	stalgardsDecimator = Weapon(slot='2H Weapons',
		name='Stalgard\'s Decimator',
		pic='media/items/legendaries/weapons/2h/swords/stalgards_decimator.png',
		category='2H Swords',
		unique='Your Melee attacks throw a piercing axe at a nearby enemy, dealing <span>550 - 700%</span> weapon damage as Physical',
		random_primaries='2',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	stalgardsDecimator.save()
	stalgardsDecimator.affixes.add(mainStat)

	theGrandfather = Weapon(slot='2H Weapons',
		name='The Grandfather',
		pic='media/items/legendaries/weapons/2h/swords/the_grandfather.png',
		category='2H Swords',
		random_primaries='1',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	theGrandfather.save()
	theGrandfather.affixes.add(mainStat, grandfatherLife, durability)

	theSultanOfBlindingSand = Weapon(slot='2H Weapons',
		name='The Sultan of Blinding Sand',
		pic='media/items/legendaries/weapons/2h/swords/the_sultan_of_blinding_sand.png',
		category='2H Swords',
		random_primaries='2',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	theSultanOfBlindingSand.save()
	theSultanOfBlindingSand.affixes.add(mainStat, sultanBlindChance)

	theZweihander = Weapon(slot='2H Weapons',
		name='The Zweihander',
		pic='media/items/legendaries/weapons/2h/swords/the_zweihander.png',
		category='2H Swords',
		random_primaries='2',
		random_secondaries='1',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	theZweihander.save()
	theZweihander.affixes.add(mainStat, killExp)

	warmonger = Weapon(slot='2H Weapons',
		name='Warmonger',
		pic='media/items/legendaries/weapons/2h/swords/warmonger.png',
		category='2H Swords',
		random_primaries='1',
		random_secondaries='2',
		owner='bb-cs-mk-wd-wz',
		patch='23')
	warmonger.save()
	warmonger.affixes.add(mainStat, sockets)

	for weapon in Weapon.objects.filter(category="2H Swords"):
		weapon.inherent = '<span class="inherent"><span>1.15</span> Attacks per Second</span>'
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
        ('legendaries', '0002_1h_weapons'),
    ]

    operations = [
        migrations.RunPython(load_2h_axes),
        migrations.RunPython(load_bows),
        migrations.RunPython(load_crossbows),
        migrations.RunPython(load_daibos),
        migrations.RunPython(load_2h_flails),
        migrations.RunPython(load_2h_maces),
        migrations.RunPython(load_2h_mighty_weapons),
        migrations.RunPython(load_polearms),
        migrations.RunPython(load_staves),
        migrations.RunPython(load_2h_swords),
        migrations.RunPython(load_slugs)
    ]