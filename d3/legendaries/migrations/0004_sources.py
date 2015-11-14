# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_sources(apps, schema_editor):
	Source = apps.get_model("legendaries", "Source")
	SourceAffix = apps.get_model("affixes", "SourceAffix")

	dmg = SourceAffix.objects.get(affix='dmg')
	inte = SourceAffix.objects.get(affix='inte')
	vita = SourceAffix.objects.get(affix='vita')

	life = SourceAffix.objects.get(affix='life')
	lps = SourceAffix.objects.get(affix='lps')

	chc = SourceAffix.objects.get(affix='chc')
	areaDmg = SourceAffix.objects.get(affix='areaDmg')
	eliteDmg = SourceAffix.objects.get(affix='eliteDmg')

	bleedChance = SourceAffix.objects.get(affix='bleedChance')

	cdr = SourceAffix.objects.get(affix='cdr')
	rcr = SourceAffix.objects.get(affix='rcr')
	sockets = SourceAffix.objects.get(affix='sockets')

	apCrit = SourceAffix.objects.get(affix='apCrit')

	arcaneOrb = SourceAffix.objects.get(affix='arcaneOrb')
	electrocute = SourceAffix.objects.get(affix='electrocute')
	rayOfFrost = SourceAffix.objects.get(affix='rayOfFrost')
	spectralBlade = SourceAffix.objects.get(affix='spectralBlade')
	blackHole = SourceAffix.objects.get(affix='blackHole')
	meteor = SourceAffix.objects.get(affix='meteor')
	waveOfForce = SourceAffix.objects.get(affix='waveOfForce')
	arcaneTorrent = SourceAffix.objects.get(affix='arcaneTorrent')
	shockPulse = SourceAffix.objects.get(affix='shockPulse')
	familiar = SourceAffix.objects.get(affix='familiar')
	magicMissle = SourceAffix.objects.get(affix='magicMissle')
	energyTwister = SourceAffix.objects.get(affix='energyTwister')
	blizzard = SourceAffix.objects.get(affix='blizzard')
	disintegrate = SourceAffix.objects.get(affix='disintegrate')
	explosiveBlast = SourceAffix.objects.get(affix='explosiveBlast')
	hydra = SourceAffix.objects.get(affix='hydra')


	maxAP = SourceAffix.objects.get(affix='maxAP')

	fearChance = SourceAffix.objects.get(affix='fearChance')
	stunChance = SourceAffix.objects.get(affix='stunChance')
	blindChance = SourceAffix.objects.get(affix='blindChance')
	freezeChance = SourceAffix.objects.get(affix='freezeChance')
	chillChance = SourceAffix.objects.get(affix='chillChance')
	slowChance = SourceAffix.objects.get(affix='slowChance')
	immobilizeChance = SourceAffix.objects.get(affix='immobilizeChance')
	knockbackChance = SourceAffix.objects.get(affix='knockbackChance')

	thorns = SourceAffix.objects.get(affix='thorns')
	itemHealing = SourceAffix.objects.get(affix='itemHealing')

	killExp = SourceAffix.objects.get(affix='killExp')
	extraGold = SourceAffix.objects.get(affix='extraGold')
	durability = SourceAffix.objects.get(affix='durability')
	lvlReq = SourceAffix.objects.get(affix='lvlReq')


	cosmicStrand = Source(id=0,
		name='Cosmic Strand',
		pic='/assets/media/items/legendaries/offhands/sources/cosmic_strand.png',
		unique='Teleport gains the effect of the Wormhole rune.',
		# unique_is_primary=False,
		random_primaries='4',
		random_secondaries='1')
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
		unique='Cold skills deal <span>15 - 20%</span> more damage',
		unique_is_primary=True,
		unique2='Enemies killed by Cold damage have a <span>15 - 20%</span> chance to release a Frost Nova.',
		random_primaries='2',
		random_secondaries='1')
	winterFlurry.save()
	winterFlurry.affixes.add(dmg, inte, chc)

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
