# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_shields(apps, schema_editor):
	Shield = apps.get_model("legendaries", "Shield")
	Affix = apps.get_model("affixes", "ShieldAffix")

	mainStat = Affix.objects.get(affix='mainStat')
	vita = Affix.objects.get(affix='vita')

	allRes = Affix.objects.get(affix='allRes')
	blockChance = Affix.objects.get(affix='blockChance')


	thorns = Affix.objects.get(affix='thorns')


	lidlessEleDmg = Affix.objects.get(affix='lidlessEleDmg')
	lidlessMaxResource = Affix.objects.get(affix='lidlessMaxResource')
	stormReducedMeleeDmg = Affix.objects.get(affix='stormReducedMeleeDmg')


	covensCriterion = Shield(name='Coven\'s Criterion',
		pic='/assets/media/items/legendaries/offhands/shields/covens_criterion.png',
		unique='You take <span>45 - 60%</span> less damage from blocked attacks.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='21.0 - 31.0%')
	covensCriterion.save()
	covensCriterion.affixes.add(vita, blockChance)

	defenderOfWestmarch = Shield(name='Defender Of Westmarch',
		pic='/assets/media/items/legendaries/offhands/shields/defender_of_westmarch.png',
		unique='Blocks have a chance of summoning a charging wolf that deals <span>800 - 1000%</span> weapon damage to all enemies it passes through.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='21.0 - 31.0%')
	defenderOfWestmarch.save()
	defenderOfWestmarch.affixes.add(mainStat, blockChance)

	denial = Shield(name='denial',
		pic='/assets/media/items/legendaries/offhands/shields/denial.png',
		unique='Each enemy hit by your Sweep Attack increases the damage of your next Sweep Attack by <span class="silver">30 - 40%</span>, stacking up to <span>5</span> times.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	denial.save()
	denial.affixes.add(mainStat)

	eberliCharo = Shield(name='Eberli Charo',
		pic='/assets/media/items/legendaries/offhands/shields/eberli_charo.png',
		unique='Reduces the cooldown of Heaven\'s Fury by <span>45 - 50%</span>.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	eberliCharo.save()
	eberliCharo.affixes.add(mainStat)

	freezeOfDeflection = Shield(name='Freeze Of Deflection',
		pic='/assets/media/items/legendaries/offhands/shields/freeze_of_deflection.png',
		unique='Blocking an attack has a chance to Freeze the attacker for <span>0.5 - 1.5</span> seconds.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	freezeOfDeflection.save()
	freezeOfDeflection.affixes.add(mainStat)

	ivoryTower = Shield(name='Ivory Tower',
		pic='/assets/media/items/legendaries/offhands/shields/ivory_tower.png',
		unique='Blocks release forward a Fires of Heaven.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	ivoryTower.save()
	ivoryTower.affixes.add(mainStat, vita)

	lidlessWall = Shield(name='Lidless Wall',
		pic='/assets/media/items/legendaries/offhands/shields/lidless_wall.png',
		random_primaries='2',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	lidlessWall.save()
	lidlessWall.affixes.add(mainStat, lidlessEleDmg, lidlessMaxResource)

	stormshield = Shield(name='stormshield',
		pic='/assets/media/items/legendaries/offhands/shields/stormshield.png',
		random_primaries='3',
		random_secondaries='1',
		block_chance='19.0 - 24.0%')
	stormshield.save()
	stormshield.affixes.add(mainStat, stormReducedMeleeDmg)

	votoyiasSpiker = Shield(name='Vo\'Toyias Spiker',
		pic='/assets/media/items/legendaries/offhands/shields/votoyias_spiker.png',
		unique='Enemies affected by Provoke take double damage from Thorns.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	votoyiasSpiker.save()
	votoyiasSpiker.affixes.add(mainStat, thorns)

	wallOfBone = Shield(name='Wall Of Bone',
		pic='/assets/media/items/legendaries/offhands/shields/wall_of_man.png',
		unique='<span>20 - 30%</span> chance to be protected by a shield of bones when you are hit.',
		random_primaries='4',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	wallOfBone.save()
	# wallOfBone.affixes.add()











	for shield in Shield.objects.all():
		shield.slug = slugify(shield.name)
		shield.category = 'Shield'
		shield.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0007_crusader_shields'),
    ]

    operations = [
    	migrations.RunPython(load_shields)
    ]
