# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_amulets(apps, schema_editor):
	Amulet = apps.get_model("legendaries", "Amulet")
	Affix = apps.get_model("affixes", "AmuletAffix")

	mainStat = Affix.objects.get(affix='mainStat')
	vita = Affix.objects.get(affix='vita')
	eleDmg = Affix.objects.get(affix='eleDmg')
	ias = Affix.objects.get(affix='ias')
	chc = Affix.objects.get(affix='chc')
	chd = Affix.objects.get(affix='chd')
	cdr = Affix.objects.get(affix='cdr')
	allRes = Affix.objects.get(affix='allRes')
	sockets = Affix.objects.get(affix='sockets')

	itemHealing = Affix.objects.get(affix='itemHealing')
	extraGold = Affix.objects.get(affix='extraGold')

	eyeReducedRangedDmg = Affix.objects.get(affix='eyeReducedRangedDmg')
	holySpiritRegen = Affix.objects.get(affix='holySpiritRegen')
	kymbosExtraGold = Affix.objects.get(affix='kymbosExtraGold')
	moonlightArcaneDmg = Affix.objects.get(affix='moonlightArcaneDmg')
	rondalsItemPickup = Affix.objects.get(affix='rondalsItemPickup')
	flavorMovementSpeed = Affix.objects.get(affix='flavorMovementSpeed')


	ancestors = Amulet(name='Ancestors\' Grace',
		pic='/assets/media/items/legendaries/accessories/amulets/ancestors_grace.png',
		unique='When receiving fatal damage, you are instead restored to <span class="silver">100%</span> of maximum Life and resources. This item is destroyed in the process.',
		unique_is_primary=True,
		random_primaries='2',
		random_secondaries='1')
	ancestors.save()
	ancestors.affixes.add(mainStat, vita)

	countess = Amulet(name='Countess Julia\'s Cameo',
		pic='/assets/media/items/legendaries/accessories/amulets/countess_julias_cameo.png',
		unique='Prevent all Arcane damage taken and heal yourself for <span>20 - 25%</span> of the amount prevented.',
		random_primaries='2',
		random_secondaries='1')
	countess.save()
	countess.affixes.add(mainStat, ias)

	dovu = Amulet(name='Dovu Energy Trap',
		pic='/assets/media/items/legendaries/accessories/amulets/dovu_energy_trap.png',
		unique='Increases duration of Stun effects by <span>20 - 25%</span>.',
		random_primaries='2',
		random_secondaries='1')
	dovu.save()
	dovu.affixes.add(mainStat, cdr)

	eye = Amulet(name='Eye of Elitch',
		pic='/assets/media/items/legendaries/accessories/amulets/eye_of_elitch.png',
		random_primaries='3',
		random_secondaries='1')
	eye.save()
	eye.affixes.add(eleDmg,eyeReducedRangedDmg)

	gorget = Amulet(name='Golden Gorget of Leoric',
		pic='/assets/media/items/legendaries/accessories/amulets/golden_gorget_of_leoric.png',
		unique='After earning a massacre bonus, <span>4 - 6</span> Skeletons are summoned to fight by your side for <span class="silver">10</span> seconds.',
		random_primaries='1',
		random_secondaries='1')
	gorget.save()
	gorget.affixes.add(mainStat, chc, allRes)

	halcyon = Amulet(name='Halcyon\'s Ascent',
		pic='/assets/media/items/legendaries/accessories/amulets/halcyons_ascent.png',
		unique='When you use {<span>Class Skill</span>}, you mesmerize nearby enemies with your skill, causing them to jump uncontrollably for <span>6 - 8</span> seconds.',
		random_primaries='2',
		random_secondaries='1',
		notes='Class Skill = Vengeance(DH), Wrath of the Berserker(Barb), Archon(Wiz), Big Bad Voodoo(WD), Epiphany(Monk), Akarat\'s Champion(Crusader)')
	halcyon.save()
	halcyon.affixes.add(mainStat, cdr)

	haunt = Amulet(name='Haunt of Vaxo',
		pic='/assets/media/items/legendaries/accessories/amulets/haunt_of_vaxo.png',
		unique='Summons shadow clones to your aid when you Stun an enemy. This effect may occur once every <span class="silver">30</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	haunt.save()
	haunt.affixes.add(mainStat, chc)

	hellfire = Amulet(name='Hellfire Amulet',
		pic='/assets/media/items/legendaries/accessories/amulets/hellfire_amulet.png',
		unique='Gain a {<span>Class Specific</span>} passive.',
		random_primaries='2',
		random_secondaries='1')
	hellfire.save()
	hellfire.affixes.add(mainStat, sockets)

	holy = Amulet(name='Holy Beacon',
		pic='/assets/media/items/legendaries/accessories/amulets/holy_beacon.png',
		unique='<span>+2.2 - 3.0</span> Spirit Regeneration per Second',
		unique_is_primary=True,
		random_primaries='1',
		random_secondaries='2')
	holy.save()
	holy.affixes.add(mainStat, holyDmg, holySpiritRegen)

	kymbos = Amulet(name='Kymbo\'s Gold',
		pic='/assets/media/items/legendaries/accessories/amulets/kymbos_gold.png',
		unique='Picking up gold heals you for an amount equal to the gold that was picked up.',
		random_primaries='3')
	kymbos.save()
	kymbos.affixes.add(kymbosExtraGold)

	maras = Amulet(name='Mara\'s Kaleidoscope',
		pic='/assets/media/items/legendaries/accessories/amulets/maras_kaleidoscope.png',
		unique='Prevent all Poison damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		random_primaries='2',
		random_secondaries='1')
	maras.save()
	maras.affixes.add(mainStat, chc)

	moonlight = Amulet(name='Moonlight Ward',
		pic='/assets/media/items/legendaries/accessories/amulets/moonlight_ward.png',
		unique='Enemies hit within <span class="silver">15</span> yards have a chance to spawn Arcane shards that explode and deal <span>240 - 320%</span> Arcane damage to enemies within <span class="silver">15</span> yards.',
		random_primaries='2',
		random_secondaries='1')
	moonlight.save()
	moonlight.affixes.add(chc, moonlightArcaneDmg)

	ouroboros = Amulet(name='Ouroboros',
		pic='/assets/media/items/legendaries/accessories/amulets/ouroboros.png',
		random_primaries='2',
		random_secondaries='2')
	ouroboros.save()
	ouroboros.affixes.add(mainStat, chc)

	overwhelming = Amulet(name='Overwhelming Desire',
		pic='/assets/media/items/legendaries/accessories/amulets/overwhelming_desire.png',
		unique='Chance on hit to charm the enemy. While charmed, the enemy takes <span class="silver">35%</span> more damage.',
		random_primaries='2',
		random_secondaries='1')
	overwhelming.save()
	overwhelming.affixes.add(mainStat, cdr)

	rakoffs = Amulet(name='Rakoff\'s Glass of Life',
		pic='/assets/media/items/legendaries/accessories/amulets/rakoffs_glass_of_life.png',
		unique='Enemies you kill have a <span>3 - 4%</span> additional chance to drop a health globe.',
		random_primaries='2',
		random_secondaries='1')
	rakoffs.save()
	rakoffs.affixes.add(mainStat, itemHealing)

	rondals = Amulet(name='Rondal\'s Locket',
		pic='/assets/media/items/legendaries/accessories/amulets/rondals_locket.png',
		random_primaries='3')
	rondals.save()
	rondals.affixes.add(mainStat, itemHealing, rondalsItemPickup)

	squirts = Amulet(name='Squirt\'s Necklace',
		pic='/assets/media/items/legendaries/accessories/amulets/squirts_necklace.png',
		random_primaries='2',
		random_secondaries='1')
	squirts.save()
	squirts.affixes.add(mainStat, chd, extraGold)

	talisman = Amulet(name='Talisman of Aranoch',
		pic='/assets/media/items/legendaries/accessories/amulets/talisman_of_aranoch.png',
		unique='Prevent all Cold damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		random_primaries='3',
		random_secondaries='1')
	talisman.save()
	talisman.affixes.add(mainStat)

	ess = Amulet(name='The Ess of Johan',
		pic='/assets/media/items/legendaries/accessories/amulets/the_ess_of_johan.png',
		unique='Chance on hit to pull in enemies toward your target and Slow them by <span>60 - 80%</span>.',
		random_primaries='2',
		random_secondaries='1')
	ess.save()
	ess.affixes.add(mainStat, cdr)

	flavor = Amulet(name='The Flavor of Time',
		pic='/assets/media/items/legendaries/accessories/amulets/the_flavor_of_time.png',
		random_primaries='3',
		random_secondaries='1')
	flavor.save()
	flavor.affixes.add(cdr, flavorMovementSpeed)

	star = Amulet(name='The Star of Azkaranth',
		pic='/assets/media/items/legendaries/accessories/amulets/the_star_of_azkaranth.png',
		unique='Prevent all Fire damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		random_primaries='2',
		random_secondaries='1')
	star.save()
	star.affixes.add(mainStat, cdr)

	xephirian = Amulet(name='Xephirian Amulet',
		pic='/assets/media/items/legendaries/accessories/amulets/xephirian_amulet.png',
		unique='Prevent all Lightning damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		random_primaries='2',
		random_secondaries='1')
	xephirian.save()
	xephirian.affixes.add(mainStat, ias)


	for amulet in Amulet.objects.all():
		amulet.slug = slugify(amulet.name)
		amulet.category = 'Amulet'
		amulet.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(load_amulets),
    ]