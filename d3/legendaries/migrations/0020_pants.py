# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_pants(apps, schema_editor):
	Pants = apps.get_model("legendaries", "Pants")
	Affix = apps.get_model("affixes", "PantsAffix")


	mainStat = Affix.objects.get(affix='mainStat')
	lps = Affix.objects.get(affix='lps')
	allRes = Affix.objects.get(affix='allRes')

	extraGold = Affix.objects.get(affix='extraGold')

	hammerMovementSpeed = Affix.objects.get(affix='hammerMovementSpeed')
	swampPoisDmg = Affix.objects.get(affix='swampPoisDmg')
	swampCCReduction = Affix.objects.get(affix='swampCCReduction')


	deathsBargain = Pants(name='Death\'s Bargain',
		pic='/assets/media/items/legendaries/armor/legs/deaths_bargain.png',
		unique='Gain an aura of death that deals <span>750 - 1000%</span> of your Life per Second as Physical damage to enemies within <span class="silver">16</span> yards. You no longer regenerate Life.',
		random_primaries='2',
		random_secondaries='1')
	deathsBargain.save()
	deathsBargain.affixes.add(mainStat, lps)

	depthDiggers = Pants(name='Depth Diggers',
		pic='/assets/media/items/legendaries/armor/legs/depth_diggers.png',
		unique='Primary skills that generate resource deal <span>80 - 100%</span> additional damage.',
		random_primaries='2',
		random_secondaries='1')
	depthDiggers.save()
	depthDiggers.affixes.add(mainStat, allRes)

	hammerJammers = Pants(name='Hammer Jammers',
		pic='/assets/media/items/legendaries/armor/legs/hammer_jammers.png',
		random_primaries='2',
		random_secondaries='1')
	hammerJammers.save()
	hammerJammers.affixes.add(mainStat, hammerMovementSpeed, extraGold)

	hexingPantsOfMrYan = Pants(name='Hexing Pants of Mr. Yan',
		pic='/assets/media/items/legendaries/armor/legs/hexing_pants_of_mr_yan.png',
		unique='Your resource generation and damage is increased by <span class="silver">25%</span> while moving and decreased by <span>20 - 25%</span> while standing still.',
		random_primaries='3',
		random_secondaries='1')
	hexingPantsOfMrYan.save()
	hexingPantsOfMrYan.affixes.add(mainStat)

	poxFaulds = Pants(name='Pox Faulds',
		pic='/assets/media/items/legendaries/armor/legs/pox_faulds.png',
		unique='When <span class="silver">3</span> or more enemies are within <span class="silver">12</span> yards, you release a vile stench that deals <span>450 - 550%</span> weapon damage as Poison every second for <span class="silver">5</span> seconds to enemies within <span class="silver">15</span> yards.',
		random_primaries='3',
		random_secondaries='1')
	poxFaulds.save()
	poxFaulds.affixes.add(mainStat)

	skelonsDeceit = Pants(name='Skelon\'s Deceit',
		pic='/assets/media/items/legendaries/armor/legs/skelons_deceit.png',
		random_primaries='4',
		random_secondaries='2',
		notes='crafted')
	skelonsDeceit.save()
	# skelonsDeceit.affixes.add()

	swampLandWaders = Pants(name='Swamp Land Waders',
		pic='/assets/media/items/legendaries/armor/legs/swamp_land_waders.png',
		random_primaries='2',
		random_secondaries='1')
	swampLandWaders.save()
	swampLandWaders.affixes.add(mainStat, swampPoisDmg, swampCCReduction)


	for pants in Pants.objects.all():
		pants.slug = slugify(pants.name)
		pants.category = 'Pants'
		pants.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0019_mighty_belts'),
    ]

    operations = [
    	migrations.RunPython(load_pants)
    ]
