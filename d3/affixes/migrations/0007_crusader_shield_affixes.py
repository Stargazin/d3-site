# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_crusader_shield_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "CrusaderShieldAffix")

	sockets = Affix(id=0,
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	stre = Affix(id=1,
		affix='stre',
		is_primary=True,
		desc='<span>+626 - 725</span> Strength',
		ancient='<span>+825 - 1,000</span> Strength')
	stre.save()

	vita = Affix(id=2,
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 725</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	armor = Affix(id=3,
		affix='armor',
		is_primary=True,
		desc='<span>+559 - 595</span> Armor',
		ancient='<span>+654 - 775</span> Armor')
	armor.save()

	allRes = Affix(id=4,
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	blockChance = Affix(id=5,
		affix='blockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	blockChance.save()

	reducedEliteDmg = Affix(id=6,
		affix='reducedEliteDmg',
		is_primary=True,
		desc='<span>+10.0 - 11.0%</span> Elite Damage Reduction')
	reducedEliteDmg.save()

	life = Affix(id=7,
		affix='life',
		is_primary=True,
		desc='<span>+10 - 18%</span> Life')
	life.save()

	lps = Affix(id=8,
		affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	lifePerWrath = Affix(id=9,
		affix='lifePerWrath',
		is_primary=True,
		desc='<span>+1,077 - 1,276</span> Life per Wrath spent',
		ancient='<span>+1,408 - 1,660</span> Life per Wrath spent')
	lifePerWrath.save()

	chc = Affix(id=10,
		affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	cdr = Affix(id=11,
		affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	eliteDmg = Affix(id=12,
		affix='eliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>5.0 - 8.0%</span>')
	eliteDmg.save()

	areaDmg = Affix(id=13,
		affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20%</span> Area Damage')
	areaDmg.save()

	bleedChance = Affix(id=14,
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	rcr = Affix(id=15,
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%<span> Resource Cost Reduction')
	rcr.save()

	wrathRegen = Affix(id=16,
		affix='wrathRegen',
		is_primary=True,
		desc='<span>+1.85 - 2.00</span> Wrath Regeneration')
	wrathRegen.save()

	blessedHammer = Affix(id=17,
		affix='blessedHammer',
		is_primary=True,
		desc='Increase Blessed Hammer damage by <span>10 - 15%</span>')
	blessedHammer.save()

	blessedShield = Affix(id=18,
		affix='blessedShield',
		is_primary=True,
		desc='Increase Blessed Shield damage by <span>10 - 15%</span>')
	blessedShield.save()

	bombardment = Affix(id=19,
		affix='bombardment',
		is_primary=True,
		desc='Increase Bombardment damage by <span>10 - 15%</span>')
	bombardment.save()

	condemn = Affix(id=20,
		affix='condemn',
		is_primary=True,
		desc='Increase Condemn damage by <span>10 - 15%</span>')
	condemn.save()

	fallingSword = Affix(id=21,
		affix='fallingSword',
		is_primary=True,
		desc='Increase Falling Sword damage by <span>10 - 15%</span>')
	fallingSword.save()

	fistOfTheHeavens = Affix(id=22,
		affix='fistOfTheHeavens',
		is_primary=True,
		desc='Increase Fist of the  Heavens damage by <span>10 - 15%</span>')
	fistOfTheHeavens.save()

	heavensFury = Affix(id=23,
		affix='heavensFury',
		is_primary=True,
		desc='Increase Heaven\'s Fury damage by <span>10 - 15%</span>')
	heavensFury.save()

	justice = Affix(id=24,
		affix='justice',
		is_primary=True,
		desc='Increase Justice damage by <span>10 - 15%</span>')
	justice.save()

	phalanx = Affix(id=25,
		affix='phalanx',
		is_primary=True,
		desc='Increase Phalanx damage by <span>10 - 15%</span>')
	phalanx.save()

	punish= Affix(id=26,
		affix='punish',
		is_primary=True,
		desc='Increase Punish damage by <span>10 - 15%</span>')
	punish.save()

	shieldBash= Affix(id=27,
		affix='shieldBash',
		is_primary=True,
		desc='Increase Shield Bash damage by <span>10 - 15%</span>')
	shieldBash.save()

	slash = Affix(id=28,
		affix='slash',
		is_primary=True,
		desc='Increase Slash damage by <span>10 - 15%</span>')
	slash.save()

	smite = Affix(id=29,
		affix='smite',
		is_primary=True,
		desc='Increase Smite damage by <span>10 - 15%</span>')
	smite.save()

	sweepAttack = Affix(id=30,
		affix='sweepAttack',
		is_primary=True,
		desc='Increase Sweep Attack damage by <span>10 - 15%</span>')
	sweepAttack.save()


	eleRes = Affix(id=31,
		affix='eleRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Resistance to {<span>One Element</span>}',
		ancient='<span>+176 - 210</span> Resistance to {<span>One Element</span>}')
	eleRes.save()

	physRes = Affix(id=32,
		affix='physRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Physical Resistance',
		ancient='<span>+176 - 210</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(id=33,
		affix='coldRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Cold Resistance',
		ancient='<span>+176 - 210</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(id=34,
		affix='fireRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Fire Resistance',
		ancient='<span>+176 - 210</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(id=35,
		affix='lightRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Lightning Resistance',
		ancient='<span>+176 - 210</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(id=36,
		affix='poisRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Poison Resistance',
		ancient='<span>+176 - 210</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(id=37,
		affix='arcaneRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Arcane Resistance',
		ancient='<span>+176 - 210</span> Arcane Resistance')
	arcaneRes.save()

	maxWrath = Affix(id=38,
		affix='maxWrath',
		is_primary=False,
		desc='<span>+8 - 10</span> Max Wrath')
	maxWrath.save()

	reducedRangeDmg = Affix(id=39,
		affix='reducedRangeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Ranged Damage Reduction')
	reducedRangeDmg.save()

	reducedMeleeDmg = Affix(id=40,
		affix='reducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	reducedMeleeDmg.save()

	ccReduction = Affix(id=41,
		affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	itemHealing = Affix(id=42,
		affix='itemHealing',
		is_primary=False,
		desc='<span>+</span> Healing from Health Globes and Potions',
		ancient='<span>+3</span> Healing from Health Globes and Potions')
	itemHealing.save()

	fearChance = Affix(id=43,
		affix='fearChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(id=44,
		affix='stunChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(id=45,
		affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(id=46,
		affix='freezeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(id=47,
		affix='chillChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(id=48,
		affix='slowChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(id=49,
		affix='immobilizeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(id=50,
		affix='knockbackChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Knockback on Hit')
	knockbackChance.save()

	extraGold = Affix(id=51,
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	thorns = Affix(id=52,
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()

	killExp = Affix(id=53,
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	lvlReq = Affix(id=54,
		affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()

	durability = Affix(id=55,
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0006_mojo_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_crusader_shield_affixes)
    ]
