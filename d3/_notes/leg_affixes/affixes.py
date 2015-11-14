def load__affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")

	sockets = Affix(id=,
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span></span>)')
	sockets.save()


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

	blockChance = Affix(id=,
		affix='blockChance',
		is_primary=True,
		desc='<span class="silver">+11%</span> Chance to Block')
	blockChance.save()

	reducedEliteDmg = Affix(id=,
		affix='reducedEliteDmg',
		is_primary=True,
		desc='<span>+10.0 - 11.0%</span> Elite Damage Reduction')
	reducedEliteDmg.save()

	life = Affix(id=,
		affix='life',
		is_primary=True,
		desc='<span>+%</span> Life')
	life.save()

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

	lifePerWrath = Affix(id=,
		affix='lifePerWrath',
		is_primary=True,
		desc='<span>+</span> Life per Wrath spent',
		ancient='<span>+</span> Life per Wrath spent')
	lifePerWrath.save()


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

	cdr = Affix(id=,
		affix='cdr',
		is_primary=True,
		desc='<span>+%</span> Cooldown Reduction')
	cdr.save()

	eliteDmg = Affix(id=,
		affix='eliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>%</span>')
	eliteDmg.save()

	areaDmg = Affix(id=,
		affix='areaDmg',
		is_primary=True,
		desc='<span>+%</span> Area Damage')
	areaDmg.save()

	bleedChance = Affix(id=,
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()


	rcr = Affix(id=,
		affix='rcr',
		is_primary=True,
		desc='<span>+%<span> Resource Cost Reduction')
	rcr.save()

	wrathRegen = Affix(id=,
		affix='wrathRegen',
		is_primary=True,
		desc='<span>+1.85 - 2.00</span> Wrath Regeneration')
	wrathRegen.save()

	hatredRegen = Affix(id=,
		affix='hatredRegen',
		is_primary=True,
		desc='<span>+1.35 - 1.50</span> Hatred Regeneration per Second')
	hatredRegen.save()

	apCrit = Affix(id=,
		affix='apCrit',
		is_primary=True,
		desc='<span>+3 - 4</span> Arcane Power on Critical Hits')
	apCrit.save()

	manaRegen = Affix(id=,
		affix='manaRegen',
		is_primary=True,
		desc='<span>+12.00 - 14.00</span> Mana Regeneratioin per Second')
	manaRegen.save()

#Crusader Skills
#==============================================================================
#==============================================================================
	blessedHammer = Affix(id=,
		affix='blessedHammer',
		is_primary=True,
		desc='Increase Blessed Hammer damage by <span>10 - 15%</span>')
	blessedHammer.save()

	blessedShield = Affix(id=,
		affix='blessedShield',
		is_primary=True,
		desc='Increase Blessed Shield damage by <span>10 - 15%</span>')
	blessedShield.save()

	bombardment = Affix(id=,
		affix='bombardment',
		is_primary=True,
		desc='Increase Bombardment damage by <span>10 - 15%</span>')
	bombardment.save()

	condemn = Affix(id=,
		affix='condemn',
		is_primary=True,
		desc='Increase Condemn damage by <span>10 - 15%</span>')
	condemn.save()

	fallingSword = Affix(id=,
		affix='fallingSword',
		is_primary=True,
		desc='Increase Falling Sword damage by <span>10 - 15%</span>')
	fallingSword.save()

	fistOfTheHeavens = Affix(id=,
		affix='fistOfTheHeavens',
		is_primary=True,
		desc='Increase Fist of the  Heavens damage by <span>10 - 15%</span>')
	fistOfTheHeavens.save()

	heavensFury = Affix(id=,
		affix='heavensFury',
		is_primary=True,
		desc='Increase Heaven\'s Fury damage by <span>10 - 15%</span>')
	heavensFury.save()

	justice = Affix(id=,
		affix='justice',
		is_primary=True,
		desc='Increase Justice damage by <span>10 - 15%</span>')
	justice.save()

	phalanx = Affix(id=,
		affix='phalanx',
		is_primary=True,
		desc='Increase Phalanx damage by <span>10 - 15%</span>')
	phalanx.save()

	 punish= Affix(id=,
		affix='punish',
		is_primary=True,
		desc='Increase Punish damage by <span>10 - 15%</span>')
	punish.save()

	 shieldBash= Affix(id=,
		affix='shieldBash',
		is_primary=True,
		desc='Increase Shield Bash damage by <span>10 - 15%</span>')
	shieldBash.save()

	slash = Affix(id=,
		affix='slash',
		is_primary=True,
		desc='Increase Slash damage by <span>10 - 15%</span>')
	slash.save()

	smite = Affix(id=,
		affix='smite',
		is_primary=True,
		desc='Increase Smite damage by <span>10 - 15%</span>')
	smite.save()

	sweepAttack = Affix(id=,
		affix='sweepAttack',
		is_primary=True,
		desc='Increase Sweep Attack damage by <span>10 - 15%</span>')
	sweepAttack.save()

#Demon Hunter Skills
#==============================================================================
#==============================================================================
	bolas = Affix(id=,
		affix='bolas',
		is_primary=True,
		desc='Increase Bola damage by <span>10 - 15%</span>')
	bolas.save()

	chakram = Affix(id=,
		affix='chakram',
		is_primary=True,
		desc='Increase Chakram damage by <span>10 - 15%</span>')
	chakram.save()

	clusterArrow = Affix(id=,
		affix='clusterArrow',
		is_primary=True,
		desc='Increase Cluster Arrow damage by <span>10 - 15%</span>')
	clusterArrow.save()

	companion = Affix(id=,
		affix='companion',
		is_primary=True,
		desc='Increase Companion damage by <span>10 - 15%</span>')
	companion.save()

	elementalArrow = Affix(id=,
		affix='elementalArrow',
		is_primary=True,
		desc='Increase Elemental Arrow damage by <span>10 - 15%</span>')
	elementalArrow.save()

	entanglingShot = Affix(id=,
		affix='entanglingShot',
		is_primary=True,
		desc='Increase Entangling Shot damage by <span>10 - 15%</span>')
	entanglingShot.save()

	evasiveFire = Affix(id=,
		affix='evasiveFire',
		is_primary=True,
		desc='Increase Evasive Fire damage by <span>10 - 15%</span>')
	evasiveFire.save()

	fanOfKnives = Affix(id=,
		affix='fanOfKnives',
		is_primary=True,
		desc='Increase Fan of Knives damage by <span>10 - 15%</span>')
	fanOfKnives.save()

	grenade = Affix(id=,
		affix='grenade',
		is_primary=True,
		desc='Increase Grenade damage by <span>10 - 15%</span>')
	grenade.save()

	hungeringArrow = Affix(id=,
		affix='hungeringArrow',
		is_primary=True,
		desc='Increase Hungering Arrow damage by <span>10 - 15%</span>')
	hungeringArrow.save()

	impale = Affix(id=,
		affix='impale',
		is_primary=True,
		desc='Increase Impale damage by <span>10 - 15%</span>')
	impale.save()

	multishot = Affix(id=,
		affix='multishot',
		is_primary=True,
		desc='Increase Multishot damage by <span>10 - 15%</span>')
	multishot.save()

	rainOfVengeance = Affix(id=,
		affix='rainOfVengeance',
		is_primary=True,
		desc='Increase Rain of Vengeance damage by <span>10 - 15%</span>')
	rainOfVengeance.save()

	rapidFire = Affix(id=,
		affix='rapidFire',
		is_primary=True,
		desc='Increase Rapid Fire damage by <span>10 - 15%</span>')
	rapidFire.save()

	sentry = Affix(id=,
		affix='sentry',
		is_primary=True,
		desc='Increase Sentry damage by <span>10 - 15%</span>')
	sentry.save()

	spikeTrap = Affix(id=,
		affix='spikeTrap',
		is_primary=True,
		desc='Increase Spike Trap damage by <span>10 - 15%</span>')
	spikeTrap.save()

	strafe = Affix(id=,
		affix='strafe',
		is_primary=True,
		desc='Increase Strafe damage by <span>10 - 15%</span>')
	strafe.save()

#Witch Doctor Skills
#==============================================================================
#==============================================================================
	acidCloud = Affix(id=,
		affix='acidCloud',
		is_primary=True,
		desc='Increase Acid Cloud damage by <span>10 - 15%</span>')
	acidCloud.save()

	corpseSpiders = Affix(id=,
		affix='corpseSpiders',
		is_primary=True,
		desc='Increase Corpse Spiders damage by <span>10 - 15%</span>')
	corpseSpiders.save()

	fetishArmy = Affix(id=,
		affix='fetishArmy',
		is_primary=True,
		desc='Increase Fetish Army damage by <span>10 - 15%</span>')
	fetishArmy.save()

	firebats = Affix(id=,
		affix='firebats',
		is_primary=True,
		desc='Increase Fire Bats damage by <span>10 - 15%</span>')
	firebats.save()

	firebomb = Affix(id=,
		affix='firebomb',
		is_primary=True,
		desc='Increase Fire Bomb damage by <span>10 - 15%</span>')
	firebomb.save()

	gargantuan = Affix(id=,
		affix='gargantuan',
		is_primary=True,
		desc='Increase Gargantuan damage by <span>10 - 15%</span>')
	gargantuan.save()

	graspOfTheDead = Affix(id=,
		affix='graspOfTheDead',
		is_primary=True,
		desc='Increase Grasp of the Dead damage by <span>10 - 15%</span>')
	graspOfTheDead.save()

	haunt = Affix(id=,
		affix='haunt',
		is_primary=True,
		desc='Increase Haunt damage by <span>10 - 15%</span>')
	haunt.save()

	locustSwarm = Affix(id=,
		affix='locustSwarm',
		is_primary=True,
		desc='Increase Locust Swarm damage by <span>10 - 15%</span>')
	locustSwarm.save()

	piranhas = Affix(id=,
		affix='piranhas',
		is_primary=True,
		desc='Increase Piranhas damage by <span>10 - 15%</span>')
	piranhas.save()

	plagueOfToads = Affix(id=,
		affix='plagueOfToads',
		is_primary=True,
		desc='Increase Plague of Toads damage by <span>10 - 15%</span>')
	plagueOfToads.save()

	poisonDart = Affix(id=,
		affix='poisonDart',
		is_primary=True,
		desc='Increase Poison Dart damage by <span>10 - 15%</span>')
	poisonDart.save()

	sacrifice = Affix(id=,
		affix='sacrifice',
		is_primary=True,
		desc='Increase Sacrifice damage by <span>10 - 15%</span>')
	sacrifice.save()

	spiritBarrage = Affix(id=,
		affix='spiritBarrage',
		is_primary=True,
		desc='Increase Spirit Barrage damage by <span>10 - 15%</span>')
	spiritBarrage.save()

	summonZombieDogs = Affix(id=,
		affix='summonZombieDogs',
		is_primary=True,
		desc='Increase Summon Zombie Dogs damage by <span>10 - 15%</span>')
	summonZombieDogs.save()

	wallOfDeath = Affix(id=,
		affix='wallOfDeath',
		is_primary=True,
		desc='Increase Wall of Death damage by <span>10 - 15%</span>')
	wallOfDeath.save()

	zombieCharger = Affix(id=,
		affix='zombieCharger',
		is_primary=True,
		desc='Increase Zombie Charger damage by <span>10 - 15%</span>')
	zombieCharger.save()


#Wizard Skills
#==============================================================================
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


	maxWrath = Affix(id=,
		affix='maxWrath',
		is_primary=False,
		desc='<span>+</span> Max Wrath')
	maxWrath.save()

	maxDisc = Affix(id=,
		affix='maxDisc',
		is_primary=False,
		desc='<span>+</span> Max Discipline')
	maxDisc.save()

	maxAP = Affix(id=,
		affix='maxAP',
		is_primary=False,
		desc='<span>+</span> Max Arcane Power')
	maxAP.save()

	maxMana = Affix(id=,
		affix='maxMana',
		is_primary=False,
		desc='<span>+</span> Max Mana')
	maxMana.save()


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

	ccReduction = Affix(id=,
		affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()


	lpk = Affix(id=,
		affix='lpk',
		is_primary=False,
		desc='<span>+</span> Life per Kill',
		ancient='<span>+</span> Life per Kill')
	lpk.save()

	itemHealing = Affix(id=,
		affix='itemHealing',
		is_primary=False,
		desc='<span>+</span> Healing from Health Globes and Potions',
		ancient='<span>+3</span> Healing from Health Globes and Potions')
	itemHealing.save()


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


	extraGold = Affix(id=,
		affix='extraGold',
		is_primary=False,
		desc='<span>+%</span> Extra Gold from Monsters')
	extraGold.save()

	thorns = Affix(id=,
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span></span> damage',
		ancient='Attackers take <span></span> damage')
	thorns.save()

	killExp = Affix(id=,
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	lvlReq = Affix(id=,
		affix='lvlReq',
		is_primary=False,
		desc='Lower item level requirement by <span>2 - 30</span>')
	lvlReq.save()

	durability = Affix(id=,
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()