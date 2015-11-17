# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_mighty_belts(apps, schema_editor):
	MightyBelt = apps.get_model("legendaries", "MightyBelt")
	Affix = apps.get_model("affixes", "MightyBeltAffix")


	stre = Affix.objects.get(affix='stre')
	vita = Affix.objects.get(affix='vita')
	allRes = Affix.objects.get(affix='allRes')

	maxFury = Affix.objects.get(affix='maxFury')

	girdleIAS = Affix.objects.get(affix='girdleIAS')
	kotuursBlockChance = Affix.objects.get(affix='kotuursBlockChance')


	agelessMight = MightyBelt(name='Ageless Might',
		pic='/assets/media/items/legendaries/armor/waist/mightybelts/ageless_might.png',
		random_primaries='2',
		random_secondaries='2')
	agelessMight.save()
	agelessMight.affixes.add(stre, allRes)

	chilaniksChain = MightyBelt(name='Chilanik\'s Chain',
		pic='/assets/media/items/legendaries/armor/waist/mightybelts/chilaniks_chain.png',
		unique='Using War Cry increases the movement speed for you and all allies affected by <span>30 - 40%</span> for <span class="silver">10</span> seconds.',
		random_primaries='3',
		random_secondaries='1')
	chilaniksChain.save()
	chilaniksChain.affixes.add(stre)

	dreadIron = MightyBelt(name='Dread Iron',
		pic='/assets/media/items/legendaries/armor/waist/mightybelts/dread_iron.png',
		unique='Ground Stomp causes an Avalanche.',
		random_primaries='2',
		random_secondaries='1')
	dreadIron.save()
	dreadIron.affixes.add(stre, vita)

	girdleOfGiants = MightyBelt(name='Girdle of Giants',
		pic='/assets/media/items/legendaries/armor/waist/mightybelts/girdle_of_giants.png',
		random_primaries='2',
		random_secondaries='1')
	girdleOfGiants.save()
	girdleOfGiants.affixes.add(stre, girdleIAS, maxFury)

	kotuursBrace = MightyBelt(name='Kotuur\'s Brace',
		pic='/assets/media/items/legendaries/armor/waist/mightybelts/kotuurs_brace.png',
		random_primaries='2',
		random_secondaries='2')
	kotuursBrace.save()
	kotuursBrace.affixes.add(stre, kotuursBlockChance)

	lamentation = MightyBelt(name='lamentation',
		pic='/assets/media/items/legendaries/armor/waist/mightybelts/lamentation.png',
		unique='Rend can now stack up to <span class="silver">2</span> times on an enemy.',
		random_primaries='3',
		random_secondaries='1')
	lamentation.save()
	lamentation.affixes.add(stre)

	prideOfCassius = MightyBelt(name='Pride of Cassius',
		pic='/assets/media/items/legendaries/armor/waist/mightybelts/pride_of_cassius.png',
		unique='Increases the duration of Ignore Pain by <span>4 - 6</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	prideOfCassius.save()
	prideOfCassius.affixes.add(stre, allRes)

	theUndisputedChampion = MightyBelt(name='The Undisputed Champion',
		pic='/assets/media/items/legendaries/armor/waist/mightybelts/the_undisputed_champion.png',
		unique='Frenzy gains the effect of every rune.',
		random_primaries='2',
		random_secondaries='1')
	theUndisputedChampion.save()
	theUndisputedChampion.affixes.add(stre, allRes)


	for mightyBelt in MightyBelt.objects.all():
		mightyBelt.slug = slugify(mightyBelt.name)
		mightyBelt.category = 'Mighty Belt'
		mightyBelt.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0018_belts'),
    ]

    operations = [
    	migrations.RunPython(load_mighty_belts)
    ]
