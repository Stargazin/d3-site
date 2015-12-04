# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_crafting_mats(apps, schema_editor):
	Mat = apps.get_model("miscitems", "Material")

	#Machine of Bones -- Odeg -- Leoric and Maghda
	leoricsRegret = Mat(name='Leoric\'s Regret',
		category='Hellfire Material',
		pic='/assets/media/items/mats/leorics_regret.png',
		unique='Act <span class="silver">I</span> -- Machine of Bones dropped by Odeg the Keywarden in the Fields of Misery')
	leoricsRegret.save()

	#Machine of Gluttony -- Sokahr -- Rakanotha and Ghom
	vialOfPutridness = Mat(name='Vial of Putridness',
		category='Hellfire Material',
		pic='/assets/media/items/mats/vial_of_putridness.png',
		unique='Act <span class="silver">II</span> -- Machine of Gluttony dropped by Sokahr the Keywarden in the Dahlgur Oasis')
	vialOfPutridness.save()

	#Machine of War -- Xah'Rith -- Siegebreaker and Zoltan Kulle
	idolOfTerror = Mat(name='Idol of Terror',
		category='Hellfire Material',
		pic='/assets/media/items/mats/idol_of_terror.png',
		unique='Act <span class="silver">III</span> -- Machine of War dropped by Xah\'Rith the Keywarden in Stonefort')
	idolOfTerror.save()

	#Machine of Evil -- Nekarat -- Diablo + Random
	heartOfEvil = Mat(name='Heart of Evil',
		category='Hellfire Material',
		pic='/assets/media/items/mats/heart_of_evil.png',
		unique='Act <span class="silver">IV</span> -- Machine of Evil dropped by Nekarat the Keywarden in the Gardens of Hope 2nd Tier')
	heartOfEvil.save()


	khanduranRune = Mat(name='Khanduran Rune',
		category='Horadric Cache Material',
		pic='/assets/media/items/mats/khanduran_rune.png',
		unique='Act <span class="silver">I</span> Horadric Caches')
	khanduranRune.save()

	caldeumNightshade = Mat(name='Caldeum Nightshade',
		category='Horadric Cache Material',
		pic='/assets/media/items/mats/caldeum_nightshade.png',
		unique='Act <span class="silver">II</span> Horadric Caches')
	caldeumNightshade.save()

	arreatWarTapestry = Mat(name='Arreat War Tapestry',
		category='Horadric Cache Material',
		pic='/assets/media/items/mats/arreat_war_tapestry.png',
		unique='Act <span class="silver">III</span> Horadric Caches')
	arreatWarTapestry.save()

	corruptedAngelFlesh = Mat(name='Corrupted Angel Flesh',
		category='Horadric Cache Material',
		pic='/assets/media/items/mats/corrupted_angel_flesh.png',
		unique='Act <span class="silver">IV</span> Horadric Caches')
	corruptedAngelFlesh.save()

	westmarchHolyWater = Mat(name='Westmarch Holy Water',
		category='Horadric Cache Material',
		pic='/assets/media/items/mats/westmarch_holy_water.png',
		unique='Act <span class="silver">V</span> Horadric Caches')
	westmarchHolyWater.save()


	reuseableParts = Mat(name='Reusable Parts',
		category='Crafting Material',
		pic='/assets/media/items/mats/reuseable_parts.png',
		rarity='N',
		unique='Salvage <span class="white">Normal</span> items at the Blacksmith')
	reuseableParts.save()

	arcaneDust = Mat(name='Arcane Dust',
		category='Crafting Material',
		pic='/assets/media/items/mats/arcane_dust.png',
		rarity='M',
		unique='Salvage <span class="blue">Magic</span> items at the Blacksmith')
	arcaneDust.save()

	veiledCrystal = Mat(name='Veiled Crystal',
		category='Crafting Material',
		pic='/assets/media/items/mats/veiled_crystal.png',
		rarity='R',
		unique='Salvage <span class="yellow">Rare</span> items at the Blacksmith')
	veiledCrystal.save()

	forgottenSoul = Mat(name='Forgotten Soul',
		category='Crafting Material',
		pic='/assets/media/items/mats/forgotten_soul.png',
		unique='Salvage <span class="orange">Legendary</span> items at the Blacksmith')
	forgottenSoul.save()

	deathsBreath = Mat(name='Death\'s Breath',
		category='Crafting Material',
		pic='/assets/media/items/mats/deaths_breath.png',
		rarity='R',
		unique='Dropped by Elite monsters')
	deathsBreath.save()


	essenceOfDiamond = Mat(name='Essence of Diamond',
		category='Gem Essence',
		pic='/assets/media/items/mats/essence_of_diamond.png',
		unique='Transmute gems into Diamonds',
		notes='Sold by Squirt the Peddler in Act <span class="silver">II</span>')
	essenceOfDiamond.save()

	essenceOfTopaz = Mat(name='Essence of Topaz',
		category='Gem Essence',
		pic='/assets/media/items/mats/essence_of_topaz.png',
		unique='Transmute gems into Topazes',
		notes='Sold by Squirt the Peddler in Act <span class="silver">II</span>')
	essenceOfTopaz.save()

	essenceOfRuby = Mat(name='Essence of Ruby',
		category='Gem Essence',
		pic='/assets/media/items/mats/essence_of_ruby.png',
		unique='Transmute gems into Rubies',
		notes='Sold by Squirt the Peddler in Act <span class="silver">II</span>')
	essenceOfRuby.save()

	essenceOfAmethyst = Mat(name='Essence of Amethyst',
		category='Gem Essence',
		pic='/assets/media/items/mats/essence_of_amethyst.png',
		unique='Transmute gems into Amethysts',
		notes='Sold by Squirt the Peddler in Act <span class="silver">II</span>')
	essenceOfAmethyst.save()

	essenceOfEmerald = Mat(name='Essence of Emerald',
		category='Gem Essence',
		pic='/assets/media/items/mats/essence_of_emerald.png',
		unique='Transmute gems into Emeralds',
		notes='Sold by Squirt the Peddler in Act <span class="silver">II</span>')
	essenceOfEmerald.save()

	#lvl 60 hf ammy -- drops for lvl 61-70
	#have to be lvl 60 to get right machine
		#realm of discord -- act 1 -- Odeg
		# writhing_spine
		# #realm of chaos -- act 2 -- Sokahr
		# devils_fang
		# #realm of turmoil -- act 3 -- Xah'Rith
		# vengeful_eye

	for mat in Mat.objects.all():
		mat.name_slug = slugify(mat.name)
		mat.category_slug = slugify(mat.category)
		mat.save()


def load_potions(apps, schema_editor):
	Potion = apps.get_model("miscitems", "Potion")

	Amplification = Potion(name='Bottomless Potion of Amplification',
	 	pic='/assets/media/items/potions/potion_of_amplification.png',
	 	unique='Increases healing from all sources by <span>20 - 25%</span> for <span class="silver">5</span> seconds')
	Amplification.save()

	Fear = Potion(name='Bottomless Potion of Fear',
	 	pic='/assets/media/items/potions/potion_of_fear.png',
	 	unique='Fears enemies within <span class="silver">12</span> yards for <span>3 - 4</span> seconds')
	Fear.save()

	KulleAid = Potion(name='Bottomless Potion of Kulle-Aid',
	 	pic='/assets/media/items/potions/potion_of_kulleaid.png',
	 	unique='Drinking Kulle-Aid allows you to break walls summoned by Waller elites for <span class="silver">5</span> seconds')
	KulleAid.save()

	Mutilation = Potion(name='Bottomless Potion of Mutilation',
	 	pic='/assets/media/items/potions/potion_of_mutilation.png',
	 	unique='Increases Life per Kill by <span>40,000 - 50,000</span> for <span class="silver">5</span> seconds')
	Mutilation.save()

	Regeneration = Potion(name='Bottomless Potion of Regeneration',
	 	pic='/assets/media/items/potions/potion_of_regeneration.png',
	 	unique='Restores an additional <span>75,000 - 100,000</span> Life over <span class="silver">5</span> seconds')
	Regeneration.save()

	Rejuvenation = Potion(name='Bottomless Potion of Rejuvenation',
	 	pic='/assets/media/items/potions/potion_of_rejuvenation.png',
	 	unique='Restores <span>20 - 30%</span> resource when used below <span class="silver">50%</span> health')
	Rejuvenation.save()

	Diamond = Potion(name='Bottomless Potion of the Diamond',
	 	pic='/assets/media/items/potions/potion_of_the_diamond.png',
	 	unique='Increases All Resist by <span>50 - 100</span> for <span class="silver">5</span> seconds')
	Diamond.save()

	Leech = Potion(name='Bottomless Potion of the Leech',
	 	pic='/assets/media/items/potions/potion_of_the_leech.png',
	 	unique='Increases Life per Hit by <span>15,000 - 20,000</span> for <span class="silver">5</span> seconds')
	Leech.save()

	Tower = Potion(name='Bottomless Potion of the Tower',
	 	pic='/assets/media/items/potions/potion_of_the_tower.png',
	 	unique='Increases Armor by <span class="silver">10%</span> for <span class="silver">5</span> seconds')
	Tower.save()

	for potion in Potion.objects.all():
		potion.name_slug = slugify(potion.name)
		potion.save()


def load_gems(apps, schema_editor):
	Gem = apps.get_model("miscitems", "Gem")

	baneOfThePowerful = Gem(name='Bane of the Powerful',
	 	pic='/assets/media/items/gems/bane_of_the_powerful.png',
	 	unique='Gain <span class="silver">20%</span> increased damage for <span>30.0 (+1.0)</span> seconds after killing an elite pack',
	 	rank_unique='Rank <span class="silver">25</span>: Increases damage against elites by <span class="silver">15.0%</span')
	baneOfThePowerful.save()

	baneOfTheStricken = Gem(name='Bane of the Stricken',
	 	pic='/assets/media/items/gems/bane_of_the_stricken.png',
	 	unique='Each attack you make against an enemy increases the damage it takes from your attacks by <span>0.80% (+0.01%)</span>',
	 	rank_unique='Rank <span class="silver">25</span>: Gain <span class="silver">25%</span> increased damage against bosses and Rift Guardians')
	baneOfTheStricken.save()

	baneOfTheTrapped = Gem(name='Bane of the Trapped',
	 	pic='/assets/media/items/gems/bane_of_the_trapped.png',
	 	unique='Increase damage against enemies under the effects of control-impairing effects by <span>15.00% (0.3%)</span>',
	 	rank_unique='Rank <span class="silver">25</span>: Gain an aura that reduces the movement speed of enemies within <span class="silver">15</span> yards by <span class="silver">30%</span>')
	baneOfTheTrapped.save()

	boonOfTheHoarder = Gem(name='Boon of the Hoarder',
	 	pic='/assets/media/items/gems/boon_of_the_hoarder.png',
	 	unique='<span>25.0% (+1.5%)</span> chance on killing an enemy to cause an explosion of gold',
	 	rank_unique='Rank <span class="silver">25</span>: Gain <span class="silver">30%</span> increased movement speed for <span class="silver">2</span> seconds after picking up gold')
	boonOfTheHoarder.save()

	enforcer = Gem(name='Enforcer',
	 	pic='/assets/media/items/gems/enforcer.png',
	 	unique='Increase the damage of your pets by <span>15.00% (+0.3%)</span>',
	 	rank_unique='Rank <span class="silver">25</span>: Your pets take <span class="silver">25%</span> less damage')
	enforcer.save()

	esotericAlteration = Gem(name='Esoteric Alteration',
	 	pic='/assets/media/items/gems/esoteric_alteration.png',
	 	unique='Gain <span>10.0% (+0.5%)</span> non-Physical damage reduction',
	 	rank_unique='Rank <span class="silver">25</span>: While below half Life, your resistances to Cold, Fire, Lightning, Poison, and Arcane are increased by <span class="silver">75%</span>')
	esotericAlteration.save()

	gemOfEase = Gem(name='Gem of Ease',
	 	pic='/assets/media/items/gems/gem_of_ease.png',
	 	unique='Monster kills grant <span>+500 (+50)</span> experience',
	 	rank_unique='Rank <span class="silver">25</span>: Level requirement of the item this gem is socketed into is set to <span class="silver">1</span>')
	gemOfEase.save()

	gemOfEfficaciousToxin = Gem(name='Gem of Efficacious Toxin',
	 	pic='/assets/media/items/gems/gem_of_efficacious_toxin.png',
	 	unique='Poison all enemies hit for <span>2000% (+50%)</span> weapon damage over <span class="silver">10</span> seconds',
	 	rank_unique='Rank <span class="silver">25</span>: All enemies you poison take <span class="silver">10%</span> increased damage from all sources')
	gemOfEfficaciousToxin.save()

	gogokOfSwiftness = Gem(name='Gogok of Swiftness',
	 	pic='/assets/media/items/gems/gogok_of_swiftness.png',
	 	unique='<span>50% (+1%)</span> chance on hit to gain Swiftness, increasing your Attack Speed by <span class="silver">1%</span> for <span class="silver">4</span> seconds. This effect stacks up to <span class="silver">15</span> times',
	 	rank_unique='Rank <span class="silver">25</span>: Gain <span class="silver">1%</span> Cooldown Reduction per stack of Swiftness')
	gogokOfSwiftness.save()

	iceblink = Gem(name='Iceblink',
	 	pic='/assets/media/items/gems/iceblink.png',
	 	unique='Your Cold skills now apply Chill effects and your Chill effects now Slow enemy movement by an additional <span>5.0% (+0.4%)</span>',
	 	rank_unique='Rank <span class="silver">25</span>: Gain <span class="silver">10%</span> increased Critical Hit Chance against Chilled and Frozen enemies')
	iceblink.save()

	invigoratingGemstone = Gem(name='Invigorating Gemstone',
	 	pic='/assets/media/items/gems/invigorating_gemstone.png',
	 	unique='While under any control-impairing effects, reduce all damage taken by <span>30.0% (+0.4%)</span>',
	 	rank_unique='Rank <span class="silver">25</span>: Heal for <span class="silver">20%</span> of maximum life when hit by a control-impairing effect')
	invigoratingGemstone.save()

	mirinaeTeardropOfTheStarweaver = Gem(name='Mirinae, Teardrop of the Starweaver',
	 	pic='/assets/media/items/gems/mirinae_teardrop_of_the_starweaver.png',
	 	unique='<span class="silver">15%</span> chance on hit to smite a nearby enemy for <span>2000% (+40%)</span> weapon damage as Holy',
	 	rank_unique='Rank <span class="silver">25</span>: Smite a nearby enemy every <span class="silver">5</span> seconds')
	mirinaeTeardropOfTheStarweaver.save()

	moltenWildebeestsGizzard = Gem(name='Molten Wildebeest\'s Gizzard',
	 	pic='/assets/media/items/gems/molten_wildebeests_gizzard.png',
	 	unique='Regenerates <span>10,000 (+1,000)</span> Life per Second',
	 	rank_unique='Rank <span class="silver">25</span>: After not taking damage for <span class="silver">4</span> seconds, gain an absorb shield for <span class="silver">200%</span> of your total Life per Second')
	moltenWildebeestsGizzard.save()

	moratorium = Gem(name='Moratorium',
	 	pic='/assets/media/items/gems/moratorium.png',
	 	unique='<span class="silver">25%</span> of all damage taken is instead staggered and dealt to you over <span>3.0 (+0.1)</span> seconds',
	 	rank_unique='Rank <span class="silver">25</span>: <span class="silver">10%</span> chance on kill to clear all staggered damage')
	moratorium.save()

	mutilationGuard = Gem(name='Mutilation Guard',
	 	pic='/assets/media/items/gems/mutilation_guard.png',
	 	unique='Gain <span>10.0% (+0.5%)</span> melee damage reduction',
	 	rank_unique='Rank <span class="silver">25</span>: While below <span class="silver">30%</span> Life, you may move unhindered through enemies')
	mutilationGuard.save()

	painEnhancer = Gem(name='Pain Enhancer',
	 	pic='/assets/media/items/gems/pain_enhancer.png',
	 	unique='Critical hits cause the enemy to bleed for <span>1200% (+30%)</span> weapon damage as Physical over <span class="silver">3</span> seconds',
	 	rank_unique='Rank <span class="silver">25</span>: Gain Blood Frenzy, granting you <span class="silver">3%</span> increased Attack Speed for each bleeding enemy within <span class="silver">20</span> yards')
	painEnhancer.save()

	simplicitysStrength = Gem(name='Simplicity\'s Strength',
	 	pic='/assets/media/items/gems/simplicitys_strength.png',
	 	unique='Increase the damage of primary skills by <span>25.0% (+0.5%)<span>',
	 	rank_unique='Rank <span class="silver">25</span>: Primary skills heal you for <span class="silver">2%</span> of maximum Life on hit')
	simplicitysStrength.save()

	taeguk = Gem(name='Taeguk',
	 	pic='/assets/media/items/gems/taeguk.png',
	 	unique='Gain <span class="silver">0.5%</span> increased damage for <span class="silver">3</span> seconds after spending primary resource. This effect stacks up to <span>20 (+1)</span> times',
	 	rank_unique='Rank <span class="silver">25</span>: Gain <span class="silver">0.5%</span> increased Armor for every stack')
	taeguk.save()

	wreathOfLightning = Gem(name='Wreath of Lightning',
	 	pic='/assets/media/items/gems/wreath_of_lightning.png',
	 	unique='<span class="silver">15%</span> chance on hit to gain a Wreath of Lightning, dealing <span>600% (+10%)</span> weapon damage as Lightning every second to nearby enemies for <span class="silver">3</span> seconds',
	 	rank_unique='Rank <span class="silver">25</span>: While under the effect of the Wreath of Lightning, gain <span class="silver">25%</span> increased movement speed')
	wreathOfLightning.save()

	zeisStoneOfVengeance = Gem(name='Zei\'s Stone of Vengeance',
	 	pic='/assets/media/items/gems/zeis_stone_of_vengeance.png',
	 	unique='Damage you deal is increased by <span>4.00% (+0.05%)</span> for every <span class="silver">10</span> yards between you and the enemy hit. Maximum <span>20.00% (+0.25%)</span> increase at <span class="silver">50</span> yards',
	 	rank_unique='Rank <span class="silver">25</span>: <span class="silver">20%</span> chance on hit to Stun the enemy for <span class="silver">1</span> second')
	zeisStoneOfVengeance.save()

	for gem in Gem.objects.all():
		gem.name_slug = slugify(gem.name)
		gem.save()


class Migration(migrations.Migration):

    dependencies = [
        ('miscitems', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_crafting_mats),
        migrations.RunPython(load_potions),
        migrations.RunPython(load_gems)
    ]
