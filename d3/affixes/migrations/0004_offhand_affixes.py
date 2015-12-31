# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_source_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

#Source primaries
#==============================================================================
#==============================================================================
	dmg = Affix(category='Sources',
		affix='dmg',
		is_primary=True,
		desc='<span>+340 - 370</span> -- <span>380 - 450</span> Damage',
		ancient='<span>+407- 485</span> -- <span>495 - 600</span> Damage')
	dmg.save()

	inte = Affix(category='Sources',
		affix='inte',
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	vita = Affix(category='Sources',
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	chc = Affix(category='Sources',
		affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	cdr = Affix(category='Sources',
		affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	eliteDmg = Affix(category='Sources',
		affix='eliteDmg',
		is_primary=True,
		desc='Increase damage against elites by <span>5.0 - 8.0%</span>')
	eliteDmg.save()

	areaDmg = Affix(category='Sources',
		affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20%</span> Area Damage')
	areaDmg.save()

	bleedChance = Affix(category='Sources',
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>300 - 400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	life = Affix(category='Sources',
		affix='life',
		is_primary=True,
		desc='<span>+10 - 15%</span> Life')
	life.save()

	lps = Affix(category='Sources',
		affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	rcr = Affix(category='Sources',
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	apCrit = Affix(category='Sources',
		affix='apCrit',
		is_primary=True,
		desc='<span>+3 - 4</span> Arcane Power on Critical Hits')
	apCrit.save()

	sockets = Affix(category='Sources',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Wizard Skills
#==============================================================================
	arcaneOrb = Affix(category='Sources',
		affix='arcaneOrb',
		is_primary=True,
		desc='Increase Arcane Orb damage by <span>10 - 15%</span>')
	arcaneOrb.save()

	electrocute = Affix(category='Sources',
		affix='electrocute',
		is_primary=True,
		desc='Increase Electrocute damage by <span>10 - 15%</span>')
	electrocute.save()

	rayOfFrost = Affix(category='Sources',
		affix='rayOfFrost',
		is_primary=True,
		desc='Increase Ray of Frost damage by <span>10 - 15%</span>')
	rayOfFrost.save()

	spectralBlade = Affix(category='Sources',
		affix='spectralBlade',
		is_primary=True,
		desc='Increase Spectral Blade damage by <span>10 - 15%</span>')
	spectralBlade.save()

	blackHole = Affix(category='Sources',
		affix='blackHole',
		is_primary=True,
		desc='Increase Black Hole damage by <span>10 - 15%</span>')
	blackHole.save()

	meteor = Affix(category='Sources',
		affix='meteor',
		is_primary=True,
		desc='Increase Meteor damage by <span>10 - 15%</span>')
	meteor.save()

	waveOfForce = Affix(category='Sources',
		affix='waveOfForce',
		is_primary=True,
		desc='Increase Wave of Force damage by <span>10 - 15%</span>')
	waveOfForce.save()

	arcaneTorrent = Affix(category='Sources',
		affix='arcaneTorrent',
		is_primary=True,
		desc='Increase Arcane Torrent damage by <span>10 - 15%</span>')
	arcaneTorrent.save()

	shockPulse = Affix(category='Sources',
		affix='shockPulse',
		is_primary=True,
		desc='Increase Shock Pulse damage by <span>10 - 15%</span>')
	shockPulse.save()

	familiar = Affix(category='Sources',
		affix='familiar',
		is_primary=True,
		desc='Increase Familiar damage by <span>10 - 15%</span>')
	familiar.save()

	magicMissle = Affix(category='Sources',
		affix='magicMissle',
		is_primary=True,
		desc='Increase Magic Missle damage by <span>10 - 15%</span>')
	magicMissle.save()

	energyTwister = Affix(category='Sources',
		affix='energyTwister',
		is_primary=True,
		desc='Increase Energy Twister damage by <span>10 - 15%</span>')
	energyTwister.save()

	blizzard = Affix(category='Sources',
		affix='blizzard',
		is_primary=True,
		desc='Increase Blizzard damage by <span>10 - 15%</span>')
	blizzard.save()

	disintegrate = Affix(category='Sources',
		affix='disintegrate',
		is_primary=True,
		desc='Increase Disintegrate damage by <span>10 - 15%</span>')
	disintegrate.save()

	explosiveBlast = Affix(category='Sources',
		affix='explosiveBlast',
		is_primary=True,
		desc='Increase Explosive Blast damage by <span>10 - 15%</span>')
	explosiveBlast.save()

	hydra = Affix(category='Sources',
		affix='hydra',
		is_primary=True,
		desc='Increase Hydra damage by <span>10 - 15%</span>')
	hydra.save()

#Source secondaries
#==============================================================================
#==============================================================================
	maxAP = Affix(category='Sources',
		affix='maxAP',
		is_primary=False,
		desc='<span>+10 - 14</span> Max Arcane Power')
	maxAP.save()


	fearChance = Affix(category='Sources',
		affix='fearChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(category='Sources',
		affix='stunChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(category='Sources',
		affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(category='Sources',
		affix='freezeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(category='Sources',
		affix='chillChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(category='Sources',
		affix='slowChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(category='Sources',
		affix='immobilizeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(category='Sources',
		affix='knockbackChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Knockback on Hit')
	knockbackChance.save()


	thorns = Affix(category='Sources',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,220 - 2,600</span> damage')
	thorns.save()

	itemHealing = Affix(category='Sources',
		affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29.713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()


	killExp = Affix(category='Sources',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(category='Sources',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	durability = Affix(category='Sources',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

	lvlReq = Affix(category='Sources',
		affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()

#Winter Flurry
	winterColdDmg = Affix(category='Sources',
		affix='winterColdDmg',
		is_primary=True,
		desc='Cold skills deal <span>15 - 20%</span> more damage')
	winterColdDmg.save()


def load_quiver_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

#Quiver primaries
#==============================================================================
#==============================================================================
	dext = Affix(category='Quivers',
		affix='dext',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000</span> Dexterity')
	dext.save()

	vita = Affix(category='Quivers',
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	ias = Affix(category='Quivers',
		affix='ias',
		is_primary=True,
		desc='<span>+15.0 - 20.0%</span> Attack Speed')
	ias.save()

	chc = Affix(category='Quivers',
		affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	cdr = Affix(category='Quivers',
		affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	areaDmg = Affix(category='Quivers',
		affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20%</span> Area Damage')
	areaDmg.save()

	eliteDmg = Affix(category='Quivers',
		affix='eliteDmg',
		is_primary=True,
		desc='Increase damage against elites by <span>5.0 - 8.0%</span>')
	eliteDmg.save()

	bleedChance = Affix(category='Quivers',
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	life = Affix(category='Quivers',
		affix='life',
		is_primary=True,
		desc='<span>+10 - 15%</span> Life')
	life.save()

	lps = Affix(category='Quivers',
		affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	rcr = Affix(category='Quivers',
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	hatredRegen = Affix(category='Quivers',
		affix='hatredRegen',
		is_primary=True,
		desc='<span>+1.35 - 1.50</span> Hatred Regeneration per Second')
	hatredRegen.save()

	sockets = Affix(category='Quivers',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Demon Hunter Skills
#==============================================================================
	bolas = Affix(category='Quivers',
		affix='bolas',
		is_primary=True,
		desc='Increase Bola damage by <span>10 - 15%</span>')
	bolas.save()

	chakram = Affix(category='Quivers',
		affix='chakram',
		is_primary=True,
		desc='Increase Chakram damage by <span>10 - 15%</span>')
	chakram.save()

	clusterArrow = Affix(category='Quivers',
		affix='clusterArrow',
		is_primary=True,
		desc='Increase Cluster Arrow damage by <span>10 - 15%</span>')
	clusterArrow.save()

	companion = Affix(category='Quivers',
		affix='companion',
		is_primary=True,
		desc='Increase Companion damage by <span>10 - 15%</span>')
	companion.save()

	elementalArrow = Affix(category='Quivers',
		affix='elementalArrow',
		is_primary=True,
		desc='Increase Elemental Arrow damage by <span>10 - 15%</span>')
	elementalArrow.save()

	entanglingShot = Affix(category='Quivers',
		affix='entanglingShot',
		is_primary=True,
		desc='Increase Entangling Shot damage by <span>10 - 15%</span>')
	entanglingShot.save()

	evasiveFire = Affix(category='Quivers',
		affix='evasiveFire',
		is_primary=True,
		desc='Increase Evasive Fire damage by <span>10 - 15%</span>')
	evasiveFire.save()

	fanOfKnives = Affix(category='Quivers',
		affix='fanOfKnives',
		is_primary=True,
		desc='Increase Fan of Knives damage by <span>10 - 15%</span>')
	fanOfKnives.save()

	grenade = Affix(category='Quivers',
		affix='grenade',
		is_primary=True,
		desc='Increase Grenade damage by <span>10 - 15%</span>')
	grenade.save()

	hungeringArrow = Affix(category='Quivers',
		affix='hungeringArrow',
		is_primary=True,
		desc='Increase Hungering Arrow damage by <span>10 - 15%</span>')
	hungeringArrow.save()

	impale = Affix(category='Quivers',
		affix='impale',
		is_primary=True,
		desc='Increase Impale damage by <span>10 - 15%</span>')
	impale.save()

	multishot = Affix(category='Quivers',
		affix='multishot',
		is_primary=True,
		desc='Increase Multishot damage by <span>10 - 15%</span>')
	multishot.save()

	rainOfVengeance = Affix(category='Quivers',
		affix='rainOfVengeance',
		is_primary=True,
		desc='Increase Rain of Vengeance damage by <span>10 - 15%</span>')
	rainOfVengeance.save()

	rapidFire = Affix(category='Quivers',
		affix='rapidFire',
		is_primary=True,
		desc='Increase Rapid Fire damage by <span>10 - 15%</span>')
	rapidFire.save()

	sentry = Affix(category='Quivers',
		affix='sentry',
		is_primary=True,
		desc='Increase Sentry damage by <span>10 - 15%</span>')
	sentry.save()

	spikeTrap = Affix(category='Quivers',
		affix='spikeTrap',
		is_primary=True,
		desc='Increase Spike Trap damage by <span>10 - 15%</span>')
	spikeTrap.save()

	strafe = Affix(category='Quivers',
		affix='strafe',
		is_primary=True,
		desc='Increase Strafe damage by <span>10 - 15%</span>')
	strafe.save()

#Quiver secondaries
#==============================================================================
#==============================================================================
	maxDisc = Affix(category='Quivers',
		affix='maxDisc',
		is_primary=False,
		desc='<span>+9 - 12</span> Max Discipline')
	maxDisc.save()

	fearChance = Affix(category='Quivers',
		affix='fearChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(category='Quivers',
		affix='stunChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(category='Quivers',
		affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(category='Quivers',
		affix='freezeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(category='Quivers',
		affix='chillChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(category='Quivers',
		affix='slowChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(category='Quivers',
		affix='immobilizeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(category='Quivers',
		affix='knockbackChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Knockback on Hit')
	knockbackChance.save()

	thorns = Affix(category='Quivers',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,200 - 2,600</span> damage')
	thorns.save()

	itemHealing = Affix(category='Quivers',
		affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29,713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	killExp = Affix(category='Quivers',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(category='Quivers',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	durability = Affix(category='Quivers',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

	lvlReq = Affix(category='Quivers',
		affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()

#Added in 2.4
#Bombadier's Rucksack
	bombadiersSentry = Affix(category='Quivers',
		affix='bombadiersSentry',
		is_primary=True,
		desc='Increase Sentry damage by <span>75 - 100%</span>')
	bombadiersSentry.save()

#Added in 2.4
#Dead Man's Legacy
	deadMultishot = Affix(category='Quivers',
		affix='deadMultishot',
		is_primary=True,
		desc='Increase Multishot damage by <span>75 - 100%</span>')
	deadMultishot.save()

#Holy Point Shot
	holyEleDmg = Affix(category='Quivers',
		affix='holyEleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy</span></div>')
	holyEleDmg.save()

#Added in 2.4
#Sin Seekers
	sinRapidFire = Affix(category='Quivers',
		affix='sinRapidFire',
		is_primary=True,
		desc='Increase Rapid Fire damage by <span>45 - 60%</span>')
	sinRapidFire.save()


def load_mojo_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

#Mojo primaries
#==============================================================================
#==============================================================================
	dmg = Affix(category='Mojos',
		affix='dmg',
		is_primary=True,
		desc='<span>+340 - 370</span> -- <span>380 - 450</span> Damage',
		ancient='<span>+407 - 485</span> -- <span>495 - 600</span> Damage')
	dmg.save()

	inte = Affix(category='Mojos',
		affix='inte',
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	vita = Affix(category='Mojos',
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	chc = Affix(category='Mojos',
		affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	cdr = Affix(category='Mojos',
		affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()
	
	areaDmg = Affix(category='Mojos',
		affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20-%</span> Area Damage')
	areaDmg.save()

	eliteDmg = Affix(category='Mojos',
		affix='eliteDmg',
		is_primary=True,
		desc='Increase damage against elites by <span>5.0 - 8.0%</span>')
	eliteDmg.save()

	bleedChance = Affix(category='Mojos',
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	life = Affix(category='Mojos',
		affix='life',
		is_primary=True,
		desc='<span>+10 - 15%</span> Life')
	life.save()

	lps = Affix(category='Mojos',
		affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	rcr = Affix(category='Mojos',
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	manaRegen = Affix(category='Mojos',
		affix='manaRegen',
		is_primary=True,
		desc='<span>+12.00 - 14.00</span> Mana Regeneration per Second')
	manaRegen.save()

	sockets = Affix(category='Mojos',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

#Witch Doctor Skills
#==============================================================================
	acidCloud = Affix(category='Mojos',
		affix='acidCloud',
		is_primary=True,
		desc='Increase Acid Cloud damage by <span>10 - 15%</span>')
	acidCloud.save()

	corpseSpiders = Affix(category='Mojos',
		affix='corpseSpiders',
		is_primary=True,
		desc='Increase Corpse Spiders damage by <span>10 - 15%</span>')
	corpseSpiders.save()

	fetishArmy = Affix(category='Mojos',
		affix='fetishArmy',
		is_primary=True,
		desc='Increase Fetish Army damage by <span>10 - 15%</span>')
	fetishArmy.save()

	firebats = Affix(category='Mojos',
		affix='firebats',
		is_primary=True,
		desc='Increase Fire Bats damage by <span>10 - 15%</span>')
	firebats.save()

	firebomb = Affix(category='Mojos',
		affix='firebomb',
		is_primary=True,
		desc='Increase Fire Bomb damage by <span>10 - 15%</span>')
	firebomb.save()

	gargantuan = Affix(category='Mojos',
		affix='gargantuan',
		is_primary=True,
		desc='Increase Gargantuan damage by <span>10 - 15%</span>')
	gargantuan.save()

	graspOfTheDead = Affix(category='Mojos',
		affix='graspOfTheDead',
		is_primary=True,
		desc='Increase Grasp of the Dead damage by <span>10 - 15%</span>')
	graspOfTheDead.save()

	haunt = Affix(category='Mojos',
		affix='haunt',
		is_primary=True,
		desc='Increase Haunt damage by <span>10 - 15%</span>')
	haunt.save()

	locustSwarm = Affix(category='Mojos',
		affix='locustSwarm',
		is_primary=True,
		desc='Increase Locust Swarm damage by <span>10 - 15%</span>')
	locustSwarm.save()

	piranhas = Affix(category='Mojos',
		affix='piranhas',
		is_primary=True,
		desc='Increase Piranhas damage by <span>10 - 15%</span>')
	piranhas.save()

	plagueOfToads = Affix(category='Mojos',
		affix='plagueOfToads',
		is_primary=True,
		desc='Increase Plague of Toads damage by <span>10 - 15%</span>')
	plagueOfToads.save()

	poisonDart = Affix(category='Mojos',
		affix='poisonDart',
		is_primary=True,
		desc='Increase Poison Dart damage by <span>10 - 15%</span>')
	poisonDart.save()

	sacrifice = Affix(category='Mojos',
		affix='sacrifice',
		is_primary=True,
		desc='Increase Sacrifice damage by <span>10 - 15%</span>')
	sacrifice.save()

	spiritBarrage = Affix(category='Mojos',
		affix='spiritBarrage',
		is_primary=True,
		desc='Increase Spirit Barrage damage by <span>10 - 15%</span>')
	spiritBarrage.save()

	summonZombieDogs = Affix(category='Mojos',
		affix='summonZombieDogs',
		is_primary=True,
		desc='Increase Summon Zombie Dogs damage by <span>10 - 15%</span>')
	summonZombieDogs.save()

	wallOfDeath = Affix(category='Mojos',
		affix='wallOfDeath',
		is_primary=True,
		desc='Increase Wall of Death damage by <span>10 - 15%</span>')
	wallOfDeath.save()

	zombieCharger = Affix(category='Mojos',
		affix='zombieCharger',
		is_primary=True,
		desc='Increase Zombie Charger damage by <span>10 - 15%</span>')
	zombieCharger.save()

#Mojo secondaries
#==============================================================================
#==============================================================================
	maxMana = Affix(category='Mojos',
		affix='maxMana',
		is_primary=False,
		desc='<span>+120 - 150</span> Max Mana')
	maxMana.save()

	fearChance = Affix(category='Mojos',
		affix='fearChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(category='Mojos',
		affix='stunChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(category='Mojos',
		affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(category='Mojos',
		affix='freezeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(category='Mojos',
		affix='chillChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(category='Mojos',
		affix='slowChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(category='Mojos',
		affix='immobilizeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(category='Mojos',
		affix='knockbackChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Knockback on Hit')
	knockbackChance.save()

	thorns = Affix(category='Mojos',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,200 - 2,600</span> damage')
	thorns.save()

	itemHealing = Affix(category='Mojos',
		affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29,713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	killExp = Affix(category='Mojos',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(category='Mojos',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	durability = Affix(category='Mojos',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

	lvlReq = Affix(category='Mojos',
		affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()

#Removed in 2.4
# #Thing of the Deep
# 	thingItemPickup = Affix(category='Mojos',
# 		affix='thingItemPickup',
# 		is_primary=False,
# 		desc='<span class="silver">+20</span> Yards to Gold and Globe Pickup')
# 	thingItemPickup.save()

#2.4 new
	wilkensGraspOfTheDead = Affix(category='Mojos',
		affix='wilkensGraspOfTheDead',
		is_primary=True,
		desc='Increase Grasp of the Dead damage by <span>45 - 60%</span>')
	wilkensGraspOfTheDead.save()


def load_crusader_shield_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

#Crusader shield primaries
#==============================================================================
#==============================================================================
	sockets = Affix(category='Crusader Shields',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	stre = Affix(category='Crusader Shields',
		affix='stre',
		is_primary=True,
		desc='<span>+626 - 725</span> Strength',
		ancient='<span>+825 - 1,000</span> Strength')
	stre.save()

	vita = Affix(category='Crusader Shields',
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 725</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	chc = Affix(category='Crusader Shields',
		affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	cdr = Affix(category='Crusader Shields',
		affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	eliteDmg = Affix(category='Crusader Shields',
		affix='eliteDmg',
		is_primary=True,
		desc='Increase damage against elites by <span>5.0 - 8.0%</span>')
	eliteDmg.save()

	areaDmg = Affix(category='Crusader Shields',
		affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20%</span> Area Damage')
	areaDmg.save()

	bleedChance = Affix(category='Crusader Shields',
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	armor = Affix(category='Crusader Shields',
		affix='armor',
		is_primary=True,
		desc='<span>+559 - 595</span> Armor',
		ancient='<span>+654 - 775</span> Armor')
	armor.save()

	allRes = Affix(category='Crusader Shields',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	blockChance = Affix(category='Crusader Shields',
		affix='blockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	blockChance.save()

	reducedEliteDmg = Affix(category='Crusader Shields',
		affix='reducedEliteDmg',
		is_primary=True,
		desc='<span>+10.0 - 11.0%</span> Elite Damage Reduction')
	reducedEliteDmg.save()

	life = Affix(category='Crusader Shields',
		affix='life',
		is_primary=True,
		desc='<span>+10 - 18%</span> Life')
	life.save()

	lps = Affix(category='Crusader Shields',
		affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	lifePerWrath = Affix(category='Crusader Shields',
		affix='lifePerWrath',
		is_primary=True,
		desc='<span>+1,077 - 1,276</span> Life per Wrath spent',
		ancient='<span>+1,408 - 1,660</span> Life per Wrath spent')
	lifePerWrath.save()

	rcr = Affix(category='Crusader Shields',
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	wrathRegen = Affix(category='Crusader Shields',
		affix='wrathRegen',
		is_primary=True,
		desc='<span>+1.85 - 2.00</span> Wrath Regeneration')
	wrathRegen.save()

#Crusader skills
#==============================================================================
	blessedHammer = Affix(category='Crusader Shields',
		affix='blessedHammer',
		is_primary=True,
		desc='Increase Blessed Hammer damage by <span>10 - 15%</span>')
	blessedHammer.save()

	blessedShield = Affix(category='Crusader Shields',
		affix='blessedShield',
		is_primary=True,
		desc='Increase Blessed Shield damage by <span>10 - 15%</span>')
	blessedShield.save()

	bombardment = Affix(category='Crusader Shields',
		affix='bombardment',
		is_primary=True,
		desc='Increase Bombardment damage by <span>10 - 15%</span>')
	bombardment.save()

	condemn = Affix(category='Crusader Shields',
		affix='condemn',
		is_primary=True,
		desc='Increase Condemn damage by <span>10 - 15%</span>')
	condemn.save()

	fallingSword = Affix(category='Crusader Shields',
		affix='fallingSword',
		is_primary=True,
		desc='Increase Falling Sword damage by <span>10 - 15%</span>')
	fallingSword.save()

	fistOfTheHeavens = Affix(category='Crusader Shields',
		affix='fistOfTheHeavens',
		is_primary=True,
		desc='Increase Fist of the  Heavens damage by <span>10 - 15%</span>')
	fistOfTheHeavens.save()

	heavensFury = Affix(category='Crusader Shields',
		affix='heavensFury',
		is_primary=True,
		desc='Increase Heaven\'s Fury damage by <span>10 - 15%</span>')
	heavensFury.save()

	justice = Affix(category='Crusader Shields',
		affix='justice',
		is_primary=True,
		desc='Increase Justice damage by <span>10 - 15%</span>')
	justice.save()

	phalanx = Affix(category='Crusader Shields',
		affix='phalanx',
		is_primary=True,
		desc='Increase Phalanx damage by <span>10 - 15%</span>')
	phalanx.save()

	punish= Affix(category='Crusader Shields',
		affix='punish',
		is_primary=True,
		desc='Increase Punish damage by <span>10 - 15%</span>')
	punish.save()

	shieldBash= Affix(category='Crusader Shields',
		affix='shieldBash',
		is_primary=True,
		desc='Increase Shield Bash damage by <span>10 - 15%</span>')
	shieldBash.save()

	slash = Affix(category='Crusader Shields',
		affix='slash',
		is_primary=True,
		desc='Increase Slash damage by <span>10 - 15%</span>')
	slash.save()

	smite = Affix(category='Crusader Shields',
		affix='smite',
		is_primary=True,
		desc='Increase Smite damage by <span>10 - 15%</span>')
	smite.save()

	sweepAttack = Affix(category='Crusader Shields',
		affix='sweepAttack',
		is_primary=True,
		desc='Increase Sweep Attack damage by <span>10 - 15%</span>')
	sweepAttack.save()

	eleRes = Affix(category='Crusader Shields',
		affix='eleRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Resistance to {<span>One Element</span>}<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane</span></div>',
		ancient='<span>+176 - 210</span> Resistance to {<span>One Element</span>}<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane</span></div>')
	eleRes.save()

#Crusader shield secondaries
#==============================================================================
#==============================================================================
	physRes = Affix(category='Crusader Shields',
		affix='physRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Physical Resistance',
		ancient='<span>+176 - 210</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(category='Crusader Shields',
		affix='coldRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Cold Resistance',
		ancient='<span>+176 - 210</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(category='Crusader Shields',
		affix='fireRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Fire Resistance',
		ancient='<span>+176 - 210</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(category='Crusader Shields',
		affix='lightRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Lightning Resistance',
		ancient='<span>+176 - 210</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(category='Crusader Shields',
		affix='poisRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Poison Resistance',
		ancient='<span>+176 - 210</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(category='Crusader Shields',
		affix='arcaneRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Arcane Resistance',
		ancient='<span>+176 - 210</span> Arcane Resistance')
	arcaneRes.save()

	maxWrath = Affix(category='Crusader Shields',
		affix='maxWrath',
		is_primary=False,
		desc='<span>+8 - 10</span> Max Wrath')
	maxWrath.save()

	reducedRangeDmg = Affix(category='Crusader Shields',
		affix='reducedRangeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Ranged Damage Reduction')
	reducedRangeDmg.save()

	reducedMeleeDmg = Affix(category='Crusader Shields',
		affix='reducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	reducedMeleeDmg.save()

	ccReduction = Affix(category='Crusader Shields',
		affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	itemHealing = Affix(category='Crusader Shields',
		affix='itemHealing',
		is_primary=False,
		desc='<span>+</span> Healing from Health Globes and Potions',
		ancient='<span>+3</span> Healing from Health Globes and Potions')
	itemHealing.save()

	fearChance = Affix(category='Crusader Shields',
		affix='fearChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(category='Crusader Shields',
		affix='stunChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(category='Crusader Shields',
		affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(category='Crusader Shields',
		affix='freezeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(category='Crusader Shields',
		affix='chillChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(category='Crusader Shields',
		affix='slowChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(category='Crusader Shields',
		affix='immobilizeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(category='Crusader Shields',
		affix='knockbackChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Knockback on Hit')
	knockbackChance.save()

	extraGold = Affix(category='Crusader Shields',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	thorns = Affix(category='Crusader Shields',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()

	killExp = Affix(category='Crusader Shields',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	lvlReq = Affix(category='Crusader Shields',
		affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()

	durability = Affix(category='Crusader Shields',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

#Added in 2.4
#Frydehr's Wrath
	frydehrsCondemn = Affix(category='Crusader Shields',
		affix='frydehrsCondemn',
		is_primary=True,
		desc='Increase Condemn damage by <span>150 - 200%</span>')
	frydehrsCondemn.save()

#2.4
#Jekangbord
	jekangbordBlessedShield = Affix(category='Crusader Shields',
		affix='jekangbordBlessedShield',
		is_primary=True,
		desc='Increase Blessed Shield damage by <span>150 - 200%</span>')
	jekangbordBlessedShield.save()

#Added in 2.4
#Unrelenting Phalanx
	unrelentingPhalanxDmg = Affix(category='Crusader Shields',
		affix='unrelentingPhalanxDmg',
		is_primary=True,
		desc='Increase Phalanx damage by <span>45 - 60%</span>')
	unrelentingPhalanxDmg.save()


def load_shield_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	mainStat = Affix(category='Shields',
		affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}<div class="extra"><div class="extra-x">X</div><span>Dexterity<br>Intelligence<br>Strength</span></div>')
	mainStat.save()

	vita = Affix(category='Shields',
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	allRes = Affix(category='Shields',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	blockChance = Affix(category='Shields',
		affix='blockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	blockChance.save()

	thorns = Affix(category='Shields',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()

#Lidless Wall
	lidlessEleDmg = Affix(category='Shields',
		affix='lidlessEleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage<div class="extra"><div class="extra-x">X</div><span>Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy</span></div>')
	lidlessEleDmg.save()

	lidlessMaxResource = Affix(category='Shields',
		affix='lidlessMaxResource',
		is_primary=False,
		desc='Increase Max {<span class="vary">Resource</span>}<div class="extra"><div class="extra-x">X</div><span>+10-12 Fury<br>+8-10 Wrath<br>+9-12 Discipline<br>+13-15 Spirit<br>+120-150 Mana<br>+10-14 Arcane Power</span></div>')
	lidlessMaxResource.save()

#Storm Shield
	stormReducedMeleeDmg = Affix(category='Shields',
		affix='stormReducedMeleeDmg',
		is_primary=False,
		desc='Reduces damage from melee attacks by <span>25.0 - 30.0%</span>')
	stormReducedMeleeDmg.save()


def load_ancient_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0003_2h_weapon_affixes'),
    ]

    operations = [
        migrations.RunPython(load_source_affixes),
        migrations.RunPython(load_quiver_affixes),
        migrations.RunPython(load_mojo_affixes),
        migrations.RunPython(load_crusader_shield_affixes),
        migrations.RunPython(load_shield_affixes),
        migrations.RunPython(load_ancient_affixes)
    ]
