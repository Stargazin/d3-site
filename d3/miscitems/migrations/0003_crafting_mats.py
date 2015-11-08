# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_crafting_mats(apps, schema_editor):
	Mat = apps.get_model("miscitems", "Material")

	reuseable_parts = Mat(id=0,
		name='Reusable Parts',
		#pic=,
		rarity='Normal',
		stack_amount=5000,
		desc='',
		notes='')
	reuseable_parts.save()

	arcane_dust = Mat(id=1,
		name='Arcane Dust',
		#pic=,
		rarity='Magic',
		stack_amount=5000,
		desc='',
		notes='')
	arcane_dust.save()

	veiled_crystal = Mat(id=2,
		name='Veiled Crystal',
		#pic=,
		rarity='Rare',
		stack_amount=5000,
		desc='',
		notes='')
	veiled_crystal.save()

	deaths_breath = Mat(id=3,
		name='Death\'s Breath',
		#pic=,
		rarity='Rare',
		stack_amount=5000,
		desc='',
		notes='')
	deaths_breath.save()

	forgotten_soul = Mat(id=4,
		name='Forgotten Soul',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	forgotten_soul.save()


	khanduran_rune = Mat(id=5,
		name='Khanduran Rune',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	khanduran_rune.save()

	caldeum_nightshade = Mat(id=6,
		name='Caldeum Nightshade',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	caldeum_nightshade.save()

	arreat_war_tapestry = Mat(id=7,
		name='Arreat War Tapestry',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	arreat_war_tapestry.save()

	corrupted_angel_flesh = Mat(id=8,
		name='Corrupted Angel Flesh',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	corrupted_angel_flesh.save()

	westmarch_holy_water = Mat(id=9,
		name='Westmarch Holy Water',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	westmarch_holy_water.save()


	#Machine of Bones -- Odeg -- Leoric and Maghda
	leorics_regret = Mat(id=10,
		name='Leoric\'s Regret',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	leorics_regret.save()

	#Machine of Gluttony -- Sokahr -- Rakanotha and Ghom
	vial_of_putridness = Mat(id=11,
		name='Vial of Putridness',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	vial_of_putridness.save()

	#Machine of War -- Xah'Rith -- Siegebreaker and Zoltan Kulle
	idol_of_terror = Mat(id=12,
		name='Idol of Terror',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	idol_of_terror.save()

	#Machine of Evil -- Nekarat -- Diablo + Random
	heart_of_evil = Mat(id=13,
		name='Heart of Evil',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	heart_of_evil.save()


#lvl 60 hf ammy
#drops for lvl 61-70
#have to be lvl 60 to get right machine
	#realm of discord -- act 1 -- Odeg
	writhing_spine = Mat(id=14,
		name='Writhing Spine',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	writhing_spine.save()

	#realm of chaos -- act 2 -- Sokahr
	devils_fang = Mat(id=15,
		name='Devil\'s Fang',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	devils_fang.save()

	#realm of turmoil -- act 3 -- Xah'Rith
	vengeful_eye = Mat(id=16,
		name='Vengeful Eye',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	vengeful_eye.save()


	essence_of_diamond = Mat(id=17,
		name='Essence of Diamond',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	essence_of_diamond.save()

	essence_of_topaz = Mat(id=18,
		name='Essence of Topaz',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	essence_of_topaz.save()

	essence_of_ruby = Mat(id=19,
		name='Essence of Ruby',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	essence_of_ruby.save()

	essence_of_amethyst = Mat(id=20,
		name='Essence of Amethyst',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	essence_of_amethyst.save()

	essence_of_emerald = Mat(id=21,
		name='Essence of Emerald',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		desc='',
		notes='')
	essence_of_emerald.save()



#legacy
	# black_mushroom

	# leorics_shinbone

	# wirts_bell

	# liquid_rainbow

	# gibbering_gemstone


class Migration(migrations.Migration):

    dependencies = [
        ('miscitems', '0002_auto_20151106_2036'),
    ]

    operations = [
    	migrations.RunPython(load_crafting_mats),
    ]
