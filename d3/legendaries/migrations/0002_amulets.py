# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_amulets(apps, schema_editor):
	Amulet = apps.get_model("legendaries", "Amulet")
	Affix = apps.get_model("affixes", "AmuletAffix")

	sockets = Affix.objects.get(affix='sockets')

	dmg = Affix.objects.get(affix='dmg')
	mainStat = Affix.objects.get(affix='mainStat')
	dext = Affix.objects.get(affix='dext')
	inte = Affix.objects.get(affix='inte')
	stre = Affix.objects.get(affix='stre')
	vita = Affix.objects.get(affix='vita')

	eleDmg = Affix.objects.get(affix='eleDmg')
	physDmg = Affix.objects.get(affix='physDmg')
	coldDmg = Affix.objects.get(affix='coldDmg')
	fireDmg = Affix.objects.get(affix='fireDmg')
	lightDmg = Affix.objects.get(affix='lightDmg')
	poisDmg = Affix.objects.get(affix='poisDmg')
	arcaneDmg = Affix.objects.get(affix='arcaneDmg')
	holyDmg = Affix.objects.get(affix='holyDmg')

	armor = Affix.objects.get(affix='armor')
	allRes = Affix.objects.get(affix='allRes')
	life = Affix.objects.get(affix='life')
	lps = Affix.objects.get(affix='lps')
	lph = Affix.objects.get(affix='lph')

	ias = Affix.objects.get(affix='ias')
	chc = Affix.objects.get(affix='chc')
	chd = Affix.objects.get(affix='chd')
	cdr = Affix.objects.get(affix='cdr')

	rcr = Affix.objects.get(affix='rcr')


	eleRes = Affix.objects.get(affix='eleRes')
	physRes = Affix.objects.get(affix='physRes')
	coldRes = Affix.objects.get(affix='coldRes')
	fireRes = Affix.objects.get(affix='fireRes')
	lightRes = Affix.objects.get(affix='lightRes')
	poisRes = Affix.objects.get(affix='poisRes')
	arcaneRes = Affix.objects.get(affix='arcaneRes')

	reducedRangeDmg = Affix.objects.get(affix='reducedRangeDmg')
	reducedMeleeDmg = Affix.objects.get(affix='reducedMeleeDmg')
	ccReduction = Affix.objects.get(affix='ccReduction')

	lpk = Affix.objects.get(affix='lpk')
	itemHealing = Affix.objects.get(affix='itemHealing')

	blindChance = Affix.objects.get(affix='blindChance')

	extraGold = Affix.objects.get(affix='extraGold')
	thorns = Affix.objects.get(affix='thorns')
	killExp = Affix.objects.get(affix='killExp')


	ancestors = Amulet(id=0,
		name='Ancestors\' Grace',
		pic='/assets/media/items/legendaries/accessories/amulets/ancestors_grace.png',
		unique='When receiving fatal damage, you are instead restored to <span class="silver">100%</span> of maximum Life and resources. This item is destroyed in the process.',
		unique_is_primary=True,
		random_primaries='2',
		random_secondaries='1',)
	ancestors.save()
	ancestors.affixes.add(mainStat, vita)

	countess = Amulet(id=1,
		name='Countess Julia\'s Cameo',
		pic='/assets/media/items/legendaries/accessories/amulets/countess_julias_cameo.png',
		unique='Prevent all Arcane damage taken and heal yourself for <span>20 - 25%</span> of the amount prevented.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	countess.save()
	countess.affixes.add(mainStat, ias)

	dovu = Amulet(id=2,
		name='Dovu Energy Trap',
		pic='/assets/media/items/legendaries/accessories/amulets/dovu_energy_trap.png',
		unique='Increases duration of Stun effects by <span>20 - 25%</span>.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	dovu.save()
	dovu.affixes.add(mainStat, cdr)

	eye = Amulet(id=3,
		name='Eye of Elitch',
		pic='/assets/media/items/legendaries/accessories/amulets/eye_of_elitch.png',
		unique='Reduces damage from ranged attacks by <span>27.7 - 32.9%</span>.',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1')
	eye.save()
	eye.affixes.add(eleDmg)

	gorget = Amulet(id=4,
		name='Golden Gorget of Leoric',
		pic='/assets/media/items/legendaries/accessories/amulets/golden_gorget_of_leoric.png',
		unique='After earning a massacre bonus, <span>4 - 6</span> Skeletons are summoned to fight by your side for <span class="silver>10</span> seconds.',
		unique_is_primary=False,
		random_primaries='1',
		random_secondaries='1')
	gorget.save()
	gorget.affixes.add(mainStat, allRes, chc)

	halcyon = Amulet(id=5,
		name='Halcyon\'s Ascent',
		pic='/assets/media/items/legendaries/accessories/amulets/halcyons_ascent.png',
		unique='When you use {<span>Class Skill</span>}, you mesmerize nearby enemies with your skill, causing them to jump uncontrollably for <span>6 - 8</span> seconds.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1',
		notes='Class Skill = Vengeance(DH), Wrath of the Berserker(Barb), Archon(Wiz), Big Bad Voodoo(WD), Epiphany(Monk), Akarat\'s Champion(Crusader)')
	halcyon.save()
	halcyon.affixes.add(mainStat, cdr)

	haunt = Amulet(id=6,
		name='Haunt of Vaxo',
		pic='/assets/media/items/legendaries/accessories/amulets/haunt_of_vaxo.png',
		unique='Summons shadow clones to your aid when you Stun an enemy. This effect may occur once every <span class="silver">30</span> seconds.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	haunt.save()
	haunt.affixes.add(mainStat, chc)

	hellfire = Amulet(id=7,
		name='Hellfire Amulet',
		pic='/assets/media/items/legendaries/accessories/amulets/hellfire_amulet.png',
		unique='Gain a {<span>Class Specific</span>} passive.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	hellfire.save()
	hellfire.affixes.add(mainStat, sockets)

	holy = Amulet(id=8,
		name='Holy Beacon',
		pic='/assets/media/items/legendaries/accessories/amulets/holy_beacon.png',
		unique='<span>+2.2 - 3.0</span> Spirit Regeneration per Second',
		unique_is_primary=True,
		random_primaries='1',
		random_secondaries='2')
	holy.save()
	holy.affixes.add(mainStat, holyDmg)

	kymbos = Amulet(id=9,
		name='Kymbo\'s Gold',
		pic='/assets/media/items/legendaries/accessories/amulets/kymbos_gold.png',
		unique='<span>+75 - 100%</span> Extra Gold from Monsters',
		unique_is_primary=False,
		unique2='Picking up gold heals you for an amount equal to the gold that was picked up.',
		unique2_is_primary=False,
		random_primaries='3')
	kymbos.save()
	# kymbos.affixes.add()

	maras = Amulet(id=10,
		name='Mara\'s Kaleidoscope',
		pic='/assets/media/items/legendaries/accessories/amulets/maras_kaleidoscope.png',
		unique='Prevent all Poison damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	maras.save()
	maras.affixes.add(mainStat, chc)

	moonlight = Amulet(id=11,
		name='Moonlight Ward',
		pic='/assets/media/items/legendaries/accessories/amulets/moonlight_ward.png',
		unique='Arcane skills do <span>+20 - 25%</span> more damage.',
		unique_is_primary=True,
		unique2='Enemies hit within <span class="silver">15</span> yards have a chance to spawn Arcane shards that explode and deal <span>240 - 320%</span> Arcane damage to enemies within <span class="silver">15</span> yards.',
		unique2_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	moonlight.save()
	moonlight.affixes.add(chc)

	ouroboros = Amulet(id=12,
		name='Ouroboros',
		pic='/assets/media/items/legendaries/accessories/amulets/ouroboros.png',
		random_primaries='2',
		random_secondaries='2')
	ouroboros.save()
	ouroboros.affixes.add(mainStat, chc)

	overwhelming = Amulet(id=13,
		name='Overwhelming Desire',
		pic='/assets/media/items/legendaries/accessories/amulets/overwhelming_desire.png',
		unique='Chance on hit to charm the enemy. While charmed, the enemy takes <span class="silver">35%</span> more damage.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	overwhelming.save()
	overwhelming.affixes.add(mainStat, cdr)

	rakoffs = Amulet(id=14,
		name='Rakoff\'s Glass of Life',
		pic='/assets/media/items/legendaries/accessories/amulets/rakoffs_glass_of_life.png',
		unique='Enemies you kill have a <span>3 - 4%</span> additional chance to drop a health globe.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	rakoffs.save()
	rakoffs.affixes.add(mainStat, itemHealing)

	rondals = Amulet(id=15,
		name='Rondal\'s Locket',
		pic='/assets/media/items/legendaries/accessories/amulets/rondals_locket.png',
		unique='<span>+4 - 6</span> Yards to Gold and Health Pickup',
		unique_is_primary=False,
		random_primaries='3')
	rondals.save()
	rondals.affixes.add(mainStat, itemHealing)

	squirts = Amulet(id=16,
		name='Squirt\'s Necklace',
		pic='/assets/media/items/legendaries/accessories/amulets/squirts_necklace.png',
		random_primaries='2',
		random_secondaries='1')
	squirts.save()
	squirts.affixes.add(mainStat, chd, extraGold)

	talisman = Amulet(id=17,
		name='Talisman of Aranoch',
		pic='/assets/media/items/legendaries/accessories/amulets/talisman_of_aranoch.png',
		unique='Prevent all Cold damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		unique_is_primary=False,
		random_primaries='3',
		random_secondaries='1')
	talisman.save()
	talisman.affixes.add(mainStat)

	ess = Amulet(id=18,
		name='The Ess of Johan',
		pic='/assets/media/items/legendaries/accessories/amulets/the_ess_of_johan.png',
		unique='Chance on hit to pull in enemies toward your target and Slow them by <span>60 - 80%</span>.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	ess.save()
	ess.affixes.add(mainStat, cdr)

	flavor = Amulet(id=19,
		name='The Flavor of Time',
		pic='/assets/media/items/legendaries/accessories/amulets/the_flavor_of_time.png',
		unique='<span>+10 - 12%</span> Movement Speed',
		unique_is_primary=True,
		random_primaries='3',
		random_secondaries='1')
	flavor.save()
	flavor.affixes.add(cdr)

	star = Amulet(id=20,
		name='The Star of Azkaranth',
		pic='/assets/media/items/legendaries/accessories/amulets/the_star_of_azkaranth.png',
		unique='Prevent all Fire damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	star.save()
	star.affixes.add(mainStat, cdr)

	xephirian = Amulet(id=21,
		name='Xephirian Amulet',
		pic='/assets/media/items/legendaries/accessories/amulets/xephirian_amulet.png',
		unique='Prevent all Lightning damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		unique_is_primary=False,
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