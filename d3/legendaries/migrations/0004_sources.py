# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_sources(apps, schema_editor):
	Source = apps.get_model("legendaries", "Source")
	Affix = apps.get_model("affixes", "SourceAffix")

	sockets = Affix.objects.get(affix='sockets')

	dmg = Affix.objects.get(affix='dmg')
	inte = Affix.objects.get(affix='inte')
	vita = Affix.objects.get(affix='vita')

	life = Affix.objects.get(affix='life')
	lps = Affix.objects.get(affix='lps')

	chc = Affix.objects.get(affix='chc')
	cdr = Affix.objects.get(affix='cdr')
	eliteDmg = Affix.objects.get(affix='eliteDmg')
	areaDmg = Affix.objects.get(affix='areaDmg')
	bleedChance = Affix.objects.get(affix='bleedChance')

	rcr = Affix.objects.get(affix='rcr')
	apCrit = Affix.objects.get(affix='apCrit')

	arcaneOrb = Affix.objects.get(affix='arcaneOrb')
	arcaneTorrent = Affix.objects.get(affix='arcaneTorrent')
	blackHole = Affix.objects.get(affix='blackHole')
	blizzard = Affix.objects.get(affix='blizzard')
	disintegrate = Affix.objects.get(affix='disintegrate')
	electrocute = Affix.objects.get(affix='electrocute')
	energyTwister = Affix.objects.get(affix='energyTwister')
	explosiveBlast = Affix.objects.get(affix='explosiveBlast')
	familiar = Affix.objects.get(affix='familiar')
	hydra = Affix.objects.get(affix='hydra')
	magicMissle = Affix.objects.get(affix='magicMissle')
	meteor = Affix.objects.get(affix='meteor')
	rayOfFrost = Affix.objects.get(affix='rayOfFrost')
	shockPulse = Affix.objects.get(affix='shockPulse')
	spectralBlade = Affix.objects.get(affix='spectralBlade')
	waveOfForce = Affix.objects.get(affix='waveOfForce')


	maxAP = Affix.objects.get(affix='maxAP')

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


	winterColdDmg = Affix.objects.get(affix='winterColdDmg')


	cosmicStrand = Source(id=0,
		name='Cosmic Strand',
		pic='/assets/media/items/legendaries/offhands/sources/cosmic_strand.png',
		unique='Teleport gains the effect of the Wormhole rune.',
		# unique_is_primary=False,
		random_primaries='4',
		random_secondaries='1',
		notes='crafted')
	cosmicStrand.save()
	cosmicStrand.affixes.add(dmg)

	lightOfGrace = Source(id=1,
		name='Light of Grace',
		pic='/assets/media/items/legendaries/offhands/sources/light_of_grace.png',
		unique='Ray of Frost now pierces.',
		# unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	lightOfGrace.save()
	lightOfGrace.affixes.add(dmg, inte, chc)

	mirrorball = Source(id=2,
		name='Mirrorball',
		pic='/assets/media/items/legendaries/offhands/sources/mirrorball.png',
		unique='Magic Missile fires <span>1 - 2</span> extra missiles.',
		# unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	mirrorball.save()
	mirrorball.affixes.add(dmg, inte, chc)

	mykensBallOfHate = Source(id=3,
		name='Myken\'s Ball of Hate',
		pic='/assets/media/items/legendaries/offhands/sources/mykens_ball_of_hate.png',
		unique='Electrocute can chain to enemies that have already been hit.',
		# unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	mykensBallOfHate.save()
	mykensBallOfHate.affixes.add(dmg, inte, chc)

	theOculus = Source(id=4,
		name='The Oculus',
		pic='/assets/media/items/legendaries/offhands/sources/the_oculus.png',
		unique='Taking damage has up to a <span>15 - 20%</span> chance to reset the cooldown on Teleport.',
		# unique_is_primary=False,
		random_primaries='',
		random_secondaries='')
	theOculus.save()
	theOculus.affixes.add(dmg, inte, chc, apCrit)

	triumvirate = Source(id=5,
		name='Triumvirate',
		pic='/assets/media/items/legendaries/offhands/sources/triumvirate.png',
		unique='Your Signature Spells increase the damage of Arcane Orb by <span>75 - 100%</span> for <span class="silver">6</span> seconds, stacking up to <span class="silver">3</span> times.',
		# unique_is_primary=False,
		random_primaries='2',
		random_secondaries='1')
	triumvirate.save()
	triumvirate.affixes.add(dmg, inte, chc)

	winterFlurry = Source(id=6,
		name='Winter Flurry',
		pic='/assets/media/items/legendaries/offhands/sources/winter_flurry.png',
		unique='Enemies killed by Cold damage have a <span>15 - 20%</span> chance to release a Frost Nova.',
		random_primaries='2',
		random_secondaries='1')
	winterFlurry.save()
	winterFlurry.affixes.add(dmg, inte, chc, winterColdDmg)

	# singularity = Source(id=7,
	# 	name='Singularity',
	# 	pic='/assets/media/items/legendaries/offhands/sources/singularity.png',
	# 	random_primaries='2',
	# 	random_secondaries='1',
	# 	notes='60')
	# singularity.save()
	# singularity.affixes.add(dmg, inte, apCrit, maxAP)

	for source in Source.objects.all():
		source.slug = slugify(source.name)
		source.category = 'Source'
		source.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0003_rings'),
    ]

    operations = [
    	migrations.RunPython(load_sources)
    ]
