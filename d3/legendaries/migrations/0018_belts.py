# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_belts(apps, schema_editor):
	Belt = apps.get_model("legendaries", "Belt")
	Affix = apps.get_model("affixes", "BeltAffix")


	mainStat = Affix.objects.get(affix='mainStat')
	vita = Affix.objects.get(affix='vita')
	allRes = Affix.objects.get(affix='allRes')
	rcr = Affix.objects.get(affix='rcr')

	itemPickup = Affix.objects.get(affix='itemPickup')
	extraGold = Affix.objects.get(affix='extraGold')
	durability = Affix.objects.get(affix='durability')

	troveReducedMeleeDmg = Affix.objects.get(affix='troveReducedMeleeDmg')
	fleetingIAS = Affix.objects.get(affix='fleetingIAS')
	hellcatIAS = Affix.objects.get(affix='hellcatIAS')
	saffronCCReduction = Affix.objects.get(affix='saffronCCReduction')
	stringReducedMeleeDmg = Affix.objects.get(affix='stringReducedMeleeDmg')
	witchingIAS = Affix.objects.get(affix='witchingIAS')
	witchingCHD = Affix.objects.get(affix='witchingCHD')
	thundergodsLightDmg = Affix.objects.get(affix='thundergodsLightDmg')
	thundergodsLightRes = Affix.objects.get(affix='thundergodsLightRes')
	vigilanteCDR = Affix.objects.get(affix='vigilanteCDR')


	angelHairBraid = Belt(name='Angel Hair Braid',
		pic='/assets/media/items/legendaries/armor/waist/belts/angel_hair_braid.png',
		unique='Punish gains the effect of every rune.',
		random_primaries='3',
		random_secondaries='1',
		notes='double check secondaries')
	angelHairBraid.save()
	angelHairBraid.affixes.add(mainStat, durability)

	beltOfTheTrove = Belt(name='Belt of the Trove',
		pic='/assets/media/items/legendaries/armor/waist/belts/belt_of_the_trove.png',
		unique='Every <span>6 - 8</span> seconds, call down Bombardment on a random nearby enemy.',
		random_primaries='2')
	beltOfTheTrove.save()
	beltOfTheTrove.affixes.add(mainStat, allRes, troveReducedMeleeDmg)

	beltOfTranscendence = Belt(name='Belt of Transcendence',
		pic='/assets/media/items/legendaries/armor/waist/belts/belt_of_transcendence.png',
		unique='Summon a Fetish Sycophant when you hit with a Mana spender.',
		random_primaries='2',
		random_secondaries='1')
	beltOfTranscendence.save()
	beltOfTranscendence.affixes.add(mainStat, vita)

	bindingOfTheLost = Belt(name='Binding of TheLost',
		pic='/assets/media/items/legendaries/armor/waist/belts/binding_of_the_lost.png',
		unique='Each hit with Seven-Sided Strike grants <span>3.0 - 3.5%</span> damage reduction for <span class="silver">7</span> seconds.',
		random_primaries='3',
		random_secondaries='1')
	bindingOfTheLost.save()
	bindingOfTheLost.affixes.add(mainStat)

	blessedOfHaull = Belt(name='Blessed of Haull',
		pic='/assets/media/items/legendaries/armor/waist/belts/blessed_of_haull.png',
		unique='Justice spawns a Blessed Hammer when it hits an enemy.',
		random_primaries='2',
		random_secondaries='1')
	blessedOfHaull.save()
	blessedOfHaull.affixes.add(mainStat, allRes)

	cordOfTheSherma = Belt(name='Cord of the Sherma',
		pic='/assets/media/items/legendaries/armor/waist/belts/cord_of_the_sherma.png',
		unique='Chance on hit to create a chaos field that Blinds and Slows enemies inside for <span>3 - 4</span> seconds.',
		random_primaries='2')
	cordOfTheSherma.save()
	cordOfTheSherma.affixes.add(mainStat, vita, itemPickup)

	crashingRain = Belt(name='Crashing Rain',
		pic='/assets/media/items/legendaries/armor/waist/belts/crashing_rain.png',
		unique='Rain of Vengeance also summons a crashing beast that deals <span>3000 - 4000%</span> weapon damage.',
		random_primaries='2',
		random_secondaries='1')
	crashingRain.save()
	crashingRain.affixes.add(mainStat, vita)

	fazulasImprobableChain = Belt(name='Fazula\'s Improbable Chain',
		pic='/assets/media/items/legendaries/armor/waist/belts/fazulas_improbable_chain.png',
		unique='You automatically start with <span>15 - 20</span> Archon stacks when entering Archon form.',
		random_primaries='3',
		random_secondaries='1')
	fazulasImprobableChain.save()
	fazulasImprobableChain.affixes.add(mainStat)

	fleetingStrap = Belt(name='Fleeting Strap',
		pic='/assets/media/items/legendaries/armor/waist/belts/fleeting_strap.png',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted')
	fleetingStrap.save()
	fleetingStrap.affixes.add(fleetingIAS)

	goldwrap = Belt(name='goldwrap',
		pic='/assets/media/items/legendaries/armor/waist/belts/goldwrap.png',
		unique='On gold pickup: Gain armor for <span class="silver">5</span> seconds equal to the amount picked up.',
		random_primaries='3')
	goldwrap.save()
	goldwrap.affixes.add(mainStat, extraGold)

	harringtonWaistguard = Belt(name='Harrington Waistguard',
		pic='/assets/media/items/legendaries/armor/waist/belts/harrington_waistguard.png',
		unique='Opening a chest grants <span>100 - 135%</span> increased damage for <span class="silver">10</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	harringtonWaistguard.save()
	harringtonWaistguard.affixes.add(mainStat, extraGold)

	hauntingGirdle = Belt(name='Haunting Girdle',
		pic='/assets/media/items/legendaries/armor/waist/belts/haunting_girdle.png',
		unique='Haunt releases <span class="silver">1</span> extra spirit.',
		random_primaries='2',
		random_secondaries='1')
	hauntingGirdle.save()
	hauntingGirdle.affixes.add(mainStat, vita)

	hellcatWaistguard = Belt(name='Hellcat Waistguard',
		pic='/assets/media/items/legendaries/armor/waist/belts/hellcat_waistguard.png',
		random_primaries='1',
		random_secondaries='2')
	hellcatWaistguard.save()
	hellcatWaistguard.affixes.add(mainStat, vita, hellcatIAS)

	huntersWrath = Belt(name='Hunter\'s Wrath',
		pic='/assets/media/items/legendaries/armor/waist/belts/hunters_wrath.png',
		unique='Your primary skills attack <span class="silver">30%</span> faster and deal <span>45 - 60%</span> increased damage.',
		random_primaries='2',
		random_secondaries='1')
	huntersWrath.save()
	huntersWrath.affixes.add(mainStat, vita)

	hwojWrap = Belt(name='Hwoj Wrap',
		pic='/assets/media/items/legendaries/armor/waist/belts/hwoj_wrap.png',
		unique='Locust Swarm also Slows enemies by <span>60 - 80%</span>.',
		random_primaries='2',
		random_secondaries='1')
	hwojWrap.save()
	hwojWrap.affixes.add(mainStat, allRes)

	insatiableBelt = Belt(name='Insatiable Belt',
		pic='/assets/media/items/legendaries/armor/waist/belts/insatiable_belt.png',
		unique='Picking up a Health Globe increases your maximum Life by <span class="silver">5%</span> for <span class="silver">15</span> seconds, stacking up to <span class="silver">5</span> times.',
		random_primaries='2')
	insatiableBelt.save()
	insatiableBelt.affixes.add(mainStat, vita, itemPickup)

	jangsEnvelopment = Belt(name='Jang\'s Envelopment',
		pic='/assets/media/items/legendaries/armor/waist/belts/jangs_envelopment.png',
		unique='Enemies damaged by Black Hole are also slowed by <span>60 - 80%</span> for <span class="silver">3</span> seconds.',
		random_primaries='3',
		random_secondaries='1')
	jangsEnvelopment.save()
	jangsEnvelopment.affixes.add(mainStat)

	omnislash = Belt(name='omnislash',
		pic='/assets/media/items/legendaries/armor/waist/belts/omnislash.png',
		unique='Slash attacks in all directions.',
		random_primaries='2',
		random_secondaries='1')
	omnislash.save()
	omnislash.affixes.add(mainStat, allRes)

	omyrnsChain = Belt(name='Omyrn\'s Chain',
		pic='/assets/media/items/legendaries/armor/waist/belts/omyrns_chain.png',
		unique='Drop Caltrops when using Vault.',
		random_primaries='3',
		random_secondaries='1')
	omyrnsChain.save()
	omyrnsChain.affixes.add(mainStat)

	razorStrop = Belt(name='Razor Strop',
		pic='/assets/media/items/legendaries/armor/waist/belts/razor_strop.png',
		unique='Picking up a Health Globe releases an explosion that deals <span>300 - 400%</span> weapon damage as Fire to enemies within <span class="silver">20</span> yards.',
		random_primaries='3')
	razorStrop.save()
	razorStrop.affixes.add(mainStat, itemPickup)

	sacredHarness = Belt(name='Sacred Harness',
		pic='/assets/media/items/legendaries/armor/waist/belts/sacred_harness.png',
		unique='Judgment gains the effect of the Debilitate rune and is cast at your landing location when casting Falling Sword.',
		random_primaries='3',
		random_secondaries='1')
	sacredHarness.save()
	sacredHarness.affixes.add(mainStat)

	saffronWrap = Belt(name='Saffron Wrap',
		pic='/assets/media/items/legendaries/armor/waist/belts/saffron_wrap.png',
		random_primaries='2',
		random_secondaries='1')
	saffronWrap.save()
	saffronWrap.affixes.add(mainStat, rcr, saffronCCReduction)

	sashOfKnives = Belt(name='Sash of Knives',
		pic='/assets/media/items/legendaries/armor/waist/belts/sash_of_knives.png',
		unique='With every attack, you throw a dagger at a nearby enemy for <span>500 - 650%</span> weapon damage as Physical.',
		random_primaries='3',
		random_secondaries='1')
	sashOfKnives.save()
	sashOfKnives.affixes.add(mainStat)

	seborsNightmare = Belt(name='Sebor\'s Nightmare',
		pic='/assets/media/items/legendaries/armor/waist/belts/sebors_nightmare.png',
		unique='Haunt is cast on all nearby enemies when you open a chest.',
		random_primaries='3')
	seborsNightmare.save()
	seborsNightmare.affixes.add(mainStat, itemPickup)

	stringOfEars = Belt(name='String of Ears',
		pic='/assets/media/items/legendaries/armor/waist/belts/string_of_ears.png',
		random_primaries='3',
		random_secondaries='1')
	stringOfEars.save()
	stringOfEars.affixes.add(mainStat, stringReducedMeleeDmg)

	theWitchingHour = Belt(name='The Witching Hour',
		pic='/assets/media/items/legendaries/armor/waist/belts/the_witching_hour.png',
		random_primaries='2',
		random_secondaries='2')
	theWitchingHour.save()
	theWitchingHour.affixes.add(witchingIAS, witchingCHD)

	thundergodsVigor = Belt(name='Thundergod\'s Vigor',
		pic='/assets/media/items/legendaries/armor/waist/belts/thundergods_vigor.png',
		unique='Blocking, dodging or being hit causes you to discharge bolts of electricity that deal <span>100 - 130%</span> weapon damage as Lightning.',
		random_primaries='1')
	thundergodsVigor.save()
	thundergodsVigor.affixes.add(mainStat, vita, thundergodsLightDmg, thundergodsLightRes)

	vigilanteBelt = Belt(name='Vigilante Belt',
		pic='/assets/media/items/legendaries/armor/waist/belts/vigilante_belt.png',
		random_primaries='2',
		random_secondaries='2')
	vigilanteBelt.save()
	vigilanteBelt.affixes.add(mainStat, vigilanteCDR)


	for belt in Belt.objects.all():
		belt.slug = slugify(belt.name)
		belt.category = 'Belt'
		belt.save()

class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0017_gloves'),
    ]

    operations = [
    	migrations.RunPython(load_belts)
    ]
