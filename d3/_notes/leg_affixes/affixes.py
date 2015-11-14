def load__affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")


	dmg = Affix(id=,
		affix='dmg',
		is_primary=True,
		desc='<span>+</span> -- <span></span> Damage',
		ancient='<span>+</span> -- <span></span> Damage')
	dmg.save()

	mainStat = Affix(id=,
		affix='mainStat',
		is_primary=True,
		desc='<span>+</span> {<span>Main Stat</span>}',
		ancient='<span>+</span> {<span>Main Stat</span>}')
	mainStat.save()

	dext = Affix(id=,
		affix='dext',
		is_primary=True,
		desc='<span>+</span> Dexterity',
		ancient='<span>+</span> Dexterity')
	dext.save()

	inte = Affix(id=,
		affix='inte',
		is_primary=True,
		desc='<span>+</span> Intelligence',
		ancient='<span>+</span> Intelligence')
	inte.save()

	stre = Affix(id=,
		affix='stre',
		is_primary=True,
		desc='<span>+</span> Strength',
		ancient='<span>+</span> Strength')
	stre.save()

	vita = Affix(id=,
		affix='vita',
		is_primary=True,
		desc='<span>+</span> Vitality',
		ancient='<span>+</span> Vitality')
	vita.save()


	eleDmg = Affix(id=,
		affix='eleDmg',
		is_primary=True,
		desc='Skills of {<span>One Element</span>} do <span>15 - 20%</span> more damage')
	eleDmg.save()

	physDmg = Affix(id=,
		affix='physDmg',
		is_primary=True,
		desc='Physical skills do <span>15 - 20%</span> more damage')
	physDmg.save()

	coldDmg = Affix(id=,
		affix='coldDmg',
		is_primary=True,
		desc='Cold skills do <span>15 - 20%</span> more damage')
	coldDmg.save()

	fireDmg = Affix(id=,
		affix='fireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	fireDmg.save()

	lightDmg = Affix(id=,
		affix='lightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	lightDmg.save()

	poisDmg = Affix(id=,
		affix='poisDmg',
		is_primary=True,
		desc='Poison skills do <span>15 - 20%</span> more damage')
	poisDmg.save()

	arcaneDmg = Affix(id=,
		affix='arcaneDmg',
		is_primary=True,
		desc='Arcane skills do <span>15 - 20%</span> more damage')
	arcaneDmg.save()

	holyDmg = Affix(id=,
		affix='holyDmg',
		is_primary=True,
		desc='Holy skills do <span>15 - 20%</span> more damage')
	holyDmg.save()


	life = Affix(id=,
		affix='life',
		is_primary=True,
		desc='<span>+%</span> Life')
	life.save()

	armor = Affix(id=,
		affix='armor',
		is_primary=True,
		desc='<span>+</span> Armor',
		ancient='<span>+</span> Armor')
	armor.save()

	allRes = Affix(id=,
		affix='allRes',
		is_primary=True,
		desc='<span>+</span> Resistance to All Elements',
		ancient='<span>+</span> Resistance to All Elements')
	allRes.save()

	lps = Affix(id=,
		affix='lps',
		is_primary=True,
		desc='<span>+</span> Life Regeneration per Second',
		ancient='<span>+</span> Life Regeneration per Second')
	lps.save()

	lph = Affix(id=,
		affix='lph',
		is_primary=True,
		desc='<span>+</span> Life per Hit',
		ancient='<span>+</span> Life per Hit')
	lph.save()


	ias = Affix(id=,
		affix='ias',
		is_primary=True,
		desc='<span>+%</span> Attack Speed')
	ias.save()

	chc = Affix(id=,
		affix='chc',
		is_primary=True,
		desc='<span>+%</span> Critical Hit Chance')
	chc.save()

	chd = Affix(id=,
		affix='chd',
		is_primary=True,
		desc='<span>+%</span> Critical Hit Damage')
	chd.save()

	areaDmg = Affix(id=,
		affix='areaDmg',
		is_primary=True,
		desc='<span>+%</span> Area Damage')
	areaDmg.save()

	eliteDmg = Affix(id=,
		affix='eliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>%</span>')
	eliteDmg.save()


	bleedChance = Affix(id=,
		affix='bleedChance',
		is_primary=True,
		desc='<span>%</span> chance to inflict Bleed for <span>%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()


	cdr = Affix(id=,
		affix='cdr',
		is_primary=True,
		desc='<span>+%</span> Cooldown Reduction')
	cdr.save()

	rcr = Affix(id=,
		affix='rcr',
		is_primary=True,
		desc='<span>+%<span> Resource Cost Reduction')
	rcr.save()

	sockets = Affix(id=,
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span></span>)')
	sockets.save()


	apCrit = Affix(id=,
		affix='apCrit',
		is_primary=True,
		desc='<span>+3 - 4</span> Arcane Power on Critical Hits')
	apCrit.save()



#Wizard Skills
#==============================================================================

	arcaneOrb = Affix(id=,
		affix='arcaneOrb',
		is_primary=True,
		desc='Increase Arcane Orb damage by <span>10 - 15%</span>')
	arcaneOrb.save()

	electrocute = Affix(id=,
		affix='electrocute',
		is_primary=True,
		desc='Increase Electrocute damage by <span>10 - 15%</span>')
	electrocute.save()

	rayOfFrost = Affix(id=,
		affix='rayOfFrost',
		is_primary=True,
		desc='Increase Ray of Frost damage by <span>10 - 15%</span>')
	rayOfFrost.save()

	spectralBlade = Affix(id=,
		affix='spectralBlade',
		is_primary=True,
		desc='Increase Spectral Blade damage by <span>10 - 15%</span>')
	spectralBlade.save()

	blackHole = Affix(id=,
		affix='blackHole',
		is_primary=True,
		desc='Increase Black Hole damage by <span>10 - 15%</span>')
	blackHole.save()

	meteor = Affix(id=,
		affix='meteor',
		is_primary=True,
		desc='Increase Meteor damage by <span>10 - 15%</span>')
	meteor.save()

	waveOfForce = Affix(id=,
		affix='waveOfForce',
		is_primary=True,
		desc='Increase Wave of Force damage by <span>10 - 15%</span>')
	waveOfForce.save()

	arcaneTorrent = Affix(id=,
		affix='arcaneTorrent',
		is_primary=True,
		desc='Increase Arcane Torrent damage by <span>10 - 15%</span>')
	arcaneTorrent.save()

	shockPulse = Affix(id=,
		affix='shockPulse',
		is_primary=True,
		desc='Increase Shock Pulse damage by <span>10 - 15%</span>')
	shockPulse.save()

	familiar = Affix(id=,
		affix='familiar',
		is_primary=True,
		desc='Increase Familiar damage by <span>10 - 15%</span>')
	familiar.save()

	magicMissle = Affix(id=,
		affix='magicMissle',
		is_primary=True,
		desc='Increase Magic Missle damage by <span>10 - 15%</span>')
	magicMissle.save()

	energyTwister = Affix(id=,
		affix='energyTwister',
		is_primary=True,
		desc='Increase Energy Twister damage by <span>10 - 15%</span>')
	energyTwister.save()

	blizzard = Affix(id=,
		affix='blizzard',
		is_primary=True,
		desc='Increase Blizzard damage by <span>10 - 15%</span>')
	blizzard.save()

	disintegrate = Affix(id=,
		affix='disintegrate',
		is_primary=True,
		desc='Increase Disintegrate damage by <span>10 - 15%</span>')
	disintegrate.save()

	explosiveBlast = Affix(id=,
		affix='explosiveBlast',
		is_primary=True,
		desc='Increase Explosive Blast damage by <span>10 - 15%</span>')
	explosiveBlast.save()

	hydra = Affix(id=,
		affix='hydra',
		is_primary=True,
		desc='Increase Hydra damage by <span>10 - 15%</span>')
	hydra.save()

#Secondaries
#==============================================================================
#==============================================================================

	eleRes = Affix(id=,
		affix='eleRes',
		is_primary=False,
		desc='<span>+</span> Resistance to {<span>One Element</span>}',
		ancient='<span>+</span> Resistance to {<span>One Element</span>}')
	eleRes.save()

	physRes = Affix(id=,
		affix='physRes',
		is_primary=False,
		desc='<span>+</span> Physical Resistance',
		ancient='<span>+</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(id=,
		affix='coldRes',
		is_primary=False,
		desc='<span>+</span> Cold Resistance',
		ancient='<span>+</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(id=,
		affix='fireRes',
		is_primary=False,
		desc='<span>+</span> Fire Resistance',
		ancient='<span>+</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(id=,
		affix='lightRes',
		is_primary=False,
		desc='<span>+</span> Lightning Resistance',
		ancient='<span>+</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(id=,
		affix='poisRes',
		is_primary=False,
		desc='<span>+</span> Poison Resistance',
		ancient='<span>+</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(id=,
		affix='arcaneRes',
		is_primary=False,
		desc='<span>+</span> Arcane Resistance',
		ancient='<span>+</span> Arcane Resistance')
	arcaneRes.save()


	reducedRangeDmg = Affix(id=,
		affix='reducedRangeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Ranged Damage Reduction')
	reducedRangeDmg.save()

	reducedMeleeDmg = Affix(id=,
		affix='reducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	reducedMeleeDmg.save()


	maxAP = Affix(id=,
		affix='maxAP',
		is_primary=False,
		desc='<span>+</span> Max Arcane Power')
	maxAP.save()


	fearChance = Affix(id=,
		affix='fearChance',
		is_primary=False,
		desc='<span>+%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(id=,
		affix='stunChance',
		is_primary=False,
		desc='<span>+%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(id=,
		affix='blindChance',
		is_primary=False,
		desc='<span>+%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(id=,
		affix='freezeChance',
		is_primary=False,
		desc='<span>+%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(id=,
		affix='chillChance',
		is_primary=False,
		desc='<span>+%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(id=,
		affix='slowChance',
		is_primary=False,
		desc='<span>+%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(id=,
		affix='immobilizeChance',
		is_primary=False,
		desc='<span>+%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(id=,
		affix='knockbackChance',
		is_primary=False,
		desc='<span>+%</span> chance to Knockback on Hit')
	knockbackChance.save()


	ccReduction = Affix(id=,
		affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	thorns = Affix(id=,
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span></span> damage',
		ancient='Attackers take <span></span> damage')
	thorns.save()

	itemHealing = Affix(id=,
		affix='itemHealing',
		is_primary=False,
		desc='<span>+</span> Healing from Health Globes and Potions',
		ancient='<span>+3</span> Healing from Health Globes and Potions')
	itemHealing.save()

	lpk = Affix(id=,
		affix='lpk',
		is_primary=False,
		desc='<span>+</span> Life per Kill',
		ancient='<span>+</span> Life per Kill')
	lpk.save()


	killExp = Affix(id=,
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(id=,
		affix='extraGold',
		is_primary=False,
		desc='<span>+%</span> Extra Gold from Monsters')
	extraGold.save()

	durability = Affix(id=,
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

	lvlReq = Affix(id=,
		affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()










































	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()
		else:
			pass

	migrations.RunPython(load__affixes)