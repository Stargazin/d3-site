'''
Everything about itemsets, their effects, and pieces.
Ordered by classes: Universal -> Barb -> Crusader -> etc.

Defined in order from item set -> set pieces -> set effects
'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_item_sets(apps, schema_editor):
	ItemSet = apps.get_model("itemsets", "ItemSet")
	Effect = apps.get_model("itemsets", "SetEffect")
	SetPiece = apps.get_model("itemsets", "SetPiece")

#Universal
#==============================================================================
	ashearasVestments = ItemSet(name='Asheara\'s Vestments',
		owner='Universal',
		patch='23')
	ashearasVestments.save()

	ashearasCustodian = SetPiece(name='Asheara\'s Custodian',
		pic='media/items/sets/universal/ashearas_custodian.png',
		category='Shoulders',
		itemSet=ashearasVestments)
	ashearasCustodian.save()

	ashearasWard = SetPiece(name='Asheara\'s Ward',
		pic='media/items/sets/universal/ashearas_ward.png',
		category='Gloves',
		itemSet=ashearasVestments)
	ashearasWard.save()

	ashearasPace = SetPiece(name='Asheara\'s Pace',
		pic='media/items/sets/universal/ashearas_pace.png',
		category='Pants',
		itemSet=ashearasVestments)
	ashearasPace.save()

	ashearasFinders = SetPiece(name='Asheara\'s Finders',
		pic='media/items/sets/universal/ashearas_finders.png',
		category='Boots',
		itemSet=ashearasVestments)
	ashearasFinders.save()

	ashearasVestments2 = Effect(pieces='2',
		effect='<li><p><span class="silver">+100</span> Resistance to All Elements</p></li>',
		itemSet=ashearasVestments)
	ashearasVestments2.save()

	ashearasVestments3 = Effect(pieces='3',
		effect='<li><p><span class="silver">+20%</span> Life</p></li>',
		itemSet=ashearasVestments)
	ashearasVestments3.save()

	ashearasVestments4 = Effect(pieces='4',
		effect='<li><p>Attacks cause your Followers to occasionally come to your aid</p></li>',
		itemSet=ashearasVestments)
	ashearasVestments4.save()



	aughildsAuthority = ItemSet(name='Aughild\'s Authority',
		owner='Universal',
		patch='23')
	aughildsAuthority.save()

	aughildsSpike = SetPiece(name='Aughild\'s Spike',
		pic='media/items/sets/universal/aughilds_spike.png',
		category='Helmet',
		itemSet=aughildsAuthority)
	aughildsSpike.save()

	aughildsPower = SetPiece(name='Aughild\'s Power',
		pic='media/items/sets/universal/aughilds_power.png',
		category='Shoulders',
		itemSet=aughildsAuthority)
	aughildsPower.save()

	aughildsRule = SetPiece(name='Aughild\'s Rule',
		pic='media/items/sets/universal/aughilds_rule.png',
		category='Chest Armor',
		itemSet=aughildsAuthority)
	aughildsRule.save()

	aughildsSearch = SetPiece(name='Aughild\'s Search',
		pic='media/items/sets/universal/aughilds_search.png',
		category='Bracers',
		itemSet=aughildsAuthority)
	aughildsSearch.save()

	aughildsAuthority2 = Effect(pieces='2',
		effect='<li><p>Reduces damage from Ranged attacks by <span class="silver">7.0%</span></p></li><li><p>Reduces damage from Melee attacks by <span class="silver">7.0%</span></p></li>',
		itemSet=aughildsAuthority)
	aughildsAuthority2.save()

	aughildsAuthority3 = Effect(pieces='3',
		effect='<li><p>Reduces damage from Elites by <span class="silver">15.0%</span></p></li><li><p>Increases damage against Elites by <span class="silver">15.0%</span></p></li>',
		itemSet=aughildsAuthority)
	aughildsAuthority3.save()



	bastionsOfWill = ItemSet(name='Bastions of Will',
		owner='Universal',
		patch='23')
	bastionsOfWill.save()

	focus = SetPiece(name='Focus',
		pic='media/items/sets/universal/focus.png',
		category='Ring',
		itemSet=bastionsOfWill)
	focus.save()

	restraint = SetPiece(name='Restraint',
		pic='media/items/sets/universal/restraint.png',
		category='Ring',
		itemSet=bastionsOfWill)
	restraint.save()

	bastionsOfWill2 = Effect(pieces='2',
		effect='<li><p>When you hit with a Resource-generating attack or Primary Skill, deal <span class="silver">50%</span> increased damage for <span class="silver">5</span> seconds</p></li><li><p>When you hit with a Resource-spending attack, deal <span class="silver">50%</span> increased damage for <span class="silver">5</span> seconds</p></li>',
		itemSet=bastionsOfWill)
	bastionsOfWill2.save()



	blackthornesBattlegear = ItemSet(name='Blackthorne\'s Battlegear',
		owner='Universal',
		patch='23')
	blackthornesBattlegear.save()

	blackthornesSurcoat = SetPiece(name='Blackthorne\'s Surcoat',
		pic='media/items/sets/universal/blackthornes_surcoat.png',
		category='Chest Armor',
		itemSet=blackthornesBattlegear)
	blackthornesSurcoat.save()

	blackthornesNotchedBelt = SetPiece(name='Blackthorne\'s Notched Belt',
		pic='media/items/sets/universal/blackthornes_notched_belt.png',
		category='Belt',
		itemSet=blackthornesBattlegear)
	blackthornesNotchedBelt.save()

	blackthornesJoustingMail = SetPiece(name='Blackthorne\'s Jousting Mail',
		pic='media/items/sets/universal/blackthornes_jousting_mail.png',
		category='Pants',
		itemSet=blackthornesBattlegear)
	blackthornesJoustingMail.save()

	blackthornesSpurs = SetPiece(name='Blackthorne\'s Spurs',
		pic='media/items/sets/universal/blackthornes_spurs.png',
		category='Boots',
		itemSet=blackthornesBattlegear)
	blackthornesSpurs.save()

	blackthornesDuncraigCross = SetPiece(name='Blackthorne\'s Duncraig Cross',
		pic='media/items/sets/universal/blackthornes_duncraig_cross.png',
		category='Amulet',
		itemSet=blackthornesBattlegear)
	blackthornesDuncraigCross.save()

	blackthornesBattlegear2 = Effect(pieces='2',
		effect='<li><p><span class="silver">+250</span> Vitality</p></li><li><p>Increases damage against Elites by <span class="silver">10.0%</span></p></li>',
		itemSet=blackthornesBattlegear)
	blackthornesBattlegear2.save()

	blackthornesBattlegear3 = Effect(pieces='3',
		effect='<li><p><span class="silver">+25%</span> Extra Gold from Monsters</p></li><li><p>Reduces damage from Elites by <span class="silver">10.0%</span></p></li>',
		itemSet=blackthornesBattlegear)
	blackthornesBattlegear3.save()

	blackthornesBattlegear4 = Effect(pieces='4',
		effect='<li><p>You are immune to Desecrator, Molten, and Plagued monster effects</p></li>',
		itemSet=blackthornesBattlegear)
	blackthornesBattlegear4.save()



	bornsCommand = ItemSet(name='Born\'s Command',
		owner='Universal',
		patch='23')
	bornsCommand.save()

	bornsFuriousWrath = SetPiece(name='Born\'s Furious Wrath',
		pic='media/items/sets/universal/borns_furious_wrath.png',
		category='1H Sword',
		itemSet=bornsCommand)
	bornsFuriousWrath.save()

	bornsPrivilege = SetPiece(name='Born\'s Privilege',
		pic='media/items/sets/universal/borns_privilege.png',
		category='Shoulders',
		itemSet=bornsCommand)
	bornsPrivilege.save()

	bornsFrozenSoul = SetPiece(name='Born\'s Frozen Soul',
		pic='media/items/sets/universal/borns_frozen_soul.png',
		category='Chest Armor',
		itemSet=bornsCommand)
	bornsFrozenSoul.save()

	bornsCommand2 = Effect(pieces='2',
		effect='<li><p>+15% Life</p></li>',
		itemSet=bornsCommand)
	bornsCommand2.save()

	bornsCommand3 = Effect(pieces='3',
		effect='<li><p>Reduces cooldown of all Skills by <span class="silver">10.0%</span></p></li><li><p>Increases Bonus Experience by <span class="silver">20%</span></p></li>',
		itemSet=bornsCommand)
	bornsCommand3.save()



	cainsDestiny = ItemSet(name='Cain\'s Destiny',
		owner='Universal',
		patch='23')
	cainsDestiny.save()

	cainsInsight = SetPiece(name='Cain\'s Insight',
		pic='media/items/sets/universal/cains_insight.png',
		category='Helmet',
		itemSet=cainsDestiny)
	cainsInsight.save()

	cainsScrivener = SetPiece(name='Cain\'s Scrivener',
		pic='media/items/sets/universal/cains_scrivener.png',
		category='Gloves',
		itemSet=cainsDestiny)
	cainsScrivener.save()

	cainsHabit = SetPiece(name='Cain\'s Habit',
		pic='media/items/sets/universal/cains_habit.png',
		category='Pants',
		itemSet=cainsDestiny)
	cainsHabit.save()

	cainsTravelers = SetPiece(name='Cain\'s Travelers',
		pic='media/items/sets/universal/cains_travelers.png',
		category='Boots',
		itemSet=cainsDestiny)
	cainsTravelers.save()

	cainsDestiny2 = Effect(pieces='2',
		effect='<li><p>Attack Speed Increased by <span class="silver">8.0%</span></p></li>',
		itemSet=cainsDestiny)
	cainsDestiny2.save()

	cainsDestiny3 = Effect(pieces='3',
		effect='<li><p><span class="silver">50%</span> Better Chance of Finding Magical Items</p></li><li><p>Increases Bonus Experience by <span class="silver">50%</span></p></li>',
		itemSet=cainsDestiny)
	cainsDestiny3.save()



	captainCrimsonsTrimmings = ItemSet(name='Captain Crimson\'s Trimmings',
		owner='Universal',
		patch='23')
	captainCrimsonsTrimmings.save()

	captainCrimsonsSilkGirdle = SetPiece(name='Captain Crimson\'s Silk Girdle',
		pic='media/items/sets/universal/captain_crimsons_silk_girdle.png',
		category='Belt',
		itemSet=captainCrimsonsTrimmings)
	captainCrimsonsSilkGirdle.save()

	captainCrimsonsThrust = SetPiece(name='Captain Crimson\'s Thrust',
		pic='media/items/sets/universal/captain_crimsons_thrust.png',
		category='Pants',
		itemSet=captainCrimsonsTrimmings)
	captainCrimsonsThrust.save()

	captainCrimsonsWaders = SetPiece(name='Captain Crimson\'s Waders',
		pic='media/items/sets/universal/captain_crimsons_waders.png',
		category='Boots',
		itemSet=captainCrimsonsTrimmings)
	captainCrimsonsWaders.save()

	captainCrimsonsTrimmings2 = Effect(pieces='2',
		effect='<li><p>Regenerates <span class="silver">6000</span> Life per Second</p></li><li><p>Reduces cooldown of all Skills by <span class="silver">10.0%</span></p></li>',
		itemSet=captainCrimsonsTrimmings)
	captainCrimsonsTrimmings2.save()

	captainCrimsonsTrimmings3 = Effect(pieces='3',
		effect='<li><p><span class="silver">+50</span> Resistance to All Elements</p></li><li><p>Reduces all Resource costs by <span class="silver">10%</span></p></li>',
		itemSet=captainCrimsonsTrimmings)
	captainCrimsonsTrimmings3.save()



	demonsHide = ItemSet(name='Demon\'s Hide',
		owner='Universal',
		patch='23')
	demonsHide.save()

	demonsAileron = SetPiece(name='Demon\'s Aileron',
		pic='media/items/sets/universal/demons_aileron.png',
		category='Shoulders',
		itemSet=demonsHide)
	demonsAileron.save()

	demonsMarrow = SetPiece(name='Demon\'s Marrow',
		pic='media/items/sets/universal/demons_marrow.png',
		category='Chest Armor',
		itemSet=demonsHide)
	demonsMarrow.save()

	demonsAnimus = SetPiece(name='Demon\'s Animus',
		pic='media/items/sets/universal/demons_animus.png',
		category='Bracers',
		itemSet=demonsHide)
	demonsAnimus.save()

	demonsRestraint = SetPiece(name='Demon\'s Restraint',
		pic='media/items/sets/universal/demons_restraint.png',
		category='Belt',
		itemSet=demonsHide)
	demonsRestraint.save()

	demonsPlate = SetPiece(name='Demon\'s Plate',
		pic='media/items/sets/universal/demons_plate.png',
		category='Pants',
		itemSet=demonsHide)
	demonsPlate.save()

	demonsHide2 = Effect(pieces='2',
		effect='<li><p>Ranged and Melee attackers take <span class="silver">6000</span> Fire damage per hit</p></li>',
		itemSet=demonsHide)
	demonsHide2.save()

	demonsHide3 = Effect(pieces='3',
		effect='<li><p>Chance to Deal <span class="silver">25%</span> Area Damage on Hit</p></li>',
		itemSet=demonsHide)
	demonsHide3.save()

	demonsHide4 = Effect(pieces='4',
		effect='<li><p><span class="silver">+15%</span> Damage to Demons</p></li><li><p>Chance to reflect Projectiles when you are hit by enemies</p></li>',
		itemSet=demonsHide)
	demonsHide4.save()



	endlessWalk = ItemSet(name='Endless Walk',
		owner='Universal',
		patch='24')
	endlessWalk.save()

	theTravelersPledge = SetPiece(name='The Traveler\'s Pledge',
		pic='media/items/sets/universal/the_travelers_pledge.png',
		category='Amulet',
		itemSet=endlessWalk)
	theTravelersPledge.save()

	theCompassRose = SetPiece(name='The Compass Rose',
		pic='media/items/sets/universal/the_compass_rose.png',
		category='Ring',
		itemSet=endlessWalk)
	theCompassRose.save()

#2.4
	endlessWalk2 = Effect(pieces='2',
		# effect='<li><p><span class="silver">+250</span> Vitality</p></li><li><p>Critical Hit Damage Increased by <span class="silver">50.0%</span></p></li>',
		effect='<li><p>While moving, damage taken is reduced by up to <span class="silver">50%</span></p></li><li><p>While standing still, damage dealt is increased by up to <span class="silver">100%</span></p></li>',
		itemSet=endlessWalk)
	endlessWalk2.save()



	guardiansJeopardy = ItemSet(name='Guardian\'s Jeopardy',
		owner='Universal',
		patch='23')
	guardiansJeopardy.save()

	guardiansGaze = SetPiece(name='Guardian\'s Gaze',
		pic='media/items/sets/universal/guardians_gaze.png',
		category='Helmet',
		itemSet=guardiansJeopardy)
	guardiansGaze.save()

	guardiansAversion = SetPiece(name='Guardian\'s Aversion',
		pic='media/items/sets/universal/guardians_aversion.png',
		category='Bracers',
		itemSet=guardiansJeopardy)
	guardiansAversion.save()

	guardiansCase = SetPiece(name='Guardian\'s Case',
		pic='media/items/sets/universal/guardians_case.png',
		category='Belt',
		itemSet=guardiansJeopardy)
	guardiansCase.save()

	guardiansJeopardy2 = Effect(pieces='2',
		effect='<li><p><span class="silver">+250</span> Vitality</p></li><li><p>Regenerates <span class="silver">8000</span> Life per Second</p></li>',
		itemSet=guardiansJeopardy)
	guardiansJeopardy2.save()

	guardiansJeopardy3 = Effect(pieces='3',
		effect='<li><p><span class="silver">+15%</span> Movement Speed</p></li>',
		itemSet=guardiansJeopardy)
	guardiansJeopardy3.save()



	hallowedProtectors = ItemSet(name='Hallowed Protectors',
		owner='Universal',
		patch='23')
	hallowedProtectors.save()

	hallowedBarricade = SetPiece(name='Hallowed Barricade',
		pic='media/items/sets/universal/hallowed_barricade.png',
		category='Shield',
		itemSet=hallowedProtectors)
	hallowedBarricade.save()

	hallowedBreach = SetPiece(name='Hallowed Breach',
		pic='media/items/sets/universal/hallowed_breach.png',
		category='1H Axe',
		itemSet=hallowedProtectors)
	hallowedBreach.save()

	hallowedSufferance = SetPiece(name='Hallowed Sufferance',
		pic='media/items/sets/universal/hallowed_sufferance.png',
		category='Ceremonial Knife',
		itemSet=hallowedProtectors)
	hallowedSufferance.save()

	hallowedHold = SetPiece(name='Hallowed Hold',
		pic='media/items/sets/universal/hallowed_hold.png',
		category='Fist Weapon',
		itemSet=hallowedProtectors)
	hallowedHold.save()

	hallowedCondemnation = SetPiece(name='Hallowed Condemnation',
		pic='media/items/sets/universal/hallowed_condemnation.png',
		category='Hand Crossbow',
		itemSet=hallowedProtectors)
	hallowedCondemnation.save()

	hallowedNemesis = SetPiece(name='Hallowed Nemesis',
		pic='media/items/sets/universal/hallowed_nemesis.png',
		category='1H Mighty Weapon',
		itemSet=hallowedProtectors)
	hallowedNemesis.save()

	hallowedBaton = SetPiece(name='Hallowed Baton',
		pic='media/items/sets/universal/hallowed_baton.png',
		category='Wand',
		itemSet=hallowedProtectors)
	hallowedBaton.save()

	hallowedProtectors2 = Effect(pieces='2',
		effect='<li><p><span class="silver">+100</span> Resistance to All Elements</p></li><li><p>Attack Speed Increased by <span class="silver">10.0%</span></p></li>',
		itemSet=hallowedProtectors)
	hallowedProtectors2.save()



	istvansPairedBlades = ItemSet(name='Istvan\'s Paired Blades',
		owner='Universal',
		patch='24')
	istvansPairedBlades.save()

	littleRogue = SetPiece(name='Little Rogue',
		pic='media/items/sets/universal/little_rogue.png',
		category='1H Sword',
		itemSet=istvansPairedBlades)
	littleRogue.save()

	theSlanderer = SetPiece(name='The Slanderer',
		pic='media/items/sets/universal/the_slanderer.png',
		category='1H Sword',
		itemSet=istvansPairedBlades)
	theSlanderer.save()

#2.4
	istvansPairedBlades2 = Effect(pieces='2',
		effect='<li><p>Every time you spend Primary Resource, you gain <span class="silver">6%</span> increased Attack Speed, Damage, and Armor for <span class="silver">5</span> seconds. This effect stacks up to <span class="silver">5</span> times</p></li>',
		itemSet=istvansPairedBlades)
	istvansPairedBlades2.save()



	krelmsBuffBulkwark = ItemSet(name='Krelm\'s Buff Bulkwark',
		owner='Universal',
		patch='23')
	krelmsBuffBulkwark.save()

	krelmsBuffBracers = SetPiece(name='Krelm\'s Buff Bracers',
		pic='media/items/sets/universal/krelms_buff_bracers.png',
		category='Bracers',
		itemSet=krelmsBuffBulkwark)
	krelmsBuffBracers.save()

	krelmsBuffBelt = SetPiece(name='Krelm\'s Buff Belt',
		pic='media/items/sets/universal/krelms_buff_belt.png',
		category='Belt',
		itemSet=krelmsBuffBulkwark)
	krelmsBuffBelt.save()

	krelmsBuffBulkwark2 = Effect(pieces='2',
		effect='<li><p><span class="silver">+500</span> Vitality</p></li>',
		itemSet=krelmsBuffBulkwark)
	krelmsBuffBulkwark2.save()



	legacyOfNightmares = ItemSet(name='Legacy of Nightmares',
		owner='Universal',
		patch='24')
	legacyOfNightmares.save()

	litanyOfTheUndaunted = SetPiece(name='Litany of the Undaunted',
		pic='media/items/sets/universal/litany_of_the_undaunted.png',
		category='Ring',
		itemSet=legacyOfNightmares)
	litanyOfTheUndaunted.save()

	theWailingHost = SetPiece(name='The Wailing Host',
		pic='media/items/sets/universal/the_wailing_host.png',
		category='Ring',
		itemSet=legacyOfNightmares)
	theWailingHost.save()

#2.4
	legacyOfNightmares2 = Effect(pieces='2',
		# effect='<li><p><span class="silver">+15%</span> Extra Gold from Monsters</p></li><li><p><span class="silver">+15%</span> Better Chance of Finding Magical Items</p></li><li><p>This ring sometimes summons a Skeleton when you attack</p></li>',
		effect='<li><p>While this is your only item Set Bonus your damage dealt is increased by <span class="silver">100%</span> and damage taken is reduced by <span class="silver">4%</span> for every Ancient Item you have equipped</p></li>',
		itemSet=legacyOfNightmares)
	legacyOfNightmares2.save()



	sagesJourney = ItemSet(name='Sage\'s Journey',
		owner='Universal',
		patch='23')
	sagesJourney.save()

	sagesApogee = SetPiece(name='Sage\'s Apogee',
		pic='media/items/sets/universal/sages_apogee.png',
		category='Helmet',
		itemSet=sagesJourney)
	sagesApogee.save()

	sagesPurchase = SetPiece(name='Sage\'s Purchase',
		pic='media/items/sets/universal/sages_purchase.png',
		category='Gloves',
		itemSet=sagesJourney)
	sagesPurchase.save()

	sagesPassage = SetPiece(name='Sage\'s Passage',
		pic='media/items/sets/universal/sages_passage.png',
		category='Boots',
		itemSet=sagesJourney)
	sagesPassage.save()

	sagesJourney2 = Effect(pieces='2',
		effect='<li><p>+250 Strength</p></li><li><p>+250 Dexterity</p></li><li><p>+250 Intelligence</p></li><li><p>+250 Vitality</p></li>',
		itemSet=sagesJourney)
	sagesJourney2.save()

	sagesJourney3 = Effect(pieces='3',
		effect='<li><p>Increases Death\'s Breath drops by <span class="silver">1</span></p></li>',
		itemSet=sagesJourney)
	sagesJourney3.save()

#Barbarian
#==============================================================================
	bulKathossOath = ItemSet(name='Bul-Kathos\'s Oath',
		owner='Barbarian',
		patch='23')
	bulKathossOath.save()

	bulKathossWarriorBlood = SetPiece(name='Bul-Kathos\'s Warrior Blood',
		pic='media/items/sets/barb/bul_kathoss_warrior_blood.png',
		category='1H Mighty Weapon',
		itemSet=bulKathossOath)
	bulKathossWarriorBlood.save()

	bulKathossSolemnVow = SetPiece(name='Bul-Kathos\'s Solemn Vow',
		pic='media/items/sets/barb/bul_kathoss_solemn_vow.png',
		category='1H Mighty Weapon',
		itemSet=bulKathossOath)
	bulKathossSolemnVow.save()

	bulKathossOath2 = Effect(pieces='2',
		effect='<li><p>Increases Fury Generation by <span class="silver">10</span></p></li><li><p>During Whirlwind you gain <span class="silver">30%</span> increased Attack Speed and Movement Speed</p></li>',
		itemSet=bulKathossOath)
	bulKathossOath2.save()



	mightOfTheEarth = ItemSet(name='Might of the Earth',
		owner='Barbarian',
		patch='24')
	mightOfTheEarth.save()

	eyesOfTheEarth = SetPiece(name='Eyes of the Earth',
		pic='media/items/sets/barb/eyes_of_the_earth.png',
		category='Helmet',
		itemSet=mightOfTheEarth)
	eyesOfTheEarth.save()

	spiresOfTheEarth = SetPiece(name='Spires of the Earth',
		pic='media/items/sets/barb/spires_of_the_earth.png',
		category='Shoulders',
		itemSet=mightOfTheEarth)
	spiresOfTheEarth.save()

#Added in 2.4
	spiritOfTheEarth = SetPiece(name='Spirit of the Earth',
		pic='media/items/sets/barb/spirit_of_the_earth.png',
		category='Chest Armor',
		itemSet=mightOfTheEarth)
	spiritOfTheEarth.save()
	spiritOfTheEarth

	pullOfTheEarth = SetPiece(name='Pull of the Earth',
		pic='media/items/sets/barb/pull_of_the_earth.png',
		category='Gloves',
		itemSet=mightOfTheEarth)
	pullOfTheEarth.save()

	weightOfTheEarth = SetPiece(name='Weight of the Earth',
		pic='media/items/sets/barb/weight_of_the_earth.png',
		category='Pants',
		itemSet=mightOfTheEarth)
	weightOfTheEarth.save()

#Added in 2.4
	foundationOfTheEarth = SetPiece(name='Foundation of the Earth',
		pic='media/items/sets/barb/foundation_of_the_earth.png',
		category='Boots',
		itemSet=mightOfTheEarth)
	foundationOfTheEarth.save()

#2.4
	mightOfTheEarth2 = Effect(pieces='2',
		# effect='<li><p>Reduce the cooldown of Earthquake by <span class="silver">2</span> seconds every time it kills an enemy</p></li>',
		effect='<li><p>Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by <span class="silver">1</span> second for every <span class="silver">30</span> Fury you spend</p></li>',
		itemSet=mightOfTheEarth)
	mightOfTheEarth2.save()

#2.4
	mightOfTheEarth4 = Effect(pieces='4',
		# effect='<li><p>Cause an Earthquake when you land after using Leap</p></li>',
		effect='<li><p>Leap causes an Earthquake when you land</p></li><li><p>Leap gains the effect of the Iron Impact rune and the duration and Armor bonus is increased by <span class="silver">150%</span></p></li>',
		itemSet=mightOfTheEarth)
	mightOfTheEarth4.save()

#Added in 2.4
	mightOfTheEarth6 = Effect(pieces='6',
		effect='<li><p>Increases the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear, and Seismic Slam by <span class="silver">800%</span></p></li>',
		itemSet=mightOfTheEarth)
	mightOfTheEarth6.save()



	immortalKingsCall = ItemSet(name='Immortal King\'s Call',
		owner='Barbarian',
		patch='23')
	immortalKingsCall.save()

	immortalKingsBoulderBreaker = SetPiece(name='Immortal King\'s Boulder Breaker',
		pic='media/items/sets/barb/immortal_kings_boulder_breaker.png',
		category='2H Mighty Weapon',
		itemSet=immortalKingsCall)
	immortalKingsBoulderBreaker.save()

	immortalKingsTriumph = SetPiece(name='Immortal King\'s Triumph',
		pic='media/items/sets/barb/immortal_kings_triumph.png',
		category='Helmet',
		itemSet=immortalKingsCall)
	immortalKingsTriumph.save()

	immortalKingsEternalReign = SetPiece(name='Immortal King\'s Eternal Reign',
		pic='media/items/sets/barb/immortal_kings_eternal_reign.png',
		category='Chest Armor',
		itemSet=immortalKingsCall)
	immortalKingsEternalReign.save()

	immortalKingsIrons = SetPiece(name='Immortal King\'s Irons',
		pic='media/items/sets/barb/immortal_kings_irons.png',
		category='Gloves',
		itemSet=immortalKingsCall)
	immortalKingsIrons.save()

	immortalKingsTribalBinding = SetPiece(name='Immortal King\'s Tribal Binding',
		pic='media/items/sets/barb/immortal_kings_tribal_binding.png',
		category='Belt',
		itemSet=immortalKingsCall)
	immortalKingsTribalBinding.save()

	immortalKingsStature = SetPiece(name='Immortal King\'s Stature',
		pic='media/items/sets/barb/immortal_kings_stature.png',
		category='Pants',
		itemSet=immortalKingsCall)
	immortalKingsStature.save()

	immortalKingsStride = SetPiece(name='Immortal King\'s Stride',
		pic='media/items/sets/barb/immortal_kings_stride.png',
		category='Boots',
		itemSet=immortalKingsCall)
	immortalKingsStride.save()

	immortalKingsCall2 = Effect(pieces='2',
		effect='<li><p>Call of the Ancients last until they die</p></li>',
		itemSet=immortalKingsCall)
	immortalKingsCall2.save()

	immortalKingsCall4 = Effect(pieces='4',
		effect='<li><p>Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by <span class="silver">3</span> seconds for every <span class="silver">10</span> Fury you spend with an attack</p></li>',
		itemSet=immortalKingsCall)
	immortalKingsCall4.save()

	immortalKingsCall6 = Effect(pieces='6',
		effect='<li><p>While both Wrath of the Berserker and Call of the Ancients is active, you deal <span class="silver">250%</span> increased damage</p></li>',
		itemSet=immortalKingsCall)
	immortalKingsCall6.save()



	theLegacyOfRaekor = ItemSet(name='The Legacy of Raekor',
		owner='Barbarian',
		patch='24')
	theLegacyOfRaekor.save()

	raekorsWill = SetPiece(name='Raekor\'s Will',
		pic='media/items/sets/barb/raekors_will.png',
		category='Helm',
		itemSet=theLegacyOfRaekor)
	raekorsWill.save()

	raekorsBurden = SetPiece(name='Raekor\'s Burden',
		pic='media/items/sets/barb/raekors_burden.png',
		category='Shoulders',
		itemSet=theLegacyOfRaekor)
	raekorsBurden.save()

	raekorsHeart = SetPiece(name='Raekor\'s Heart',
		pic='media/items/sets/barb/raekors_heart.png',
		category='Chest Armor',
		itemSet=theLegacyOfRaekor)
	raekorsHeart.save()

	raekorsWraps = SetPiece(name='Raekor\'s Wraps',
		pic='media/items/sets/barb/raekors_wraps.png',
		category='Gloves',
		itemSet=theLegacyOfRaekor)
	raekorsWraps.save()

	raekorsBreeches = SetPiece(name='Raekor\'s Breeches',
		pic='media/items/sets/barb/raekors_breeches.png',
		category='Pants',
		itemSet=theLegacyOfRaekor)
	raekorsBreeches.save()

	raekorsStriders = SetPiece(name='Raekor\'s Striders',
		pic='media/items/sets/barb/raekors_striders.png',
		category='Boots',
		itemSet=theLegacyOfRaekor)
	raekorsStriders.save()

#2.4
	theLegacyOfRaekor2 = Effect(pieces='2',
		# effect='<li><p>The first enemy hit by Furious Charge takes <span class="silver">100%</span> additional damage</p></li>',
		effect='<li><p>Furious Charge refunds a charge if it hits only <span class="silver">1</span> enemy</p></li>',
		itemSet=theLegacyOfRaekor)
	theLegacyOfRaekor2.save()

#2.4
	theLegacyOfRaekor4 = Effect(pieces='4',
		# effect='<li><p>Furious Charge gains the effect of every rune</p></li>',
		effect='<li><p>Furious Charge gains the effect of every rune and deals <span class="silver">300%</span> increased damage</p></li>',
		itemSet=theLegacyOfRaekor)
	theLegacyOfRaekor4.save()

#2.4
	theLegacyOfRaekor6 = Effect(pieces='6',
		# effect='<li><p>Enemies hit by your Furious Charge take <span class="silver">3000%</span> weapon damage over <span class="silver">3</span> seconds</p></li>',
		effect='<li><p>Every use of Furious Charge grants a stacking effect that increases the damage of your next Fury-spending attack by <span class="silver">300%</span></p></li><li><p>Every use of a Fury-spending attack consumes up to <span class="silver">5</span> stacks</p></li>',
		itemSet=theLegacyOfRaekor)
	theLegacyOfRaekor6.save()



	wrathOfTheWastes = ItemSet(name='Wrath of the Wastes',
		owner='Barbarian',
		patch='23')
	wrathOfTheWastes.save()

	helmOfTheWastes = SetPiece(name='Helm of the Wastes',
		pic='media/items/sets/barb/helm_of_the_wastes.png',
		category='Helmet',
		itemSet=wrathOfTheWastes)
	helmOfTheWastes.save()

	pauldronsOfTheWastes = SetPiece(name='Pauldrons of the Wastes',
		pic='media/items/sets/barb/pauldrons_of_the_wastes.png',
		category='Shoulders',
		itemSet=wrathOfTheWastes)
	pauldronsOfTheWastes.save()

	cuirassOfTheWastes = SetPiece(name='Cuirass of the Wastes',
		pic='media/items/sets/barb/cuirass_of_the_wastes.png',
		category='Chest Armor',
		itemSet=wrathOfTheWastes)
	cuirassOfTheWastes.save()

	gauntletOfTheWastes = SetPiece(name='Gauntlet of the Wastes',
		pic='media/items/sets/barb/gauntlet_of_the_wastes.png',
		category='Gloves',
		itemSet=wrathOfTheWastes)
	gauntletOfTheWastes.save()

	tassetOfTheWastes = SetPiece(name='Tasset of the Wastes',
		pic='media/items/sets/barb/tasset_of_the_wastes.png',
		category='Pants',
		itemSet=wrathOfTheWastes)
	tassetOfTheWastes.save()

	sabatonOfTheWastes = SetPiece(name='Sabaton of the Wastes',
		pic='media/items/sets/barb/sabaton_of_the_wastes.png',
		category='Boots',
		itemSet=wrathOfTheWastes)
	sabatonOfTheWastes.save()

	wrathOfTheWastes2 = Effect(pieces='2',
		effect='<li><p>Increase the damage per second of Rend by <span class="silver">500%</span> and its duration to <span class="silver">15</span> seconds</p></li>',
		itemSet=wrathOfTheWastes)
	wrathOfTheWastes2.save()

	wrathOfTheWastes4 = Effect(pieces='4',
		effect='<li><p>During Whirlwind you gain <span class="silver">40%</span> damage reduction</p></li>',
		itemSet=wrathOfTheWastes)
	wrathOfTheWastes4.save()

	wrathOfTheWastes6 = Effect(pieces='6',
		effect='<li><p>Whirlwind gains the effect of the Dust Devils rune and Dust Devils damage is increased to <span class="silver">2500%</span> weapon damage</p></li>',
		itemSet=wrathOfTheWastes)
	wrathOfTheWastes6.save()

#Crusader
#==============================================================================
	armorOfAkkhan = ItemSet(name='Armor of Akkhan',
		owner='Crusader',
		patch='24')
	armorOfAkkhan.save()

	helmOfAkkhan = SetPiece(name='Helm of Akkhan',
		pic='media/items/sets/sader/helm_of_akkhan.png',
		category='Helmet',
		itemSet=armorOfAkkhan)
	helmOfAkkhan.save()

	pauldronsOfAkkhan = SetPiece(name='Pauldrons of Akkhan',
		pic='media/items/sets/sader/pauldrons_of_akkhan.png',
		category='Shoulders',
		itemSet=armorOfAkkhan)
	pauldronsOfAkkhan.save()

	breastplateOfAkkhan = SetPiece(name='Breastplate of Akkhan',
		pic='media/items/sets/sader/breastplate_of_akkhan.png',
		category='Chest Armor',
		itemSet=armorOfAkkhan)
	breastplateOfAkkhan.save()

	gauntletsOfAkkhan = SetPiece(name='Gauntlets of Akkhan',
		pic='media/items/sets/sader/gauntlets_of_akkhan.png',
		category='Gloves',
		itemSet=armorOfAkkhan)
	gauntletsOfAkkhan.save()

	cuissesOfAkkhan = SetPiece(name='Cuisses of Akkhan',
		pic='media/items/sets/sader/cuisses_of_akkhan.png',
		category='Pants',
		itemSet=armorOfAkkhan)
	cuissesOfAkkhan.save()

	sabatonsOfAkkhan = SetPiece(name='Sabatons of Akkhan',
		pic='media/items/sets/sader/sabatons_of_akkhan.png',
		category='Boots',
		itemSet=armorOfAkkhan)
	sabatonsOfAkkhan.save()

#2.4
	armorOfAkkhan2 = Effect(pieces='2',
		# effect='<li><p><span class="silver">+500</span> Strength</p></li>',
		effect='<li><p>Reduces the cost of all abilities by <span class="silver">50%</span> while Akarat\'s Champion is active</p></li>',
		itemSet=armorOfAkkhan)
	armorOfAkkhan2.save()

#2.4
	armorOfAkkhan4 = Effect(pieces='4',
		# effect='<li><p>Reduce the cost of all abilities by <span class="silver">50%</span> while Akarat\'s Champion is active</p></li>',
		effect='<li><p>Reduce the cooldown of Akarat\'s Champion by <span class="silver">50%</span></p></li>',
		itemSet=armorOfAkkhan)
	armorOfAkkhan4.save()

#2.4
	armorOfAkkhan6 = Effect(pieces='6',
		# effect='<li><p>Reduce the cooldown of Akarat\'s Champion by <span class="silver">50%</span></p></li>',
		effect='<li><p>While Akarat\'s Champion is active, you deal <span class="silver">450%</span> increased damage</p></li>',
		itemSet=armorOfAkkhan)
	armorOfAkkhan6.save()


#2.4
	norvaldsFervor = ItemSet(name='Norvald\'s Fervor',
		owner='Crusader',
		patch='24')
	norvaldsFervor.save()

	flailOfTheCharge = SetPiece(name='Flail of the Charge',
		pic='media/items/sets/sader/flail_of_the_charge.png',
		category='2H Flail',
		itemSet=norvaldsFervor)
	flailOfTheCharge.save()

	shieldOfTheSteed = SetPiece(name='Shield of the Steed',
		pic='media/items/sets/sader/shield_of_the_steed.png',
		category='Crusader Shield',
		itemSet=norvaldsFervor)
	shieldOfTheSteed.save()

	norvaldsFervor2 = Effect(pieces='2',
		effect='<li><p>Increases the duration of Steed Charge by <span class="silver">2</span> seconds</p></li><li><p>Every enemy killed while Steed Charge is active reduces the cooldown by <span class="silver">1</span> second</p></li><li><p>Gain <span class="silver">100%</span> increased damage while Steed Charge is active and for <span class="silver">5</span> seconds after Steed Charge ends</p></li>',
		itemSet=norvaldsFervor)
	norvaldsFervor2.save()



	rolandsLegacy = ItemSet(name='Roland\'s Legacy',
		owner='Crusader',
		patch='24')
	rolandsLegacy.save()

	rolandsVisage = SetPiece(name='Roland\'s Visage',
		pic='media/items/sets/sader/rolands_visage.png',
		category='Helmet',
		itemSet=rolandsLegacy)
	rolandsVisage.save()

	rolandsMantle = SetPiece(name='Roland\'s Mantle',
		pic='media/items/sets/sader/rolands_mantle.png',
		category='Shoulders',
		itemSet=rolandsLegacy)
	rolandsMantle.save()

	rolandsBearing = SetPiece(name='Roland\'s Bearing',
		pic='media/items/sets/sader/rolands_bearing.png',
		category='Chest Armor',
		itemSet=rolandsLegacy)
	rolandsBearing.save()

	rolandsGrasp = SetPiece(name='Roland\'s Grasp',
		pic='media/items/sets/sader/rolands_grasp.png',
		category='Gloves',
		itemSet=rolandsLegacy)
	rolandsGrasp.save()

	rolandsDetermination = SetPiece(name='Roland\'s Determination',
		pic='media/items/sets/sader/rolands_determination.png',
		category='Pants',
		itemSet=rolandsLegacy)
	rolandsDetermination.save()

	rolandsStride = SetPiece(name='Roland\'s Stride',
		pic='media/items/sets/sader/rolands_stride.png',
		category='Boots',
		itemSet=rolandsLegacy)
	rolandsStride.save()

	rolandsLegacy2 = Effect(pieces='2',
		effect='<li><p>Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by <span class="silver">1</span> second</p></li>',
		itemSet=rolandsLegacy)
	rolandsLegacy2.save()

	rolandsLegacy4 = Effect(pieces='4',
		effect='<li><p>Increase the damage of Shield Bash and Sweep Attack by <span class="silver">500%</span></p></li>',
		itemSet=rolandsLegacy)
	rolandsLegacy4.save()

#2.4
	rolandsLegacy6 = Effect(pieces='6',
		# effect='<li><p>Every use of Shield Bash or Sweep Attack that hits an enemy grants <span class="silver">30%</span> increased Attack Speed for <span class="silver">3</span> seconds. This effect stacks up to <span class="silver">5</span> times</p></li>',
		effect='<li><p>Every use of Shield Bash or Sweep Attack that hits an enemy grants <span class="silver">50%</span> increased Attack Speed and <span class="silver">10%</span> Damage Reduction for <span class="silver">5</span> seconds. This effect stacks up to <span class="silver">5</span> times</p></li>',
		itemSet=rolandsLegacy)
	rolandsLegacy6.save()



	seekerOfTheLight = ItemSet(name='Seeker of the Light',
		owner='Crusader',
		patch='24')
	seekerOfTheLight.save()

	crownOfTheLight = SetPiece(name='Crown of the Light',
		pic='media/items/sets/sader/crown_of_the_light.png',
		category='Helmet',
		itemSet=seekerOfTheLight)
	crownOfTheLight.save()

	mountainOfTheLight = SetPiece(name='Mountain of the Light',
		pic='media/items/sets/sader/mountain_of_the_light.png',
		category='Shoulders',
		itemSet=seekerOfTheLight)
	mountainOfTheLight.save()

	heartOfTheLight = SetPiece(name='Heart of the Light',
		pic='media/items/sets/sader/heart_of_the_light.png',
		category='Chest Armor',
		itemSet=seekerOfTheLight)
	heartOfTheLight.save()

	willOfTheLight = SetPiece(name='Will of the Light',
		pic='media/items/sets/sader/will_of_the_light.png',
		category='Gloves',
		itemSet=seekerOfTheLight)
	willOfTheLight.save()

	towersOfTheLight = SetPiece(name='Towers of the Light',
		pic='media/items/sets/sader/towers_of_the_light.png',
		category='Pants',
		itemSet=seekerOfTheLight)
	towersOfTheLight.save()

	foundationOfTheLight = SetPiece(name='Foundation of the Light',
		pic='media/items/sets/sader/foundation_of_the_light.png',
		category='Boots',
		itemSet=seekerOfTheLight)
	foundationOfTheLight.save()

	seekerOfTheLight2 = Effect(pieces='2',
		effect='<li><p>Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by <span class="silver">1</span> second</p></li>',
		itemSet=seekerOfTheLight)
	seekerOfTheLight2.save()

	seekerOfTheLight4 = Effect(pieces='4',
		effect='<li><p>You take <span class="silver">50%</span> less damage for <span class="silver">8</span> seconds after landing with Falling Sword</p></li>',
		itemSet=seekerOfTheLight)
	seekerOfTheLight4.save()

#2.4
	seekerOfTheLight6 = Effect(pieces='6',
		effect='<li><p>Increase the damage of Blessed Hammer by <span class="silver">1250%</span> and Falling Sword by <span class="silver">500%</span></p></li>',
		itemSet=seekerOfTheLight)
	seekerOfTheLight6.save()


#2.4 universal -> sader
	thornsOfTheInvoker = ItemSet(name='Thorns of the Invoker',
		owner='Crusader',
		patch='24')
	thornsOfTheInvoker.save()

	crownOfTheInvoker = SetPiece(name='Crown of the Invoker',
		pic='media/items/sets/sader/crown_of_the_invoker.png',
		category='Helmet',
		itemSet=thornsOfTheInvoker)
	crownOfTheInvoker.save()

	burdenOfTheInvoker = SetPiece(name='Burden of the Invoker',
		pic='media/items/sets/sader/burden_of_the_invoker.png',
		category='Shoulders',
		itemSet=thornsOfTheInvoker)
	burdenOfTheInvoker.save()

	prideOfTheInvoker = SetPiece(name='Pride of the Invoker',
		pic='media/items/sets/sader/pride_of_the_invoker.png',
		category='Gloves',
		itemSet=thornsOfTheInvoker)
	prideOfTheInvoker.save()

	shacklesOfTheInvoker = SetPiece(name='Shackles of the Invoker',
		pic='media/items/sets/sader/shackles_of_the_invoker.png',
		category='Bracers',
		itemSet=thornsOfTheInvoker)
	shacklesOfTheInvoker.save()

	renewalOfTheInvoker = SetPiece(name='Renewal of the Invoker',
		pic='media/items/sets/sader/renewal_of_the_invoker.png',
		category='Pants',
		itemSet=thornsOfTheInvoker)
	renewalOfTheInvoker.save()

	zealOfTheInvoker = SetPiece(name='Zeal of the Invoker',
		pic='media/items/sets/sader/zeal_of_the_invoker.png',
		category='Boots',
		itemSet=thornsOfTheInvoker)
	zealOfTheInvoker.save()

#2.4
	thornsOfTheInvoker2 = Effect(pieces='2',
		# effect='<li><p>Ranged and melee attackers take <span class="silver">4000</span> damage per hit</p></li>',
		effect='<li><p>Your Thorns damage now hits all enemies in a <span class="silver">15</span> yard radius</p></li><li><p>Each time you hit an enemy with Punish or Slash or block an attack, your Thorns damage is increased by <span class="silver">25%</span> for <span class="silver">2</span> seconds</p></li>',
		itemSet=thornsOfTheInvoker)
	thornsOfTheInvoker2.save()

#2.4
	thornsOfTheInvoker4 = Effect(pieces='4',
		# effect='<li><p>Your Thorns damage now hits all enemies in a <span class="silver">15</span> yard radius</p></li>',
		effect='<li><p>You take <span class="silver">50%</span> less damage for <span class="silver">20</span> seconds after casting Bombardment</p></li>',
		itemSet=thornsOfTheInvoker)
	thornsOfTheInvoker4.save()

#2.4
	thornsOfTheInvoker6 = Effect(pieces='6',
		effect='<li><p>Attack speed of Punish and Slash are increased by <span class="silver">50%</span> and deal <span class="silver">600%</span> of your Thorns damage to the first enemy hit</p></li>',
		itemSet=thornsOfTheInvoker)
	thornsOfTheInvoker6.save()

#Demon Hunter
#==============================================================================
	danettasHatred = ItemSet(name='Danetta\'s Hatred',
		owner='Demon Hunter',
		patch='24')
	danettasHatred.save()

	danettasRevenge = SetPiece(name='Danetta\'s Revenge',
		pic='media/items/sets/dh/danettas_revenge.png',
		category='Hand Crossbow',
		itemSet=danettasHatred)
	danettasRevenge.save()

	danettasSpite = SetPiece(name='Danetta\'s Spite',
		pic='media/items/sets/dh/danettas_spite.png',
		category='Hand Crossbow',
		itemSet=danettasHatred)
	danettasSpite.save()

#2.4
	danettasHatred2 = Effect(pieces='2',
		effect='<li><p>Vault costs <span class="silver">8</span> Hatred instead of Discipline</p></li><li><p>Vault deals <span class="silver">800%</span> increased damage</p></li>',
		itemSet=danettasHatred)
	danettasHatred2.save()



	embodimentOfTheMarauder = ItemSet(name='Embodiment of the Marauder',
		owner='Demon Hunter',
		patch='24')
	embodimentOfTheMarauder.save()

	maraudersVisage = SetPiece(name='Marauder\'s Visage',
		pic='media/items/sets/dh/marauders_visage.png',
		category='Helmet',
		itemSet=embodimentOfTheMarauder)
	maraudersVisage.save()

	maraudersSpines = SetPiece(name='Marauder\'s Spines',
		pic='media/items/sets/dh/marauders_spines.png',
		category='Shoulders',
		itemSet=embodimentOfTheMarauder)
	maraudersSpines.save()

	maraudersCarapace = SetPiece(name='Marauder\'s Carapace',
		pic='media/items/sets/dh/marauders_carapace.png',
		category='Chest Armor',
		itemSet=embodimentOfTheMarauder)
	maraudersCarapace.save()

	maraudersGloves = SetPiece(name='Marauder\'s Gloves',
		pic='media/items/sets/dh/marauders_gloves.png',
		category='Gloves',
		itemSet=embodimentOfTheMarauder)
	maraudersGloves.save()

	maraudersEncasement = SetPiece(name='Marauder\'s Encasement',
		pic='media/items/sets/dh/marauders_encasement.png',
		category='Pants',
		itemSet=embodimentOfTheMarauder)
	maraudersEncasement.save()

	maraudersTreads = SetPiece(name='Marauder\'s Treads',
		pic='media/items/sets/dh/marauders_treads.png',
		category='Boots',
		itemSet=embodimentOfTheMarauder)
	maraudersTreads.save()

	embodimentOfTheMarauder2 = Effect(pieces='2',
		effect='<li><p>Companion calls all Companions to your side</p></li>',
		itemSet=embodimentOfTheMarauder)
	embodimentOfTheMarauder2.save()

#2.4
	embodimentOfTheMarauder4 = Effect(pieces='4',
		effect='<li><p>Sentries deal <span class="silver">300%</span> increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do</p></li>',
		itemSet=embodimentOfTheMarauder)
	embodimentOfTheMarauder4.save()

#2.4
	embodimentOfTheMarauder6 = Effect(pieces='6',
		effect='<li><p>Your Primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal <span class="silver">600%</span> increased damage for each active Sentry</p></li>',
		itemSet=embodimentOfTheMarauder)
	embodimentOfTheMarauder6.save()



	natalyasVengeance = ItemSet(name='Natalya\'s Vengeance',
		owner='Demon Hunter',
		patch='24')
	natalyasVengeance.save()

	natalyasSlayer = SetPiece(name='Natalya\'s Slayer',
		pic='media/items/sets/dh/natalyas_slayer.png',
		category='Hand Crossbow',
		itemSet=natalyasVengeance)
	natalyasSlayer.save()

	natalyasSight = SetPiece(name='Natalya\'s Sight',
		pic='media/items/sets/dh/natalyas_sight.png',
		category='Helmet',
		itemSet=natalyasVengeance)
	natalyasSight.save()

	natalyasEmbrace = SetPiece(name='Natalya\'s Embrace',
		pic='media/items/sets/dh/natalyas_embrace.png',
		category='Cloak',
		itemSet=natalyasVengeance)
	natalyasEmbrace.save()

	natalyasTouch = SetPiece(name='Natalya\'s Touch',
		pic='media/items/sets/dh/natalyas_touch.png',
		category='Gloves',
		itemSet=natalyasVengeance)
	natalyasTouch.save()

	natalyasLeggings = SetPiece(name='Natalya\'s Leggings',
		pic='media/items/sets/dh/natalyas_leggings.png',
		category='Pants',
		itemSet=natalyasVengeance)
	natalyasLeggings.save()

	natalyasBloodyFootprints = SetPiece(name='Natalya\'s Bloody Footprints',
		pic='media/items/sets/dh/natalyas_bloody_footprints.png',
		category='Boots',
		itemSet=natalyasVengeance)
	natalyasBloodyFootprints.save()

	natalyasReflection = SetPiece(name='Natalya\'s Reflection',
		pic='media/items/sets/dh/natalyas_reflection.png',
		category='Ring',
		itemSet=natalyasVengeance)
	natalyasReflection.save()

#2.4
	natalyasVengeance2 = Effect(pieces='2',
		effect='<li><p>Reduce the cooldown of Rain of Vengeance by <span class="silver">4</span> seconds when you hit with a Hatred-generating attack or Hatred-spending attack</p></li>',
		itemSet=natalyasVengeance)
	natalyasVengeance2.save()

	natalyasVengeance4 = Effect(pieces='4',
		effect='<li><p>Rain of Vengeance deals <span class="silver">100%</span> increased damage</p></li>',
		itemSet=natalyasVengeance)
	natalyasVengeance4.save()

#2.4
	natalyasVengeance6 = Effect(pieces='6',
		effect='<li><p>After casting Rain of Vengeance, deal <span class="silver">400%</span> increased damage and take <span class="silver">60%</span> reduced damage for <span class="silver">10</span> seconds</p></li>',
		itemSet=natalyasVengeance)
	natalyasVengeance6.save()



	theShadowsMantle = ItemSet(name='The Shadow\'s Mantle',
		owner='Demon Hunter',
		patch='24')
	theShadowsMantle.save()

#Added in 2.4
	theShadowsMask = SetPiece(name='The Shadow\'s Mask',
		pic='media/items/sets/dh/the_shadows_mask.png',
		category='Helmet',
		itemSet=theShadowsMantle)
	theShadowsMask.save()

#Added in 2.4
	theShadowsBurden = SetPiece(name='The Shadow\'s Burden',
		pic='media/items/sets/dh/the_shadows_burden.png',
		category='Shoulders',
		itemSet=theShadowsMantle)
	theShadowsBurden.save()

	theShadowsBane = SetPiece(name='The Shadow\'s Bane',
		pic='media/items/sets/dh/the_shadows_bane.png',
		category='Chest Armor',
		itemSet=theShadowsMantle)
	theShadowsBane.save()

	theShadowsGrasp = SetPiece(name='The Shadow\'s Grasp',
		pic='media/items/sets/dh/the_shadows_grasp.png',
		category='Gloves',
		itemSet=theShadowsMantle)
	theShadowsGrasp.save()

	theShadowsCoil = SetPiece(name='The Shadow\'s Coil',
		pic='media/items/sets/dh/the_shadows_coil.png',
		category='Pants',
		itemSet=theShadowsMantle)
	theShadowsCoil.save()

	theShadowsHeels = SetPiece(name='The Shadow\'s Heels',
		pic='media/items/sets/dh/the_shadows_heels.png',
		category='Boots',
		itemSet=theShadowsMantle)
	theShadowsHeels.save()

#2.4
	theShadowsMantle2 = Effect(pieces='2',
		# effect='<li><p>When receiving fatal damage, you instead automatically cast Smoke Screen and are healed to <span class="silver">25%</span> Life. This effect may occur once every <span class="silver">120</span> seconds</p></li>',
		effect='<li><p>Your damage is increased by <span class="silver">600%</span> while you have a Melee Weapon equipped</p></li>',
		itemSet=theShadowsMantle)
	theShadowsMantle2.save()

#2.4
	theShadowsMantle4 = Effect(pieces='4',
		# effect='<li><p>Shadow Power gains the effect of every rune</p></li>',
		effect='<li><p>Shadow Power gains the effect of all runes and lasts forever</p></li>',
		itemSet=theShadowsMantle)
	theShadowsMantle4.save()

#Added in 2.4
	theShadowsMantle6 = Effect(pieces='6',
		effect='<li><p>Impale deals an additional <span class="silver">40,000%</span> weapon damage to the first enemy hit</p></li>',
		itemSet=theShadowsMantle)
	theShadowsMantle6.save()


	unhallowedEssence = ItemSet(name='Unhallowed Essence',
		owner='Demon Hunter',
		patch='24')
	unhallowedEssence.save()

	accursedVisage = SetPiece(name='Accursed Visage',
		pic='media/items/sets/dh/accursed_visage.png',
		category='Helmet',
		itemSet=unhallowedEssence)
	accursedVisage.save()

	unsanctifiedShoulders = SetPiece(name='Unsanctified Shoulders',
		pic='media/items/sets/dh/unsanctified_shoulders.png',
		category='Shoulders',
		itemSet=unhallowedEssence)
	unsanctifiedShoulders.save()

	cageOfTheHellborn = SetPiece(name='Cage of the Hellborn',
		pic='media/items/sets/dh/cage_of_the_hellborn.png',
		category='Chest Armor',
		itemSet=unhallowedEssence)
	cageOfTheHellborn.save()

	fiendishGrips = SetPiece(name='Fiendish Grips',
		pic='media/items/sets/dh/fiendish_grips.png',
		category='Gloves',
		itemSet=unhallowedEssence)
	fiendishGrips.save()

	unholyPlates = SetPiece(name='Unholy Plates',
		pic='media/items/sets/dh/unholy_plates.png',
		category='Pants',
		itemSet=unhallowedEssence)
	unholyPlates.save()

	hellWalkers = SetPiece(name='Hell Walkers',
		pic='media/items/sets/dh/hell_walkers.png',
		category='Boots',
		itemSet=unhallowedEssence)
	hellWalkers.save()

#2.4 check
	unhallowedEssence2 = Effect(pieces='2',
		# effect='<li><p>Your generators also generate <span class="silver">1</span> Discipline</p></li>',
		effect='<li><p>Your Generators now generate <span class="silver">2</span> additional Hatred</li>',
		itemSet=unhallowedEssence)
	unhallowedEssence2.save()

#2.4
	unhallowedEssence4 = Effect(pieces='4',
		effect='<li><p>Gain <span class="silver">60%</span> damage reduction and deal <span class="silver">60%</span> increased damage for <span class="silver">8</span> seconds if no enemy is within <span class="silver">10</span> yards of you</p></li>',
		itemSet=unhallowedEssence)
	unhallowedEssence4.save()

#2.4
	unhallowedEssence6 = Effect(pieces='6',
		effect='<li><p>Your Resource generators, Multishot, and Vengeance deal <span class="silver">20%</span> increased damage for every point of Discipline you have</p></li>',
		itemSet=unhallowedEssence)
	unhallowedEssence6.save()

#Monk
#==============================================================================
	innasMantra = ItemSet(name='Inna\'s Mantra',
		owner='Monk',
		patch='24')
	innasMantra.save()

	innasReach = SetPiece(name='Inna\'s Reach',
		pic='media/items/sets/monk/innas_reach.png',
		category='Daibo',
		itemSet=innasMantra)
	innasReach.save()

	innasRadiance = SetPiece(name='Inna\'s Radiance',
		pic='media/items/sets/monk/innas_radiance.png',
		category='Spirit Stone',
		itemSet=innasMantra)
	innasRadiance.save()

	innasVastExpanse = SetPiece(name='Inna\'s Vast Expanse',
		pic='media/items/sets/monk/innas_vast_expanse.png',
		category='Chest Armor',
		itemSet=innasMantra)
	innasVastExpanse.save()

	innasHold = SetPiece(name='Inna\'s Hold',
		pic='media/items/sets/monk/innas_hold.png',
		category='Gloves',
		itemSet=innasMantra)
	innasHold.save()

	innasFavor = SetPiece(name='Inna\'s Favor',
		pic='media/items/sets/monk/innas_favor.png',
		category='Belt',
		itemSet=innasMantra)
	innasFavor.save()

	innasTemperance = SetPiece(name='Inna\'s Temperance',
		pic='media/items/sets/monk/innas_temperance.png',
		category='Pants',
		itemSet=innasMantra)
	innasTemperance.save()

	innasSandals = SetPiece(name='Inna\'s Sandals',
		pic='media/items/sets/monk/innas_sandals.png',
		category='Boots',
		itemSet=innasMantra)
	innasSandals.save()

	innasMantra2 = Effect(pieces='2',
		effect='<li><p>Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by <span class="silver">100%</span></p></li>',
		itemSet=innasMantra)
	innasMantra2.save()

	innasMantra4 = Effect(pieces='4',
		effect='<li><p>Gain the base effect of all four Mantras at all times</p></li>',
		itemSet=innasMantra)
	innasMantra4.save()

#2.4
	innasMantra6 = Effect(pieces='6',
		# effect='<li><p>Mystic Ally casts Cyclone Strike, Exploding Palm, Lashing Tail Kick, Seven-Sided Strike, and Wave of Light when you do</p></li>',
		effect='<li><p>Gain the effects of every Mystic Ally rune at all times and your damage is increased by <span class="silver">50%</span> for each Mystic Ally you have</p></li>',
		itemSet=innasMantra)
	innasMantra6.save()



	monkeyKingsGarb = ItemSet(name='Monkey King\'s Garb',
		owner='Monk',
		patch='24')
	monkeyKingsGarb.save()

	sunwukosCrown = SetPiece(name='Sunwuko\'s Crown',
		pic='media/items/sets/monk/sunwukos_crown.png',
		category='Helmet',
		itemSet=monkeyKingsGarb)
	sunwukosCrown.save()

	sunwukosBalance = SetPiece(name='Sunwuko\'s Balance',
		pic='media/items/sets/monk/sunwukos_balance.png',
		category='Shoulders',
		itemSet=monkeyKingsGarb)
	sunwukosBalance.save()

#2.4
	sunwukosSoul = SetPiece(name='Sunwuko\'s Soul',
		pic='media/items/sets/monk/sunwukos_soul.png',
		category='Chest Armor',
		itemSet=monkeyKingsGarb)
	sunwukosSoul.save()

	sunwukosPaws = SetPiece(name='Sunwuko\'s Paws',
		pic='media/items/sets/monk/sunwukos_paws.png',
		category='Gloves',
		itemSet=monkeyKingsGarb)
	sunwukosPaws.save()

#2.4
	sunwukosLeggings = SetPiece(name='Sunwuko\'s Leggings',
		pic='media/items/sets/monk/sunwukos_leggings.png',
		category='Pants',
		itemSet=monkeyKingsGarb)
	sunwukosLeggings.save()

	sunwukosShines = SetPiece(name='Sunwuko\'s Shines',
		pic='media/items/sets/monk/sunwukos_shines.png',
		category='Amulet',
		itemSet=monkeyKingsGarb)
	sunwukosShines.save()

#2.4
	monkeyKingsGarb2 = Effect(pieces='2',
		# effect='<li><p>Casting Cyclone Strike, Exploding Palm, Lashing Tail Kick, Tempest Rush or Wave of Light causes a decoy to spawn that taunts nearby enemies and then explodes for <span class="silver">1000%</span> weapon damage</p></li>',
		effect='<li><p>Your damage taken is reduced by <span class="silver">50%</span> while Sweeping Wind is active</p></li>',
		itemSet=monkeyKingsGarb)
	monkeyKingsGarb2.save()

#2.4
	monkeyKingsGarb4 = Effect(pieces='4',
		# effect='<li><p>When your decoys explode, you gain a buff that increases the damage of Cyclone Strike, Exploding Palm, Lashing Tail Kick, Tempest Rush and Wave of Light by <span class="silver">500%</span> for <span class="silver">3</span> seconds</p></li>',
		effect='<li><p>Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for <span class="silver">500%</span> weapon damage for each stack of Sweeping Wind you have</p></li>',
		itemSet=monkeyKingsGarb)
	monkeyKingsGarb4.save()

#2.4
	monkeyKingsGarb6 = Effect(pieces='6',
		# effect='<li><p>When your decoys explode, you gain a buff that increases the damage of Cyclone Strike, Exploding Palm, Lashing Tail Kick, Tempest Rush and Wave of Light by <span class="silver">500%</span> for <span class="silver">3</span> seconds</p></li>',
		effect='<li><p>Lashing Tail Kick, Tempest Rush, and Wave of Light consume a stack of Sweeping Wind to deal <span class="silver">1500%</span> increased damage</p></li>',
		itemSet=monkeyKingsGarb)
	monkeyKingsGarb6.save()


	raimentOfAThousandStorms = ItemSet(name='Raiment of a Thousand Storms',
		owner='Monk',
		patch='24')
	raimentOfAThousandStorms.save()

	maskOfTheSearingSky = SetPiece(name='Mask of the Searing Sky',
		pic='media/items/sets/monk/mask_of_the_searing_sky.png',
		category='Helmet',
		itemSet=raimentOfAThousandStorms)
	maskOfTheSearingSky.save()

	mantleOfTheUpsideDownSinners = SetPiece(name='Mantle of the Upside-Down Sinners',
		pic='media/items/sets/monk/mantle_of_the_upside_down_sinners.png',
		category='Shoulders',
		itemSet=raimentOfAThousandStorms)
	mantleOfTheUpsideDownSinners.save()

	heartOfTheCrashingWave = SetPiece(name='Heart of the Crashing Wave',
		pic='media/items/sets/monk/heart_of_the_crashing_wave.png',
		category='Chest Armor',
		itemSet=raimentOfAThousandStorms)
	heartOfTheCrashingWave.save()

	fistsOfThunder = SetPiece(name='Fists of Thunder',
		pic='media/items/sets/monk/fists_of_thunder.png',
		category='Gloves',
		itemSet=raimentOfAThousandStorms)
	fistsOfThunder.save()

	scalesOfTheDancingSerpent = SetPiece(name='Scales of the Dancing Serpent',
		pic='media/items/sets/monk/scales_of_the_dancing_serpent.png',
		category='Pants',
		itemSet=raimentOfAThousandStorms)
	scalesOfTheDancingSerpent.save()

	eightDemonBoots = SetPiece(name='Eight-Demon Boots',
		pic='media/items/sets/monk/eight_demon_boots.png',
		category='Boots',
		itemSet=raimentOfAThousandStorms)
	eightDemonBoots.save()

#2.4
	raimentOfAThousandStorms2 = Effect(pieces='2',
		effect='<li><p>Your Spirit Generators have <span class="silver">25%</span> increased attack speed and <span class="silver">100%</span> increased damage</p></li>',
		itemSet=raimentOfAThousandStorms)
	raimentOfAThousandStorms2.save()

	raimentOfAThousandStorms4 = Effect(pieces='4',
		effect='<li><p>Dashing Strike spends <span class="silver">75</span> Spirit, but refunds a Charge when it does</p></li>',
		itemSet=raimentOfAThousandStorms)
	raimentOfAThousandStorms4.save()

	raimentOfAThousandStorms6 = Effect(pieces='6',
		effect='<li><p>Your Spirit Generators increase the weapon damage of Dashing Strike to <span class="silver">12500%</span> for <span class="silver">6</span> seconds</p></li>',
		itemSet=raimentOfAThousandStorms)
	raimentOfAThousandStorms6.save()



	shenlongsSpirit = ItemSet(name='Shenlong\'s Spirit',
		owner='Monk',
		patch='23')
	shenlongsSpirit.save()


	shenlongsFistOfLegend = SetPiece(name='Shenlong\'s Fist of Legend',
		pic='media/items/sets/monk/shenlongs_fist_of_legend.png',
		category='Fist Weapon',
		itemSet=shenlongsSpirit)
	shenlongsFistOfLegend.save()

	shenlongsRelentlessAssault = SetPiece(name='Shenlong\'s Relentless Assault',
		pic='media/items/sets/monk/shenlongs_relentless_assault.png',
		category='Fist Weapon',
		itemSet=shenlongsSpirit)
	shenlongsRelentlessAssault.save()

	shenlongsSpirit2 = Effect(pieces='2',
		effect='<li><p>When reaching maximum Spirit, all damage is increased by <span class="silver">100%</span>, but you no longer passively regenerate Spirit and <span class="silver">65</span> Spirit is drained every second until you run out of Spirit</p></li><li><p>The damage of your Spirit Generators is increased by <span class="silver">1.5%</span> for each point of Spirit you have</p></li>',
		itemSet=shenlongsSpirit)
	shenlongsSpirit2.save()



	ulianasStrategem = ItemSet(name='Uliana\'s Strategem',
		owner='Monk',
		patch='23')
	ulianasStrategem.save()

	ulianasSpirit = SetPiece(name='Uliana\'s Spirit',
		pic='media/items/sets/monk/ulianas_spirit.png',
		category='Helmet',
		itemSet=ulianasStrategem)
	ulianasSpirit.save()

	ulianasStrength = SetPiece(name='Uliana\'s Strength',
		pic='media/items/sets/monk/ulianas_strength.png',
		category='Shoulders',
		itemSet=ulianasStrategem)
	ulianasStrength.save()

	ulianasHeart = SetPiece(name='Uliana\'s Heart',
		pic='media/items/sets/monk/ulianas_heart.png',
		category='Chest Armor',
		itemSet=ulianasStrategem)
	ulianasHeart.save()

	ulianasFury = SetPiece(name='Uliana\'s Fury',
		pic='media/items/sets/monk/ulianas_fury.png',
		category='Gloves',
		itemSet=ulianasStrategem)
	ulianasFury.save()

	ulianasBurden = SetPiece(name='Uliana\'s Burden',
		pic='media/items/sets/monk/ulianas_burden.png',
		category='Pants',
		itemSet=ulianasStrategem)
	ulianasBurden.save()

	ulianasDestiny = SetPiece(name='Uliana\'s Destiny',
		pic='media/items/sets/monk/ulianas_destiny.png',
		category='Boots',
		itemSet=ulianasStrategem)
	ulianasDestiny.save()

	ulianasStrategem2 = Effect(pieces='2',
		effect='<li><p>Every third hit of your Spirit Generators applies Exploding Palm</p></li>',
		itemSet=ulianasStrategem)
	ulianasStrategem2.save()

	ulianasStrategem4 = Effect(pieces='4',
		effect='<li><p>Your Seven-Sided Strike deals its total damage with each hit</p></li>',
		itemSet=ulianasStrategem)
	ulianasStrategem4.save()

	ulianasStrategem6 = Effect(pieces='6',
		effect='<li><p>Your Seven-Sided Strike detonates your Exploding Palm</p></li>',
		itemSet=ulianasStrategem)
	ulianasStrategem6.save()

#Witch Doctor
#==============================================================================
	helltoothHarness = ItemSet(name='Helltooth Harness',
		owner='Witch Doctor',
		patch='23')
	helltoothHarness.save()

	helltoothMask = SetPiece(name='Helltooth Mask',
		pic='media/items/sets/wd/helltooth_mask.png',
		category='Helmet',
		itemSet=helltoothHarness)
	helltoothMask.save()

	helltoothMantle = SetPiece(name='Helltooth Mantle',
		pic='media/items/sets/wd/helltooth_mantle.png',
		category='Shoulders',
		itemSet=helltoothHarness)
	helltoothMantle.save()

	helltoothTunic = SetPiece(name='Helltooth Tunic',
		pic='media/items/sets/wd/helltooth_tunic.png',
		category='Chest Armor',
		itemSet=helltoothHarness)
	helltoothTunic.save()

	helltoothGauntlets = SetPiece(name='Helltooth Gauntlets',
		pic='media/items/sets/wd/helltooth_gauntlets.png',
		category='Gloves',
		itemSet=helltoothHarness)
	helltoothGauntlets.save()

	helltoothLegGuards = SetPiece(name='Helltooth Leg Guards',
		pic='media/items/sets/wd/helltooth_leg_guards.png',
		category='Pants',
		itemSet=helltoothHarness)
	helltoothLegGuards.save()

	helltoothGreaves = SetPiece(name='Helltooth Greaves',
		pic='media/items/sets/wd/helltooth_greaves.png',
		category='Boots',
		itemSet=helltoothHarness)
	helltoothGreaves.save()

	helltoothHarness2 = Effect(pieces='2',
		effect='<li><p>Enemies hit by your Primary Skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed, taking <span class="silver">1500%</span> weapon damage every second, and taking <span class="silver">20%</span> increased damage from all sources for <span class="silver">10</span> seconds</p></li>',
		itemSet=helltoothHarness)
	helltoothHarness2.save()

	helltoothHarness4 = Effect(pieces='4',
		effect='<li><p>After applying Necrosis to an enemy, you take <span class="silver">50%</span> reduced damage for <span class="silver">10</span> seconds</p></li>',
		itemSet=helltoothHarness)
	helltoothHarness4.save()

	helltoothHarness6 = Effect(pieces='6',
		effect='<li><p>After casting Wall of Death, gain <span class="silver">900%</span> increased damage for <span class="silver">15</span> seconds to your Primary Skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death</p></li>',
		itemSet=helltoothHarness)
	helltoothHarness6.save()



	manajumasWay = ItemSet(name='Manajuma\'s Way',
		owner='Witch Doctor',
		patch='24')
	manajumasWay.save()

	manajumasCarvingKnife = SetPiece(name='Manajuma\'s Carving Knife',
		pic='media/items/sets/wd/manajumas_carving_knife.png',
		category='Ceremonial Knife',
		itemSet=manajumasWay)
	manajumasCarvingKnife.save()

	manajumasGoryFetch = SetPiece(name='Manajuma\'s Gory Fetch',
		pic='media/items/sets/wd/manajumas_gory_fetch.png',
		category='Mojo',
		itemSet=manajumasWay)
	manajumasGoryFetch.save()

#2.4
	manajumasWay2 = Effect(pieces='2',
		effect='<li><p>Hex - Angry Chicken explosion damage is increased by <span class="silver">400%</span> and slain enemies trigger an additional explosion</p></li><li><p>Hex - Angry Chicken lasts <span class="silver">15</span> seconds and movement speed as a chicken is increased by an additional <span class="silver">100%</span></p></li>',
		itemSet=manajumasWay)
	manajumasWay2.save()



	raimentOfTheJadeHarvester = ItemSet(name='Raiment of the Jade Harvester',
		owner='Witch Doctor',
		patch='24')
	raimentOfTheJadeHarvester.save()

	jadeHarvestersWisdom = SetPiece(name='Jade Harvester\'s Wisdom',
		pic='media/items/sets/wd/jade_harvesters_wisdom.png',
		category='Helmet',
		itemSet=raimentOfTheJadeHarvester)
	jadeHarvestersWisdom.save()

	jadeHarvestersJoy = SetPiece(name='Jade Harvester\'s Joy',
		pic='media/items/sets/wd/jade_harvesters_joy.png',
		category='Shoulders',
		itemSet=raimentOfTheJadeHarvester)
	jadeHarvestersJoy.save()

	jadeHarvestersPeace = SetPiece(name='Jade Harvester\'s Peace',
		pic='media/items/sets/wd/jade_harvesters_peace.png',
		category='Chest Armor',
		itemSet=raimentOfTheJadeHarvester)
	jadeHarvestersPeace.save()

	jadeHarvestersMercy = SetPiece(name='Jade Harvester\'s Mercy',
		pic='media/items/sets/wd/jade_harvesters_mercy.png',
		category='Gloves',
		itemSet=raimentOfTheJadeHarvester)
	jadeHarvestersMercy.save()

	jadeHarvestersCourage = SetPiece(name='Jade Harvester\'s Courage',
		pic='media/items/sets/wd/jade_harvesters_courage.png',
		category='Pants',
		itemSet=raimentOfTheJadeHarvester)
	jadeHarvestersCourage.save()

	jadeHarvestersSwiftness = SetPiece(name='Jade Harvester\'s Swiftness',
		pic='media/items/sets/wd/jade_harvesters_swiftness.png',
		category='Boots',
		itemSet=raimentOfTheJadeHarvester)
	jadeHarvestersSwiftness.save()

#2.4
	raimentOfTheJadeHarvester2 = Effect(pieces='2',
		effect='<li><p>When Haunt lands on an enemy already affected by Haunt, it instantly deals <span class="silver">60</span> seconds worth of Haunt damage</p></li>',
		itemSet=raimentOfTheJadeHarvester)
	raimentOfTheJadeHarvester2.save()

#2.4
	raimentOfTheJadeHarvester4 = Effect(pieces='4',
		effect='<li><p>Soul Harvest gains the effect of every rune and has its cooldown lowered by <span class="silver">1</span> second every time you cast Haunt or Locust Swarm</p></li>',
		itemSet=raimentOfTheJadeHarvester)
	raimentOfTheJadeHarvester4.save()

#2.4
	raimentOfTheJadeHarvester6 = Effect(pieces='6',
		effect='<li><p>Soul Harvest consumes your damage over time effects on enemies, instantly dealing <span class="silver">150</span> seconds worth of remaining damage</p></li>',
		itemSet=raimentOfTheJadeHarvester)
	raimentOfTheJadeHarvester6.save()



	spiritOfArachyr = ItemSet(name='Spirit of Arachyr',
		owner='Witch Doctor',
		patch='24')
	spiritOfArachyr.save()

	arachyrsVisage = SetPiece(name='Arachyr\'s Visage',
		pic='media/items/sets/wd/arachyrs_visage.png',
		category='Helmet',
		itemSet=spiritOfArachyr)
	arachyrsVisage.save()

	arachyrsMantle = SetPiece(name='Arachyr\'s Mantle',
		pic='media/items/sets/wd/arachyrs_mantle.png',
		category='Shoulders',
		itemSet=spiritOfArachyr)
	arachyrsMantle.save()

	arachyrsCarapace = SetPiece(name='Arachyr\'s Carapace',
		pic='media/items/sets/wd/arachyrs_carapace.png',
		category='Chest Armor',
		itemSet=spiritOfArachyr)
	arachyrsCarapace.save()

	arachyrsClaws = SetPiece(name='Arachyr\'s Claws',
		pic='media/items/sets/wd/arachyrs_claws.png',
		category='Gloves',
		itemSet=spiritOfArachyr)
	arachyrsClaws.save()

	arachyrsLegs = SetPiece(name='Arachyr\'s Legs',
		pic='media/items/sets/wd/arachyrs_legs.png',
		category='Pants',
		itemSet=spiritOfArachyr)
	arachyrsLegs.save()

	arachyrsStride = SetPiece(name='Arachyr\'s Stride',
		pic='media/items/sets/wd/arachyrs_stride.png',
		category='Boots',
		itemSet=spiritOfArachyr)
	arachyrsStride.save()

	spiritOfArachyr2 = Effect(pieces='2',
		effect='<li><p>Summon a permanent Spider Queen who leaves behind webs that deal <span class="silver">4000%</span> weapon damage over <span class="silver">5</span> seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders</p></li>',
		itemSet=spiritOfArachyr)
	spiritOfArachyr2.save()

#2.4
	spiritOfArachyr4 = Effect(pieces='4',
		effect='<li><p>Hex gains the effect of the Toad of Hugeness rune. While Toad of Hugeness is active, you take <span class="silver">50%</span> reduced damage. After Toad of Hugeness is summoned, you will heal for <span class="silver">10%</span> of your max Life per second for <span class="silver">15</span> seconds</p></li>',
		itemSet=spiritOfArachyr)
	spiritOfArachyr4.save()

#2.4
	spiritOfArachyr6 = Effect(pieces='6',
		effect='<li><p>The damage of your Creature Skills is increased by <span class="silver">1200%</span>. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas</p></li>',
		itemSet=spiritOfArachyr)
	spiritOfArachyr6.save()



	zunimassasHaunt = ItemSet(name='Zunimassa\'s Haunt',
		owner='Witch Doctor',
		patch='24')
	zunimassasHaunt.save()

	zunimassasVision = SetPiece(name='Zunimassa\'s Vision',
		pic='media/items/sets/wd/zunimassas_vision.png',
		category='Voodoo Mask',
		itemSet=zunimassasHaunt)
	zunimassasVision.save()

	zunimassasMarrow = SetPiece(name='Zunimassa\'s Marrow',
		pic='media/items/sets/wd/zunimassas_marrow.png',
		category='Chest Armor',
		itemSet=zunimassasHaunt)
	zunimassasMarrow.save()

	zunimassasFingerWraps = SetPiece(name='Zunimassa\'s Finger Wraps',
		pic='media/items/sets/wd/zunimassas_finger_wraps.png',
		category='Gloves',
		itemSet=zunimassasHaunt)
	zunimassasFingerWraps.save()

	zunimassasCloth = SetPiece(name='Zunimassa\'s Cloth',
		pic='media/items/sets/wd/zunimassas_cloth.png',
		category='Pants',
		itemSet=zunimassasHaunt)
	zunimassasCloth.save()

	zunimassasTrail = SetPiece(name='Zunimassa\'s Trail',
		pic='media/items/sets/wd/zunimassas_trail.png',
		category='Boots',
		itemSet=zunimassasHaunt)
	zunimassasTrail.save()

	zunimassasStringOfSkulls = SetPiece(name='Zunimassa\'s String of Skulls',
		pic='media/items/sets/wd/zunimassas_string_of_skulls.png',
		category='Mojo',
		itemSet=zunimassasHaunt)
	zunimassasStringOfSkulls.save()

	zunimassasPox = SetPiece(name='Zunimassa\'s Pox',
		pic='media/items/sets/wd/zunimassas_pox.png',
		category='Ring',
		itemSet=zunimassasHaunt)
	zunimassasPox.save()

	zunimassasHaunt2 = Effect(pieces='2',
		effect='<li><p>Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by <span class="silver">80%</span></p></li>',
		itemSet=zunimassasHaunt)
	zunimassasHaunt2.save()

	zunimassasHaunt4 = Effect(pieces='4',
		effect='<li><p>You and your Pets take <span class="silver">2%</span> less damage for every Fetish you have alive</p></li>',
		itemSet=zunimassasHaunt)
	zunimassasHaunt4.save()

#2.4
	zunimassasHaunt6 = Effect(pieces='6',
		effect='<li><p>Enemies hit by your Mana spenders take <span class="silver">800%</span> more damage from your Pets for <span class="silver">8</span> seconds</p></li>',
		itemSet=zunimassasHaunt)
	zunimassasHaunt6.save()

#Wizard
#==============================================================================
	chantodosResolve = ItemSet(name='Chantodo\'s Resolve',
		owner='Wizard',
		patch='23')
	chantodosResolve.save()

	chantodosWill = SetPiece(name='Chantodo\'s Will',
		pic='media/items/sets/wiz/chantodos_will.png',
		category='Wand',
		itemSet=chantodosResolve)
	chantodosWill.save()

	chantodosForce = SetPiece(name='Chantodo\'s Force',
		pic='media/items/sets/wiz/chantodos_force.png',
		category='Source',
		itemSet=chantodosResolve)
	chantodosForce.save()

	chantodosResolve2 = Effect(pieces='2',
		effect='<li><p>Every second while in Archon form you expel a Wave of Destruction, dealing <span class="silver">350%</span> weapon damage to enemies within <span class="silver">30</span> yards</p></li><li><p>Every time you hit with an attack while not in Archon form, <span class="silver">350%</span> weapon damage is added to the Wave of Destruction, stacking up to <span class="silver">20</span> times</p></li>',
		itemSet=chantodosResolve)
	chantodosResolve2.save()



	delseresMagnumOpus = ItemSet(name='Delsere\'s Magnum Opus',
		owner='Wizard',
		patch='24')
	delseresMagnumOpus.save()

	shroudedMask = SetPiece(name='Shrouded Mask',
		pic='media/items/sets/wiz/shrouded_mask.png',
		category='Helmet',
		itemSet=delseresMagnumOpus)
	shroudedMask.save()

	dashingPauldronsOfDespair = SetPiece(name='Dashing Pauldrons of Despair',
		pic='media/items/sets/wiz/dashing_pauldrons_of_despair.png',
		category='Shoulders',
		itemSet=delseresMagnumOpus)
	dashingPauldronsOfDespair.save()

	harnessOfTruth = SetPiece(name='Harness of Truth',
		pic='media/items/sets/wiz/harness_of_truth.png',
		category='Chest Armor',
		itemSet=delseresMagnumOpus)
	harnessOfTruth.save()

	fierceGauntlets = SetPiece(name='Fierce Gauntlets',
		pic='media/items/sets/wiz/fierce_gauntlets.png',
		category='Gloves',
		itemSet=delseresMagnumOpus)
	fierceGauntlets.save()

	legGuardsOfMystery = SetPiece(name='Leg Guards of Mystery',
		pic='media/items/sets/wiz/leg_guards_of_mystery.png',
		category='Pants',
		itemSet=delseresMagnumOpus)
	legGuardsOfMystery.save()

	stridersOfDestiny = SetPiece(name='Striders of Destiny',
		pic='media/items/sets/wiz/striders_of_destiny.png',
		category='Boots',
		itemSet=delseresMagnumOpus)
	stridersOfDestiny.save()

#2.4
	delseresMagnumOpus2 = Effect(pieces='2',
		effect='<li><p>Casting Arcane Orb, Energy Twister, Magic Missile, Shock Pulse, Explosive Blast, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by <span class="silver">2</span> seconds</p></li>',
		itemSet=delseresMagnumOpus)
	delseresMagnumOpus2.save()

#2.4
	delseresMagnumOpus4 = Effect(pieces='4',
		# effect='<li><p>Enemies affected by your Slow Time take <span class="silver">2000%</span> weapon damage every second</p></li>',
		effect='<li><p>You take <span class="silver">50%</span> reduced damage while inside your Slow Time. Allies gain half this benefit.</p></li>',
		itemSet=delseresMagnumOpus)
	delseresMagnumOpus4.save()

#2.4
	delseresMagnumOpus6 = Effect(pieces='6',
		effect='<li><p>Enemies affected by your Slow Time take <span class="silver">2000%</span> more damage from your Arcane Orb, Energy Twister, Magic Missile and Shock Pulse abilities</p></li>',
		itemSet=delseresMagnumOpus)
	delseresMagnumOpus6.save()



	firebirdsFinery = ItemSet(name='Firebird\'s Finery',
		owner='Wizard',
		patch='24')
	firebirdsFinery.save()

	firebirdsEye = SetPiece(name='Firebird\'s Eye',
		pic='media/items/sets/wiz/firebirds_eye.png',
		category='Source',
		itemSet=firebirdsFinery)
	firebirdsEye.save()

	firebirdsPlume = SetPiece(name='Firebird\'s Plume',
		pic='media/items/sets/wiz/firebirds_plume.png',
		category='Helmet',
		itemSet=firebirdsFinery)
	firebirdsPlume.save()

	firebirdsPinions = SetPiece(name='Firebird\'s Pinions',
		pic='media/items/sets/wiz/firebirds_pinions.png',
		category='Shoulders',
		itemSet=firebirdsFinery)
	firebirdsPinions.save()

	firebirdsBreast = SetPiece(name='Firebird\'s Breast',
		pic='media/items/sets/wiz/firebirds_breast.png',
		category='Chest Armor',
		itemSet=firebirdsFinery)
	firebirdsBreast.save()

	firebirdsTalons = SetPiece(name='Firebird\'s Talons',
		pic='media/items/sets/wiz/firebirds_talons.png',
		category='Gloves',
		itemSet=firebirdsFinery)
	firebirdsTalons.save()

	firebirdsDown = SetPiece(name='Firebird\'s Down',
		pic='media/items/sets/wiz/firebirds_down.png',
		category='Pants',
		itemSet=firebirdsFinery)
	firebirdsDown.save()

	firebirdsTarsi = SetPiece(name='Firebird\'s Tarsi',
		pic='media/items/sets/wiz/firebirds_tarsi.png',
		category='Boots',
		itemSet=firebirdsFinery)
	firebirdsTarsi.save()

#2.4
	firebirdsFinery2 = Effect(pieces='2',
		effect='<li><p>When you die, a Meteor falls from the sky and revives you. This effect has a <span class="silver">60</span> second cooldown</p></li>',
		itemSet=firebirdsFinery)
	firebirdsFinery2.save()

#2.4
	firebirdsFinery4 = Effect(pieces='4',
		effect='<li><p>Dealing Fire damage causes the enemy to take the same amount of damage over <span class="silver">3</span> seceonds, stacking up to <span class="silver">3000%</span> weapon damage as Fire per second. After reaching <span class="silver">3000%</span> damage per second, the enemy will burn until they die</p></li>',
		itemSet=firebirdsFinery)
	firebirdsFinery4.save()

#2.4
	firebirdsFinery6 = Effect(pieces='6',
		effect='<li><p>Your damage is increased by <span class="silver">25%</span> for each enemy that is burning. Elites that are burning increase your damage by <span class="silver">600%</span>. You can only have one Elite damage bonus active at a time.</p></li>',
		itemSet=firebirdsFinery)
	firebirdsFinery6.save()



	talRashasElements = ItemSet(name='Tal Rasha\'s Elements',
		owner='Wizard',
		patch='24')
	talRashasElements.save()

	talRashasUnwaveringGlare = SetPiece(name='Tal Rasha\'s Unwavering Glare',
		pic='media/items/sets/wiz/tal_rashas_unwavering_glare.png',
		category='Source',
		itemSet=talRashasElements)
	talRashasUnwaveringGlare.save()

	talRashasGuiseOfWisdom = SetPiece(name='Tal Rasha\'s Guise of Wisdom',
		pic='media/items/sets/wiz/tal_rashas_guise_of_wisdom.png',
		category='Helmet',
		itemSet=talRashasElements)
	talRashasGuiseOfWisdom.save()

	talRashasRelentlessPursuit = SetPiece(name='Tal Rasha\'s Relentless Pursuit',
		pic='media/items/sets/wiz/tal_rashas_relentless_pursuit.png',
		category='Chest Armor',
		itemSet=talRashasElements)
	talRashasRelentlessPursuit.save()

	talRashasGrasp = SetPiece(name='Tal Rasha\'s Grasp',
		pic='media/items/sets/wiz/tal_rashas_grasp.png',
		category='Gloves',
		itemSet=talRashasElements)
	talRashasGrasp.save()

	talRashasBrace = SetPiece(name='Tal Rasha\'s Brace',
		pic='media/items/sets/wiz/tal_rashas_brace.png',
		category='Belt',
		itemSet=talRashasElements)
	talRashasBrace.save()

	talRashasStride = SetPiece(name='Tal Rasha\'s Stride',
		pic='media/items/sets/wiz/tal_rashas_stride.png',
		category='Pants',
		itemSet=talRashasElements)
	talRashasStride.save()

	talRashasAllegiance = SetPiece(name='Tal Rasha\'s Allegiance',
		pic='media/items/sets/wiz/tal_rashas_allegiance.png',
		category='Amulet',
		itemSet=talRashasElements)
	talRashasAllegiance.save()

	talRashasElements2 = Effect(pieces='2',
		effect='<li><p>Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an <span class="silver">8</span> second cooldown for each damage type</p></li>',
		itemSet=talRashasElements)
	talRashasElements2.save()

#2.4
	talRashasElements4 = Effect(pieces='4',
		# effect='<li><p>Attacks increase your resistance to that damage type by <span class="silver">100%</span> for <span class="silver">6</span> seconds</p></li>',
		effect='<li><p>Arcane, Cold, Fire, and Lightning Attacks each increase all of your Resistances by <span class="silver">25%</span> for <span class="silver">8</span> seconds</p></li>',
		itemSet=talRashasElements)
	talRashasElements4.save()

#2.4
	talRashasElements6 = Effect(pieces='6',
		effect='<li><p>Attacks increase your damage by <span class="silver">300%</span> for <span class="silver">8</span> seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At <span class="silver">4</span> stacks, each different Elemental Attack extends the duration by <span class="silver">2</span> seconds, up to a maximum of <span class="silver">8</span> seconds</p></li>',
		itemSet=talRashasElements)
	talRashasElements6.save()



	vyrsAmazingArcana = ItemSet(name='Vyr\'s Amazing Arcana',
		owner='Wizard',
		patch='23')
	vyrsAmazingArcana.save()

	vyrsSightlessSkull = SetPiece(name='Vyr\'s Sightless Skull',
		pic='media/items/sets/wiz/vyrs_sightless_skull.png',
		category='Helmet',
		itemSet=vyrsAmazingArcana)
	vyrsSightlessSkull.save()

	vyrsProudPauldrons = SetPiece(name='Vyr\'s Proud Pauldrons',
		pic='media/items/sets/wiz/vyrs_proud_pauldrons.png',
		category='Shoulders',
		itemSet=vyrsAmazingArcana)
	vyrsProudPauldrons.save()

	vyrsAstonishingAura = SetPiece(name='Vyr\'s Astonishing Aura',
		pic='media/items/sets/wiz/vyrs_astonishing_aura.png',
		category='Chest Armor',
		itemSet=vyrsAmazingArcana)
	vyrsAstonishingAura.save()

	vyrsGraspingGauntlets = SetPiece(name='Vyr\'s Grasping Gauntlets',
		pic='media/items/sets/wiz/vyrs_grasping_gauntlets.png',
		category='Gloves',
		itemSet=vyrsAmazingArcana)
	vyrsGraspingGauntlets.save()

	vyrsFantasticFinery = SetPiece(name='Vyr\'s Fantastic Finery',
		pic='media/items/sets/wiz/vyrs_fantastic_finery.png',
		category='Pants',
		itemSet=vyrsAmazingArcana)
	vyrsFantasticFinery.save()

	vyrsSwaggeringStance = SetPiece(name='Vyr\'s Swaggering Stance',
		pic='media/items/sets/wiz/vyrs_swaggering_stance.png',
		category='Boots',
		itemSet=vyrsAmazingArcana)
	vyrsSwaggeringStance.save()

	vyrsAmazingArcana2 = Effect(pieces='2',
		effect='<li><p>Archon gains the effect of every rune</p></li>',
		itemSet=vyrsAmazingArcana)
	vyrsAmazingArcana2.save()

	vyrsAmazingArcana4 = Effect(pieces='4',
		effect='<li><p>Archon stacks also increase your Attack Speed, Armor and Resistances by <span class="silver">1%</span></p></li>',
		itemSet=vyrsAmazingArcana)
	vyrsAmazingArcana4.save()

	vyrsAmazingArcana6 = Effect(pieces='6',
		effect='<li><p>You also gain Archon stacks when you hit with an Archon ability</p></li>',
		itemSet=vyrsAmazingArcana)
	vyrsAmazingArcana6.save()


	for itemSet in ItemSet.objects.all():
		itemSet.name_slug = slugify(itemSet.name)
		itemSet.owner_slug = slugify(itemSet.owner)
		itemSet.save()

	for setPiece in SetPiece.objects.all():
		setPiece.name_slug = slugify(setPiece.name)
		setPiece.save()

class Migration(migrations.Migration):

    dependencies = [
        ('itemsets', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(load_item_sets),
    ]