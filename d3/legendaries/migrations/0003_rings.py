# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_rings(apps, schema_editor):
	Ring = apps.get_model("legendaries", "Ring")
	RingAffix = apps.get_model("affixes", "RingAffix")

	dmg = RingAffix.objects.get(pk=0)
	mainStat = RingAffix.objects.get(pk=1)
	dext = RingAffix.objects.get(pk=2)
	inte = RingAffix.objects.get(pk=3)
	stre = RingAffix.objects.get(pk=4)
	vita = RingAffix.objects.get(pk=5)
	life = RingAffix.objects.get(pk=6)
	armor = RingAffix.objects.get(pk=7)
	allRes = RingAffix.objects.get(pk=8)
	lps = RingAffix.objects.get(pk=9)
	lph = RingAffix.objects.get(pk=10)
	ias = RingAffix.objects.get(pk=11)
	chc = RingAffix.objects.get(pk=12)
	chd = RingAffix.objects.get(pk=13)
	areaDmg = RingAffix.objects.get(pk=14)
	cdr = RingAffix.objects.get(pk=15)
	rcr = RingAffix.objects.get(pk=16)
	sockets = RingAffix.objects.get(pk=17)

	eleRes = RingAffix.objects.get(pk=18)
	physRes = RingAffix.objects.get(pk=19)
	coldRes = RingAffix.objects.get(pk=20)
	fireRes = RingAffix.objects.get(pk=21)
	lightRes = RingAffix.objects.get(pk=22)
	poisRes = RingAffix.objects.get(pk=23)
	arcaneRes = RingAffix.objects.get(pk=24)
	ccReduction = RingAffix.objects.get(pk=25)
	thorns = RingAffix.objects.get(pk=26)
	itemHealing = RingAffix.objects.get(pk=27)
	lpk = RingAffix.objects.get(pk=28)
	exp = RingAffix.objects.get(pk=29)
	extraGold = RingAffix.objects.get(pk=30)


	arcstone = Ring(id=0,
		category='Ring',
		name='Arcstone',
		pic='/assets/media/items/legendaries/accessories/rings/arcstone.png',
		unique='Lightning pulses periodically between all wearers of this item, dealing <span>1000 - 1500%</span> weapon damage.',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1')
	arcstone.save()
	arcstone.affixes.add(mainStat)

	avarice = Ring(id=1,
		category='Ring',
		name='Avarice Band',
		pic='/assets/media/items/legendaries/accessories/rings/avarice_band.png',
		unique='Each time you pick up gold, increase your Gold and Health Pickup radius by <span class="silver">1</span> yard for <span class="silver">10</span> seconds, stacking up to <span class="silver">30</span> times.',
		unique_is_primary=False,
		random_primaries='2')
	avarice.save()
	avarice.affixes.add(mainStat, chc, extraGold)

	hollow_whispers = Ring(id=2,
		category='Ring',
		name='Band of Hollow Whispers',
		pic='/assets/media/items/legendaries/accessories/rings/band_of_hollow_whispers.png',
		unique='This ring occasionally haunts nearby enemies.',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1')
	hollow_whispers.save()
	hollow_whispers.affixes.add(mainStat)

	rue_chambers = Ring(id=3,
		category='Ring',
		name='Band of the Rue Chambers',
		pic='/assets/media/items/legendaries/accessories/rings/band_of_the_rue_chambers.png',
		unique='Your Spirit Generators generate <span>40 - 50%</span> more Spirit.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	rue_chambers.save()
	rue_chambers.affixes.add(mainStat, ias)

	broken_promises = Ring(id=4,
		category='Ring',
		name='Broken Promises',
		pic='/assets/media/items/legendaries/accessories/rings/broken_promises.png',
		unique='After <span class="silver">5</span> consecutive non-critical hits, your chance to critically hit is increased to <span class="silver">100%</span> for <span class="silver">3</span> seconds.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	broken_promises.save()
	broken_promises.affixes.add(mainStat, rcr)

	bulkathoss = Ring(id=5,
		category='Ring',
		name='Bul-Kathos\'s Wedding Band',
		pic='/assets/media/items/legendaries/accessories/rings/bul-kathoss_wedding_band.png',
		unique='You drain life from enemies around you.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	bulkathoss.save()
	bulkathoss.affixes.add(mainStat, chd)

	convention = Ring(id=6,
		category='Ring',
		name='Convention of Elements',
		pic='/assets/media/items/legendaries/accessories/rings/convention_of_elements.png',
		unique='Gain <span>150 - 200%</span> increased damage to a single element for <span class="silver">4</span> seconds. This effect rotates through the elements available to your class in the following order: Arcane, Cold, Fire, Holy, Lightning, Physical, Poison.',
		unique_is_primary=False,
		random_primaries='1',
		random_secondaries='1')
	convention.save()
	convention.affixes.add(mainStat, chc, sockets)

	eternal = Ring(id=7,
		category='Ring',
		name='Eternal Union',
		pic='/assets/media/items/legendaries/accessories/rings/eternal_union.png',
		unique='Increases the duration of Phalanx avatars by <span class="silver">200%</span>.',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1')
	eternal.save()
	eternal.affixes.add(mainStat)

	halo = Ring(id=8,
		category='Ring',
		name='Halo of Arlyse',
		pic='/assets/media/items/legendaries/accessories/rings/halo_of_arlyse.png',
		unique='Your Ice Armor now reduces damage from melee attacks by <span>50 - 60%</span> and automatically casts Frost Nova whenever you take <span class="silver">10%</span> of your Life in damage.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	halo.save()
	halo.affixes.add(mainStat, sockets)

	hellfire_35 = Ring(id=9,
		category='Ring',
		name='Hellfire Ring (60)',
		pic='/assets/media/items/legendaries/accessories/rings/hellfire_ring_35.png',
		unique='Increases Bonus Experience by 35%',
		unique_is_primary=False,
		unique2='Chance to launch an explosive ball of Hellfire when you attack.',
		unique2_is_primary=False,
		random_primaries='3',
		random_secondaries='1',
		notes='Can also have Vit')
	hellfire_35.save()
	hellfire_35.affixes.add(mainStat)

	hellfire_45 = Ring(id=10,
		category='Ring',
		name='Hellfire Ring (70)',
		pic='/assets/media/items/legendaries/accessories/rings/hellfire_ring_45.png',
		unique='Increases Bonus Experience by <span class="silver">45%</span>',
		unique_is_primary=False,
		unique2='Chance on hit to engulf the ground in lava, dealing <span class="silver">200%</span> weapon damage per second for <span class="silver">6</span> seconds.',
		unique2_is_primary=False,
		random_primaries='4',
		random_secondaries='1')
	hellfire_45.save()
	hellfire_45.affixes.add()

	justice = Ring(id=11,
		category='Ring',
		name='Justice Lantern',
		pic='/assets/media/items/legendaries/accessories/rings/justice_lantern.png',
		unique='<span class="silver">+12%</span> Chance to Block',
		unique_is_primary=True,
		unique2='<span>+35 - 50%</span> Crowd Control Duration Reduction',
		unique2_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	justice.save()
	justice.affixes.add(mainStat)

	kredes = Ring(id=12,
		category='Ring',
		name='Krede\'s Flame',
		pic='/assets/media/items/legendaries/accessories/rings/kredes_flame.png',
		unique='Taking Fire damage restores your primary resource.',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1')
	kredes.save()
	kredes.affixes.add(mainStat)

	leorics = Ring(id=13,
		category='Ring',
		name='Leoric\'s Signet',
		pic='/assets/media/items/legendaries/accessories/rings/leorics_signet.png',
		unique='Increases Bonus Experience by <span>20 - 30%</span>',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	leorics.save()
	leorics.affixes.add(mainStat, chc)

	manald = Ring(id=14,
		category='Ring',
		name='Manald Heal',
		pic='/assets/media/items/legendaries/accessories/rings/manald_heal.png',
		unique='+Max {<span>Class Resource</span>}',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1',
		notes='???')
	manald.save()
	manald.affixes.add(mainStat)

	nagel = Ring(id=15,
		category='Ring',
		name='Nagelring',
		pic='/assets/media/items/legendaries/accessories/rings/nagelring.png',
		unique='<span>25 - 50%</span> Better Chance of Finding Magical Items',
		unique_is_primary=False,
		unique2='Summons a Fallen Lunatic to your side every <span>10 - 12</span> seconds.',
		unique2_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	nagel.save()
	nagel.affixes.add(mainStat)

	obsidian = Ring(id=16,
		category='Ring',
		name='Obsidian Ring of the Zodiac',
		pic='/assets/media/items/legendaries/accessories/rings/obsidian_ring_of_the_zodiac.png',
		unique='Reduce the remaining cooldown of one of your skills by <span class="silver">1</span> seconds when you hit with a resource-spending attack.',
		unique_is_primary=False,
		unique2='Ignores Durability Loss',
		unique2_is_primary=False,
		random_secondaries='1')
	obsidian.save()
	obsidian.affixes.add(ias, chc, cdr, rcr)

	oculus = Ring(id=17,
		category='Ring',
		name='Oculus Ring',
		pic='/assets/media/items/legendaries/accessories/rings/oculus_ring.png',
		unique='<span>+12.0 - 16.0%</span> Elite Damage Reduction',
		unique_is_primary=True,
		unique2='Chance to create an area of focused power on killing a monster. Damage is increased by <span>35 - 40%</span> while standing in the area.',
		unique2_is_primary=False,
		random_secondaries='1')
	oculus.save()
	oculus.affixes.add(mainStat, allRes, ias)

	pandemonium = Ring(id=18,
		category='Ring',
		name='Pandemonium Loop',
		pic='/assets/media/items/legendaries/accessories/rings/pandemonium_loop.png',
		unique='<span>+10.0 - 15.0%</span> chance to Fear on Hit',
		unique_is_primary=False,
		unique2='Enemies slain while Feared die in a bloody explosion and cause other nearby enemies to flee in Fear.',
		unique2_is_primary=False,
		random_primaries='3')
	pandemonium.save()
	pandemonium.affixes.add(mainStat)

	puzzle = Ring(id=19,
		category='Ring',
		name='Puzzle Ring',
		pic='/assets/media/items/legendaries/accessories/rings/puzzle_ring.png',
		unique='Summon a treasure goblin who picks up normal-quality items for you. After picking up <span>12 - 16</span> items, he drops a rare item with a chance for a legendary.',
		unique_is_primary=False,
		random_primaries='2')
	puzzle.save()
	puzzle.affixes.add(mainStat, ias, extraGold)

	rechels = Ring(id=20,
		category='Ring',
		name='Rechel\'s Ring of Larceny',
		pic='/assets/media/items/legendaries/accessories/rings/rechels_ring_of_larceny.png',
		unique='<span>+1.0 - 5.1%</span> chance to Fear on Hit',
		unique_is_primary=False,
		unique2='Gain <span>45 - 60%</span> increased movement speed for 4 seconds after Fearing an enemy.',
		unique2_is_primary=False,
		random_primaries='3')
	rechels.save()
	rechels.affixes.add(mainStat)

	rorg = Ring(id=21,
		category='Ring',
		name='Ring of Royal Grandeur',
		pic='/assets/media/items/legendaries/accessories/rings/ring_of_royal_grandeur.png',
		unique='Reduces the number of items needed for set bonuses by <span class="silver">1</span> (to a minimum of <span class="silver">2</span>).',
		unique_is_primary=False,
		random_primaries='1',
		random_secondaries='1')
	rorg.save()
	rorg.affixes.add(mainStat, ias, lph)

	rogars = Ring(id=22,
		category='Ring',
		name='Rogar\'s Huge Stone',
		pic='/assets/media/items/legendaries/accessories/rings/rogars_huge_stone.png',
		unique='Increase your Life per Second by up to <span>75 - 100%</span> based on your missing Life.',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1')
	rogars.save()
	rogars.affixes.add(mainStat)

	skull = Ring(id=23,
		category='Ring',
		name='Skull Grasp',
		pic='/assets/media/items/legendaries/accessories/rings/skull_grasp.png',
		unique='Increase the damage of Whirlwind by <span>300 - 400%</span> weapon damage.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	skull.save()
	skull.affixes.add(mainStat, chc)

	stolen = Ring(id=24,
		category='Ring',
		name='Stolen Ring',
		pic='/assets/media/items/legendaries/accessories/rings/stolen_ring.png',
		unique='Increases Gold and Health Pickup by <span>1 - 2</span> Yards.',
		unique_is_primary=False,
		random_primaries='3')
	stolen.save()
	stolen.affixes.add(mainStat, extraGold)

	soj = Ring(id=25,
		category='Ring',
		name='Stone of Jordan',
		pic='/assets/media/items/legendaries/accessories/rings/stone_of_jordan.png',
		unique='Skills of {<span>One Element</span>} do <span>15 - 20%</span> more damage',
		unique_is_primary=True,
		unique2='Increases damage against elites by <span>25.0 - 30.0%</span>',
		unique2_is_primary=True,
		unique3='+Max {<span>Class Resource</span>}',
		unique3_is_primary=False,
		random_primaries='1',
		random_secondaries='1',
		notes='???')
	soj.save()
	soj.affixes.add(mainStat)

	short_mans = Ring(id=26,
		category='Ring',
		name='The Short Man\'s Finger',
		pic='/assets/media/items/legendaries/accessories/rings/the_short_mans_finger.png',
		unique='Gargantuan instead summons <span class="silver">3</span> smaller gargantuans each more powerful than before.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	short_mans.save()
	short_mans.affixes.add(mainStat, chd)

	tall_mans = Ring(id=27,
		category='Ring',
		name='The Tall Man\'s Finger',
		pic='/assets/media/items/legendaries/accessories/rings/the_tall_mans_finger.png',
		unique='Zombie Dogs instead summons a single gargantuan dog with more damage and health than all other dogs combined.',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1')
	tall_mans.save()
	tall_mans.affixes.add(mainStat)

	unity = Ring(id=28,
		category='Ring',
		name='Unity',
		pic='/assets/media/items/legendaries/accessories/rings/unity.png',
		unique='Increases damage against elites by <span>12.0 - 15.0%</span>',
		unique_is_primary=True,
		unique2='All damage taken is split between wearers of this item.',
		unique2_is_primary=False,
		random_primaries='1',
		random_secondaries='1')
	unity.save()
	unity.affixes.add(mainStat, chc)

	wyrdward = Ring(id=29,
		category='Ring',
		name='Wyrdward',
		pic='/assets/media/items/legendaries/accessories/rings/wyrdward.png',
		unique='Lightning damage has a <span>25 - 35%</span> chance to Stun for <span class="silver">1.5</span> seconds.',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1')
	wyrdward.save()
	wyrdward.affixes.add(mainStat)


	for ring in Ring.objects.all():
		ring.slug = slugify(ring.name)
		ring.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0002_amulets'),
    ]

    operations = [
    	migrations.RunPython(load_rings)
    ]
