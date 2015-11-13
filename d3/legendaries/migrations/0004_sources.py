# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_sources(apps, schema_editor):
	Source = apps.get_model("legendaries", "Source")
	SourceAffix = apps.get_model("affixes", "SourceAffix")

	dmg = Affix.objects.get(affix='dmg')
	inte = Affix.objects.get(affix='inte')
	vita = Affix.objects.get(affix='vita')

	life = Affix.objects.get(affix='life')
	lps = Affix.objects.get(affix='lps')

	chc = Affix.objects.get(affix='chc')
	areaDmg = Affix.objects.get(affix='areaDmg')
	eliteDmg = Affix.objects.get(affix='eliteDmg')

	bleedChance = Affix.objects.get(affix='bleedChance')

	cdr = Affix.objects.get(affix='cdr')
	rcr = Affix.objects.get(affix='rcr')
	sockets = Affix.objects.get(affix='sockets')

	apCrit = Affix.objects.get(affix='apCrit')

	arcaneOrb = Affix.objects.get(affix='arcaneOrb')
	electrocute = Affix.objects.get(affix='electrocute')
	rayOfFrost = Affix.objects.get(affix='rayOfFrost')
	spectralBlade = Affix.objects.get(affix='spectralBlade')
	blackHole = Affix.objects.get(affix='blackHole')
	meteor = Affix.objects.get(affix='meteor')
	waveOfForce = Affix.objects.get(affix='waveOfForce')
	arcaneTorrent = Affix.objects.get(affix='arcaneTorrent')
	shockPulse = Affix.objects.get(affix='shockPulse')
	familiar = Affix.objects.get(affix='familiar')
	magicMissle = Affix.objects.get(affix='magicMissle')
	energyTwister = Affix.objects.get(affix='energyTwister')
	blizzard = Affix.objects.get(affix='blizzard')
	disintegrate = Affix.objects.get(affix='disintegrate')
	explosiveBlast = Affix.objects.get(affix='explosiveBlast')
	hydra = Affix.objects.get(affix='hydra')


	maxAP = Affix.objects.get(affix='maxAP')

	fearChance = Affix.objects.get(affix='fearChance')
	stunChance = Affix.objects.get(affix='stunChance')
	blindChance = Affix.objects.get(affix='blindChance')
	freezeChance = Affix.objects.get(affix='freezeChance')
	chillChance = Affix.objects.get(affix='chillChance')
	slowChance = Affix.objects.get(affix='slowChance')
	immobilizeChance = Affix.objects.get(affix='immobilizeChance')
	knockbackChance = Affix.objects.get(affix='knockbackChance')

	thorns = Affix.objects.get(affix='thorns')
	itemHealing = Affix.objects.get(affix='itemHealing')

	killExp = Affix.objects.get(affix='killExp')
	extraGold = Affix.objects.get(affix='extraGold')
	durability = Affix.objects.get(affix='durability')
	lvlReq = Affix.objects.get(affix='lvlReq')


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0003_rings'),
    ]

    operations = [
    	migrations.RunPython(load_sources)
    ]
