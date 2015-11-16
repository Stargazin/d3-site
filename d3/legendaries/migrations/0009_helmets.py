# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify

def load_helmets(apps, schema_editor):
	Helmet = apps.get_model("legendaries", "Helmet")
	Affix = apps.get_model("affixes", "HelmetAffix")

	mainStat = Affix.objects.get(affix='mainStat')
	vita = Affix.objects.get(affix='vita')
	chc = Affix.objects.get(affix='chc')
	allRes = Affix.objects.get(affix='allRes')
	sockets = Affix.objects.get(affix='sockets')

	andarielsIAS = Affix.objects.get(affix='andarielsIAS')
	andarielsFireDmgTaken = Affix.objects.get(affix='andarielsFireDmgTaken')
	andarielsEleDmg = Affix.objects.get(affix='andarielsEleDmg')
	andarielsPoisRes = Affix.objects.get(affix='andarielsPoisRes')
	blindBlindchance = Affix.objects.get(affix='blindBlindchance')
	mempoIAS = Affix.objects.get(affix='mempoIAS')
	helmBlockChance = Affix.objects.get(affix='helmBlockChance')


	andarielsVisage = Helmet(name='Andariel\'s Visage',
		pic='/assets/media/items/legendaries/armor/head/helmets/andariels_visage.png',
		unique='Attacks release a Poison Nova that deals <span>350 - 450%</span> weapon damage as Poison to enemies within <span class="silver">10</span> yards.',
		random_primaries='1')
	andarielsVisage.save()
	andarielsVisage.affixes.add(mainStat, andarielsEleDmg, andarielsIAS, andarielsFireDmgTaken, andarielsPoisRes)

	blindFaith = Helmet(name='Blind Faith',
		pic='/assets/media/items/legendaries/armor/head/helmets/blind_faith.png',
		random_primaries='3',
		random_secondaries='1')
	blindFaith.save()
	blindFaith.affixes.add(mainStat, blindBlindchance)

	brokenCrown = Helmet(name='Broken Crown',
		pic='/assets/media/items/legendaries/armor/head/helmets/broken_crown.png',
		unique='Whenever a gem drops, a gem of the type socketed into your helmet also drops.',
		random_primaries='2',
		random_secondaries='1')
	brokenCrown.save()
	brokenCrown.affixes.add(mainStat, sockets)

	deathseersCowl = Helmet(name='Deathseer\'s Cowl',
		pic='/assets/media/items/legendaries/armor/head/helmets/deathseers_cowl.png',
		unique='<span>15 - 20%</span> chance on being hit by an Undead enemy to charm it for <span class="silver">2</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	deathseersCowl.save()
	deathseersCowl.affixes.add(mainStat, sockets)

	leoricsCrown = Helmet(name='Leoric\'s Crown',
		pic='/assets/media/items/legendaries/armor/head/helmets/leorics_crown.png',
		unique='Increase the effect of any gem socketed into this item by <span>75 - 100%</span>.',
		random_primaries='2',
		random_secondaries='1')
	leoricsCrown.save()
	leoricsCrown.affixes.add(mainStat, sockets)

	mempoOfTwilight = Helmet(name='Mempo of Twilight',
		pic='/assets/media/items/legendaries/armor/head/helmets/mempo_of_twilight.png',
		unique='',
		random_primaries='',
		random_secondaries='')
	mempoOfTwilight.save()
	mempoOfTwilight.affixes.add(mainStat, mempoIAS, allRes, sockets)

	pridesFall = Helmet(name='Pride\'s Fall',
		pic='/assets/media/items/legendaries/armor/head/helmets/prides_fall.png',
		unique='Your resource costs are reduced by <span class="silver">30%</span> after not taking damage for <span class="silver">5</span> seconds.',
		random_primaries='1',
		random_secondaries='1')
	pridesFall.save()
	pridesFall.affixes.add(mainStat, vita, chc)

	skullOfResonance = Helmet(name='Skull Of Resonance',
		pic='/assets/media/items/legendaries/armor/head/helmets/skull_of_resonance.png',
		unique='Threatening Shout has a chance to Charm enemies and cause them to join your side.',
		random_primaries='1',
		random_secondaries='1')
	skullOfResonance.save()
	skullOfResonance.affixes.add(mainStat, allRes, sockets)

	theHelmOfRule = Helmet(name='The Helm of Rule',
		pic='/assets/media/items/legendaries/armor/head/helmets/the_helm_of_rule.png',
		random_primaries='2',
		random_secondaries='2')
	theHelmOfRule.save()
	theHelmOfRule.affixes.add(vita, helmBlockChance)


	for helmet in Helmet.objects.all():
		helmet.slug = slugify(helmet.name)
		helmet.category = 'Helmet'
		helmet.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0008_shields'),
    ]

    operations = [
    	migrations.RunPython(load_helmets)
    ]
