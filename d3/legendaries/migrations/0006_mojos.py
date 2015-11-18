# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_mojos(apps, schema_editor):
	Mojo = apps.get_model("legendaries", "Mojo")
	Affix = apps.get_model("affixes", "MojoAffix")

	dmg = Affix.objects.get(affix='dmg')
	inte = Affix.objects.get(affix='inte')
	chc = Affix.objects.get(affix='chc')
	lps = Affix.objects.get(affix='lps')
	manaRegen = Affix.objects.get(affix='manaRegen')
	sacrifice = Affix.objects.get(affix='sacrifice')

	maxMana = Affix.objects.get(affix='maxMana')
	durability = Affix.objects.get(affix='durability')


	thingItemPickup = Affix.objects.get(affix='thingItemPickup')


	gazingDemise = Mojo(name='Gazing Demise',
		pic='/assets/media/items/legendaries/offhands/mojos/gazing_demise.png',
		random_primaries='1',
		random_secondaries='2')
	gazingDemise.save()
	gazingDemise.affixes.add(dmg, inte, lps, manaRegen)

	henrisPerquisition = Mojo(name='Henri\'s Perquisition',
		pic='/assets/media/items/legendaries/offhands/mojos/henris_perquisition.png',
		unique='The first time an enemy deals damage to you, reduce that damage by <span>60 - 80%</span> and Charm the enemy for <span class="silver">3</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	henrisPerquisition.save()
	henrisPerquisition.affixes.add(dmg, inte, chc, durability)

	homunculus = Mojo(name='homunculus',
		pic='/assets/media/items/legendaries/offhands/mojos/homunculus.png',
		unique='A Zombie Dog is automatically summoned to your side every <span class="silver">2</span> seconds.',
		random_primaries='2')
	homunculus.save()
	homunculus.affixes.add(dmg, inte, chc, sacrifice, maxMana)

	shukranisTriumph = Mojo(name='Shukrani\'s Triumph',
		pic='/assets/media/items/legendaries/offhands/mojos/shukranis_triumph.png',
		unique='Spirit Walk lasts until you attack or until an enemy is within <span class="silver">30</span> yards of you.',
		random_primaries='1',
		random_secondaries='1')
	shukranisTriumph.save()
	shukranisTriumph.affixes.add(dmg, inte, chc, manaRegen)

	spite = Mojo(name='spite',
		pic='/assets/media/items/legendaries/offhands/mojos/spite.png',
		random_primaries='3',
		random_secondaries='1')
	spite.save()
	spite.affixes.add(dmg, chc, maxMana)

	thingOfTheDeep = Mojo(name='Thing Of The Deep',
		pic='/assets/media/items/legendaries/offhands/mojos/thing_of_the_deep.png',
		random_primaries='1')
	thingOfTheDeep.save()
	thingOfTheDeep.affixes.add(dmg, inte, chc, manaRegen, maxMana, thingItemPickup)

	uhkapianSerpent = Mojo(name='Uhkapian Serpent',
		pic='/assets/media/items/legendaries/offhands/mojos/uhkapian_serpent.png',
		unique='<span>25 - 30%</span> of the damage you take is redirected to your Zombie Dogs.',
		random_primaries='2',
		random_secondaries='1')
	uhkapianSerpent.save()
	uhkapianSerpent.affixes.add(dmg, inte, chc)


	for mojo in Mojo.objects.all():
		mojo.slug = slugify(mojo.name)
		mojo.category = 'Mojo'
		mojo.save()


class Migration(migrations.Migration):
    dependencies = [
        ('legendaries', '0005_quivers'),
    ]

    operations = [
    	migrations.RunPython(load_mojos)
    ]
