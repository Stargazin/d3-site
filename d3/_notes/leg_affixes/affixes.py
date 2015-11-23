def load__affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")


	dmg = Affix(category='',
		affix='dmg',
		is_primary=True,
		desc='<span>+</span> -- <span></span> Damage',
		ancient='<span>+</span> -- <span></span> Damage')
	dmg.save()

	percentDmg = Affix(category='',
		affix='percentDmg',
		is_primary=True,
		desc='<span>+6 - 10%</span> Damage')
	percentDmg.save()

	mainStat = Affix(category='',
		affix='mainStat',
		is_primary=True,
		desc='<span>+</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	dext = Affix(category='',
		affix='dext',
		is_primary=True,
		desc='<span>+</span> Dexterity',
		ancient='<span>+</span> Dexterity')
	dext.save()

	inte = Affix(category='',
		affix='inte', 
		is_primary=True,
		desc='<span>+</span> Intelligence',
		ancient='<span>+</span> Intelligence')
	inte.save()

	stre = Affix(category='',
		affix='stre',
		is_primary=True,
		desc='<span>+</span> Strength',
		ancient='<span>+</span> Strength')
	stre.save()

	vita = Affix(category='',
		affix='vita',
		is_primary=True,
		desc='<span>+</span> Vitality',
		ancient='<span>+</span> Vitality')
	vita.save()


	eleDmg = Affix(category='',
		affix='eleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy')
	eleDmg.save()

	physDmg = Affix(category='',
		affix='physDmg',
		is_primary=True,
		desc='Physical skills do <span>15 - 20%</span> more damage')
	physDmg.save()

	coldDmg = Affix(category='',
		affix='coldDmg',
		is_primary=True,
		desc='Cold skills do <span>15 - 20%</span> more damage')
	coldDmg.save()

	fireDmg = Affix(category='',
		affix='fireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	fireDmg.save()

	lightDmg = Affix(category='',
		affix='lightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	lightDmg.save()

	poisDmg = Affix(category='',
		affix='poisDmg',
		is_primary=True,
		desc='Poison skills do <span>15 - 20%</span> more damage')
	poisDmg.save()

	arcaneDmg = Affix(category='',
		affix='arcaneDmg',
		is_primary=True,
		desc='Arcane skills do <span>15 - 20%</span> more damage')
	arcaneDmg.save()

	holyDmg = Affix(category='',
		affix='holyDmg',
		is_primary=True,
		desc='Holy skills do <span>15 - 20%</span> more damage')
	holyDmg.save()


	ias = Affix(category='',
		affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	chc = Affix(category='',
		affix='chc',
		is_primary=True,
		desc='<span>+</span> Critical Hit Chance')
	chc.save()

	chd = Affix(category='',
		affix='chd',
		is_primary=True,
		desc='<span>+</span> Critical Hit Damage')
	chd.save()

	cdr = Affix(category='',
		affix='cdr',
		is_primary=True,
		desc='<span>+</span> Cooldown Reduction')
	cdr.save()

	eliteDmg = Affix(category='',
		affix='eliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span></span>')
	eliteDmg.save()

	areaDmg = Affix(category='',
		affix='areaDmg',
		is_primary=True,
		desc='<span>+</span> Area Damage')
	areaDmg.save()

	bleedChance = Affix(category='',
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()


	armor = Affix(category='',
		affix='armor',
		is_primary=True,
		desc='<span>+</span> Armor',
		ancient='<span>+</span> Armor')
	armor.save()

	allRes = Affix(category='',
		affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	blockChance = Affix(category='',
		affix='blockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	blockChance.save()

	reducedEliteDmg = Affix(category='',
		affix='reducedEliteDmg',
		is_primary=True,
		desc='<span>+10.0 - 11.0%</span> Elite Damage Reduction')
	reducedEliteDmg.save()

	life = Affix(category='',
		affix='life',
		is_primary=True,
		desc='<span>+</span> Life')
	life.save()

	lps = Affix(category='',
		affix='lps',
		is_primary=True,
		desc='<span>+6,448 - 7,678</span> Life Regeneration per Second',
		ancient='<span>+8,445 - 10,000</span> Life Regeneration per Second')
	lps.save()

	lph = Affix(category='',
		affix='lph',
		is_primary=True,
		desc='<span>+</span> Life per Hit',
		ancient='<span>+</span> Life per Hit')
	lph.save()

	lifePerWrath = Affix(category='',
		affix='lifePerWrath',
		is_primary=True,
		desc='<span>+</span> Life per Wrath spent',
		ancient='<span>+</span> Life per Wrath spent')
	lifePerWrath.save()

	lifePerSpirit = Affix(category='',
		affix='lifePerSpirit',
		is_primary=True,
		desc='<span>+353 - 415</span> Life per Spirit spent',
		ancient='<span>+456 - 540</span> Life per Spirit spent')
	lifePerSpirit.save()


	rcr = Affix(category='',
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	wrathRegen = Affix(category='',
		affix='wrathRegen',
		is_primary=True,
		desc='<span>+1.85 - 2.00</span> Wrath Regeneration per Second')
	wrathRegen.save()

	hatredRegen = Affix(category='',
		affix='hatredRegen',
		is_primary=True,
		desc='<span>+1.35 - 1.50</span> Hatred Regeneration per Second')
	hatredRegen.save()

	spiritRegen = Affix(category='',
		affix='spiritRegen',
		is_primary=True,
		desc='<span>+2.17 - 3.00</span> Spirit Regeneration per Second')
	spiritRegen.save()

	apCrit = Affix(category='',
		affix='apCrit',
		is_primary=True,
		desc='<span>+3 - 4</span> Arcane Power on Critical Hits')
	apCrit.save()

	manaRegen = Affix(category='',
		affix='manaRegen',
		is_primary=True,
		desc='<span>+12.00 - 14.00</span> Mana Regeneratioin per Second')
	manaRegen.save()


	movementSpeed = Affix(category='',
		affix='movementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	movementSpeed.save()

	sockets = Affix(category='',
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()


	skillDmg = Affix(category='',
		affix='skillDmg',
		is_primary=True,
		desc='Increases {<span class="vary">Skill Damage</span>} by <span>10 - 15%</span>'
		notes='<br>')
	skillDmg.save()

#Crusader Skills
#==============================================================================
#==============================================================================
	blessedHammer = Affix(category='',
		affix='blessedHammer',
		is_primary=True,
		desc='Increase Blessed Hammer damage by <span>10 - 15%</span>')
	blessedHammer.save()

	blessedShield = Affix(category='',
		affix='blessedShield',
		is_primary=True,
		desc='Increase Blessed Shield damage by <span>10 - 15%</span>')
	blessedShield.save()

	bombardment = Affix(category='',
		affix='bombardment',
		is_primary=True,
		desc='Increase Bombardment damage by <span>10 - 15%</span>')
	bombardment.save()

	condemn = Affix(category='',
		affix='condemn',
		is_primary=True,
		desc='Increase Condemn damage by <span>10 - 15%</span>')
	condemn.save()

	fallingSword = Affix(category='',
		affix='fallingSword',
		is_primary=True,
		desc='Increase Falling Sword damage by <span>10 - 15%</span>')
	fallingSword.save()

	fistOfTheHeavens = Affix(category='',
		affix='fistOfTheHeavens',
		is_primary=True,
		desc='Increase Fist of the  Heavens damage by <span>10 - 15%</span>')
	fistOfTheHeavens.save()

	heavensFury = Affix(category='',
		affix='heavensFury',
		is_primary=True,
		desc='Increase Heaven\'s Fury damage by <span>10 - 15%</span>')
	heavensFury.save()

	justice = Affix(category='',
		affix='justice',
		is_primary=True,
		desc='Increase Justice damage by <span>10 - 15%</span>')
	justice.save()

	phalanx = Affix(category='',
		affix='phalanx',
		is_primary=True,
		desc='Increase Phalanx damage by <span>10 - 15%</span>')
	phalanx.save()

	 punish= Affix(
category='',	 	affix='punish',
		is_primary=True,
		desc='Increase Punish damage by <span>10 - 15%</span>')
	punish.save()

	 shieldBash= Affix(
category='',	 	affix='shieldBash',
		is_primary=True,
		desc='Increase Shield Bash damage by <span>10 - 15%</span>')
	shieldBash.save()

	slash = Affix(category='',
		affix='slash',
		is_primary=True,
		desc='Increase Slash damage by <span>10 - 15%</span>')
	slash.save()

	smite = Affix(category='',
		affix='smite',
		is_primary=True,
		desc='Increase Smite damage by <span>10 - 15%</span>')
	smite.save()

	sweepAttack = Affix(category='',
		affix='sweepAttack',
		is_primary=True,
		desc='Increase Sweep Attack damage by <span>10 - 15%</span>')
	sweepAttack.save()

#Demon Hunter Skills
#==============================================================================
#==============================================================================
	bolas = Affix(category='',
		affix='bolas',
		is_primary=True,
		desc='Increase Bola damage by <span>10 - 15%</span>')
	bolas.save()

	chakram = Affix(category='',
		affix='chakram',
		is_primary=True,
		desc='Increase Chakram damage by <span>10 - 15%</span>')
	chakram.save()

	clusterArrow = Affix(category='',
		affix='clusterArrow',
		is_primary=True,
		desc='Increase Cluster Arrow damage by <span>10 - 15%</span>')
	clusterArrow.save()

	companion = Affix(category='',
		affix='companion',
		is_primary=True,
		desc='Increase Companion damage by <span>10 - 15%</span>')
	companion.save()

	elementalArrow = Affix(category='',
		affix='elementalArrow',
		is_primary=True,
		desc='Increase Elemental Arrow damage by <span>10 - 15%</span>')
	elementalArrow.save()

	entanglingShot = Affix(category='',
		affix='entanglingShot',
		is_primary=True,
		desc='Increase Entangling Shot damage by <span>10 - 15%</span>')
	entanglingShot.save()

	evasiveFire = Affix(category='',
		affix='evasiveFire',
		is_primary=True,
		desc='Increase Evasive Fire damage by <span>10 - 15%</span>')
	evasiveFire.save()

	fanOfKnives = Affix(category='',
		affix='fanOfKnives',
		is_primary=True,
		desc='Increase Fan of Knives damage by <span>10 - 15%</span>')
	fanOfKnives.save()

	grenade = Affix(category='',
		affix='grenade',
		is_primary=True,
		desc='Increase Grenade damage by <span>10 - 15%</span>')
	grenade.save()

	hungeringArrow = Affix(category='',
		affix='hungeringArrow',
		is_primary=True,
		desc='Increase Hungering Arrow damage by <span>10 - 15%</span>')
	hungeringArrow.save()

	impale = Affix(category='',
		affix='impale',
		is_primary=True,
		desc='Increase Impale damage by <span>10 - 15%</span>')
	impale.save()

	multishot = Affix(category='',
		affix='multishot',
		is_primary=True,
		desc='Increase Multishot damage by <span>10 - 15%</span>')
	multishot.save()

	rainOfVengeance = Affix(category='',
		affix='rainOfVengeance',
		is_primary=True,
		desc='Increase Rain of Vengeance damage by <span>10 - 15%</span>')
	rainOfVengeance.save()

	rapidFire = Affix(category='',
		affix='rapidFire',
		is_primary=True,
		desc='Increase Rapid Fire damage by <span>10 - 15%</span>')
	rapidFire.save()

	sentry = Affix(category='',
		affix='sentry',
		is_primary=True,
		desc='Increase Sentry damage by <span>10 - 15%</span>')
	sentry.save()

	spikeTrap = Affix(category='',
		affix='spikeTrap',
		is_primary=True,
		desc='Increase Spike Trap damage by <span>10 - 15%</span>')
	spikeTrap.save()

	strafe = Affix(category='',
		affix='strafe',
		is_primary=True,
		desc='Increase Strafe damage by <span>10 - 15%</span>')
	strafe.save()

#Monk Skills
#==============================================================================
#==============================================================================
	explodingPalm = Affix(category='',
		affix='explodingPalm',
		is_primary=True,
		desc='Increase Exploding Palm damage by <span>10 - 15%</span>')
	explodingPalm.save()

	lashingTailKick = Affix(category='',
		affix='Lashing Tail Kick',
		is_primary=True,
		desc='Increase lashingTailKick damage by <span>10 - 15%</span>')
	lashingTailKick.save()

	tempestRush = Affix(category='',
		affix='tempestRush',
		is_primary=True,
		desc='Increase Tempest Rush damage by <span>10 - 15%</span>')
	tempestRush.save()

	waveOfLight = Affix(category='',
		affix='waveOfLight',
		is_primary=True,
		desc='Increase Wave of Light damage by <span>10 - 15%</span>')
	waveOfLight.save()

#Witch Doctor Skills
#==============================================================================
#==============================================================================
	acidCloud = Affix(category='',
		affix='acidCloud',
		is_primary=True,
		desc='Increase Acid Cloud damage by <span>10 - 15%</span>')
	acidCloud.save()

	corpseSpiders = Affix(category='',
		affix='corpseSpiders',
		is_primary=True,
		desc='Increase Corpse Spiders damage by <span>10 - 15%</span>')
	corpseSpiders.save()

	fetishArmy = Affix(category='',
		affix='fetishArmy',
		is_primary=True,
		desc='Increase Fetish Army damage by <span>10 - 15%</span>')
	fetishArmy.save()

	firebats = Affix(category='',
		affix='firebats',
		is_primary=True,
		desc='Increase Fire Bats damage by <span>10 - 15%</span>')
	firebats.save()

	firebomb = Affix(category='',
		affix='firebomb',
		is_primary=True,
		desc='Increase Fire Bomb damage by <span>10 - 15%</span>')
	firebomb.save()

	gargantuan = Affix(category='',
		affix='gargantuan',
		is_primary=True,
		desc='Increase Gargantuan damage by <span>10 - 15%</span>')
	gargantuan.save()

	graspOfTheDead = Affix(category='',
		affix='graspOfTheDead',
		is_primary=True,
		desc='Increase Grasp of the Dead damage by <span>10 - 15%</span>')
	graspOfTheDead.save()

	haunt = Affix(category='',
		affix='haunt',
		is_primary=True,
		desc='Increase Haunt damage by <span>10 - 15%</span>')
	haunt.save()

	locustSwarm = Affix(category='',
		affix='locustSwarm',
		is_primary=True,
		desc='Increase Locust Swarm damage by <span>10 - 15%</span>')
	locustSwarm.save()

	piranhas = Affix(category='',
		affix='piranhas',
		is_primary=True,
		desc='Increase Piranhas damage by <span>10 - 15%</span>')
	piranhas.save()

	plagueOfToads = Affix(category='',
		affix='plagueOfToads',
		is_primary=True,
		desc='Increase Plague of Toads damage by <span>10 - 15%</span>')
	plagueOfToads.save()

	poisonDart = Affix(category='',
		affix='poisonDart',
		is_primary=True,
		desc='Increase Poison Dart damage by <span>10 - 15%</span>')
	poisonDart.save()

	sacrifice = Affix(category='',
		affix='sacrifice',
		is_primary=True,
		desc='Increase Sacrifice damage by <span>10 - 15%</span>')
	sacrifice.save()

	spiritBarrage = Affix(category='',
		affix='spiritBarrage',
		is_primary=True,
		desc='Increase Spirit Barrage damage by <span>10 - 15%</span>')
	spiritBarrage.save()

	summonZombieDogs = Affix(category='',
		affix='summonZombieDogs',
		is_primary=True,
		desc='Increase Summon Zombie Dogs damage by <span>10 - 15%</span>')
	summonZombieDogs.save()

	wallOfDeath = Affix(category='',
		affix='wallOfDeath',
		is_primary=True,
		desc='Increase Wall of Death damage by <span>10 - 15%</span>')
	wallOfDeath.save()

	zombieCharger = Affix(category='',
		affix='zombieCharger',
		is_primary=True,
		desc='Increase Zombie Charger damage by <span>10 - 15%</span>')
	zombieCharger.save()


#Wizard Skills
#==============================================================================
#==============================================================================
	arcaneOrb = Affix(category='',
		affix='arcaneOrb',
		is_primary=True,
		desc='Increase Arcane Orb damage by <span>10 - 15%</span>')
	arcaneOrb.save()

	electrocute = Affix(category='',
		affix='electrocute',
		is_primary=True,
		desc='Increase Electrocute damage by <span>10 - 15%</span>')
	electrocute.save()

	rayOfFrost = Affix(category='',
		affix='rayOfFrost',
		is_primary=True,
		desc='Increase Ray of Frost damage by <span>10 - 15%</span>')
	rayOfFrost.save()

	spectralBlade = Affix(category='',
		affix='spectralBlade',
		is_primary=True,
		desc='Increase Spectral Blade damage by <span>10 - 15%</span>')
	spectralBlade.save()

	blackHole = Affix(category='',
		affix='blackHole',
		is_primary=True,
		desc='Increase Black Hole damage by <span>10 - 15%</span>')
	blackHole.save()

	meteor = Affix(category='',
		affix='meteor',
		is_primary=True,
		desc='Increase Meteor damage by <span>10 - 15%</span>')
	meteor.save()

	waveOfForce = Affix(category='',
		affix='waveOfForce',
		is_primary=True,
		desc='Increase Wave of Force damage by <span>10 - 15%</span>')
	waveOfForce.save()

	arcaneTorrent = Affix(category='',
		affix='arcaneTorrent',
		is_primary=True,
		desc='Increase Arcane Torrent damage by <span>10 - 15%</span>')
	arcaneTorrent.save()

	shockPulse = Affix(category='',
		affix='shockPulse',
		is_primary=True,
		desc='Increase Shock Pulse damage by <span>10 - 15%</span>')
	shockPulse.save()

	familiar = Affix(category='',
		affix='familiar',
		is_primary=True,
		desc='Increase Familiar damage by <span>10 - 15%</span>')
	familiar.save()

	magicMissle = Affix(category='',
		affix='magicMissle',
		is_primary=True,
		desc='Increase Magic Missle damage by <span>10 - 15%</span>')
	magicMissle.save()

	energyTwister = Affix(category='',
		affix='energyTwister',
		is_primary=True,
		desc='Increase Energy Twister damage by <span>10 - 15%</span>')
	energyTwister.save()

	blizzard = Affix(category='',
		affix='blizzard',
		is_primary=True,
		desc='Increase Blizzard damage by <span>10 - 15%</span>')
	blizzard.save()

	disintegrate = Affix(category='',
		affix='disintegrate',
		is_primary=True,
		desc='Increase Disintegrate damage by <span>10 - 15%</span>')
	disintegrate.save()

	explosiveBlast = Affix(category='',
		affix='explosiveBlast',
		is_primary=True,
		desc='Increase Explosive Blast damage by <span>10 - 15%</span>')
	explosiveBlast.save()

	hydra = Affix(category='',
		affix='hydra',
		is_primary=True,
		desc='Increase Hydra damage by <span>10 - 15%</span>')
	hydra.save()

#Secondaries
#==============================================================================
#==============================================================================
	eleRes = Affix(category='',
		affix='eleRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Resistance to {<span class="vary">One Element</span>}',
		ancient='<span>+176 - 210</span> Resistance to {<span class="vary">One Element</span>}',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane')
	eleRes.save()

	physRes = Affix(category='',
		affix='physRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Physical Resistance',
		ancient='<span>+176 - 210</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(category='',
		affix='coldRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Cold Resistance',
		ancient='<span>+176 - 210</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(category='',
		affix='fireRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Fire Resistance',
		ancient='<span>+176 - 210</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(category='',
		affix='lightRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Lightning Resistance',
		ancient='<span>+176 - 210</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(category='',
		affix='poisRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Poison Resistance',
		ancient='<span>+176 - 210</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(category='',
		affix='arcaneRes',
		is_primary=False,
		desc='<span>+141 - 160</span> Arcane Resistance',
		ancient='<span>+176 - 210</span> Arcane Resistance')
	arcaneRes.save()

	maxResource = Affix(category='',
		affix='maxResource',
		is_primary=False,
		desc='Increase Max {<span class="vary">Resource</span>}',
		notes='Fury<br>Wrath<br>Discipline<br>Spirit<br>Mana<br>Arcane Power')
	maxResource.save()

	maxFury = Affix(category='',
		affix='maxFury',
		is_primary=False,
		desc='<span>+</span> Max Fury')
	maxFury.save()

	maxWrath = Affix(category='',
		affix='maxWrath',
		is_primary=False,
		desc='<span>+</span> Max Wrath')
	maxWrath.save()

	maxDisc = Affix(category='',
		affix='maxDisc',
		is_primary=False,
		desc='<span>+9 - 12</span> Max Discipline')
	maxDisc.save()

	maxAP = Affix(category='',
		affix='maxAP',
		is_primary=False,
		desc='<span>+10 - 14</span> Max Arcane Power')
	maxAP.save()

	maxMana = Affix(category='',
		affix='maxMana',
		is_primary=False,
		desc='<span>+</span> Max Mana')
	maxMana.save()


	reducedRangedDmg = Affix(category='',
		affix='reducedRangedDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Ranged Damage Reduction')
	reducedRangedDmg.save()

	reducedMeleeDmg = Affix(category='',
		affix='reducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	reducedMeleeDmg.save()

	ccReduction = Affix(category='',
		affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()


	lpk = Affix(category='',
		affix='lpk',
		is_primary=False,
		desc='<span>+</span> Life per Kill',
		ancient='<span>+</span> Life per Kill')
	lpk.save()

	itemHealing = Affix(category='',
		affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29,713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	itemPickup = Affix(category='',
		affix='itemPickup',
		is_primary=False,
		desc='<span>+1 - 2</span> Yards to Gold and Globe Pickup')
	itemPickup.save()


	ccChance = Affix(category='',
		affix='ccChance',
		is_primary=False,
		desc='<span>+1.0 - 5.1%</span> chance to {<span class="vary">Crowd Control</span>} on Hit')
	ccChance.save()

	fearChance = Affix(category='',
		affix='fearChance',
		is_primary=False,
		desc='<span>+</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(category='',
		affix='stunChance',
		is_primary=False,
		desc='<span>+</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(category='',
		affix='blindChance',
		is_primary=False,
		desc='<span>+</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(category='',
		affix='freezeChance',
		is_primary=False,
		desc='<span>+</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(category='',
		affix='chillChance',
		is_primary=False,
		desc='<span>+</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(category='',
		affix='slowChance',
		is_primary=False,
		desc='<span>+</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(category='',
		affix='immobilizeChance',
		is_primary=False,
		desc='<span>+</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(category='',
		affix='knockbackChance',
		is_primary=False,
		desc='<span>+</span> chance to Knockback on Hit')
	knockbackChance.save()


	extraGold = Affix(category='',
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	thorns = Affix(category='',
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()

	killExp = Affix(category='',
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	lvlReq = Affix(category='',
		affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()

	durability = Affix(category='',
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()