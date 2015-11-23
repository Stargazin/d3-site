# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_crafting_mats(apps, schema_editor):
	Mat = apps.get_model("miscitems", "Material")

	reuseable_parts = Mat(name='Reusable Parts',
		#pic=,
		rarity='Normal',
		stack_amount=5000,
		unique='',
		notes='')
	reuseable_parts.save()

	arcane_dust = Mat(name='Arcane Dust',
		#pic=,
		rarity='Magic',
		stack_amount=5000,
		unique='',
		notes='')
	arcane_dust.save()

	veiled_crystal = Mat(name='Veiled Crystal',
		#pic=,
		rarity='Rare',
		stack_amount=5000,
		unique='',
		notes='')
	veiled_crystal.save()

	deaths_breath = Mat(name='Death\'s Breath',
		#pic=,
		rarity='Rare',
		stack_amount=5000,
		unique='',
		notes='')
	deaths_breath.save()

	forgotten_soul = Mat(name='Forgotten Soul',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	forgotten_soul.save()


	khanduran_rune = Mat(name='Khanduran Rune',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	khanduran_rune.save()

	caldeum_nightshade = Mat(name='Caldeum Nightshade',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	caldeum_nightshade.save()

	arreat_war_tapestry = Mat(name='Arreat War Tapestry',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	arreat_war_tapestry.save()

	corrupted_angel_flesh = Mat(name='Corrupted Angel Flesh',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	corrupted_angel_flesh.save()

	westmarch_holy_water = Mat(name='Westmarch Holy Water',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	westmarch_holy_water.save()


	#Machine of Bones -- Odeg -- Leoric and Maghda
	leorics_regret = Mat(name='Leoric\'s Regret',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	leorics_regret.save()

	#Machine of Gluttony -- Sokahr -- Rakanotha and Ghom
	vial_of_putridness = Mat(name='Vial of Putridness',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	vial_of_putridness.save()

	#Machine of War -- Xah'Rith -- Siegebreaker and Zoltan Kulle
	idol_of_terror = Mat(name='Idol of Terror',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	idol_of_terror.save()

	#Machine of Evil -- Nekarat -- Diablo + Random
	heart_of_evil = Mat(name='Heart of Evil',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	heart_of_evil.save()


#lvl 60 hf ammy
#drops for lvl 61-70
#have to be lvl 60 to get right machine
	#realm of discord -- act 1 -- Odeg
	writhing_spine = Mat(name='Writhing Spine',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	writhing_spine.save()

	#realm of chaos -- act 2 -- Sokahr
	devils_fang = Mat(name='Devil\'s Fang',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	devils_fang.save()

	#realm of turmoil -- act 3 -- Xah'Rith
	vengeful_eye = Mat(name='Vengeful Eye',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	vengeful_eye.save()


	essence_of_diamond = Mat(name='Essence of Diamond',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	essence_of_diamond.save()

	essence_of_topaz = Mat(name='Essence of Topaz',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	essence_of_topaz.save()

	essence_of_ruby = Mat(name='Essence of Ruby',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	essence_of_ruby.save()

	essence_of_amethyst = Mat(name='Essence of Amethyst',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	essence_of_amethyst.save()

	essence_of_emerald = Mat(name='Essence of Emerald',
		#pic=,
		rarity='Legendary',
		stack_amount=5000,
		unique='',
		notes='')
	essence_of_emerald.save()


#legacy
	# black_mushroom

	# leorics_shinbone

	# wirts_bell

	# liquid_rainbow

	# gibbering_gemstone

	for mat in Mat.objects.all():
		mat.name_slug = slugify(mat.name)
		mat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('miscitems', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(load_crafting_mats),
    ]
