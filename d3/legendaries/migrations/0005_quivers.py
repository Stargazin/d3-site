# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_quivers(apps, schema_editor):
	Quiver = apps.get_model("legendaries", "Quiver")
	Affix = apps.get_model("affixes", "QuiverAffix")

	sockets = Affix.objects.get(affix='sockets')

	dext = Affix.objects.get(affix='dext')
	vita = Affix.objects.get(affix='vita')

	life = Affix.objects.get(affix='life')
	lps = Affix.objects.get(affix='lps')

	ias = Affix.objects.get(affix='ias')
	chc = Affix.objects.get(affix='chc')
	cdr = Affix.objects.get(affix='cdr')
	eliteDmg = Affix.objects.get(affix='eliteDmg')
	areaDmg = Affix.objects.get(affix='areaDmg')
	bleedChance = Affix.objects.get(affix='bleedChance')

	rcr = Affix.objects.get(affix='rcr')
	hatredRegen = Affix.objects.get(affix='hatredRegen')

	bolas = Affix.objects.get(affix='bolas')
	chakram = Affix.objects.get(affix='chakram')
	clusterArrow = Affix.objects.get(affix='clusterArrow')
	companion = Affix.objects.get(affix='companion')
	elementalArrow = Affix.objects.get(affix='elementalArrow')
	entanglingShot = Affix.objects.get(affix='entanglingShot')
	evasiveFire = Affix.objects.get(affix='evasiveFire')
	fanOfKnives = Affix.objects.get(affix='fanOfKnives')
	grenade = Affix.objects.get(affix='grenade')
	hungeringArrow = Affix.objects.get(affix='hungeringArrow')
	impale = Affix.objects.get(affix='impale')
	multishot = Affix.objects.get(affix='multishot')
	rainOfVengeance = Affix.objects.get(affix='rainOfVengeance')
	rapidFire = Affix.objects.get(affix='rapidFire')
	sentry = Affix.objects.get(affix='sentry')
	spikeTrap = Affix.objects.get(affix='spikeTrap')
	strafe = Affix.objects.get(affix='strafe')


	maxDisc = Affix.objects.get(affix='maxDisc')

	itemHealing = Affix.objects.get(affix='itemHealing')

	fearChance = Affix.objects.get(affix='fearChance')
	stunChance = Affix.objects.get(affix='stunChance')
	blindChance = Affix.objects.get(affix='blindChance')
	freezeChance = Affix.objects.get(affix='freezeChance')
	chillChance = Affix.objects.get(affix='chillChance')
	slowChance = Affix.objects.get(affix='slowChance')
	immobilizeChance = Affix.objects.get(affix='immobilizeChance')
	knockbackChance = Affix.objects.get(affix='knockbackChance')

	extraGold = Affix.objects.get(affix='extraGold')
	thorns = Affix.objects.get(affix='thorns')
	killExp = Affix.objects.get(affix='killExp')
	lvlReq = Affix.objects.get(affix='lvlReq')
	durability = Affix.objects.get(affix='durability')


	holyEleDmg = Affix.objects.get(affix='holyEleDmg')


	archfiendArrows = Quiver(name='Archfiend Arrows',
		pic='/assets/media/items/legendaries/offhands/quivers/archfiend_arrows.png',
		random_primaries='2',
		random_secondaries='2')
	archfiendArrows.save()
	archfiendArrows.affixes.add(ias, chc, eliteDmg)

	bombadiersRucksack = Quiver(name='Bombadier\'s Rucksack',
		pic='/assets/media/items/legendaries/offhands/quivers/bombardiers_rucksack.png',
		unique='You may have <span class="silver">2</span> additional Sentries.',
		random_primaries='2',
		random_secondaries='1')
	bombadiersRucksack.save()
	bombadiersRucksack.affixes.add(dext, ias, chc)

	deadMansLegacy = Quiver(name='DeadMan\'s Legacy',
		pic='/assets/media/items/legendaries/offhands/quivers/dead_mans_legacy.png',
		unique='Multishot hits enemies below <span>50 - 60%</span> health twice.',
		random_primaries='2',
		random_secondaries='1')
	deadMansLegacy.save()
	deadMansLegacy.affixes.add(dext, ias, chc)

	emimeisDuffel = Quiver(name='Emimei\'s Duffel',
		pic='/assets/media/items/legendaries/offhands/quivers/emimeis_duffel.png',
		unique='Bolas now explode instantly.',
		random_primaries='3',
		random_secondaries='1')
	emimeisDuffel.save()
	emimeisDuffel.affixes.add(dext, ias)

	fletchersPride = Quiver(name='Fletcher\'s Pride',
		pic='/assets/media/items/legendaries/offhands/quivers/fletchers_pride.png',
		random_primaries='2',
		random_secondaries='2')
	fletchersPride.save()
	fletchersPride.affixes.add(dext, ias, rcr)

	holyPointShot = Quiver(name='Holy Point Shot',
		pic='/assets/media/items/legendaries/offhands/quivers/holy_point_shot.png',
		random_primaries='2',
		random_secondaries='2')
	holyPointShot.save()
	holyPointShot.affixes.add(dext, ias, holyEleDmg)

	meticulousBolts = Quiver(name='Meticulous Bolts',
		pic='/assets/media/items/legendaries/offhands/quivers/meticulous_bolts.png',
		unique='Elemental Arrow - Ball Lightning now travels at <span>30 - 40%</span> speed.',
		random_primaries='3',
		random_secondaries='1')
	meticulousBolts.save()
	meticulousBolts.affixes.add(dext, ias)

	sinSeekers = Quiver(name='Sin Seekers',
		pic='/assets/media/items/legendaries/offhands/quivers/sin_seekers.png',
		random_primaries='2',
		random_secondaries='2')
	sinSeekers.save()
	sinSeekers.affixes.add(dext, ias, chc)

	spinesOfSeethingHatred = Quiver(name='Spines of Seeth ingHatred',
		pic='/assets/media/items/legendaries/offhands/quivers/spines_of_seething_hatred.png',
		unique='Chakram now generates <span>3 - 4</span> Hatred.',
		random_primaries='3',
		random_secondaries='1')
	spinesOfSeethingHatred.save()
	spinesOfSeethingHatred.affixes.add(dext, ias)

	theNinthCirriSatchel = Quiver(name='The Ninth Cirri Satchel',
		pic='/assets/media/items/legendaries/offhands/quivers/the_ninth_cirri_satchel.png',
		unique='Hungering Arrow has <span>20 - 25%</span> additional chance to pierce.',
		random_primaries='3',
		random_secondaries='1')
	theNinthCirriSatchel.save()
	theNinthCirriSatchel.affixes.add(dext, ias)


	for quiver in Quiver.objects.all():
		quiver.slug = slugify(quiver.name)
		quiver.category = 'Quiver'
		quiver.save()

class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0004_sources'),
    ]

    operations = [
    	migrations.RunPython(load_quivers)
    ]
