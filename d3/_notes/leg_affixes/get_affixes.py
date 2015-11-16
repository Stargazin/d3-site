#Primaries
#==============================================================================
#==============================================================================
	dmg = Affix.objects.get(affix='dmg')
	mainStat = Affix.objects.get(affix='mainStat')
	dext = Affix.objects.get(affix='dext')
	inte = Affix.objects.get(affix='inte')
	stre = Affix.objects.get(affix='stre')
	vita = Affix.objects.get(affix='vita')

	eleDmg = Affix.objects.get(affix='eleDmg')
	physDmg = Affix.objects.get(affix='physDmg')
	coldDmg = Affix.objects.get(affix='coldDmg')
	fireDmg = Affix.objects.get(affix='fireDmg')
	lightDmg = Affix.objects.get(affix='lightDmg')
	poisDmg = Affix.objects.get(affix='poisDmg')
	arcaneDmg = Affix.objects.get(affix='arcaneDmg')
	holyDmg = Affix.objects.get(affix='holyDmg')

	ias = Affix.objects.get(affix='ias')
	chc = Affix.objects.get(affix='chc')
	chd = Affix.objects.get(affix='chd')
	cdr = Affix.objects.get(affix='cdr')
	eliteDmg = Affix.objects.get(affix='eliteDmg')
	areaDmg = Affix.objects.get(affix='areaDmg')
	bleedChance = Affix.objects.get(affix='bleedChance')

	armor = Affix.objects.get(affix='armor')
	allRes = Affix.objects.get(affix='allRes')
	blockChance = Affix.objects.get(affix='blockChance')
	reducedEliteDmg = Affix.objects.get(affix='reducedEliteDmg')
	life = Affix.objects.get(affix='life')
	lps = Affix.objects.get(affix='lps')
	lph = Affix.objects.get(affix='lph')
	lifePerWrath = Affix.objects.get(affix='lifePerWrath')

	rcr = Affix.objects.get(affix='rcr')
	wrathRegen = Affix.objects.get(affix='wrathRegen')
	hatredRegen = Affix.objects.get(affix='hatredRegen')
	apCrit = Affix.objects.get(affix='apCrit')
	manaRegen = Affix.objects.get(affix='manaRegen')

	sockets = Affix.objects.get(affix='sockets')

	skillDmg = Affix.objects.get(affix='skillDmg')

#Crusader Skills
#==============================================================================
	blessedHammer = Affix.objects.get(affix='blessedHammer')
	blessedShield = Affix.objects.get(affix='blessedShield')
	bombardment = Affix.objects.get(affix='bombardment')
	condemn = Affix.objects.get(affix='condemn')
	fallingSword = Affix.objects.get(affix='fallingSword')
	fistOfTheHeavens = Affix.objects.get(affix='fistOfTheHeavens')
	heavensFury = Affix.objects.get(affix='heavensFury')
	justice = Affix.objects.get(affix='justice')
	phalanx = Affix.objects.get(affix='phalanx')
	punish = Affix.objects.get(affix='punish')
	shieldBash = Affix.objects.get(affix='shieldBash')
	slash = Affix.objects.get(affix='slash')
	smite = Affix.objects.get(affix='smite')
	sweepAttack = Affix.objects.get(affix='sweepAttack')

#Demon Hunter Skills
#==============================================================================
	bolas = Affix.objects.get(affix='bolas')
	chakram = Affix.objects.get(affix='chakram')
	clusterArrow = Affix.objects.get(affix='clusterArrow')
	companion = Affix.objects.get(affix='companion')
	elementalArrow = Affix.objects.get(affix='elementalArrow')
	entanglingShot = Affix.objects.get(affix='entanglingShot')
	evasiveFire = Affix.objects.get(affix='evasiveFire')
	fanOfKnives = Affix.objects.get(affix='fanOfKnives')
	grenade = Affix.objects.get(affix='grenade')
	hungeringArrow = Affix.objects.get(affix='hungeringArrow')
	impale = Affix.objects.get(affix='impale')
	multishot = Affix.objects.get(affix='multishot')
	rainOfVengeance = Affix.objects.get(affix='rainOfVengeance')
	rapidFire = Affix.objects.get(affix='rapidFire')
	sentry = Affix.objects.get(affix='sentry')
	spikeTrap = Affix.objects.get(affix='spikeTrap')
	strafe = Affix.objects.get(affix='strafe')

#Monk Skills
#==============================================================================
	explodingPalm = Affix.objects.get(affix='explodingPalm')
	lashingTailKick = Affix.objects.get(affix='lashingTailKick')
	tempestRush = Affix.objects.get(affix='tempestRush')
	waveOfLight = Affix.objects.get(affix='waveOfLight')

#Witch Doctor Skills
#==============================================================================
	acidCloud = Affix.objects.get(affix='acidCloud')
	corpseSpiders = Affix.objects.get(affix='corpseSpiders')
	fetishArmy = Affix.objects.get(affix='fetishArmy')
	firebats = Affix.objects.get(affix='firebats')
	firebomb = Affix.objects.get(affix='firebomb')
	gargantuan = Affix.objects.get(affix='gargantuan')
	graspOfTheDead = Affix.objects.get(affix='graspOfTheDead')
	haunt = Affix.objects.get(affix='haunt')
	locustSwarm = Affix.objects.get(affix='locustSwarm')
	piranhas = Affix.objects.get(affix='piranhas')
	plagueOfToads = Affix.objects.get(affix='plagueOfToads')
	poisonDart = Affix.objects.get(affix='poisonDart')
	sacrifice = Affix.objects.get(affix='sacrifice')
	spiritBarrage = Affix.objects.get(affix='spiritBarrage')
	summonZombieDogs = Affix.objects.get(affix='summonZombieDogs')
	wallOfDeath = Affix.objects.get(affix='wallOfDeath')
	zombieCharger = Affix.objects.get(affix='zombieCharger')

#Wizard Skills
#==============================================================================
	arcaneOrb = Affix.objects.get(affix='arcaneOrb')
	arcaneTorrent = Affix.objects.get(affix='arcaneTorrent')
	blackHole = Affix.objects.get(affix='blackHole')
	blizzard = Affix.objects.get(affix='blizzard')
	disintegrate = Affix.objects.get(affix='disintegrate')
	electrocute = Affix.objects.get(affix='electrocute')
	energyTwister = Affix.objects.get(affix='energyTwister')
	explosiveBlast = Affix.objects.get(affix='explosiveBlast')
	familiar = Affix.objects.get(affix='familiar')
	hydra = Affix.objects.get(affix='hydra')
	magicMissle = Affix.objects.get(affix='magicMissle')
	meteor = Affix.objects.get(affix='meteor')
	rayOfFrost = Affix.objects.get(affix='rayOfFrost')
	shockPulse = Affix.objects.get(affix='shockPulse')
	spectralBlade = Affix.objects.get(affix='spectralBlade')
	waveOfForce = Affix.objects.get(affix='waveOfForce')

#Secondaries
#==============================================================================
#==============================================================================
	eleRes = Affix.objects.get(affix='eleRes')
	physRes = Affix.objects.get(affix='physRes')
	coldRes = Affix.objects.get(affix='coldRes')
	fireRes = Affix.objects.get(affix='fireRes')
	lightRes = Affix.objects.get(affix='lightRes')
	poisRes = Affix.objects.get(affix='poisRes')
	arcaneRes = Affix.objects.get(affix='arcaneRes')

	maxResource = Affix.objects.get(affix='maxResource')
	maxWrath = Affix.objects.get(affix='maxWrath')
	maxDisc = Affix.objects.get(affix='maxDisc')
	maxAP = Affix.objects.get(affix='maxAP')
	maxMana = Affix.objects.get(affix='maxMana')

	reducedRangedDmg = Affix.objects.get(affix='reducedRangedDmg')
	reducedMeleeDmg = Affix.objects.get(affix='reducedMeleeDmg')
	ccReduction = Affix.objects.get(affix='ccReduction')

	lpk = Affix.objects.get(affix='lpk')
	itemHealing = Affix.objects.get(affix='itemHealing')
	itemPickup = Affix.objects.get(affix='itemPickup')

	fearChance = Affix.objects.get(affix='fearChance')
	stunChance = Affix.objects.get(affix='stunChance')
	blindChance = Affix.objects.get(affix='blindChance')
	freezeChance = Affix.objects.get(affix='freezeChance')
	chillChance = Affix.objects.get(affix='chillChance')
	slowChance = Affix.objects.get(affix='slowChance')
	immobilizeChance = Affix.objects.get(affix='immobilizeChance')
	knockbackChance = Affix.objects.get(affix='knockbackChance')

	extraGold = Affix.objects.get(affix='extraGold')
	thorns = Affix.objects.get(affix='thorns')
	killExp = Affix.objects.get(affix='killExp')
	lvlReq = Affix.objects.get(affix='lvlReq')
	durability = Affix.objects.get(affix='durability')