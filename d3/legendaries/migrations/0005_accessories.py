# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_amulets(apps, schema_editor):
	Accessory = apps.get_model("legendaries", "Accessory")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(slot='Amulets',
		affix='mainStat')
	vita = Affix.objects.get(slot='Amulets',
		affix='vita')
	eleDmg = Affix.objects.get(slot='Amulets',
		affix='eleDmg')
	holyDmg = Affix.objects.get(slot='Amulets',
		affix='holyDmg')
	ias = Affix.objects.get(slot='Amulets',
		affix='ias')
	chc = Affix.objects.get(slot='Amulets',
		affix='chc')
	chd = Affix.objects.get(slot='Amulets',
		affix='chd')
	cdr = Affix.objects.get(slot='Amulets',
		affix='cdr')
	allRes = Affix.objects.get(slot='Amulets',
		affix='allRes')
	sockets = Affix.objects.get(slot='Amulets',
		affix='sockets')

	itemHealing = Affix.objects.get(slot='Amulets',
		affix='itemHealing')
	extraGold = Affix.objects.get(slot='Amulets',
		affix='extraGold')

	eyeReducedRangedDmg = Affix.objects.get(slot='Amulets',
		affix='eyeReducedRangedDmg')
	holySpiritRegen = Affix.objects.get(slot='Amulets',
		affix='holySpiritRegen')
	kymbosExtraGold = Affix.objects.get(slot='Amulets',
		affix='kymbosExtraGold')
	moonlightArcaneDmg = Affix.objects.get(slot='Amulets',
		affix='moonlightArcaneDmg')
	rondalsItemPickup = Affix.objects.get(slot='Amulets',
		affix='rondalsItemPickup')
	flavorMovementSpeed = Affix.objects.get(slot='Amulets',
		affix='flavorMovementSpeed')

	ancestors = Accessory(slot='Amulets',
		name='Ancestors\' Grace',
		pic='/assets/media/items/legendaries/accessories/amulets/ancestors_grace.png',
		unique='When receiving fatal damage, you are instead restored to <span class="silver">100%</span> of maximum Life and resources. This item is destroyed in the process.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	ancestors.save()
	ancestors.affixes.add(mainStat, vita)

	countess = Accessory(slot='Amulets',
		name='Countess Julia\'s Cameo',
		pic='/assets/media/items/legendaries/accessories/amulets/countess_julias_cameo.png',
		unique='Prevent all Arcane damage taken and heal yourself for <span>20 - 25%</span> of the amount prevented.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	countess.save()
	countess.affixes.add(mainStat, ias)

	dovu = Accessory(slot='Amulets',
		name='Dovu Energy Trap',
		pic='/assets/media/items/legendaries/accessories/amulets/dovu_energy_trap.png',
		unique='Increases duration of Stun effects by <span>20 - 25%</span>.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	dovu.save()
	dovu.affixes.add(mainStat, cdr)

	eye = Accessory(slot='Amulets',
		name='Eye of Elitch',
		pic='/assets/media/items/legendaries/accessories/amulets/eye_of_elitch.png',
		random_primaries='3',
		random_secondaries='1',
		owner='all')
	eye.save()
	eye.affixes.add(eleDmg,eyeReducedRangedDmg)

	gorget = Accessory(slot='Amulets',
		name='Golden Gorget of Leoric',
		pic='/assets/media/items/legendaries/accessories/amulets/golden_gorget_of_leoric.png',
		unique='After earning a massacre bonus, <span>4 - 6</span> Skeletons are summoned to fight by your side for <span class="silver">10</span> seconds.',
		random_primaries='1',
		random_secondaries='1',
		owner='all')
	gorget.save()
	gorget.affixes.add(mainStat, chc, allRes)

	halcyon = Accessory(slot='Amulets',
		name='Halcyon\'s Ascent',
		pic='/assets/media/items/legendaries/accessories/amulets/halcyons_ascent.png',
		unique='When you use {<span class="vary">Class Skill</span>}, you mesmerize nearby enemies with your skill, causing them to jump uncontrollably for <span>6 - 8</span> seconds.<div class="extra"><div class="extra-x">X</div><span><strong>Barbarian: </strong>Wrath of the Berserker<br><strong>Crusader: </strong>Akarat\'s Champion<br><strong>Demon Hunter: </strong>Vengeance<br><strong>Monk: </strong>Epiphany<br><strong>Witch Doctor: </strong>Big Bad Voodoo<br><strong>Wizard: </strong>Archon</span></div>',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	halcyon.save()
	halcyon.affixes.add(mainStat, cdr)

	haunt = Accessory(slot='Amulets',
		name='Haunt of Vaxo',
		pic='/assets/media/items/legendaries/accessories/amulets/haunt_of_vaxo.png',
		unique='Summons shadow clones to your aid when you Stun an enemy. This effect may occur once every <span class="silver">30</span> seconds.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	haunt.save()
	haunt.affixes.add(mainStat, chc)

	hellfire = Accessory(slot='Amulets',
		name='Hellfire Amulet',
		pic='/assets/media/items/legendaries/accessories/amulets/hellfire_amulet.png',
		unique='Gain a [random] {<span class="vary">Class</span>} specific passive.<div class="extra"><div class="extra-x">X</div><span>Barbarian<br>Crusader<br>Demon Hunter<br>Monk<br>Witich Doctor<br>Wizard</span></div>',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	hellfire.save()
	hellfire.affixes.add(mainStat, sockets)

	holy = Accessory(slot='Amulets',
		name='Holy Beacon',
		pic='/assets/media/items/legendaries/accessories/amulets/holy_beacon.png',
		unique='<span>+2.2 - 3.0</span> Spirit Regeneration per Second',
		unique_is_primary=True,
		random_primaries='1',
		random_secondaries='2',
		owner='all')
	holy.save()
	holy.affixes.add(mainStat, holyDmg, holySpiritRegen)

	kymbos = Accessory(slot='Amulets',
		name='Kymbo\'s Gold',
		pic='/assets/media/items/legendaries/accessories/amulets/kymbos_gold.png',
		unique='Picking up gold heals you for an amount equal to the gold that was picked up.',
		random_primaries='3',
		owner='all')
	kymbos.save()
	kymbos.affixes.add(kymbosExtraGold)

	maras = Accessory(slot='Amulets',
		name='Mara\'s Kaleidoscope',
		pic='/assets/media/items/legendaries/accessories/amulets/maras_kaleidoscope.png',
		unique='Prevent all Poison damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	maras.save()
	maras.affixes.add(mainStat, chc)

	moonlight = Accessory(slot='Amulets',
		name='Moonlight Ward',
		pic='/assets/media/items/legendaries/accessories/amulets/moonlight_ward.png',
		unique='Enemies hit within <span class="silver">15</span> yards have a chance to spawn Arcane shards that explode and deal <span>240 - 320%</span> Arcane damage to enemies within <span class="silver">15</span> yards.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	moonlight.save()
	moonlight.affixes.add(chc, moonlightArcaneDmg)

	ouroboros = Accessory(slot='Amulets',
		name='Ouroboros',
		pic='/assets/media/items/legendaries/accessories/amulets/ouroboros.png',
		random_primaries='2',
		random_secondaries='2',
		owner='all')
	ouroboros.save()
	ouroboros.affixes.add(mainStat, chc)

	overwhelming = Accessory(slot='Amulets',
		name='Overwhelming Desire',
		pic='/assets/media/items/legendaries/accessories/amulets/overwhelming_desire.png',
		unique='Chance on hit to charm the enemy. While charmed, the enemy takes <span class="silver">35%</span> more damage.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	overwhelming.save()
	overwhelming.affixes.add(mainStat, cdr)

	rakoffs = Accessory(slot='Amulets',
		name='Rakoff\'s Glass of Life',
		pic='/assets/media/items/legendaries/accessories/amulets/rakoffs_glass_of_life.png',
		unique='Enemies you kill have a <span>3 - 4%</span> additional chance to drop a health globe.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	rakoffs.save()
	rakoffs.affixes.add(mainStat, itemHealing)

	rondals = Accessory(slot='Amulets',
		name='Rondal\'s Locket',
		pic='/assets/media/items/legendaries/accessories/amulets/rondals_locket.png',
		random_primaries='3',
		owner='all')
	rondals.save()
	rondals.affixes.add(mainStat, itemHealing, rondalsItemPickup)

	squirts = Accessory(slot='Amulets',
		name='Squirt\'s Necklace',
		pic='/assets/media/items/legendaries/accessories/amulets/squirts_necklace.png',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	squirts.save()
	squirts.affixes.add(mainStat, chd, extraGold)

	talisman = Accessory(slot='Amulets',
		name='Talisman of Aranoch',
		pic='/assets/media/items/legendaries/accessories/amulets/talisman_of_aranoch.png',
		unique='Prevent all Cold damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		random_primaries='3',
		random_secondaries='1',
		owner='all')
	talisman.save()
	talisman.affixes.add(mainStat)

	ess = Accessory(slot='Amulets',
		name='The Ess of Johan',
		pic='/assets/media/items/legendaries/accessories/amulets/the_ess_of_johan.png',
		unique='Chance on hit to pull in enemies toward your target and Slow them by <span>60 - 80%</span>.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	ess.save()
	ess.affixes.add(mainStat, cdr)

	flavor = Accessory(slot='Amulets',
		name='The Flavor of Time',
		pic='/assets/media/items/legendaries/accessories/amulets/the_flavor_of_time.png',
		random_primaries='3',
		random_secondaries='1',
		owner='all')
	flavor.save()
	flavor.affixes.add(cdr, flavorMovementSpeed)

	star = Accessory(slot='Amulets',
		name='The Star of Azkaranth',
		pic='/assets/media/items/legendaries/accessories/amulets/the_star_of_azkaranth.png',
		unique='Prevent all Fire damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	star.save()
	star.affixes.add(mainStat, cdr)

	xephirian = Accessory(slot='Amulets',
		name='Xephirian Amulet',
		pic='/assets/media/items/legendaries/accessories/amulets/xephirian_amulet.png',
		unique='Prevent all Lightning damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	xephirian.save()
	xephirian.affixes.add(mainStat, ias)


def load_rings(apps, schema_editor):
	Accessory = apps.get_model("legendaries", "Accessory")
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix.objects.get(slot='Rings',
		affix='mainStat')
	ias = Affix.objects.get(slot='Rings',
		affix='ias')
	chc = Affix.objects.get(slot='Rings',
		affix='chc')
	chd = Affix.objects.get(slot='Rings',
		affix='chd')
	cdr = Affix.objects.get(slot='Rings',
		affix='cdr')
	rcr = Affix.objects.get(slot='Rings',
		affix='rcr')
	allRes = Affix.objects.get(slot='Rings',
		affix='allRes')
	lph = Affix.objects.get(slot='Rings',
		affix='lph')
	sockets = Affix.objects.get(slot='Rings',
		affix='sockets')

	extraGold = Affix.objects.get(slot='Rings',
		affix='extraGold')

	justiceBlockChance = Affix.objects.get(slot='Rings',
		affix='justiceBlockChance')
	justiceCCReduction = Affix.objects.get(slot='Rings',
		affix='justiceCCReduction')
	hellfireBonusExp = Affix.objects.get(slot='Rings',
		affix='hellfireBonusExp')
	leoricsBonusExp = Affix.objects.get(slot='Rings',
		affix='leoricsBonusExp')
	manaldMaxResource = Affix.objects.get(slot='Rings',
		affix='manaldMaxResource')
	nagelringMagicFind = Affix.objects.get(slot='Rings',
		affix='nagelringMagicFind')
	obsidianDurability = Affix.objects.get(slot='Rings',
		affix='obsidianDurability')
	oculusEliteDmg = Affix.objects.get(slot='Rings',
		affix='oculusEliteDmg')
	pandemoniumFearChance = Affix.objects.get(slot='Rings',
		affix='pandemoniumFearChance')
	rechelsFearChance = Affix.objects.get(slot='Rings',
		affix='rechelsFearChance')
	stolenItemPickup = Affix.objects.get(slot='Rings',
		affix='stolenItemPickup')
	stoneEleDmg = Affix.objects.get(slot='Rings',
		affix='stoneEleDmg')
	stoneEliteDmg = Affix.objects.get(slot='Rings',
		affix='stoneEliteDmg')
	stoneMaxResource = Affix.objects.get(slot='Rings',
		affix='stoneMaxResource')
	unityEliteDmg = Affix.objects.get(slot='Rings',
		affix='unityEliteDmg')

	arcstone = Accessory(slot='Rings',
		name='Arcstone',
		pic='/assets/media/items/legendaries/accessories/rings/arcstone.png',
		unique='Lightning pulses periodically between all wearers of this item, dealing <span>1000 - 1500%</span> weapon damage.',
		random_primaries='3',
		random_secondaries='1',
		owner='all')
	arcstone.save()
	arcstone.affixes.add(mainStat)

	avarice = Accessory(slot='Rings',
		name='Avarice Band',
		pic='/assets/media/items/legendaries/accessories/rings/avarice_band.png',
		unique='Each time you pick up gold, increase your Gold and Health Pickup radius by <span class="silver">1</span> yard for <span class="silver">10</span> seconds, stacking up to <span class="silver">30</span> times.',
		random_primaries='2',
		owner='all')
	avarice.save()
	avarice.affixes.add(mainStat, chc, extraGold)

	hollow_whispers = Accessory(slot='Rings',
		name='Band of Hollow Whispers',
		pic='/assets/media/items/legendaries/accessories/rings/band_of_hollow_whispers.png',
		unique='This ring occasionally haunts nearby enemies.',
		random_primaries='3',
		random_secondaries='1',
		owner='all')
	hollow_whispers.save()
	hollow_whispers.affixes.add(mainStat)

	rue_chambers = Accessory(slot='Rings',
		name='Band of the Rue Chambers',
		pic='/assets/media/items/legendaries/accessories/rings/band_of_the_rue_chambers.png',
		unique='Your Spirit Generators generate <span>40 - 50%</span> more Spirit.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	rue_chambers.save()
	rue_chambers.affixes.add(mainStat, ias)

	broken_promises = Accessory(slot='Rings',
		name='Broken Promises',
		pic='/assets/media/items/legendaries/accessories/rings/broken_promises.png',
		unique='After <span class="silver">5</span> consecutive non-critical hits, your chance to critically hit is increased to <span class="silver">100%</span> for <span class="silver">3</span> seconds.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	broken_promises.save()
	broken_promises.affixes.add(mainStat, rcr)

	bulkathoss = Accessory(slot='Rings',
		name='Bul-Kathos\'s Wedding Band',
		pic='/assets/media/items/legendaries/accessories/rings/bul-kathoss_wedding_band.png',
		unique='You drain life from enemies around you.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	bulkathoss.save()
	bulkathoss.affixes.add(mainStat, chd)

	convention = Accessory(slot='Rings',
		name='Convention of Elements',
		pic='/assets/media/items/legendaries/accessories/rings/convention_of_elements.png',
		unique='Gain <span>150 - 200%</span> increased damage to a single element for <span class="silver">4</span> seconds. This effect rotates through the elements available to your class in the following order: Arcane, Cold, Fire, Holy, Lightning, Physical, Poison.',
		random_primaries='1',
		random_secondaries='1',
		owner='all')
	convention.save()
	convention.affixes.add(mainStat, chc, sockets)

	eternal = Accessory(slot='Rings',
		name='Eternal Union',
		pic='/assets/media/items/legendaries/accessories/rings/eternal_union.png',
		unique='Increases the duration of Phalanx avatars by <span class="silver">200%</span>.',
		random_primaries='3',
		random_secondaries='1',
		owner='sader')
	eternal.save()
	eternal.affixes.add(mainStat)

	halo = Accessory(slot='Rings',
		name='Halo of Arlyse',
		pic='/assets/media/items/legendaries/accessories/rings/halo_of_arlyse.png',
		unique='Your Ice Armor now reduces damage from melee attacks by <span>50 - 60%</span> and automatically casts Frost Nova whenever you take <span class="silver">10%</span> of your Life in damage.',
		random_primaries='2',
		random_secondaries='1',
		owner='wiz')
	halo.save()
	halo.affixes.add(mainStat, sockets)

	hellfire = Accessory(slot='Rings',
		name='Hellfire Ring',
		pic='/assets/media/items/legendaries/accessories/rings/hellfire_ring.png',
		unique='Chance on hit to engulf the ground in lava, dealing <span class="silver">200%</span> weapon damage per second for <span class="silver">6</span> seconds.',
		random_primaries='4',
		random_secondaries='1',
		owner='all')
	hellfire.save()
	hellfire.affixes.add(hellfireBonusExp)

	justice = Accessory(slot='Rings',
		name='Justice Lantern',
		pic='/assets/media/items/legendaries/accessories/rings/justice_lantern.png',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	justice.save()
	justice.affixes.add(mainStat, justiceBlockChance, justiceCCReduction)

	kredes = Accessory(slot='Rings',
		name='Krede\'s Flame',
		pic='/assets/media/items/legendaries/accessories/rings/kredes_flame.png',
		unique='Taking Fire damage restores your primary resource.',
		random_primaries='3',
		random_secondaries='1',
		owner='all')
	kredes.save()
	kredes.affixes.add(mainStat)

	leorics = Accessory(slot='Rings',
		name='Leoric\'s Signet',
		pic='/assets/media/items/legendaries/accessories/rings/leorics_signet.png',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	leorics.save()
	leorics.affixes.add(mainStat, chc, leoricsBonusExp)

	manald = Accessory(slot='Rings',
		name='Manald Heal',
		pic='/assets/media/items/legendaries/accessories/rings/manald_heal.png',
		random_primaries='3',
		random_secondaries='1',
		owner='all')
	manald.save()
	manald.affixes.add(mainStat, manaldMaxResource)

	nagel = Accessory(slot='Rings',
		name='Nagelring',
		pic='/assets/media/items/legendaries/accessories/rings/nagelring.png',
		unique='Summons a Fallen Lunatic to your side every <span>10 - 12</span> seconds.',
		random_primaries='2',
		random_secondaries='1',
		owner='all')
	nagel.save()
	nagel.affixes.add(mainStat, nagelringMagicFind)

	obsidian = Accessory(slot='Rings',
		name='Obsidian Ring of the Zodiac',
		pic='/assets/media/items/legendaries/accessories/rings/obsidian_ring_of_the_zodiac.png',
		unique='Reduce the remaining cooldown of one of your skills by <span class="silver">1</span> seconds when you hit with a resource-spending attack.',
		random_secondaries='1',
		owner='all')
	obsidian.save()
	obsidian.affixes.add(ias, chc, cdr, rcr, obsidianDurability)

	oculus = Accessory(slot='Rings',
		name='Oculus Ring',
		pic='/assets/media/items/legendaries/accessories/rings/oculus_ring.png',
		unique='Chance to create an area of focused power on killing a monster. Damage is increased by <span>35 - 40%</span> while standing in the area.',
		random_secondaries='1',
		owner='all')
	oculus.save()
	oculus.affixes.add(mainStat, allRes, ias, oculusEliteDmg)

	pandemonium = Accessory(slot='Rings',
		name='Pandemonium Loop',
		pic='/assets/media/items/legendaries/accessories/rings/pandemonium_loop.png',
		unique='Enemies slain while Feared die in a bloody explosion and cause other nearby enemies to flee in Fear.',
		random_primaries='3',
		owner='all')
	pandemonium.save()
	pandemonium.affixes.add(mainStat, pandemoniumFearChance)

	puzzle = Accessory(slot='Rings',
		name='Puzzle Ring',
		pic='/assets/media/items/legendaries/accessories/rings/puzzle_ring.png',
		unique='Summon a treasure goblin who picks up normal-quality items for you. After picking up <span>12 - 16</span> items, he drops a rare item with a chance for a legendary.',
		random_primaries='2',
		owner='all')
	puzzle.save()
	puzzle.affixes.add(mainStat, ias, extraGold)

	rechels = Accessory(slot='Rings',
		name='Rechel\'s Ring of Larceny',
		pic='/assets/media/items/legendaries/accessories/rings/rechels_ring_of_larceny.png',
		unique='Gain <span>45 - 60%</span> increased movement speed for 4 seconds after Fearing an enemy.',
		random_primaries='3',
		owner='all')
	rechels.save()
	rechels.affixes.add(mainStat, rechelsFearChance)

	rorg = Accessory(slot='Rings',
		name='Ring of Royal Grandeur',
		pic='/assets/media/items/legendaries/accessories/rings/ring_of_royal_grandeur.png',
		unique='Reduces the number of items needed for set bonuses by <span class="silver">1</span> (to a minimum of <span class="silver">2</span>).',
		random_primaries='1',
		random_secondaries='1',
		owner='all')
	rorg.save()
	rorg.affixes.add(mainStat, ias, lph)

	rogars = Accessory(slot='Rings',
		name='Rogar\'s Huge Stone',
		pic='/assets/media/items/legendaries/accessories/rings/rogars_huge_stone.png',
		unique='Increase your Life per Second by up to <span>75 - 100%</span> based on your missing Life.',
		random_primaries='3',
		random_secondaries='1',
		owner='all')
	rogars.save()
	rogars.affixes.add(mainStat)

	skull = Accessory(slot='Rings',
		name='Skull Grasp',
		pic='/assets/media/items/legendaries/accessories/rings/skull_grasp.png',
		unique='Increase the damage of Whirlwind by <span>300 - 400%</span> weapon damage.',
		random_primaries='2',
		random_secondaries='1',
		owner='barb')
	skull.save()
	skull.affixes.add(mainStat, chc)

	stolen = Accessory(slot='Rings',
		name='Stolen Ring',
		pic='/assets/media/items/legendaries/accessories/rings/stolen_ring.png',
		random_primaries='3',
		owner='all')
	stolen.save()
	stolen.affixes.add(mainStat, extraGold, stolenItemPickup)

	soj = Accessory(slot='Rings',
		name='Stone of Jordan',
		pic='/assets/media/items/legendaries/accessories/rings/stone_of_jordan.png',
		random_primaries='1',
		random_secondaries='1',
		owner='all')
	soj.save()
	soj.affixes.add(mainStat, stoneEleDmg, stoneEliteDmg, stoneMaxResource)

	short_mans = Accessory(slot='Rings',
		name='The Short Man\'s Finger',
		pic='/assets/media/items/legendaries/accessories/rings/the_short_mans_finger.png',
		unique='Gargantuan instead summons <span class="silver">3</span> smaller gargantuans each more powerful than before.',
		random_primaries='2',
		random_secondaries='1',
		owner='wd')
	short_mans.save()
	short_mans.affixes.add(mainStat, chd)

	tall_mans = Accessory(slot='Rings',
		name='The Tall Man\'s Finger',
		pic='/assets/media/items/legendaries/accessories/rings/the_tall_mans_finger.png',
		unique='Zombie Dogs instead summons a single gargantuan dog with more damage and health than all other dogs combined.',
		random_primaries='3',
		random_secondaries='1',
		owner='wd')
	tall_mans.save()
	tall_mans.affixes.add(mainStat)

	unity = Accessory(slot='Rings',
		name='Unity',
		pic='/assets/media/items/legendaries/accessories/rings/unity.png',
		unique='All damage taken is split between wearers of this item.',
		random_primaries='1',
		random_secondaries='1',
		owner='all')
	unity.save()
	unity.affixes.add(mainStat, chc, unityEliteDmg)

	wyrdward = Accessory(slot='Rings',
		name='Wyrdward',
		pic='/assets/media/items/legendaries/accessories/rings/wyrdward.png',
		unique='Lightning damage has a <span>25 - 35%</span> chance to Stun for <span class="silver">1.5</span> seconds.',
		random_primaries='3',
		random_secondaries='1',
		owner='all')
	wyrdward.save()
	wyrdward.affixes.add(mainStat)


def load_follower_items(apps, schema_editor):
	Accessory = apps.get_model("legendaries", "Accessory")

	handOfTheProphet = Accessory(slot='Followers',
		name='Hand of the Prophet',
		pic='/assets/media/items/legendaries/accessories/followeritems/enchantress_focus.png',
		unique='Equip on Follower: Gain access to all skills.',
		random_primaries='4',
		owner='all')
	handOfTheProphet.save()

	smokingThurible = Accessory(slot='Followers',
		name='Smoking Thurible',
		pic='/assets/media/items/legendaries/accessories/followeritems/enchantress_focus.png',
		unique='Equip on Follower: Your follower cannot die.',
		random_primaries='4',
		owner='all')
	smokingThurible.save()

	vadimsSurge = Accessory(slot='Followers',
		name='Vadim\'s Surge',
		pic='/assets/media/items/legendaries/accessories/followeritems/enchantress_focus.png',
		unique='Equip on Follower: Reduce the cooldown of all Follower skills by <span class="silver">50%</span>.',
		random_primaries='4',
		owner='all')
	vadimsSurge.save()

	ribaldEtchings = Accessory(slot='Followers',
		name='Ribald Etchings',
		pic='/assets/media/items/legendaries/accessories/followeritems/scoundrel_token.png',
		unique='Equip on Follower: Gain access to all skills.',
		random_primaries='4',
		owner='all')
	ribaldEtchings.save()

	skeletonKey = Accessory(slot='Followers',
		name='Skeleton Key',
		pic='/assets/media/items/legendaries/accessories/followeritems/scoundrel_token.png',
		unique='Equip on Follower: Your follower cannot die.',
		random_primaries='4',
		owner='all')
	skeletonKey.save()

	slipkasLetterOpener = Accessory(slot='Followers',
		name='Slipka\'s Letter Opener',
		pic='/assets/media/items/legendaries/accessories/followeritems/scoundrel_token.png',
		unique='Equip on Follower: Reduce the cooldown of all Follower skills by <span class="silver">50%</span>.',
		random_primaries='4',
		owner='all')
	slipkasLetterOpener.save()

	enchantingFavor = Accessory(slot='Followers',
		name='Enchanting Favor',
		pic='/assets/media/items/legendaries/accessories/followeritems/templar_relic.png',
		unique='Equip on Follower: Your follower cannot die.',
		random_primaries='4',
		owner='all')
	enchantingFavor.save()

	hillenbrandsTrainingSword = Accessory(slot='Followers',
		name='Hillenbrand\'s Training Sword',
		pic='/assets/media/items/legendaries/accessories/followeritems/templar_relic.png',
		unique='Equip on Follower: Reduce the cooldown of all Follower skills by <span class="silver">50%</span>.',
		random_primaries='4',
		owner='all')
	hillenbrandsTrainingSword.save()

	relicOfAkart = Accessory(slot='Followers',
		name='Relic of Akart',
		pic='/assets/media/items/legendaries/accessories/followeritems/templar_relic.png',
		unique='Equip on Follower: Gain access to all skills.',
		random_primaries='4',
		owner='all')
	relicOfAkart.save()


def load_misc_info(apps, schema_editor):
	Accessory = apps.get_model("legendaries", "Accessory")

	for accessory in Accessory.objects.all():
		accessory.name_slug = slugify(accessory.name)
		accessory.slot_slug = slugify(accessory.slot)
		accessory.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0004_offhands'),
    ]

    operations = [
        migrations.RunPython(load_amulets),
        migrations.RunPython(load_rings),
        migrations.RunPython(load_follower_items),
        migrations.RunPython(load_misc_info)
    ]
