# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


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


	for mojo in Mojo.objects.all():
		mojo.slug = slugify(Mojo.name)
		mojo.category = 'Mojo'
		mojo.save()


class Migration(migrations.Migration):
    dependencies = [
        ('legendaries', '0005_quivers'),
    ]

    operations = [
    	migrations.RunPython(load_mojos)
    ]
