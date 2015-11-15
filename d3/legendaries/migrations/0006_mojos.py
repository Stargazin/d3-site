# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_mojos(apps, schema_editor):
	Mojo = apps.get_model("legendaries", "Mojo")
	Affix = apps.get_model("affixes", "MojoAffix")

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
	manaRegen = Affix.objects.get(affix='manaRegen')

	acidCloud = Affix.objects.get(affix='acidCloud')
	corpseSpiders = Affix.objects.get(affix='corpseSpiders')
	fetishArmy = Affix.objects.get(affix='fetishArmy')
	firebats = Affix.objects.get(affix='firebats')
	firebomb = Affix.objects.get(affix='firebomb')
	gargantuan = Affix.objects.get(affix='gargantuan')
	graspOfTheDead = Affix.objects.get(affix='graspOfTheDead')
	haunt = Affix.objects.get(affix='haunt')
	locustSwarm = Affix.objects.get(affix='locustSwarm')
	piranhas = Affix.objects.get(affix='piranhas')
	plagueOfToads = Affix.objects.get(affix='plagueOfToads')
	poisonDart = Affix.objects.get(affix='poisonDart')
	sacrifice = Affix.objects.get(affix='sacrifice')
	spiritBarrage = Affix.objects.get(affix='spiritBarrage')
	summonZombieDogs = Affix.objects.get(affix='summonZombieDogs')
	wallOfDeath = Affix.objects.get(affix='wallOfDeath')
	zombieCharger = Affix.objects.get(affix='zombieCharger')


	maxMana = Affix.objects.get(affix='maxMana')

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


	gazingDemise = Mojo(name='Gazing Demise',
		pic='/assets/media/items/legendaries/offhands/mojos/gazing_demise.png',
		unique='',
		random_primaries='1',
		random_secondaries='2')
	gazingDemise.save()
	gazingDemise.affixes.add(dmg, inte, lps, manaRegen)

	henrisPerquisition = Mojo(name='Henri\'s Perquisition',
		pic='/assets/media/items/legendaries/offhands/mojos/henris_perquisition.png',
		unique='The first time an enemy deals damage to you, reduce that damage by <span>60 - 80%</span> and Charm the enemy for <span class="silver>3</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	henrisPerquisition.save()
	henrisPerquisition.affixes.add(dmg, inte, chc, durability)

	homunculus = Mojo(name='homunculus',
		pic='/assets/media/items/legendaries/offhands/mojos/homunculus.png',
		unique='A Zombie Dog is automatically summoned to your side every <span class="silver>2</span> seconds.',
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
		unique='Increases Gold and Health Pickup by <span class="silver">20</span> Yards.',
		random_primaries='1')
	thingOfTheDeep.save()
	thingOfTheDeep.affixes.add(dmg, inte, chc, manaRegen, maxMana)

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
