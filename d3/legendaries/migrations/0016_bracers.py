# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_bracers(apps, schema_editor):
	Bracers = apps.get_model("legendaries", "Bracers")
	Affix = apps.get_model("affixes", "BracersAffix")


	mainStat = Affix.objects.get(affix='mainStat')
	vita = Affix.objects.get(affix='vita')
	eleDmg = Affix.objects.get(affix='eleDmg')
	chc = Affix.objects.get(affix='chc')
	lps = Affix.objects.get(affix='lps')

	itemPickup = Affix.objects.get(affix='itemPickup')
	extraGold = Affix.objects.get(affix='extraGold')
	thorns = Affix.objects.get(affix='thorns')

	lacuniIAS = Affix.objects.get(affix='lacuniIAS')
	lacuniMovementSpeed = Affix.objects.get(affix='lacuniMovementSpeed')
	slaveMovementSpeed = Affix.objects.get(affix='slaveMovementSpeed')
	slaveLPK = Affix.objects.get(affix='slaveLPK')
	steadyIAS = Affix.objects.get(affix='steadyIAS')


	ancientParthanDefenders = Bracers(name='Ancient Parthan Defenders',
		pic='/assets/media/items/legendaries/armor/wrists/ancient_parthan_defenders.png',
		unique='Each stunned enemy within <span class="silver">25</span> yards reduces your damage taken by <span>9 - 12%</span>.',
		random_primaries='3',
		random_secondaries='1')
	ancientParthanDefenders.save()
	ancientParthanDefenders.affixes.add(mainStat)

	bracersOfDestruction = Bracers(name='Bracers of Destruction',
		pic='/assets/media/items/legendaries/armor/wrists/bracers_of_destruction.png',
		unique='Seismic Slam deals <span>300 - 400%</span> increased damage to the first <span class="silver">5</span> enemies it hits.',
		random_primaries='2',
		random_secondaries='1')
	bracersOfDestruction.save()
	bracersOfDestruction.affixes.add(mainStat)

	bracersOfTheFirstMen = Bracers(name='Bracers of the FirstMen',
		pic='/assets/media/items/legendaries/armor/wrists/bracers_of_the_first_men.png',
		unique='Hammer of the Ancients attacks <span class="silver">50%</span> faster and deals <span>150 - 200%</span> increased damage.',
		random_primaries='2',
		random_secondaries='1')
	bracersOfTheFirstMen.save()
	bracersOfTheFirstMen.affixes.add(mainStat, chc)

	coilsOfTheFirstSpider = Bracers(name='Coils of the First Spider',
		pic='/assets/media/items/legendaries/armor/wrists/coils_of_the_first_spider.png',
		unique='While channeling Firebats, you take <span class="silver">30%</span> reduced damage and gain <span>60,000 - 80,000</span> Life per Hit.',
		random_primaries='2')
	coilsOfTheFirstSpider.save()
	coilsOfTheFirstSpider.affixes.add(mainStat, chc, lps)

	custerianWristguards = Bracers(name='Custerian Wristguards',
		pic='/assets/media/items/legendaries/armor/wrists/custerian_wristguards.png',
		unique='Picking up gold grants experience.',
		random_primaries='3',
		random_secondaries='')
	custerianWristguards.save()
	custerianWristguards.affixes.add(chc, extraGold)

	drakonsLesson = Bracers(name='Drakon\'s Lesson',
		pic='/assets/media/items/legendaries/armor/wrists/drakons_lesson.png',
		unique='When your Shield Bash hits <span class="silver">3</span> or fewer enemies, its damage is increased by <span>150 - 200%</span> and <span class="silver">25%</span> of its Wrath Cost is refunded.',
		random_primaries='2',
		random_secondaries='1')
	drakonsLesson.save()
	drakonsLesson.affixes.add(mainStat, chc)

	gabrielsVambraces = Bracers(name='Gabriel\'s Vambraces',
		pic='/assets/media/items/legendaries/armor/wrists/gabriels_vambraces.png',
		unique='When your Blessed Hammer hits <span class="silver">3</span> or fewer enemies, <span>75 - 100%</span> of its Wrath Cost is refunded.',
		random_primaries='2',
		random_secondaries='1')
	gabrielsVambraces.save()
	gabrielsVambraces.affixes.add(mainStat, chc)

	gungdoGear = Bracers(name='Gungdo Gear',
		pic='/assets/media/items/legendaries/armor/wrists/gungdo_gear.png',
		unique='Exploding Palm\'s on-death explosion applies Exploding Palm.',
		random_primaries='2',
		random_secondaries='1')
	gungdoGear.save()
	gungdoGear.affixes.add(mainStat, eleDmg)

	jeramsBracers = Bracers(name='Jeram\'s Bracers',
		pic='/assets/media/items/legendaries/armor/wrists/jerams_bracers.png',
		unique='Wall of Death deals <span>75 - 100%</span> increased damage and can be cast up to three times within <span class="silver">2</span> seconds before the cooldown begins.',
		random_primaries='2',
		random_secondaries='1')
	jeramsBracers.save()
	jeramsBracers.affixes.add(mainStat, chc)

	kethryesSplint = Bracers(name='Kethrye\'s Splint',
		pic='/assets/media/items/legendaries/armor/wrists/kethryes_splint.png',
		random_primaries='4',
		random_secondaries='2')
	kethryesSplint.save()
	# kethryesSplint.affixes.add()

	lacuniProwlers = Bracers(name='Lacuni Prowlers',
		pic='/assets/media/items/legendaries/armor/wrists/lacuni_prowlers.png',
		random_primaries='2',
		random_secondaries='1')
	lacuniProwlers.save()
	lacuniProwlers.affixes.add(lacuniIAS, lacuniMovementSpeed, thorns)

	nemesisBracers = Bracers(name='Nemesis Bracers',
		pic='/assets/media/items/legendaries/armor/wrists/nemesis_bracers.png',
		unique='Shrines and Pylons will spawn an enemy champion.',
		random_primaries='3',
		random_secondaries='1')
	nemesisBracers.save()
	nemesisBracers.affixes.add(mainStat)

	promiseOfGlory = Bracers(name='Promise of Glory',
		pic='/assets/media/items/legendaries/armor/wrists/promise_of_glory.png',
		unique='<span>4 - 6%</span> chance to spawn a Nephalem Glory globe when you Blind an enemy.',
		random_primaries='2',
		random_secondaries='1')
	promiseOfGlory.save()
	promiseOfGlory.affixes.add(mainStat, chc)

	ranslorsFolly = Bracers(name='Ranslor\'s Folly',
		pic='/assets/media/items/legendaries/armor/wrists/ranslors_folly.png',
		unique='Energy Twister periodically pulls in lesser enemies within <span class="silver">30</span> yards.',
		random_primaries='2',
		random_secondaries='1')
	ranslorsFolly.save()
	ranslorsFolly.affixes.add(mainStat, chc)

	reapersWraps = Bracers(name='Reaper\'s Wraps',
		pic='/assets/media/items/legendaries/armor/wrists/reapers_wraps.png',
		unique='Health globes restore <span>25 - 30%</span> of your primary resource.',
		random_primaries='4',
		random_secondaries='2',
		notes='crafted')
	reapersWraps.save()
	# reapersWraps.affixes.add()

	sanguinaryVambraces = Bracers(name='Sanguinary Vambraces',
		pic='/assets/media/items/legendaries/armor/wrists/sanguinary_vambraces.png',
		unique='Chance on being hit to deal <span class="silver">1000%</span> of your Thorns damage to nearby enemies.',
		random_primaries='2')
	sanguinaryVambraces.save()
	sanguinaryVambraces.affixes.add(mainStat, chc, thorns)

	slaveBonds = Bracers(name='slaveBonds',
		pic='/assets/media/items/legendaries/armor/wrists/slave_bonds.png',
		random_primaries='2',
		random_secondaries='1')
	slaveBonds.save()
	slaveBonds.affixes.add(mainStat, slaveMovementSpeed, slaveLPK)

	spiritGuards = Bracers(name='spiritGuards',
		pic='/assets/media/items/legendaries/armor/wrists/spirit_guards.png',
		unique='Your Spirit Generators reduce your damage taken by <span>30 - 40%</span> for <span class="silver">3</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	spiritGuards.save()
	spiritGuards.affixes.add(mainStat, chc)

	steadyStrikers = Bracers(name='steadyStrikers',
		pic='/assets/media/items/legendaries/armor/wrists/steady_strikers.png',
		random_primaries='2',
		random_secondaries='2')
	steadyStrikers.save()
	steadyStrikers.affixes.add(mainStat, steadyIAS)

	strongarmBracers = Bracers(name='Strongarm Bracers',
		pic='/assets/media/items/legendaries/armor/wrists/strongarm_bracers.png',
		unique='Enemies hit by knockbacks suffer <span>20 - 30%</span> more damage for <span class="silver">5</span> seconds when they land.',
		random_primaries='1',
		random_secondaries='1')
	strongarmBracers.save()
	strongarmBracers.affixes.add(mainStat, vita, chc)

	trangoulCoils = Bracers(name='Trangoul Coils',
		pic='/assets/media/items/legendaries/armor/wrists/trangoul_coils.png',
		unique='Healing wells replenish all resources and reduce all cooldowns by <span>45 - 60</span> seconds.',
		random_primaries='3',
		random_secondaries='1')
	trangoulCoils.save()
	trangoulCoils.affixes.add(mainStat)

	warzechianArmguards = Bracers(name='Warzechian Armguards',
		pic='/assets/media/items/legendaries/armor/wrists/warzechian_armguards.png',
		unique='Every time you destroy a wreckable object, you gain a short burst of speed.',
		random_primaries='2')
	warzechianArmguards.save()
	warzechianArmguards.affixes.add(mainStat, chc, itemPickup)

	wrapsOfClarity = Bracers(name='Wraps of Clarity',
		pic='/assets/media/items/legendaries/armor/wrists/wraps_of_clarity.png',
		unique='Your Hatred Generators reduce your damage taken by <span>30 - 35%</span> for <span class="silver">5</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	wrapsOfClarity.save()
	wrapsOfClarity.affixes.add(mainStat, chc)


	for bracers in Bracers.objects.all():
		bracers.slug = slugify(bracers.name)
		bracers.category = 'Bracers'
		bracers.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0015_cloaks'),
    ]

    operations = [
    	migrations.RunPython(load_bracers)
    ]
