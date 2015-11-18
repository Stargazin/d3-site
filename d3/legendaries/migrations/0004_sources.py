# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_sources(apps, schema_editor):
	Source = apps.get_model("legendaries", "Source")
	Affix = apps.get_model("affixes", "SourceAffix")


	dmg = Affix.objects.get(affix='dmg')
	inte = Affix.objects.get(affix='inte')
	chc = Affix.objects.get(affix='chc')
	apCrit = Affix.objects.get(affix='apCrit')

	winterColdDmg = Affix.objects.get(affix='winterColdDmg')


	cosmicStrand = Source(name='Cosmic Strand',
		pic='/assets/media/items/legendaries/offhands/sources/cosmic_strand.png',
		unique='Teleport gains the effect of the Wormhole rune.',
		random_primaries='4',
		random_secondaries='1',
		notes='crafted')
	cosmicStrand.save()
	cosmicStrand.affixes.add(dmg)

	lightOfGrace = Source(name='Light of Grace',
		pic='/assets/media/items/legendaries/offhands/sources/light_of_grace.png',
		unique='Ray of Frost now pierces.',
		random_primaries='2',
		random_secondaries='1')
	lightOfGrace.save()
	lightOfGrace.affixes.add(dmg, inte, chc)

	mirrorball = Source(name='Mirrorball',
		pic='/assets/media/items/legendaries/offhands/sources/mirrorball.png',
		unique='Magic Missile fires <span>1 - 2</span> extra missiles.',
		random_primaries='2',
		random_secondaries='1')
	mirrorball.save()
	mirrorball.affixes.add(dmg, inte, chc)

	mykensBallOfHate = Source(name='Myken\'s Ball of Hate',
		pic='/assets/media/items/legendaries/offhands/sources/mykens_ball_of_hate.png',
		unique='Electrocute can chain to enemies that have already been hit.',
		random_primaries='2',
		random_secondaries='1')
	mykensBallOfHate.save()
	mykensBallOfHate.affixes.add(dmg, inte, chc)

	theOculus = Source(name='The Oculus',
		pic='/assets/media/items/legendaries/offhands/sources/the_oculus.png',
		unique='Taking damage has up to a <span>15 - 20%</span> chance to reset the cooldown on Teleport.',
		random_primaries='',
		random_secondaries='')
	theOculus.save()
	theOculus.affixes.add(dmg, inte, chc, apCrit)

	triumvirate = Source(name='Triumvirate',
		pic='/assets/media/items/legendaries/offhands/sources/triumvirate.png',
		unique='Your Signature Spells increase the damage of Arcane Orb by <span>75 - 100%</span> for <span class="silver">6</span> seconds, stacking up to <span class="silver">3</span> times.',
		random_primaries='2',
		random_secondaries='1')
	triumvirate.save()
	triumvirate.affixes.add(dmg, inte, chc)

	winterFlurry = Source(name='Winter Flurry',
		pic='/assets/media/items/legendaries/offhands/sources/winter_flurry.png',
		unique='Enemies killed by Cold damage have a <span>15 - 20%</span> chance to release a Frost Nova.',
		random_primaries='2',
		random_secondaries='1')
	winterFlurry.save()
	winterFlurry.affixes.add(dmg, inte, chc, winterColdDmg)


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
