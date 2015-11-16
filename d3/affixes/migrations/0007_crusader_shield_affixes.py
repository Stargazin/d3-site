# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_crusader_shield_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "CrusaderShieldAffix")

	sockets = Affix(affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	stre = Affix(affix='stre',
		is_primary=True,
		desc='<span>+626 - 725</span> Strength',
		ancient='<span>+825 - 1,000</span> Strength')
	stre.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+626 - 725</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	chc = Affix(affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	cdr = Affix(affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	eliteDmg = Affix(affix='eliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>5.0 - 8.0%</span>')
	eliteDmg.save()

	areaDmg = Affix(affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20%</span> Area Damage')
	areaDmg.save()

	bleedChance = Affix(affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	armor = Affix(affix='armor',
		is_primary=True,
		desc='<span>+559 - 595</span> Armor',
		ancient='<span>+654 - 775</span> Armor')
	armor.save()

	allRes = Affix(affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	blockChance = Affix(affix='blockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	blockChance.save()

	reducedEliteDmg = Affix(affix='reducedEliteDmg',
		is_primary=True,
		desc='<span>+10.0 - 11.0%</span> Elite Damage Reduction')
	reducedEliteDmg.save()

	life = Affix(affix='life',
		is_primary=True,
		desc='<span>+10 - 18%</span> Life')
	life.save()

	lps = Affix(affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	lifePerWrath = Affix(affix='lifePerWrath',
		is_primary=True,
		desc='<span>+1,077 - 1,276</span> Life per Wrath spent',
		ancient='<span>+1,408 - 1,660</span> Life per Wrath spent')
	lifePerWrath.save()

	rcr = Affix(affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	wrathRegen = Affix(affix='wrathRegen',
		is_primary=True,
		desc='<span>+1.85 - 2.00</span> Wrath Regeneration')
	wrathRegen.save()

	blessedHammer = Affix(affix='blessedHammer',
		is_primary=True,
		desc='Increase Blessed Hammer damage by <span>10 - 15%</span>')
	blessedHammer.save()

	blessedShield = Affix(affix='blessedShield',
		is_primary=True,
		desc='Increase Blessed Shield damage by <span>10 - 15%</span>')
	blessedShield.save()

	bombardment = Affix(affix='bombardment',
		is_primary=True,
		desc='Increase Bombardment damage by <span>10 - 15%</span>')
	bombardment.save()

	condemn = Affix(affix='condemn',
		is_primary=True,
		desc='Increase Condemn damage by <span>10 - 15%</span>')
	condemn.save()

	fallingSword = Affix(affix='fallingSword',
		is_primary=True,
		desc='Increase Falling Sword damage by <span>10 - 15%</span>')
	fallingSword.save()

	fistOfTheHeavens = Affix(affix='fistOfTheHeavens',
		is_primary=True,
		desc='Increase Fist of the  Heavens damage by <span>10 - 15%</span>')
	fistOfTheHeavens.save()

	heavensFury = Affix(affix='heavensFury',
		is_primary=True,
		desc='Increase Heaven\'s Fury damage by <span>10 - 15%</span>')
	heavensFury.save()

	justice = Affix(affix='justice',
		is_primary=True,
		desc='Increase Justice damage by <span>10 - 15%</span>')
	justice.save()

	phalanx = Affix(affix='phalanx',
		is_primary=True,
		desc='Increase Phalanx damage by <span>10 - 15%</span>')
	phalanx.save()

	punish= Affix(affix='punish',
		is_primary=True,
		desc='Increase Punish damage by <span>10 - 15%</span>')
	punish.save()

	shieldBash= Affix(affix='shieldBash',
		is_primary=True,
		desc='Increase Shield Bash damage by <span>10 - 15%</span>')
	shieldBash.save()

	slash = Affix(affix='slash',
		is_primary=True,
		desc='Increase Slash damage by <span>10 - 15%</span>')
	slash.save()

	smite = Affix(affix='smite',
		is_primary=True,
		desc='Increase Smite damage by <span>10 - 15%</span>')
	smite.save()

	sweepAttack = Affix(affix='sweepAttack',
		is_primary=True,
		desc='Increase Sweep Attack damage by <span>10 - 15%</span>')
	sweepAttack.save()


	eleRes = Affix(affix='eleRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Resistance to {<span>One Element</span>}',
		ancient='<span>+176 - 210</span> Resistance to {<span>One Element</span>}')
	eleRes.save()

	physRes = Affix(affix='physRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Physical Resistance',
		ancient='<span>+176 - 210</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(affix='coldRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Cold Resistance',
		ancient='<span>+176 - 210</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(affix='fireRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Fire Resistance',
		ancient='<span>+176 - 210</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(affix='lightRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Lightning Resistance',
		ancient='<span>+176 - 210</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(affix='poisRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Poison Resistance',
		ancient='<span>+176 - 210</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(affix='arcaneRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Arcane Resistance',
		ancient='<span>+176 - 210</span> Arcane Resistance')
	arcaneRes.save()

	maxWrath = Affix(affix='maxWrath',
		is_primary=False,
		desc='<span>+8 - 10</span> Max Wrath')
	maxWrath.save()

	reducedRangeDmg = Affix(affix='reducedRangeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Ranged Damage Reduction')
	reducedRangeDmg.save()

	reducedMeleeDmg = Affix(affix='reducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	reducedMeleeDmg.save()

	ccReduction = Affix(affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	itemHealing = Affix(affix='itemHealing',
		is_primary=False,
		desc='<span>+</span> Healing from Health Globes and Potions',
		ancient='<span>+3</span> Healing from Health Globes and Potions')
	itemHealing.save()

	fearChance = Affix(affix='fearChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(affix='stunChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(affix='freezeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(affix='chillChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(affix='slowChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(affix='immobilizeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(affix='knockbackChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Knockback on Hit')
	knockbackChance.save()

	extraGold = Affix(affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	thorns = Affix(affix='thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()

	killExp = Affix(affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	lvlReq = Affix(affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()

	durability = Affix(affix='durability',
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
