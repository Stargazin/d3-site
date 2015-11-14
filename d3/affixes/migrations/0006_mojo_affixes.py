# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_mojo_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "MojoAffix")

	dmg = Affix(id=0,
		affix='dmg',
		is_primary=True,
		desc='<span>+340 - 370</span> -- <span>380 - 450</span> Damage',
		ancient='<span>+407 - 485</span> -- <span>495 - 600</span> Damage')
	dmg.save()

	inte = Affix(id=1,
		affix='inte',
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	vita = Affix(id=2,
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	life = Affix(id=3,
		affix='life',
		is_primary=True,
		desc='<span>+10 - 15%</span> Life')
	life.save()

	lps = Affix(id=4,
		affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	chc = Affix(id=5,
		affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	areaDmg = Affix(id=6,
		affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20-%</span> Area Damage')
	areaDmg.save()

	eliteDmg = Affix(id=7,
		affix='eliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>5.0 - 8.0%</span>')
	eliteDmg.save()

	bleedChance = Affix(id=8,
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	cdr = Affix(id=9,
		affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	rcr = Affix(id=10,
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%<span> Resource Cost Reduction')
	rcr.save()

	sockets = Affix(id=11,
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	manaRegen = Affix(id=12,
		affix='manaRegen',
		is_primary=True,
		desc='<span>+12.00 - 14.00</span> Mana Regeneratioin per Second')
	manaRegen.save()

	acidCloud = Affix(id=13,
		affix='acidCloud',
		is_primary=True,
		desc='Increase Acid Cloud damage by <span>10 - 15%</span>')
	acidCloud.save()

	corpseSpiders = Affix(id=14,
		affix='corpseSpiders',
		is_primary=True,
		desc='Increase Corpse Spiders damage by <span>10 - 15%</span>')
	corpseSpiders.save()

	fetishArmy = Affix(id=15,
		affix='fetishArmy',
		is_primary=True,
		desc='Increase Fetish Army damage by <span>10 - 15%</span>')
	fetishArmy.save()

	firebats = Affix(id=16,
		affix='firebats',
		is_primary=True,
		desc='Increase Fire Bats damage by <span>10 - 15%</span>')
	firebats.save()

	firebomb = Affix(id=17,
		affix='firebomb',
		is_primary=True,
		desc='Increase Fire Bomb damage by <span>10 - 15%</span>')
	firebomb.save()

	gargantuan = Affix(id=18,
		affix='gargantuan',
		is_primary=True,
		desc='Increase Gargantuan damage by <span>10 - 15%</span>')
	gargantuan.save()

	graspOfTheDead = Affix(id=19,
		affix='graspOfTheDead',
		is_primary=True,
		desc='Increase Grasp of the Dead damage by <span>10 - 15%</span>')
	graspOfTheDead.save()

	haunt = Affix(id=20,
		affix='haunt',
		is_primary=True,
		desc='Increase Haunt damage by <span>10 - 15%</span>')
	haunt.save()

	locustSwarm = Affix(id=21,
		affix='locustSwarm',
		is_primary=True,
		desc='Increase Locust Swarm damage by <span>10 - 15%</span>')
	locustSwarm.save()

	piranhas = Affix(id=22,
		affix='piranhas',
		is_primary=True,
		desc='Increase Piranhas damage by <span>10 - 15%</span>')
	piranhas.save()

	plagueOfToads = Affix(id=23,
		affix='plagueOfToads',
		is_primary=True,
		desc='Increase Plague of Toads damage by <span>10 - 15%</span>')
	plagueOfToads.save()

	poisonDart = Affix(id=24,
		affix='poisonDart',
		is_primary=True,
		desc='Increase Poison Dart damage by <span>10 - 15%</span>')
	poisonDart.save()

	sacrifice = Affix(id=25,
		affix='sacrifice',
		is_primary=True,
		desc='Increase Sacrifice damage by <span>10 - 15%</span>')
	sacrifice.save()

	spiritBarrage = Affix(id=26,
		affix='spiritBarrage',
		is_primary=True,
		desc='Increase Spirit Barrage damage by <span>10 - 15%</span>')
	spiritBarrage.save()

	summonZombieDogs = Affix(id=27,
		affix='summonZombieDogs',
		is_primary=True,
		desc='Increase Summon Zombie Dogs damage by <span>10 - 15%</span>')
	summonZombieDogs.save()

	wallOfDeath = Affix(id=28,
		affix='wallOfDeath',
		is_primary=True,
		desc='Increase Wall of Death damage by <span>10 - 15%</span>')
	wallOfDeath.save()

	zombieCharger = Affix(id=29,
		affix='zombieCharger',
		is_primary=True,
		desc='Increase Zombie Charger damage by <span>10 - 15%</span>')
	zombieCharger.save()


	maxMana = Affix(id=30,
		affix='maxMana',
		is_primary=False,
		desc='<span>+120 - 150</span> Max Mana')
	maxMana.save()

	fearChance = Affix(id=31,
		affix='fearChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(id=32,
		affix='stunChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(id=33,
		affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(id=34,
		affix='freezeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(id=35,
		affix='chillChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(id=36,
		affix='slowChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(id=37,
		affix='immobilizeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(id=38,
		affix='knockbackChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Knockback on Hit')
	knockbackChance.save()

	thorns = Affix(id=39,
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,200 - 2,600</span> damage')
	thorns.save()

	itemHealing = Affix(id=40,
		affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29,713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	killExp = Affix(id=41,
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(id=42,
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	durability = Affix(id=43,
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

	lvlReq = Affix(id=44,
		affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0005_quiver_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_mojo_affixes)
    ]
