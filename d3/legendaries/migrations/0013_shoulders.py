# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_shoulders(apps, schema_editor):
	Shoulders = apps.get_model("legendaries", "Shoulders")
	Affix = apps.get_model("affixes", "ShouldersAffix")


	mainStat = Affix.objects.get(affix='mainStat')
	vita = Affix.objects.get(affix='vita')
	armor = Affix.objects.get(affix='armor')

	itemHealing = Affix.objects.get(affix='itemHealing')
	extraGold = Affix.objects.get(affix='extraGold')

	profaneItemPickup = Affix.objects.get(affix='profaneItemPickup')


	corruption = Shoulders(name='Corruption',
		pic='/assets/media/items/legendaries/armor/shoulders/corruption.png',
		random_primaries='4',
		random_secondaries='2',
		notes='crafted')
	corruption.save()
	# corruption.affixes.add()

	deathWatchMantle = Shoulders(name='Death Watch Mantle',
		pic='/assets/media/items/legendaries/armor/shoulders/death_watch_mantle.png',
		unique='<span>25 - 35%</span> chance to explode in a fan of knives for <span>750 - 950%</span> weapon damage when hit.',
		random_primaries='3',
		random_secondaries='1')
	deathWatchMantle.save()
	deathWatchMantle.affixes.add(mainStat)

	furyOfTheAncients = Shoulders(name='Fury of The Ancients',
		pic='/assets/media/items/legendaries/armor/shoulders/fury_of_the_ancients.png',
		unique='Call of the Ancients gains the effect of the Ancients\' Fury rune.',
		random_primaries='3',
		random_secondaries='1')
	furyOfTheAncients.save()
	furyOfTheAncients.affixes.add(mainStat)

	homingPads = Shoulders(name='Homing Pads',
		pic='/assets/media/items/legendaries/armor/shoulders/homing_pads.png',
		unique='Your Town Portal is no longer interrupted by taking damage. While casting Town Portal you gain a protective bubble that reduces damage taken by <span>50 - 65%</span>.',
		random_primaries='3')
	homingPads.save()
	homingPads.affixes.add(mainStat, extraGold)

	pauldronsOfTheSkeletonKing = Shoulders(name='Pauldrons of the Skeleton King',
		pic='/assets/media/items/legendaries/armor/shoulders/pauldrons_of_the_skeleton_king.png',
		unique='When receiving fatal damage, there is a chance that you are instead restored to <span class="silver">25%</span> of maximum Life and cause nearby enemies to flee in fear.',
		random_primaries='1',
		random_secondaries='1')
	pauldronsOfTheSkeletonKing.save()
	pauldronsOfTheSkeletonKing.affixes.add(mainStat, vita, armor)

	profanePauldrons = Shoulders(name='Profane Pauldrons',
		pic='/assets/media/items/legendaries/armor/shoulders/profane_pauldrons.png',
		random_primaries='3')
	profanePauldrons.save()
	profanePauldrons.affixes.add(mainStat, itemHealing, profaneItemPickup)

	spauldersOfZakara = Shoulders(name='Spaulders of Zakara',
		pic='/assets/media/items/legendaries/armor/shoulders/spaulders_of_zakara.png',
		unique='Your items become indestructible.',
		random_primaries='3',
		random_secondaries='1')
	spauldersOfZakara.save()
	spauldersOfZakara.affixes.add(mainStat)

	vileWard = Shoulders(name='Vile Ward',
		pic='/assets/media/items/legendaries/armor/shoulders/vile_ward.png',
		unique='Furious Charge deals <span>30 - 35%</span> increased damage for every enemy hit while charging.',
		random_primaries='3',
		random_secondaries='2',
		notes='double check affixes')
	vileWard.save()
	vileWard.affixes.add(mainStat)


	for shoulders in Shoulders.objects.all():
		shoulders.slug = slugify(shoulders.name)
		shoulders.category = 'Shoulders'
		shoulders.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0012_wizard_hats'),
    ]

    operations = [
    	migrations.RunPython(load_shoulders)
    ]
