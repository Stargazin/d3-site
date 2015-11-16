# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_source_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "SourceAffix")

	dmg = Affix(affix='dmg',
		is_primary=True,
		desc='<span>+340 - 370</span> -- <span>380 - 450</span> Damage',
		ancient='<span>+407- 485</span> -- <span>495 - 600</span> Damage')
	dmg.save()

	inte = Affix(affix='inte',
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
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
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>300 - 400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	life = Affix(affix='life',
		is_primary=True,
		desc='<span>+10 - 15%</span> Life')
	life.save()

	lps = Affix(affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	rcr = Affix(affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	apCrit = Affix(affix='apCrit',
		is_primary=True,
		desc='<span>+3 - 4</span> Arcane Power on Critical Hits')
	apCrit.save()

	sockets = Affix(affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Wizard Skills
#==============================================================================

	arcaneOrb = Affix(affix='arcaneOrb',
		is_primary=True,
		desc='Increase Arcane Orb damage by <span>10 - 15%</span>')
	arcaneOrb.save()

	electrocute = Affix(affix='electrocute',
		is_primary=True,
		desc='Increase Electrocute damage by <span>10 - 15%</span>')
	electrocute.save()

	rayOfFrost = Affix(affix='rayOfFrost',
		is_primary=True,
		desc='Increase Ray of Frost damage by <span>10 - 15%</span>')
	rayOfFrost.save()

	spectralBlade = Affix(affix='spectralBlade',
		is_primary=True,
		desc='Increase Spectral Blade damage by <span>10 - 15%</span>')
	spectralBlade.save()

	blackHole = Affix(affix='blackHole',
		is_primary=True,
		desc='Increase Black Hole damage by <span>10 - 15%</span>')
	blackHole.save()

	meteor = Affix(affix='meteor',
		is_primary=True,
		desc='Increase Meteor damage by <span>10 - 15%</span>')
	meteor.save()

	waveOfForce = Affix(affix='waveOfForce',
		is_primary=True,
		desc='Increase Wave of Force damage by <span>10 - 15%</span>')
	waveOfForce.save()

	arcaneTorrent = Affix(affix='arcaneTorrent',
		is_primary=True,
		desc='Increase Arcane Torrent damage by <span>10 - 15%</span>')
	arcaneTorrent.save()

	shockPulse = Affix(affix='shockPulse',
		is_primary=True,
		desc='Increase Shock Pulse damage by <span>10 - 15%</span>')
	shockPulse.save()

	familiar = Affix(affix='familiar',
		is_primary=True,
		desc='Increase Familiar damage by <span>10 - 15%</span>')
	familiar.save()

	magicMissle = Affix(affix='magicMissle',
		is_primary=True,
		desc='Increase Magic Missle damage by <span>10 - 15%</span>')
	magicMissle.save()

	energyTwister = Affix(affix='energyTwister',
		is_primary=True,
		desc='Increase Energy Twister damage by <span>10 - 15%</span>')
	energyTwister.save()

	blizzard = Affix(affix='blizzard',
		is_primary=True,
		desc='Increase Blizzard damage by <span>10 - 15%</span>')
	blizzard.save()

	disintegrate = Affix(affix='disintegrate',
		is_primary=True,
		desc='Increase Disintegrate damage by <span>10 - 15%</span>')
	disintegrate.save()

	explosiveBlast = Affix(affix='explosiveBlast',
		is_primary=True,
		desc='Increase Explosive Blast damage by <span>10 - 15%</span>')
	explosiveBlast.save()

	hydra = Affix(affix='hydra',
		is_primary=True,
		desc='Increase Hydra damage by <span>10 - 15%</span>')
	hydra.save()

#Secondaries
#==============================================================================
#==============================================================================

	maxAP = Affix(affix='maxAP',
		is_primary=False,
		desc='<span>+10 - 14</span> Max Arcane Power')
	maxAP.save()


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


	thorns = Affix(affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,220 - 2,600</span> damage')
	thorns.save()

	itemHealing = Affix(affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29.713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()


	killExp = Affix(affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	durability = Affix(affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

	lvlReq = Affix(affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()


#Winter Flurry
	winterColdDmg = Affix(affix='winterColdDmg',
		is_primary=True,
		desc='Cold skills deal <span>15 - 20%</span> more damage')
	winterColdDmg.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()
		else:
			pass


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0003_ring_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_source_affixes)
    ]
