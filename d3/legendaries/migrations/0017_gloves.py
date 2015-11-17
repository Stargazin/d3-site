# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_gloves(apps, schema_editor):
	Gloves = apps.get_model("legendaries", "Gloves")
	Affix = apps.get_model("affixes", "GlovesAffix")


	mainStat = Affix.objects.get(affix='mainStat')
	ias = Affix.objects.get(affix='ias')
	chc = Affix.objects.get(affix='chc')
	chd = Affix.objects.get(affix='chd')
	lph = Affix.objects.get(affix='lph')

	frostburnColdDmg = Affix.objects.get(affix='frostburnColdDmg')
	magefistFireDmg = Affix.objects.get(affix='magefistFireDmg')
	stoneImmobilizeChance = Affix.objects.get(affix='stoneImmobilizeChance')


	frostburn = Gloves(name='Frostburn',
		pic='/assets/media/items/legendaries/armor/hands/frostburn.png',
		unique='Your Cold damage has up to a <span>34 - 45%</span> chance to Freeze enemies.',
		random_primaries='2',
		random_secondaries='1')
	frostburn.save()
	frostburn.affixes.add(mainStat, frostburnColdDmg)

	gladiatorGauntlets = Gloves(name='Gladiator Gauntlets',
		pic='/assets/media/items/legendaries/armor/hands/gladiator_gauntlets.png',
		unique='After earning a massacre bonus, gold rains from sky.',
		random_primaries='2',
		random_secondaries='1')
	gladiatorGauntlets.save()
	gladiatorGauntlets.affixes.add(mainStat, chc)

	glovesOfWorship = Gloves(name='Gloves Of Worship',
		pic='/assets/media/items/legendaries/armor/hands/gloves_of_worship.png',
		unique='Shrine effects last for <span class="silver">10</span> minutes.',
		random_primaries='1',
		random_secondaries='1')
	glovesOfWorship.save()
	glovesOfWorship.affixes.add(mainStat, chd, lph)

	magefist = Gloves(name='magefist',
		pic='/assets/media/items/legendaries/armor/hands/magefist.png',
		random_primaries='2',
		random_secondaries='1')
	magefist.save()
	magefist.affixes.add(mainStat, magefistFireDmg, ias)

	pendersPurchase = Gloves(name='Penders Purchase',
		pic='/assets/media/items/legendaries/armor/hands/penders_purchase.png',
		random_primaries='4',
		random_secondaries='2',
		notes='crafted')
	pendersPurchase.save()
	# pendersPurchase.affixes.add()

	stArchewsGage = Gloves(name='St. Archew\'s Gage',
		pic='/assets/media/items/legendaries/armor/hands/st_archews_gage.png',
		unique='The first time an elite pack damages you, gain an absorb shield equal to <span>120 - 150%</span> of your maximum Life for <span class="silver">10</span> seconds.',
		random_primaries='3',
		random_secondaries='1')
	stArchewsGage.save()
	stArchewsGage.affixes.add(mainStat)

	stoneGauntlets = Gloves(name='Stone Gauntlets',
		pic='/assets/media/items/legendaries/armor/hands/stone_guantlets.png',
		random_primaries='3',
		random_secondaries='1')
	stoneGauntlets.save()
	stoneGauntlets.affixes.add(mainStat, stoneImmobilizeChance)

	taskerAndTheo = Gloves(name='Tasker and Theo',
		pic='/assets/media/items/legendaries/armor/hands/tasker_and_theo.png',
		unique='Increase attack speed of your pets by <span>40 - 50%</span>.',
		random_primaries='2',
		random_secondaries='1')
	taskerAndTheo.save()
	taskerAndTheo.affixes.add(mainStat, ias)


	for gloves in Gloves.objects.all():
		gloves.slug = slugify(gloves.name)
		gloves.category = 'Gloves'
		gloves.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0016_bracers'),
    ]

    operations = [
    	migrations.RunPython(load_gloves)
    ]
