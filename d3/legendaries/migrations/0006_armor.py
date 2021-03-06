'''
Needed affixes and item-specific affixes are defined first.
Items of category/slot defined after.
'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_helmets(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(category='Helmets',
		affix='mainStat')
	vita = Affix.objects.get(category='Helmets',
		affix='vita')
	chc = Affix.objects.get(category='Helmets',
		affix='chc')
	allRes = Affix.objects.get(category='Helmets',
		affix='allRes')
	sockets = Affix.objects.get(category='Helmets',
		affix='sockets')

	andarielsIAS = Affix.objects.get(category='Helmets',
		affix='andarielsIAS')
	andarielsFireDmgTaken = Affix.objects.get(category='Helmets',
		affix='andarielsFireDmgTaken')
	andarielsEleDmg = Affix.objects.get(category='Helmets',
		affix='andarielsEleDmg')
	andarielsPoisRes = Affix.objects.get(category='Helmets',
		affix='andarielsPoisRes')
	blindBlindchance = Affix.objects.get(category='Helmets',
		affix='blindBlindchance')
	mempoIAS = Affix.objects.get(category='Helmets',
		affix='mempoIAS')
	helmBlockChance = Affix.objects.get(category='Helmets',
		affix='helmBlockChance')

	andarielsVisage = Armor(category='Helmets',
		name='Andariel\'s Visage',
		pic='media/items/legendaries/armor/head/helmets/andariels_visage.png',
		unique='Attacks release a Poison Nova that deals <span>350 - 450%</span> weapon damage as Poison to enemies within <span class="silver">10</span> yards',
		random_primaries='1',
		owner='all',
		patch='23')
	andarielsVisage.save()
	andarielsVisage.affixes.add(mainStat, andarielsEleDmg, andarielsIAS, andarielsFireDmgTaken, andarielsPoisRes)

	blindFaith = Armor(category='Helmets',
		name='Blind Faith',
		pic='media/items/legendaries/armor/head/helmets/blind_faith.png',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	blindFaith.save()
	blindFaith.affixes.add(mainStat, blindBlindchance)

	brokenCrown = Armor(category='Helmets',
		name='Broken Crown',
		pic='media/items/legendaries/armor/head/helmets/broken_crown.png',
		unique='Whenever a gem drops, a gem of the type socketed into your helmet also drops',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	brokenCrown.save()
	brokenCrown.affixes.add(mainStat, sockets)

	deathseersCowl = Armor(category='Helmets',
		name='Deathseer\'s Cowl',
		pic='media/items/legendaries/armor/head/helmets/deathseers_cowl.png',
		unique='<span>15 - 20%</span> chance on being hit by an Undead enemy to Charm it for <span class="silver">2</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	deathseersCowl.save()
	deathseersCowl.affixes.add(mainStat, sockets)

	leoricsCrown = Armor(category='Helmets',
		name='Leoric\'s Crown',
		pic='media/items/legendaries/armor/head/helmets/leorics_crown.png',
		unique='Increase the effect of any gem socketed into this item by <span>75 - 100%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	leoricsCrown.save()
	leoricsCrown.affixes.add(mainStat, sockets)

	mempoOfTwilight = Armor(category='Helmets',
		name='Mempo of Twilight',
		pic='media/items/legendaries/armor/head/helmets/mempo_of_twilight.png',
		unique='',
		random_primaries='',
		random_secondaries='',
		owner='all',
		patch='23')
	mempoOfTwilight.save()
	mempoOfTwilight.affixes.add(mainStat, mempoIAS, allRes, sockets)

	pridesFall = Armor(category='Helmets',
		name='Pride\'s Fall',
		pic='media/items/legendaries/armor/head/helmets/prides_fall.png',
		unique='Your Resource Costs are reduced by <span class="silver">30%</span> after not taking damage for <span class="silver">5</span> seconds',
		random_primaries='1',
		random_secondaries='1',
		owner='all',
		patch='23')
	pridesFall.save()
	pridesFall.affixes.add(mainStat, vita, chc)

	skullOfResonance = Armor(category='Helmets',
		name='Skull of Resonance',
		pic='media/items/legendaries/armor/head/helmets/skull_of_resonance.png',
		unique='Threatening Shout has a chance to Charm enemies and cause them to join your side',
		random_primaries='1',
		random_secondaries='1',
		owner='bb',
		patch='23')
	skullOfResonance.save()
	skullOfResonance.affixes.add(mainStat, allRes, sockets)

	theHelmOfRule = Armor(category='Helmets',
		name='The Helm of Rule',
		pic='media/items/legendaries/armor/head/helmets/the_helm_of_rule.png',
		random_primaries='2',
		random_secondaries='2',
		owner='all',
		patch='23')
	theHelmOfRule.save()
	theHelmOfRule.affixes.add(vita, helmBlockChance)

#2.4 new
	visageOfGunes = Armor(category='Helmets',
		name='Visage of Gunes',
		pic='media/items/legendaries/2.4/armor/visage_of_gunes.png',
		unique='Vengeance gains the effect of the Dark Heart rune',
		random_primaries='2',
		random_secondaries='1',
		owner='dh',
		patch='24')
	visageOfGunes.save()
	visageOfGunes.affixes.add(mainStat, sockets)

#2.4 new
	warhelmOfKassar = Armor(category='Helmets',
		name='Warhelm of Kassar',
		pic='media/items/legendaries/2.4/armor/warhelm_of_kassar.png',
		unique='Reduce the cooldown and increase the damage of Phalanx by <span>45 - 60%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='24')
	warhelmOfKassar.save()
	warhelmOfKassar.affixes.add(mainStat, sockets)

	for armor in Armor.objects.filter(category='Helmets'):
		armor.inherent = '<span class="inherent"><span>660 - 759</span> Armor</span>'
		armor.slot = 'Head'
		armor.save()


def load_spirit_stones(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	dext = Affix.objects.get(category='Spirit Stones',
		affix='dext')
	chc = Affix.objects.get(category='Spirit Stones',
		affix='chc')
	sockets = Affix.objects.get(category='Spirit Stones',
		affix='sockets')
	skillDmg = Affix.objects.get(category='Spirit Stones',
		affix='skillDmg')

	ccReduction = Affix.objects.get(category='Spirit Stones',
		affix='ccReduction')
	killExp = Affix.objects.get(category='Spirit Stones',
		affix='killExp')

	eyeLightDmg = Affix.objects.get(category='Spirit Stones',
		affix='eyeLightDmg')
	gyanaLashingTailKick = Affix.objects.get(category='Spirit Stones',
		affix='gyanaLashingTailKick')
	tzoWaveOfLight = Affix.objects.get(category='Spirit Stones',
		affix='tzoWaveOfLight')


	bezoarStone = Armor(category='Spirit Stones',
		name='Bezoar Stone',
		pic='media/items/legendaries/armor/head/spiritstones/bezoar_stone.png',
		random_primaries='2',
		random_secondaries='2',
		patch='23')
	bezoarStone.save()
	bezoarStone.affixes.add(dext, skillDmg)

	erlangShen = Armor(category='Spirit Stones',
		name='Erlang Shen',
		pic='media/items/legendaries/armor/head/spiritstones/erlang_shen.png',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	erlangShen.save()
	erlangShen.affixes.add(dext, ccReduction)

	eyeOfPeshkov = Armor(category='Spirit Stones',
		name='Eye of Peshkov',
		pic='media/items/legendaries/armor/head/spiritstones/eye_of_peshkov.png',
		unique='Reduce the cooldown of Breath of Heaven by <span>38 - 50%</span>',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	eyeOfPeshkov.save()
	eyeOfPeshkov.affixes.add(dext, sockets)

#2.4
	gyanaNaKashu = Armor(category='Spirit Stones',
		name='Gyana Na Kashu',
		pic='media/items/legendaries/armor/head/spiritstones/gyana_na_kashu.png',
		unique='Lashing Tail Kick releases a piercing Fireball that deals <span>525 - 700%</span> weapon damage as Fire to enemies within <span class="silver">10</span> yards on impact',
		random_primaries='2',
		random_secondaries='1',
		patch='24')
	gyanaNaKashu.save()
	gyanaNaKashu.affixes.add(dext, gyanaLashingTailKick, sockets)

	kekegisUnbreakableSpirit = Armor(category='Spirit Stones',
		name='Kekegi\'s Unbreakable Spirit',
		pic='media/items/legendaries/armor/head/spiritstones/kekegis_unbreakable_spirit.png',
		unique='Damaging enemies has a chance to grant you an effect that removes the Spirit cost of your abilities for <span>2 - 4</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	kekegisUnbreakableSpirit.save()
	kekegisUnbreakableSpirit.affixes.add(dext, chc)

	madstone = Armor(category='Spirit Stones',
		name='Madstone',
		pic='media/items/legendaries/armor/head/spiritstones/madstone.png',
		unique='Your Seven-Sided Strike applies Exploding Palm',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	madstone.save()
	madstone.affixes.add(dext)

	seeNoEvil = Armor(category='Spirit Stones',
		name='See No Evil',
		pic='media/items/legendaries/armor/head/spiritstones/see_no_evil.png',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	seeNoEvil.save()
	seeNoEvil.affixes.add(dext, killExp)

	theEyeOfTheStorm = Armor(category='Spirit Stones',
		name='The Eye of the Storm',
		pic='media/items/legendaries/armor/head/spiritstones/the_eye_of_the_storm.png',
		random_primaries='2',
		random_secondaries='2',
		patch='23')
	theEyeOfTheStorm.save()
	theEyeOfTheStorm.affixes.add(dext, eyeLightDmg)

	theLawsOfSeph = Armor(category='Spirit Stones',
		name='The Laws of Seph',
		pic='media/items/legendaries/armor/head/spiritstones/the_laws_of_seph.png',
		unique='Using Blinding Flash restores <span>125 - 165</span> Spirit',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	theLawsOfSeph.save()
	theLawsOfSeph.affixes.add(dext, sockets)

	theMindsEye = Armor(category='Spirit Stones',
		name='The Mind\'s Eye',
		pic='media/items/legendaries/armor/head/spiritstones/the_minds_eye.png',
		unique='Inner Sanctuary increases Spirit Regeneration per second by <span>10 - 15</span>',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	theMindsEye.save()
	theMindsEye.affixes.add(dext, sockets)

	tzoKrinsGaze = Armor(category='Spirit Stones',
		name='Tzo Krin\'s Gaze',
		pic='media/items/legendaries/armor/head/spiritstones/tzo_krins_gaze.png',
		unique='Wave of Light is now cast at your enemy',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	tzoKrinsGaze.save()
	tzoKrinsGaze.affixes.add(dext, tzoWaveOfLight)

	for armor in Armor.objects.filter(category='Spirit Stones'):
		armor.inherent = '<span class="inherent"><span>660 - 759</span> Armor</span>'
		armor.slot = 'Head'
		armor.owner = 'mk'
		armor.save()


def load_voodoo_masks(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	inte = Affix.objects.get(category='Voodoo Masks',
		affix='inte')
	chc = Affix.objects.get(category='Voodoo Masks',
		affix='chc')
	sockets = Affix.objects.get(category='Voodoo Masks',
		affix='sockets')

	maxMana = Affix.objects.get(category='Voodoo Masks',
		affix='maxMana')
	killExp = Affix.objects.get(category='Voodoo Masks',
		affix='killExp')

	carnevil = Armor(category='Voodoo Masks',
		name='Carnevil',
		pic='media/items/legendaries/armor/head/voodoomasks/carnevil.png',
		unique='The <span class="silver">5</span> Fetishes closest to you will shoot a powerful Poison Dart every time you do',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	carnevil.save()
	carnevil.affixes.add(inte, chc)

	maskOfJeram = Armor(category='Voodoo Masks',
		name='Mask of Jeram',
		pic='media/items/legendaries/armor/head/voodoomasks/mask_of_jeram.png',
		unique='Pets deal <span>75 - 100%</span> more damage',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	maskOfJeram.save()
	maskOfJeram.affixes.add(inte, sockets)

	quetzalcoatl = Armor(category='Voodoo Masks',
		name='Quetzalcoatl',
		pic='media/items/legendaries/armor/head/voodoomasks/quetzalcoatl.png',
		unique='Locust Swarm and Haunt now deal their damage in half of the normal duration',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	quetzalcoatl.save()
	quetzalcoatl.affixes.add(inte)

	splitTusk = Armor(category='Voodoo Masks',
		name='Split Tusk',
		pic='media/items/legendaries/armor/head/voodoomasks/split_tusk.png',
		random_primaries='3',
		patch='23')
	splitTusk.save()
	splitTusk.affixes.add(inte, maxMana, killExp)

	theGrinReaper = Armor(category='Voodoo Masks',
		name='The Grin Reaper',
		pic='media/items/legendaries/armor/head/voodoomasks/the_grin_reaper.png',
		unique='Chance when attacking to summon horrific Mimics that cast some of your equipped skills',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	theGrinReaper.save()
	theGrinReaper.affixes.add(inte, sockets)

	tiklandianVisage = Armor(category='Voodoo Masks',
		name='Tiklandian Visage',
		pic='media/items/legendaries/armor/head/voodoomasks/tiklandian_visage.png',
		unique='Horrify causes you to Fear and Root enemies around you for <span>6 - 8</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	tiklandianVisage.save()
	tiklandianVisage.affixes.add(inte)

	visageOfGiyua = Armor(category='Voodoo Masks',
		name='Visage of Giyua',
		pic='media/items/legendaries/armor/head/voodoomasks/visage_of_giyua.png',
		unique='Summon a Fetish Army after you kill <span class="silver">2</span> Elites',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	visageOfGiyua.save()
	visageOfGiyua.affixes.add(inte)

	for armor in Armor.objects.filter(category='Voodoo Masks'):
		armor.inherent = '<span class="inherent"><span>660 - 759</span> Armor</span>'
		armor.slot = 'Head'
		armor.owner = 'wd'
		armor.save()


def load_wizard_hats(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	inte = Affix.objects.get(category='Wizard Hats',
		affix='inte')
	sockets = Affix.objects.get(category='Wizard Hats',
		affix='sockets')
	apCrit = Affix.objects.get(category='Wizard Hats',
		affix='apCrit')

	maxAP = Affix.objects.get(category='Wizard Hats',
		affix='maxAP')

	stormLightDmg = Affix.objects.get(category='Wizard Hats',
		affix='stormLightDmg')

	archmagesVicalyke = Armor(category='Wizard Hats',
		name='Archmage\'s Vicalyke',
		pic='media/items/legendaries/armor/head/wizardhats/archmages_vicalyke.png',
		unique='Your Mirror Images have a chance to multiply when killed by enemies',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	archmagesVicalyke.save()
	archmagesVicalyke.affixes.add(inte)

	crownOfThePrimus = Armor(category='Wizard Hats',
		name='Crown of the Primus',
		pic='media/items/legendaries/armor/head/wizardhats/crown_of_the_primus.png',
		unique='Slow Time gains the effect of every rune',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	crownOfThePrimus.save()
	crownOfThePrimus.affixes.add(inte, sockets)

	darkMagesShade = Armor(category='Wizard Hats',
		name='Dark Mage\'s Shade',
		pic='media/items/legendaries/armor/head/wizardhats/dark_mages_shade.png',
		unique='Automatically cast Diamond Skin when you fall below <span class="silver">35%</span> Life. This effect may occur once every <span>15 - 20</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	darkMagesShade.save()
	darkMagesShade.affixes.add(inte)

	stormCrow = Armor(category='Wizard Hats',
		name='Storm Crow',
		pic='media/items/legendaries/armor/head/wizardhats/storm_crow.png',
		unique='<span>20 - 40%</span> chance to cast a Fiery Ball when attacking',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	stormCrow.save()
	stormCrow.affixes.add(inte, stormLightDmg)

	theMagistrate = Armor(category='Wizard Hats',
		name='The Magistrate',
		pic='media/items/legendaries/armor/head/wizardhats/the_magistrate.png',
		unique='Frost Hydra now periodically casts Frost Nova',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	theMagistrate.save()
	theMagistrate.affixes.add(inte, sockets)

	theSwami = Armor(category='Wizard Hats',
		name='The Swami',
		pic='media/items/legendaries/armor/head/wizardhats/the_swami.png',
		unique='The bonuses from Archon stacks now last for <span>15 - 20</span> seconds after Archon expires',
		random_primaries='1',
		random_secondaries='1',
		patch='23')
	theSwami.save()
	theSwami.affixes.add(inte, apCrit, maxAP)

	velvetCamaral = Armor(category='Wizard Hats',
		name='velvet Camaral',
		pic='media/items/legendaries/armor/head/wizardhats/velvet_camaral.png',
		unique='Double the number of enemies your Electrocute jumps to',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	velvetCamaral.save()
	velvetCamaral.affixes.add(inte, sockets)

	for armor in Armor.objects.filter(category='Wizard Hats'):
		armor.inherent = '<span class="inherent"><span>660 - 759</span> Armor</span>'
		armor.slot = 'Head'
		armor.owner = 'wz'
		armor.save()


def load_shoulders(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(slot="Shoulders",
		affix='mainStat')
	vita = Affix.objects.get(slot="Shoulders",
		affix='vita')
	armor = Affix.objects.get(slot="Shoulders",
		affix='armor')

	itemHealing = Affix.objects.get(slot="Shoulders",
		affix='itemHealing')
	extraGold = Affix.objects.get(slot="Shoulders",
		affix='extraGold')

	corruptionItemPickup = Affix.objects.get(slot="Shoulders",
		affix='corruptionItemPickup')

#Changed for 2.4
	corruption = Armor(slot='Shoulders',
		name='Corruption',
		pic='media/items/legendaries/armor/shoulders/corruption.png',
		random_primaries='4',
		# random_secondaries='2',
		notes='crafted',
		owner='all',
		patch='24')
	corruption.save()
	corruption.affixes.add(itemHealing, corruptionItemPickup)

	deathWatchMantle = Armor(slot='Shoulders',
		name='Death Watch Mantle',
		pic='media/items/legendaries/armor/shoulders/death_watch_mantle.png',
		unique='<span>25 - 35%</span> chance to explode in a Fan of Knives for <span>750 - 950%</span> weapon damage when hit',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	deathWatchMantle.save()
	deathWatchMantle.affixes.add(mainStat)

	furyOfTheAncients = Armor(slot='Shoulders',
		name='Fury of the Ancients',
		pic='media/items/legendaries/armor/shoulders/fury_of_the_ancients.png',
		unique='Call of the Ancients gains the effect of the Ancients\' Fury rune',
		random_primaries='3',
		random_secondaries='1',
		owner='bb',
		patch='23')
	furyOfTheAncients.save()
	furyOfTheAncients.affixes.add(mainStat)

	homingPads = Armor(slot='Shoulders',
		name='Homing Pads',
		pic='media/items/legendaries/armor/shoulders/homing_pads.png',
		unique='Your Town Portal is no longer interrupted by taking damage. While casting Town Portal you gain a protective bubble that reduces damage taken by <span>50 - 65%</span>',
		random_primaries='3',
		owner='all',
		patch='23')
	homingPads.save()
	homingPads.affixes.add(mainStat, extraGold)

#2.4 new
	lefebvresSoliloquy = Armor(slot='Shoulders',
		name='Lefebvere\'s Soliloquy',
		pic='media/items/legendaries/2.4/armor/lefebvres_soliloquy.png',
		unique='Cyclone Strike reduces your damage taken by <span>40 - 50%</span> for <span class="silver">5</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		owner='mk',
		patch='24')
	lefebvresSoliloquy.save()
	lefebvresSoliloquy.affixes.add(mainStat)

#2.4 new
	mantleOfChanneling = Armor(slot='Shoulders',
		name='Mantle of Channeling',
		pic='media/items/legendaries/2.4/armor/mantle_of_channeling.png',
		unique='While channeling {<span class="vary">Class Skill</span>}, you deal <span>20 - 25%</span> increased damage and take <span class="silver">25%</span> reduced damage<div class="extra"><div class="extra-x">X</div><span><strong>Barbarian: </strong>Whirlwind<br><strong>Demon Hunter: </strong>Rapid Fire | Strafe<br><strong>Monk: </strong>Tempest Rush<br><strong>Witch Doctor: </strong>Firebats<br><strong>Wizard: </strong>Arcane Torrent | Disintegrate | Ray of Frost</span></div>',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='24')
	mantleOfChanneling.save()
	mantleOfChanneling.affixes.add(mainStat, vita)

	pauldronsOfTheSkeletonKing = Armor(slot='Shoulders',
		name='Pauldrons of the Skeleton King',
		pic='media/items/legendaries/armor/shoulders/pauldrons_of_the_skeleton_king.png',
		unique='When receiving fatal damage, there is a chance that you are instead restored to <span class="silver">25%</span> of your max Life and cause nearby enemies to flee in fear',
		random_primaries='1',
		random_secondaries='1',
		owner='all',
		patch='23')
	pauldronsOfTheSkeletonKing.save()
	pauldronsOfTheSkeletonKing.affixes.add(mainStat, vita, armor)

#No longer drops in 2.4
	# profanePauldrons = Armor(slot='Shoulders',
	# 	name='Profane Pauldrons',
	# 	pic='media/items/legendaries/armor/shoulders/profane_pauldrons.png',
	# 	random_primaries='3',
	# 	owner='all',
	#patch='23')
	# profanePauldrons.save()
	# profanePauldrons.affixes.add(mainStat, itemHealing, profaneItemPickup)

	spauldersOfZakara = Armor(slot='Shoulders',
		name='Spaulders of Zakara',
		pic='media/items/legendaries/armor/shoulders/spaulders_of_zakara.png',
		unique='Your items become Indestructible',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	spauldersOfZakara.save()
	spauldersOfZakara.affixes.add(mainStat)

	vileWard = Armor(slot='Shoulders',
		name='Vile Ward',
		pic='media/items/legendaries/armor/shoulders/vile_ward.png',
		unique='Furious Charge deals <span>30 - 35%</span> increased damage for every enemy hit while charging',
		random_primaries='3',
		random_secondaries='2',
		notes='double check affixes',
		owner='bb',
		patch='23')
	vileWard.save()
	vileWard.affixes.add(mainStat)

	for armor in Armor.objects.filter(slot='Shoulders'):
		armor.inherent = '<span class="inherent"><span>586 - 674</span> Armor</span>'
		armor.save()


def load_chest_armor(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(category='Chest Armors',
		affix='mainStat')
	vita = Affix.objects.get(category='Chest Armors',
		affix='vita')
	allRes = Affix.objects.get(category='Chest Armors',
		affix='allRes')

	thorns = Affix.objects.get(category='Chest Armors',
		affix='thorns')
	durability = Affix.objects.get(category='Chest Armors',
		affix='durability')

	cindercoatFireDmg = Affix.objects.get(category='Chest Armors',
		affix='cindercoatFireDmg')
	goldskinExtraGold = Affix.objects.get(category='Chest Armors',
		affix='goldskinExtraGold')
	tyraelsDemonDmg = Affix.objects.get(category='Chest Armors',
		affix='tyraelsDemonDmg')

#2.4
	aquilaCuirass = Armor(category='Chest Armors',
		name='Aquila Cuirass',
		pic='media/items/legendaries/armor/torso/chestarmor/aquila_cuirass.png',
		unique='While above <span>90 - 95%</span> Primary Resource, all damage taken is reduced by <span class="silver">50%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='24')
	aquilaCuirass.save()
	aquilaCuirass.affixes.add(mainStat, vita)

	armorOfTheKindRegent = Armor(category='Chest Armors',
		name='Armor of the Kind Regent',
		pic='media/items/legendaries/armor/torso/chestarmor/armor_of_the_kind_regent.png',
		unique='Smite will now also be cast at a second nearby enemy',
		random_primaries='3',
		random_secondaries='1',
		owner='cs',
		patch='23')
	armorOfTheKindRegent.save()
	armorOfTheKindRegent.affixes.add(mainStat)

	chaingmail = Armor(category='Chest Armors',
		name='Chaingmail',
		pic='media/items/legendaries/armor/torso/chestarmor/chaingmail.png',
		unique='After earning a Survival Bonus, quickly heal to full Life',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	chaingmail.save()
	chaingmail.affixes.add(mainStat, allRes)

	cindercoat = Armor(category='Chest Armors',
		name='Cindercoat',
		pic='media/items/legendaries/armor/torso/chestarmor/cindercoat.png',
		unique='Reduces the resource cost of Fire skills by <span>23 - 30%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	cindercoat.save()
	cindercoat.affixes.add(mainStat, cindercoatFireDmg)

	goldskin = Armor(category='Chest Armors',
		name='Goldskin',
		pic='media/items/legendaries/armor/torso/chestarmor/goldskin.png',
		unique='Chance for enemies to drop Gold when you hit them',
		random_primaries='2',
		owner='all',
		patch='23')
	goldskin.save()
	goldskin.affixes.add(mainStat, allRes, goldskinExtraGold)

#2.4
	heartOfIron = Armor(category='Chest Armors',
		name='Heart of Iron',
		pic='media/items/legendaries/armor/torso/chestarmor/heart_of_iron.png',
		unique='Gain Thorns equal to <span>250 - 300%</span> of your Vitality',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='24')
	heartOfIron.save()
	heartOfIron.affixes.add(mainStat, vita, thorns)

	mantleOfTheRydraelm = Armor(category='Chest Armors',
		name='Mantle of the Rydraelm',
		pic='media/items/legendaries/armor/torso/chestarmor/mantle_of_the_rydraelm.png',
		random_primaries='4',
		random_secondaries='6',
		notes='crafted',
		owner='all')
	mantleOfTheRydraelm.save()

	shiMizusHaori = Armor(category='Chest Armors',
		name='Shi Mizu\'s Haori',
		pic='media/items/legendaries/armor/torso/chestarmor/shi_mizus_haori.png',
		unique='While below <span>20 - 25%</span> Life, all attacks are guaranteed Critical Hits',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	shiMizusHaori.save()
	shiMizusHaori.affixes.add(mainStat)

	tyraelsMight = Armor(category='Chest Armors',
		name='Tyrael\'s Might',
		pic='media/items/legendaries/armor/torso/chestarmor/tyraels_might.png',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	tyraelsMight.save()
	tyraelsMight.affixes.add(mainStat, allRes, tyraelsDemonDmg, durability)

	for armor in Armor.objects.filter(category='Chest Armor'):
		armor.inherent = '<span class="inherent"><span>660 - 759</span> Armor</span>'
		armor.slot = 'Torso'
		armor.save()


def load_cloaks(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	dext = Affix.objects.get(category='Cloaks',
		affix='dext')
	vita = Affix.objects.get(category='Cloaks',
		affix='vita')
	armor = Affix.objects.get(category='Cloaks',
		affix='armor')
	sockets = Affix.objects.get(category='Cloaks',
		affix='sockets')

	beckonSail = Armor(category='Cloaks',
		name='Beckon Sail',
		pic='media/items/legendaries/armor/torso/cloaks/beckon_sail.png',
		unique='When receiving fatal damage, you instead automatically cast Smoke Screen and are healed to <span class="silver">25%</span> Life. This effect may occur once every <span class="silver">120</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	beckonSail.save()
	beckonSail.affixes.add(dext, sockets)

	blackfeather = Armor(category='Cloaks',
		name='Blackfeather',
		pic='media/items/legendaries/armor/torso/cloaks/blackfeather.png',
		unique='Dodging or getting hit by a ranged attack automatically shoots a Homing Rocket back at the attacker for <span>600 - 800%</span> weapon damage as Physical',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	blackfeather.save()
	blackfeather.affixes.add(dext, sockets)

	capeOfTheDarkNight = Armor(category='Cloaks',
		name='Cape of the Dark Night',
		pic='media/items/legendaries/armor/torso/cloaks/cape_of_the_dark_night.png',
		unique='Automatically drop Caltrops when you are hit. This effect may only occur once every <span class="silver">6</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	capeOfTheDarkNight.save()
	capeOfTheDarkNight.affixes.add(dext)

	cloakOfDeception = Armor(category='Cloaks',
		name='Cloak of Deception',
		pic='media/items/legendaries/armor/torso/cloaks/cloak_of_deception.png',
		random_primaries='1',
		random_secondaries='1',
		patch='23')
	cloakOfDeception.save()
	cloakOfDeception.affixes.add(dext, vita, armor)

	theCloakOfTheGarwulf = Armor(category='Cloaks',
		name='The Cloak of the Garwulf',
		pic='media/items/legendaries/armor/torso/cloaks/the_cloak_of_the_garwulf.png',
		unique='Companion - Wolf Companion now summons <span class="silver">3</span> wolves',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	theCloakOfTheGarwulf.save()
	theCloakOfTheGarwulf.affixes.add(dext)

	for armor in Armor.objects.filter(category='Cloaks'):
		armor.inherent = '<span class="inherent"><span>660 - 759</span> Armor</span>'
		armor.slot = 'Torso'
		armor.owner = 'dh'
		armor.save()


def load_bracers(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(slot='Bracers',
		affix='mainStat')
	vita = Affix.objects.get(slot='Bracers',
		affix='vita')
	eleDmg = Affix.objects.get(slot='Bracers',
		affix='eleDmg')
	chc = Affix.objects.get(slot='Bracers',
		affix='chc')
	lps = Affix.objects.get(slot='Bracers',
		affix='lps')

	itemPickup = Affix.objects.get(slot='Bracers',
		affix='itemPickup')
	extraGold = Affix.objects.get(slot='Bracers',
		affix='extraGold')
	thorns = Affix.objects.get(slot='Bracers',
		affix='thorns')

	lacuniIAS = Affix.objects.get(slot='Bracers',
		affix='lacuniIAS')
	lacuniMovementSpeed = Affix.objects.get(slot='Bracers',
		affix='lacuniMovementSpeed')

#2.4 new
	akkhansManacles = Armor(slot='Bracers',
		name='Akkhan\'s Manacles',
		pic='media/items/legendaries/2.4/armor/akkhans_manacles.png',
		unique='Blessed Shield damage is increased by <span>400 - 500%</span> for the first enemy it hits',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='24')
	akkhansManacles.save()
	akkhansManacles.affixes.add(mainStat, chc)

	ancientParthanDefenders = Armor(slot='Bracers',
		name='Ancient Parthan Defenders',
		pic='media/items/legendaries/armor/wrists/ancient_parthan_defenders.png',
		unique='Each stunned enemy within <span class="silver">25</span> yards reduces your damage taken by <span>9 - 12%</span>',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	ancientParthanDefenders.save()
	ancientParthanDefenders.affixes.add(mainStat)

#2.4 new
	ashnagarrsBloodBracer = Armor(slot='Bracers',
		name='Ashnagarr\'s Blood Bracer',
		pic='media/items/legendaries/armor/wrists/ashnagarrs_blood_bracer.png',
		unique='Increases the potency of your shields by <span class="silver">100%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='wz',
		patch='24')
	ashnagarrsBloodBracer.save()
	ashnagarrsBloodBracer.affixes.add(mainStat, chc)

#2.4 new
	bindingsOfTheLesserGods = Armor(slot='Bracers',
		name='Bindings of the Lesser Gods',
		pic='media/items/legendaries/2.4/armor/bindings_of_the_lesser_gods.png',
		unique='Enemies hit by your Cyclone Strike take <span>150 - 200%</span> more damage from your Mystic Ally for <span class="silver">5</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		owner='mk',
		patch='24')
	bindingsOfTheLesserGods.save()
	bindingsOfTheLesserGods.affixes.add(mainStat, chc)

	bracersOfDestruction = Armor(slot='Bracers',
		name='Bracers of Destruction',
		pic='media/items/legendaries/armor/wrists/bracers_of_destruction.png',
		unique='Seismic Slam deals <span>300 - 400%</span> increased damage to the first <span class="silver">5</span> enemies it hits',
		random_primaries='2',
		random_secondaries='1',
		owner='bb',
		patch='23')
	bracersOfDestruction.save()
	bracersOfDestruction.affixes.add(mainStat)

#2.4 new
	bracersOfFury = Armor(slot='Bracers',
		name='Bracers of Fury',
		pic='media/items/legendaries/2.4/armor/bracers_of_fury.png',
		unique='Heaven\'s Fury deals <span>150 - 200%</span> increased damage to enemies that are Blinded, Immobilized, or Stunned',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='24')
	bracersOfFury.save()
	bracersOfFury.affixes.add(mainStat, chc)

	bracersOfTheFirstMen = Armor(slot='Bracers',
		name='Bracers of the First Men',
		pic='media/items/legendaries/armor/wrists/bracers_of_the_first_men.png',
		unique='Hammer of the Ancients attacks <span class="silver">50%</span> faster and deals <span>150 - 200%</span> increased damage',
		random_primaries='2',
		random_secondaries='1',
		owner='bb',
		patch='23')
	bracersOfTheFirstMen.save()
	bracersOfTheFirstMen.affixes.add(mainStat, chc)

#2.4 new
	cesarsMemento = Armor(slot='Bracers',
		name='Cesar\'s Memento',
		pic='media/items/legendaries/2.4/armor/cesars_memento.png',
		unique='Enemies take <span>300 - 400%</span> increased damage from your Tempest Rush for <span class="silver">5</span> seconds after you hit them with a Blind, Freeze, or Stun',
		random_primaries='2',
		random_secondaries='1',
		owner='mk',
		patch='24')
	cesarsMemento.save()
	cesarsMemento.affixes.add(mainStat, chc)

	coilsOfTheFirstSpider = Armor(slot='Bracers',
		name='Coils of the First Spider',
		pic='media/items/legendaries/armor/wrists/coils_of_the_first_spider.png',
		unique='While channeling Firebats, you take <span class="silver">30%</span> reduced damage and gain <span>60,000 - 80,000</span> Life per Hit',
		random_primaries='2',
		owner='wd',
		patch='23')
	coilsOfTheFirstSpider.save()
	coilsOfTheFirstSpider.affixes.add(mainStat, chc, lps)

	custerianWristguards = Armor(slot='Bracers',
		name='Custerian Wristguards',
		pic='media/items/legendaries/armor/wrists/custerian_wristguards.png',
		unique='Picking up Gold grants Experience',
		random_primaries='3',
		random_secondaries='',
		owner='all',
		patch='23')
	custerianWristguards.save()
	custerianWristguards.affixes.add(chc, extraGold)

#2.4
	drakonsLesson = Armor(slot='Bracers',
		name='Drakon\'s Lesson',
		pic='media/items/legendaries/armor/wrists/drakons_lesson.png',
		unique='When your Shield Bash hits <span class="silver">3</span> or fewer enemies, its damage is increased by <span>300 - 400%</span> and <span class="silver">25%</span> of its Wrath Cost is refunded',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='24')
	drakonsLesson.save()
	drakonsLesson.affixes.add(mainStat, chc)

	gabrielsVambraces = Armor(slot='Bracers',
		name='Gabriel\'s Vambraces',
		pic='media/items/legendaries/armor/wrists/gabriels_vambraces.png',
		unique='When your Blessed Hammer hits <span class="silver">3</span> or fewer enemies, <span>75 - 100%</span> of its Wrath Cost is refunded',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='23')
	gabrielsVambraces.save()
	gabrielsVambraces.affixes.add(mainStat, chc)

	gungdoGear = Armor(slot='Bracers',
		name='Gungdo Gear',
		pic='media/items/legendaries/armor/wrists/gungdo_gear.png',
		unique='Exploding Palm\'s on-death explosion applies Exploding Palm',
		random_primaries='2',
		random_secondaries='1',
		owner='mk',
		patch='23')
	gungdoGear.save()
	gungdoGear.affixes.add(mainStat, eleDmg)

	jeramsBracers = Armor(slot='Bracers',
		name='Jeram\'s Bracers',
		pic='media/items/legendaries/armor/wrists/jerams_bracers.png',
		unique='Wall of Death deals <span>75 - 100%</span> increased damage and can be cast up to three times within <span class="silver">2</span> seconds before the cooldown begins',
		random_primaries='2',
		random_secondaries='1',
		owner='wd',
		patch='23')
	jeramsBracers.save()
	jeramsBracers.affixes.add(mainStat, chc)

	kethryesSplint = Armor(slot='Bracers',
		name='Kethrye\'s Splint',
		pic='media/items/legendaries/armor/wrists/kethryes_splint.png',
		random_primaries='4',
		random_secondaries='2',
		owner='all',
		patch='23')
	kethryesSplint.save()
	# kethryesSplint.affixes.add()

	lacuniProwlers = Armor(slot='Bracers',
		name='Lacuni Prowlers',
		pic='media/items/legendaries/armor/wrists/lacuni_prowlers.png',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	lacuniProwlers.save()
	lacuniProwlers.affixes.add(lacuniIAS, lacuniMovementSpeed, thorns)

#2.4 new
	lakumbrasOrnament = Armor(slot='Bracers',
		name='Lakumbra\'s Ornament',
		pic='media/items/legendaries/2.4/armor/lakumbras_ornament.png',
		unique='Reduces all damage taken by <span class="silver">6%</span> for each stack of Soul Harvest you have',
		random_primaries='2',
		random_secondaries='1',
		owner='wd',
		patch='24')
	lakumbrasOrnament.save()
	lakumbrasOrnament.affixes.add(mainStat, chc)

	nemesisBracers = Armor(slot='Bracers',
		name='Nemesis Bracers',
		pic='media/items/legendaries/armor/wrists/nemesis_bracers.png',
		unique='Shrines and Pylons will spawn an enemy champion',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	nemesisBracers.save()
	nemesisBracers.affixes.add(mainStat)

#2.4 new
	pintosPride = Armor(slot='Bracers',
		name='Pinto\'s Pride',
		pic='media/items/legendaries/2.4/armor/pintos_pride.png',
		unique='Wave of Light also Slows enemies by <span class="silver">80%</span> for <span class="silver">3</span> seconds and deals <span>125 - 150%</span> increased damage',
		random_primaries='2',
		random_secondaries='1',
		owner='mk',
		patch='24')
	pintosPride.save()
	pintosPride.affixes.add(mainStat, chc)

	promiseOfGlory = Armor(slot='Bracers',
		name='Promise of Glory',
		pic='media/items/legendaries/armor/wrists/promise_of_glory.png',
		unique='<span>4 - 6%</span> chance to spawn a Nephalem Glory globe when you Blind an enemy',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	promiseOfGlory.save()
	promiseOfGlory.affixes.add(mainStat, chc)

	ranslorsFolly = Armor(slot='Bracers',
		name='Ranslor\'s Folly',
		pic='media/items/legendaries/armor/wrists/ranslors_folly.png',
		unique='Energy Twister periodically pulls in lesser enemies within <span class="silver">30</span> yards',
		random_primaries='2',
		random_secondaries='1',
		owner='wz',
		patch='23')
	ranslorsFolly.save()
	ranslorsFolly.affixes.add(mainStat, chc)

	reapersWraps = Armor(slot='Bracers',
		name='Reaper\'s Wraps',
		pic='media/items/legendaries/armor/wrists/reapers_wraps.png',
		unique='Health Globes restore <span>25 - 30%</span> of your Primary Resource',
		random_primaries='4',
		random_secondaries='2',
		notes='crafted',
		owner='all',
		patch='23')
	reapersWraps.save()
	# reapersWraps.affixes.add()

	sanguinaryVambraces = Armor(slot='Bracers',
		name='Sanguinary Vambraces',
		pic='media/items/legendaries/armor/wrists/sanguinary_vambraces.png',
		unique='Chance on being hit to deal <span class="silver">1000%</span> of your Thorns damage to nearby enemies',
		random_primaries='2',
		owner='all',
		patch='23')
	sanguinaryVambraces.save()
	sanguinaryVambraces.affixes.add(mainStat, chc, thorns)

#2.4 new
	skularsSalvation = Armor(slot='Bracers',
		name='Skular\'s Salvation',
		pic='media/items/legendaries/2.4/armor/skulars_salvation.png',
		unique='Increases the damage of Ancient Spear - Boulder Toss by <span class="silver">100%</span>. When your Boulder Toss hits <span class="silver">5</span> or fewer enemies the damage is increased by <span>120 - 150%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='bb',
		patch='24')
	skularsSalvation.save()
	skularsSalvation.affixes.add(mainStat, chc)

#Removed in 2.4
	# slaveBonds = Armor(slot='Bracers',
	# 	name='Slave Bonds',
	# 	pic='media/items/legendaries/armor/wrists/slave_bonds.png',
	# 	random_primaries='2',
	# 	random_secondaries='1',
	# 	owner='all',
	# 	patch='23')
	# slaveBonds.save()
	# slaveBonds.affixes.add(mainStat, slaveMovementSpeed, slaveLPK)

	spiritGuards = Armor(slot='Bracers',
		name='Spirit Guards',
		pic='media/items/legendaries/armor/wrists/spirit_guards.png',
		unique='Your Spirit Generators reduce your damage taken by <span>30 - 40%</span> for <span class="silver">3</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		owner='mk',
		patch='23')
	spiritGuards.save()
	spiritGuards.affixes.add(mainStat, chc)

#Removed in 2.4
	# steadyStrikers = Armor(slot='Bracers',
	# 	name='Steady Strikers',
	# 	pic='media/items/legendaries/armor/wrists/steady_strikers.png',
	# 	random_primaries='2',
	# 	random_secondaries='2',
	# 	owner='all',
	# patch='23')
	# steadyStrikers.save()
	# steadyStrikers.affixes.add(mainStat, steadyIAS)

	strongarmBracers = Armor(slot='Bracers',
		name='Strongarm Bracers',
		pic='media/items/legendaries/armor/wrists/strongarm_bracers.png',
		unique='Enemies hit by Knockbacks suffer <span>20 - 30%</span> more damage for <span class="silver">5</span> seconds when they land',
		random_primaries='1',
		random_secondaries='1',
		owner='all',
		patch='23')
	strongarmBracers.save()
	strongarmBracers.affixes.add(mainStat, vita, chc)

	trangoulCoils = Armor(slot='Bracers',
		name='Trangoul Coils',
		pic='media/items/legendaries/armor/wrists/trangoul_coils.png',
		unique='Healing Wells replenish all resources and reduce all cooldowns by <span>45 - 60</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	trangoulCoils.save()
	trangoulCoils.affixes.add(mainStat)

#2.4 new
	vambracesOfSescheron = Armor(slot='Bracers',
		name='Vambraces of Sescheron',
		pic='media/items/legendaries/2.4/armor/vambraces_of_sescheron.png',
		unique='Primary Skills heal you for <span>5 - 6%</span> of your missing Life',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='24')
	vambracesOfSescheron.save()
	vambracesOfSescheron.affixes.add(mainStat, chc)

	warzechianArmguards = Armor(slot='Bracers',
		name='Warzechian Armguards',
		pic='media/items/legendaries/armor/wrists/warzechian_armguards.png',
		unique='Every time you destroy a wreckable object, you gain a short burst of speed',
		random_primaries='2',
		owner='all',
		patch='23')
	warzechianArmguards.save()
	warzechianArmguards.affixes.add(mainStat, chc, itemPickup)

	wrapsOfClarity = Armor(slot='Bracers',
		name='Wraps of Clarity',
		pic='media/items/legendaries/armor/wrists/wraps_of_clarity.png',
		unique='Your Hatred Generators reduce your damage taken by <span>30 - 35%</span> for <span class="silver">5</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	wrapsOfClarity.save()
	wrapsOfClarity.affixes.add(mainStat, chc)

	for armor in Armor.objects.filter(slot='Bracers'):
		armor.inherent = '<span class="inherent"><span>366 - 421</span> Armor</span>'
		armor.save()


def load_gloves(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(slot='Gloves',
		affix='mainStat')
	ias = Affix.objects.get(slot='Gloves',
		affix='ias')
	chc = Affix.objects.get(slot='Gloves',
		affix='chc')
	chd = Affix.objects.get(slot='Gloves',
		affix='chd')
	lph = Affix.objects.get(slot='Gloves',
		affix='lph')

	frostburnColdDmg = Affix.objects.get(slot='Gloves',
		affix='frostburnColdDmg')
	magefistFireDmg = Affix.objects.get(slot='Gloves',
		affix='magefistFireDmg')
	stoneImmobilizeChance = Affix.objects.get(slot='Gloves',
		affix='stoneImmobilizeChance')

	frostburn = Armor(slot='Gloves',
		name='Frostburn',
		pic='media/items/legendaries/armor/hands/frostburn.png',
		unique='Your Cold damage has up to a <span>34 - 45%</span> chance to Freeze enemies',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	frostburn.save()
	frostburn.affixes.add(mainStat, frostburnColdDmg)

	gladiatorGauntlets = Armor(slot='Gloves',
		name='Gladiator Gauntlets',
		pic='media/items/legendaries/armor/hands/gladiator_gauntlets.png',
		unique='After earning a Massacre Bonus, Gold rains from sky',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	gladiatorGauntlets.save()
	gladiatorGauntlets.affixes.add(mainStat, chc)

	glovesOfWorship = Armor(slot='Gloves',
		name='Gloves of Worship',
		pic='media/items/legendaries/armor/hands/gloves_of_worship.png',
		unique='Shrine effects last for <span class="silver">10</span> minutes',
		random_primaries='1',
		random_secondaries='1',
		patch='23')
	glovesOfWorship.save()
	glovesOfWorship.affixes.add(mainStat, chd, lph)

	magefist = Armor(slot='Gloves',
		name='Magefist',
		pic='media/items/legendaries/armor/hands/magefist.png',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	magefist.save()
	magefist.affixes.add(mainStat, magefistFireDmg, ias)

	pendersPurchase = Armor(slot='Gloves',
		name='Penders Purchase',
		pic='media/items/legendaries/armor/hands/penders_purchase.png',
		random_primaries='4',
		random_secondaries='2',
		notes='crafted',
		patch='23')
	pendersPurchase.save()
	# pendersPurchase.affixes.add()

	stArchewsGage = Armor(slot='Gloves',
		name='St. Archew\'s Gage',
		pic='media/items/legendaries/armor/hands/st_archews_gage.png',
		unique='The first time an Elite pack damages you, gain an absorb shield equal to <span>120 - 150%</span> of your max Life for <span class="silver">10</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	stArchewsGage.save()
	stArchewsGage.affixes.add(mainStat)

	stoneGauntlets = Armor(slot='Gloves',
		name='Stone Gauntlets',
		pic='media/items/legendaries/armor/hands/stone_guantlets.png',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	stoneGauntlets.save()
	stoneGauntlets.affixes.add(mainStat, stoneImmobilizeChance)

	taskerAndTheo = Armor(slot='Gloves',
		name='Tasker and Theo',
		pic='media/items/legendaries/armor/hands/tasker_and_theo.png',
		unique='Increase Attack Speed of your pets by <span>40 - 50%</span>',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	taskerAndTheo.save()
	taskerAndTheo.affixes.add(mainStat, ias)

	for armor in Armor.objects.filter(slot='Gloves'):
		armor.inherent = '<span class="inherent"><span>513 - 590</span> Armor</span>'
		armor.owner = 'all'
		armor.save()


def load_belts(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(category='Belts',
		affix='mainStat')
	vita = Affix.objects.get(category='Belts',
		affix='vita')
	allRes = Affix.objects.get(category='Belts',
		affix='allRes')
	rcr = Affix.objects.get(category='Belts',
		affix='rcr')

	itemPickup = Affix.objects.get(category='Belts',
		affix='itemPickup')
	extraGold = Affix.objects.get(category='Belts',
		affix='extraGold')
	durability = Affix.objects.get(category='Belts',
		affix='durability')

	troveReducedMeleeDmg = Affix.objects.get(category='Belts',
		affix='troveReducedMeleeDmg')
	fleetingIAS = Affix.objects.get(category='Belts',
		affix='fleetingIAS')
	hellcatIAS = Affix.objects.get(category='Belts',
		affix='hellcatIAS')
	kyoshirosSweepingWind = Affix.objects.get(category='Belts',
		affix='kyoshirosSweepingWind')
	saffronCCReduction = Affix.objects.get(category='Belts',
		affix='saffronCCReduction')
	# stringReducedMeleeDmg = Affix.objects.get(category='Belts',
	# 	affix='stringReducedMeleeDmg')
	witchingIAS = Affix.objects.get(category='Belts',
		affix='witchingIAS')
	witchingCHD = Affix.objects.get(category='Belts',
		affix='witchingCHD')
	thundergodsLightDmg = Affix.objects.get(category='Belts',
		affix='thundergodsLightDmg')
	thundergodsLightRes = Affix.objects.get(category='Belts',
		affix='thundergodsLightRes')
	vigilanteCDR = Affix.objects.get(category='Belts',
		affix='vigilanteCDR')

	angelHairBraid = Armor(category='Belts',
		name='Angel Hair Braid',
		pic='media/items/legendaries/armor/waist/belts/angel_hair_braid.png',
		unique='Punish gains the effect of every rune',
		random_primaries='3',
		random_secondaries='1',
		notes='double check secondaries',
		owner='cs',
		patch='23')
	angelHairBraid.save()
	angelHairBraid.affixes.add(mainStat, durability)

	beltOfTheTrove = Armor(category='Belts',
		name='Belt of the Trove',
		pic='media/items/legendaries/armor/waist/belts/belt_of_the_trove.png',
		unique='Every <span>6 - 8</span> seconds, call down Bombardment on a random nearby enemy',
		random_primaries='2',
		owner='cs',
		patch='23')
	beltOfTheTrove.save()
	beltOfTheTrove.affixes.add(mainStat, allRes, troveReducedMeleeDmg)

	beltOfTranscendence = Armor(category='Belts',
		name='Belt of Transcendence',
		pic='media/items/legendaries/armor/waist/belts/belt_of_transcendence.png',
		unique='Summon a Fetish Sycophant when you hit with a Mana spender',
		random_primaries='2',
		random_secondaries='1',
		owner='wd',
		patch='23')
	beltOfTranscendence.save()
	beltOfTranscendence.affixes.add(mainStat, vita)

	bindingOfTheLost = Armor(category='Belts',
		name='Binding of the Lost',
		pic='media/items/legendaries/armor/waist/belts/binding_of_the_lost.png',
		unique='Each hit with Seven-Sided Strike grants <span>3.0 - 3.5%</span> damage reduction for <span class="silver">7</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		owner='mk',
		patch='23')
	bindingOfTheLost.save()
	bindingOfTheLost.affixes.add(mainStat)

	blessedOfHaull = Armor(category='Belts',
		name='Blessed of Haull',
		pic='media/items/legendaries/armor/waist/belts/blessed_of_haull.png',
		unique='Justice spawns a Blessed Hammer when it hits an enemy',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='23')
	blessedOfHaull.save()
	blessedOfHaull.affixes.add(mainStat, allRes)

#2.4 new
	chainOfShadows = Armor(category='Belts',
		name='Chain of Shadows',
		pic='media/items/legendaries/2.4/armor/chain_of_shadows.png',
		unique='After using Impale, your Vault costs no resource for <span class="silver">2</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		owner='dh',
		patch='24')
	chainOfShadows.save()
	chainOfShadows.affixes.add(mainStat, vita)

	cordOfTheSherma = Armor(category='Belts',
		name='Cord of the Sherma',
		pic='media/items/legendaries/armor/waist/belts/cord_of_the_sherma.png',
		unique='Chance on hit to create a chaos field that Blinds and Slows enemies inside for <span>3 - 4</span> seconds',
		random_primaries='2',
		owner='all',
		patch='23')
	cordOfTheSherma.save()
	cordOfTheSherma.affixes.add(mainStat, vita, itemPickup)

	crashingRain = Armor(category='Belts',
		name='Crashing Rain',
		pic='media/items/legendaries/armor/waist/belts/crashing_rain.png',
		unique='Rain of Vengeance also summons a Crashing Beast that deals <span>3000 - 4000%</span> weapon damage',
		random_primaries='2',
		random_secondaries='1',
		owner='dh',
		patch='23')
	crashingRain.save()
	crashingRain.affixes.add(mainStat, vita)

#2.4
	fazulasImprobableChain = Armor(category='Belts',
		name='Fazula\'s Improbable Chain',
		pic='media/items/legendaries/armor/waist/belts/fazulas_improbable_chain.png',
		unique='You automatically start with <span>40 - 50</span> Archon stacks when entering Archon form',
		random_primaries='3',
		random_secondaries='1',
		owner='wz',
		patch='24')
	fazulasImprobableChain.save()
	fazulasImprobableChain.affixes.add(mainStat)

	fleetingStrap = Armor(category='Belts',
		name='Fleeting Strap',
		pic='media/items/legendaries/armor/waist/belts/fleeting_strap.png',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted',
		owner='all',
		patch='23')
	fleetingStrap.save()
	fleetingStrap.affixes.add(fleetingIAS)

	goldwrap = Armor(category='Belts',
		name='Goldwrap',
		pic='media/items/legendaries/armor/waist/belts/goldwrap.png',
		unique='On Gold pickup: Gain Armor for <span class="silver">5</span> seconds equal to the amount picked up',
		random_primaries='3',
		owner='all',
		patch='23')
	goldwrap.save()
	goldwrap.affixes.add(mainStat, extraGold)

	harringtonWaistguard = Armor(category='Belts',
		name='Harrington Waistguard',
		pic='media/items/legendaries/armor/waist/belts/harrington_waistguard.png',
		unique='Opening a Chest grants <span>100 - 135%</span> increased damage for <span class="silver">10</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	harringtonWaistguard.save()
	harringtonWaistguard.affixes.add(mainStat, extraGold)

	hauntingGirdle = Armor(category='Belts',
		name='Haunting Girdle',
		pic='media/items/legendaries/armor/waist/belts/haunting_girdle.png',
		unique='Haunt releases <span class="silver">1</span> extra Spirit',
		random_primaries='2',
		random_secondaries='1',
		owner='wd',
		patch='23')
	hauntingGirdle.save()
	hauntingGirdle.affixes.add(mainStat, vita)

	hellcatWaistguard = Armor(category='Belts',
		name='Hellcat Waistguard',
		pic='media/items/legendaries/armor/waist/belts/hellcat_waistguard.png',
		random_primaries='1',
		random_secondaries='2',
		owner='all',
		patch='23')
	hellcatWaistguard.save()
	hellcatWaistguard.affixes.add(mainStat, vita, hellcatIAS)

#2.4 new
	hergbrashsBindings = Armor(category='Belts',
		name='Hergbrash\'s Bindings',
		pic='media/items/legendaries/2.4/armor/hergbrashs_bindings.png',
		unique='Reduces the Arcane Power cost of Arcane Torrent, Disintegrate, and Ray of Frost by <span>50 - 65%</span>',
		random_primaries='3',
		random_secondaries='1',
		owner='wz',
		patch='24')
	hergbrashsBindings.save()
	hergbrashsBindings.affixes.add(mainStat)

	huntersWrath = Armor(category='Belts',
		name='Hunter\'s Wrath',
		pic='media/items/legendaries/armor/waist/belts/hunters_wrath.png',
		unique='Your Primary skills attack <span class="silver">30%</span> faster and deal <span>45 - 60%</span> increased damage',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	huntersWrath.save()
	huntersWrath.affixes.add(mainStat, vita)

	hwojWrap = Armor(category='Belts',
		name='Hwoj Wrap',
		pic='media/items/legendaries/armor/waist/belts/hwoj_wrap.png',
		unique='Locust Swarm also Slows enemies by <span>60 - 80%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='wd',
		patch='23')
	hwojWrap.save()
	hwojWrap.affixes.add(mainStat, allRes)

	insatiableBelt = Armor(category='Belts',
		name='Insatiable Belt',
		pic='media/items/legendaries/armor/waist/belts/insatiable_belt.png',
		unique='Picking up a Health Globe increases your max Life by <span class="silver">5%</span> for <span class="silver">15</span> seconds, stacking up to <span class="silver">5</span> times',
		random_primaries='2',
		owner='all',
		patch='23')
	insatiableBelt.save()
	insatiableBelt.affixes.add(mainStat, vita, itemPickup)

	jangsEnvelopment = Armor(category='Belts',
		name='Jang\'s Envelopment',
		pic='media/items/legendaries/armor/waist/belts/jangs_envelopment.png',
		unique='Enemies damaged by Black Hole are also slowed by <span>60 - 80%</span> for <span class="silver">3</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		owner='wz',
		patch='23')
	jangsEnvelopment.save()
	jangsEnvelopment.affixes.add(mainStat)

#2.4 new
	kyoshirosSoul = Armor(category='Belts',
		name='Kyoshiro\'s Soul',
		pic='media/items/legendaries/2.4/armor/kyoshiros_soul.png',
		unique='Sweeping Wind gains <span class="silver">2</span> stacks every second it does not deal damage to any enemies',
		random_primaries='3',
		random_secondaries='1',
		owner='mk',
		patch='24')
	kyoshirosSoul.save()
	kyoshirosSoul.affixes.add(mainStat, kyoshirosSweepingWind)

	omnislash = Armor(category='Belts',
		name='Omnislash',
		pic='media/items/legendaries/armor/waist/belts/omnislash.png',
		unique='Slash attacks in all directions',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='23')
	omnislash.save()
	omnislash.affixes.add(mainStat, allRes)

	omyrnsChain = Armor(category='Belts',
		name='Omyrn\'s Chain',
		pic='media/items/legendaries/armor/waist/belts/omyrns_chain.png',
		unique='Drop Caltrops when using Vault',
		random_primaries='3',
		random_secondaries='1',
		owner='dh',
		patch='23')
	omyrnsChain.save()
	omyrnsChain.affixes.add(mainStat)

	razorStrop = Armor(category='Belts',
		name='Razor Strop',
		pic='media/items/legendaries/armor/waist/belts/razor_strop.png',
		unique='Picking up a Health Globe releases an explosion that deals <span>300 - 400%</span> weapon damage as Fire to enemies within <span class="silver">20</span> yards',
		random_primaries='3',
		owner='all',
		patch='23')
	razorStrop.save()
	razorStrop.affixes.add(mainStat, itemPickup)

	sacredHarness = Armor(category='Belts',
		name='Sacred Harness',
		pic='media/items/legendaries/armor/waist/belts/sacred_harness.png',
		unique='Judgment gains the effect of the Debilitate rune and is cast at your landing location when casting Falling Sword',
		random_primaries='3',
		random_secondaries='1',
		owner='cs',
		patch='23')
	sacredHarness.save()
	sacredHarness.affixes.add(mainStat)

	saffronWrap = Armor(category='Belts',
		name='Saffron Wrap',
		pic='media/items/legendaries/armor/waist/belts/saffron_wrap.png',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	saffronWrap.save()
	saffronWrap.affixes.add(mainStat, rcr, saffronCCReduction)

	sashOfKnives = Armor(category='Belts',
		name='Sash of Knives',
		pic='media/items/legendaries/armor/waist/belts/sash_of_knives.png',
		unique='With every attack, you throw a Dagger at a nearby enemy for <span>500 - 650%</span> weapon damage as Physical',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	sashOfKnives.save()
	sashOfKnives.affixes.add(mainStat)

	seborsNightmare = Armor(category='Belts',
		name='Sebor\'s Nightmare',
		pic='media/items/legendaries/armor/waist/belts/sebors_nightmare.png',
		unique='Haunt is cast on all nearby enemies when you open a Chest',
		random_primaries='3',
		owner='wd',
		patch='23')
	seborsNightmare.save()
	seborsNightmare.affixes.add(mainStat, itemPickup)

#2.4
	stringOfEars = Armor(category='Belts',
		name='String of Ears',
		pic='media/items/legendaries/armor/waist/belts/string_of_ears.png',
		unique='<span>+25.0 - 30.0%</span> Melee Damage Reduction',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='24')
	stringOfEars.save()
	# stringOfEars.affixes.add(mainStat, stringReducedMeleeDmg)
	stringOfEars.affixes.add(mainStat)

#2.4 new
	theShameOfDelsere = Armor(category='Belts',
		name='The Shame of Deslere',
		pic='media/items/legendaries/2.4/armor/the_shame_of_delsere.png',
		unique='Your Signature Spells attack <span class="silver">50%</span> faster and restore <span>9 - 12</span> Arcane Power',
		random_primaries='3',
		random_secondaries='1',
		owner='wz',
		patch='24')
	theShameOfDelsere.save()
	theShameOfDelsere.affixes.add(mainStat)

	theWitchingHour = Armor(category='Belts',
		name='The Witching Hour',
		pic='media/items/legendaries/armor/waist/belts/the_witching_hour.png',
		random_primaries='2',
		random_secondaries='2',
		owner='all',
		patch='23')
	theWitchingHour.save()
	theWitchingHour.affixes.add(witchingIAS, witchingCHD)

	thundergodsVigor = Armor(category='Belts',
		name='Thundergod\'s Vigor',
		pic='media/items/legendaries/armor/waist/belts/thundergods_vigor.png',
		unique='Blocking, dodging or being hit causes you to discharge bolts of electricity that deal <span>100 - 130%</span> weapon damage as Lightning',
		random_primaries='1',
		owner='all',
		patch='23')
	thundergodsVigor.save()
	thundergodsVigor.affixes.add(mainStat, vita, thundergodsLightDmg, thundergodsLightRes)

	vigilanteBelt = Armor(category='Belts',
		name='Vigilante Belt',
		pic='media/items/legendaries/armor/waist/belts/vigilante_belt.png',
		random_primaries='2',
		random_secondaries='2',
		owner='all',
		patch='23')
	vigilanteBelt.save()
	vigilanteBelt.affixes.add(mainStat, vigilanteCDR)

#2.4 new
	zoeysSecret = Armor(category='Belts',
		name='Zoey\'s Secret',
		pic='media/items/legendaries/2.4/armor/zoeys_secret.png',
		unique='You take <span>8 - 9%</span> less damage for each Companion you have active',
		random_primaries='2',
		random_secondaries='1',
		owner='dh',
		patch='24')
	zoeysSecret.save()
	zoeysSecret.affixes.add(mainStat, vita)

	for armor in Armor.objects.filter(category='Belts'):
		armor.inherent = '<span class="inherent"><span>440 - 506</span> Armor</span>'
		armor.slot = 'Waist'
		armor.save()


def load_mighty_belts(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")


	stre = Affix.objects.get(category='Mighty Belts',
		affix='stre')
	vita = Affix.objects.get(category='Mighty Belts',
		affix='vita')
	allRes = Affix.objects.get(category='Mighty Belts',
		affix='allRes')

	maxFury = Affix.objects.get(category='Mighty Belts',
		affix='maxFury')

	dreadAvalanche = Affix.objects.get(category='Mighty Belts',
		affix='dreadAvalanche')
	girdleIAS = Affix.objects.get(category='Mighty Belts',
		affix='girdleIAS')
	kotuursBlockChance = Affix.objects.get(category='Mighty Belts',
		affix='kotuursBlockChance')


	agelessMight = Armor(category='Mighty Belts',
		name='Ageless Might',
		pic='media/items/legendaries/armor/waist/mightybelts/ageless_might.png',
		random_primaries='2',
		random_secondaries='2',
		patch='23')
	agelessMight.save()
	agelessMight.affixes.add(stre, allRes)

	chilaniksChain = Armor(category='Mighty Belts',
		name='Chilanik\'s Chain',
		pic='media/items/legendaries/armor/waist/mightybelts/chilaniks_chain.png',
		unique='Using War Cry increases the Movement Speed for you and all allies affected by <span>30 - 40%</span> for <span class="silver">10</span> seconds',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	chilaniksChain.save()
	chilaniksChain.affixes.add(stre)

#2.4
	dreadIron = Armor(category='Mighty Belts',
		name='Dread Iron',
		pic='media/items/legendaries/armor/waist/mightybelts/dread_iron.png',
		unique='Ground Stomp causes an Avalanche',
		random_primaries='1',
		random_secondaries='1',
		patch='24')
	dreadIron.save()
	dreadIron.affixes.add(stre, vita, dreadAvalanche)

	girdleOfGiants = Armor(category='Mighty Belts',
		name='Girdle of Giants',
		pic='media/items/legendaries/armor/waist/mightybelts/girdle_of_giants.png',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	girdleOfGiants.save()
	girdleOfGiants.affixes.add(stre, girdleIAS, maxFury)

	kotuursBrace = Armor(category='Mighty Belts',
		name='Kotuur\'s Brace',
		pic='media/items/legendaries/armor/waist/mightybelts/kotuurs_brace.png',
		random_primaries='2',
		random_secondaries='2',
		patch='23')
	kotuursBrace.save()
	kotuursBrace.affixes.add(stre, kotuursBlockChance)

	lamentation = Armor(category='Mighty Belts',
		name='Lamentation',
		pic='media/items/legendaries/armor/waist/mightybelts/lamentation.png',
		unique='Rend can now stack up to <span class="silver">2</span> times on an enemy',
		random_primaries='3',
		random_secondaries='1',
		patch='23')
	lamentation.save()
	lamentation.affixes.add(stre)

	prideOfCassius = Armor(category='Mighty Belts',
		name='Pride of Cassius',
		pic='media/items/legendaries/armor/waist/mightybelts/pride_of_cassius.png',
		unique='Increases the duration of Ignore Pain by <span>4 - 6</span> seconds',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	prideOfCassius.save()
	prideOfCassius.affixes.add(stre, allRes)

	theUndisputedChampion = Armor(category='Mighty Belts',
		name='The Undisputed Champion',
		pic='media/items/legendaries/armor/waist/mightybelts/the_undisputed_champion.png',
		unique='Frenzy gains the effect of every rune',
		random_primaries='2',
		random_secondaries='1',
		patch='23')
	theUndisputedChampion.save()
	theUndisputedChampion.affixes.add(stre, allRes)

	for armor in Armor.objects.filter(category='Mighty Belts'):
		armor.inherent = '<span class="inherent"><span>516 - 675</span> Armor</span>'
		armor.slot = 'Waist'
		armor.owner = 'bb'
		armor.save()


def load_pants(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(slot='Pants',
		affix='mainStat')
	lps = Affix.objects.get(slot='Pants',
		affix='lps')
	allRes = Affix.objects.get(slot='Pants',
		affix='allRes')
	sockets = Affix.objects.get(slot='Pants',
		affix='sockets')

	extraGold = Affix.objects.get(slot='Pants',
		affix='extraGold')

	swampPoisDmg = Affix.objects.get(slot='Pants',
		affix='swampPoisDmg')
	swampCCReduction = Affix.objects.get(slot='Pants',
		affix='swampCCReduction')

	deathsBargain = Armor(slot='Pants',
		name='Death\'s Bargain',
		pic='media/items/legendaries/armor/legs/deaths_bargain.png',
		unique='Gain an aura of death that deals <span>750 - 1000%</span> of your Life per Second as Physical damage to enemies within <span class="silver">16</span> yards. You no longer regenerate Life',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	deathsBargain.save()
	deathsBargain.affixes.add(mainStat, lps)

	depthDiggers = Armor(slot='Pants',
		name='Depth Diggers',
		pic='media/items/legendaries/armor/legs/depth_diggers.png',
		unique='Primary skills that generate resource deal <span>80 - 100%</span> additional damage',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	depthDiggers.save()
	depthDiggers.affixes.add(mainStat, allRes)

#2.4
	hammerJammers = Armor(slot='Pants',
		name='Hammer Jammers',
		pic='media/items/legendaries/armor/legs/hammer_jammers.png',
		unique='Enemies take <span>300 - 400%</span> increased damage from your Blessed Hammers for <span class="silver">10</span> seconds after you hit them with a Blind, Immobilize, or Stun',
		random_primaries='2',
		random_secondaries='1',
		owner='cs',
		patch='24')
	hammerJammers.save()
	hammerJammers.affixes.add(mainStat, sockets)

	hexingPantsOfMrYan = Armor(slot='Pants',
		name='Hexing Pants of Mr. Yan',
		pic='media/items/legendaries/armor/legs/hexing_pants_of_mr_yan.png',
		unique='Your Resource generation and damage is increased by <span class="silver">25%</span> while moving and decreased by <span>20 - 25%</span> while standing still',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	hexingPantsOfMrYan.save()
	hexingPantsOfMrYan.affixes.add(mainStat)

	poxFaulds = Armor(slot='Pants',
		name='Pox Faulds',
		pic='media/items/legendaries/armor/legs/pox_faulds.png',
		unique='When <span class="silver">3</span> or more enemies are within <span class="silver">12</span> yards, you release a vile stench that deals <span>450 - 550%</span> weapon damage as Poison every second for <span class="silver">5</span> seconds to enemies within <span class="silver">15</span> yards',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	poxFaulds.save()
	poxFaulds.affixes.add(mainStat)

	skelonsDeceit = Armor(slot='Pants',
		name='Skelon\'s Deceit',
		pic='media/items/legendaries/armor/legs/skelons_deceit.png',
		random_primaries='4',
		random_secondaries='2',
		notes='crafted',
		owner='all',
		patch='23')
	skelonsDeceit.save()
	# skelonsDeceit.affixes.add()

	swampLandWaders = Armor(slot='Pants',
		name='Swamp Land Waders',
		pic='media/items/legendaries/armor/legs/swamp_land_waders.png',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	swampLandWaders.save()
	swampLandWaders.affixes.add(mainStat, swampPoisDmg, swampCCReduction)

	for armor in Armor.objects.filter(slot='Pants'):
		armor.inherent = '<span class="inherent"><span>660 - 759</span> Armor</span>'
		armor.save()


def load_boots(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(slot='Boots',
		affix='mainStat')
	vita = Affix.objects.get(slot='Boots',
		affix='vita')
	allRes = Affix.objects.get(slot='Boots',
		affix='allRes')
	armor = Affix.objects.get(slot='Boots',
		affix='armor')
	lps = Affix.objects.get(slot='Boots',
		affix='lps')
	movementSpeed = Affix.objects.get(slot='Boots',
		affix='movementSpeed')

	iceReducedColdDmg = Affix.objects.get(slot='Boots',
		affix='iceReducedColdDmg')

	boardWalkers = Armor(slot='Boots',
		name='Board Walkers',
		pic='media/items/legendaries/armor/feet/board_walkers.png',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted',
		owner='all',
		patch='23')
	boardWalkers.save()
	boardWalkers.affixes.add(movementSpeed)

#Removed in 2.4
	# bojAnglers = Armor(slot='Boots',
	# 	name='Boj Anglers',
	# 	pic='media/items/legendaries/armor/feet/boj_anglers.png',
	# 	random_primaries='2',
	# 	random_secondaries='2',
	# 	owner='all',
	# 	patch='23')
	# bojAnglers.save()
	# bojAnglers.affixes.add(mainStat, bojSkillDmg)

	bootsOfDisregard = Armor(slot='Boots',
		name='Boots of Disregard',
		pic='media/items/legendaries/armor/feet/boots_of_disregard.png',
		unique='Gain <span>10000</span> Life regeneration per Second for each second you stand still. This effect stacks up to <span>4</span> times',
		random_primaries='1',
		random_secondaries='1',
		owner='all',
		patch='23')
	bootsOfDisregard.save()
	bootsOfDisregard.affixes.add(vita, armor, lps)

	fireWalkers = Armor(slot='Boots',
		name='Fire Walkers',
		pic='media/items/legendaries/armor/feet/fire_walkers.png',
		unique='Burn the ground you walk on, dealing <span>300 - 400%</span> weapon damage each second',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	fireWalkers.save()
	fireWalkers.affixes.add(mainStat, movementSpeed)

	iceClimbers = Armor(slot='Boots',
		name='Ice Climbers',
		pic='media/items/legendaries/armor/feet/ice_climbers.png',
		unique='Gain immunity to Freeze and Immobilize effects',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	iceClimbers.save()
	iceClimbers.affixes.add(mainStat, allRes, iceReducedColdDmg)

	illusoryBoots = Armor(slot='Boots',
		name='Illusory Boots',
		pic='media/items/legendaries/armor/feet/illusory_boots.png',
		unique='You may move unhindered through enemies',
		random_primaries='1',
		random_secondaries='1',
		owner='all',
		patch='23')
	illusoryBoots.save()
	illusoryBoots.affixes.add(mainStat, allRes, movementSpeed)

	irontoeMudsputters = Armor(slot='Boots',
		name='Irontoe Mudsputters',
		pic='media/items/legendaries/armor/feet/irontoe_mudsputters.png',
		unique='Gain up to <span>25 - 30%</span> increased Movement Speed based on amount of Life missing',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	irontoeMudsputters.save()
	irontoeMudsputters.affixes.add(mainStat, vita)

	lutSocks = Armor(slot='Boots',
		name='Lut Socks',
		pic='media/items/legendaries/armor/feet/lut_socks.png',
		unique='Leap can be cast again within <span class="silver">2</span> seconds before the cooldown begins',
		random_primaries='3',
		random_secondaries='1',
		owner='all',
		patch='23')
	lutSocks.save()
	lutSocks.affixes.add(mainStat)

	nilfursBoast = Armor(slot='Boots',
		name='Nilfur\'s Boast',
		pic='media/items/legendaries/armor/feet/nilfurs_boast.png',
		unique='Increase the damage of Meteor by <span class="silver">100%</span>. When your Meteor hits <span class="silver">3</span> or fewer enemies, the damage is increased by <span>150 - 200%</span>',
		random_primaries='2',
		random_secondaries='1',
		owner='all',
		patch='23')
	nilfursBoast.save()
	nilfursBoast.affixes.add(mainStat, allRes)

#2.4 new
	riveraDancers = Armor(slot='Boots',
		name='Rivera Dancers',
		pic='media/items/legendaries/2.4/armor/rivera_dancers.png',
		unique='Lashing Tail Kick attacks <span class="silver">50%</span> faster and deals <span>250 - 300%</span> increased damage',
		random_primaries='2',
		random_secondaries='1',
		owner='mk',
		patch='24')
	riveraDancers.save()
	riveraDancers.affixes.add(mainStat, allRes)

	theCrudestBoots = Armor(slot='Boots',
		name='The Crudest Boots',
		pic='media/items/legendaries/armor/feet/the_crudest_boots.png',
		unique='Mystic Ally summons <span class="silver">2</span> extra Mystic Allies that fight by your side',
		random_primaries='2',
		random_secondaries='1',
		owner='mk',
		patch='23')
	theCrudestBoots.save()
	theCrudestBoots.affixes.add(mainStat, movementSpeed)

	for armor in Armor.objects.filter(slot='Boots'):
		armor.inherent = '<span class="inherent"><span>513 - 590</span> Armor</span>'
		armor.save()


def load_slugify(apps, schema_editor):
	Armor = apps.get_model("legendaries", "Armor")

	for armor in Armor.objects.all():
		armor.name_slug = slugify(armor.name)
		armor.slot_slug = slugify(armor.slot)
		armor.category_slug = slugify(armor.category)
		armor.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0005_accessories'),
    ]

    operations = [
        migrations.RunPython(load_helmets),
        migrations.RunPython(load_spirit_stones),
        migrations.RunPython(load_voodoo_masks),
        migrations.RunPython(load_wizard_hats),
        migrations.RunPython(load_shoulders),
        migrations.RunPython(load_chest_armor),
        migrations.RunPython(load_cloaks),
        migrations.RunPython(load_bracers),
        migrations.RunPython(load_gloves),
        migrations.RunPython(load_belts),
        migrations.RunPython(load_mighty_belts),
        migrations.RunPython(load_pants),
        migrations.RunPython(load_boots),
        migrations.RunPython(load_slugify)
    ]
