def load__affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")


	dmg = Affix(affix='dmg',
		is_primary=True,
		desc='<span>+</span> -- <span></span> Damage',
		ancient='<span>+</span> -- <span></span> Damage')
	dmg.save()

	mainStat = Affix(affix='mainStat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+825 - 1,000</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	dext = Affix(affix='dext',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000</span> Dexterity')
	dext.save()

	inte = Affix(affix='inte', 
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	stre = Affix(affix='stre',
		is_primary=True,
		desc='<span>+626 - 750</span> Strength',
		ancient='<span>+825 - 1,000</span> Strength')
	stre.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()


	eleDmg = Affix(affix='eleDmg',
		is_primary=True,
		desc='Skills of {<span class="vary">One Element</span>} do <span>15 - 20%</span> more damage',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane<br>Holy')
	eleDmg.save()

	physDmg = Affix(affix='physDmg',
		is_primary=True,
		desc='Physical skills do <span>15 - 20%</span> more damage')
	physDmg.save()

	coldDmg = Affix(affix='coldDmg',
		is_primary=True,
		desc='Cold skills do <span>15 - 20%</span> more damage')
	coldDmg.save()

	fireDmg = Affix(affix='fireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	fireDmg.save()

	lightDmg = Affix(affix='lightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	lightDmg.save()

	poisDmg = Affix(affix='poisDmg',
		is_primary=True,
		desc='Poison skills do <span>15 - 20%</span> more damage')
	poisDmg.save()

	arcaneDmg = Affix(affix='arcaneDmg',
		is_primary=True,
		desc='Arcane skills do <span>15 - 20%</span> more damage')
	arcaneDmg.save()

	holyDmg = Affix(affix='holyDmg',
		is_primary=True,
		desc='Holy skills do <span>15 - 20%</span> more damage')
	holyDmg.save()



	ias = Affix(affix='ias',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	chc = Affix(affix='chc',
		is_primary=True,
		desc='<span>+%</span> Critical Hit Chance')
	chc.save()

	chd = Affix(affix='chd',
		is_primary=True,
		desc='<span>+%</span> Critical Hit Damage')
	chd.save()

	cdr = Affix(affix='cdr',
		is_primary=True,
		desc='<span>+%</span> Cooldown Reduction')
	cdr.save()

	eliteDmg = Affix(affix='eliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>%</span>')
	eliteDmg.save()

	areaDmg = Affix(affix='areaDmg',
		is_primary=True,
		desc='<span>+%</span> Area Damage')
	areaDmg.save()

	bleedChance = Affix(affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()


	armor = Affix(affix='armor',
		is_primary=True,
		desc='<span>+</span> Armor',
		ancient='<span>+</span> Armor')
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
		desc='<span>+%</span> Life')
	life.save()

	lps = Affix(affix='lps',
		is_primary=True,
		desc='<span>+</span> Life Regeneration per Second',
		ancient='<span>+</span> Life Regeneration per Second')
	lps.save()

	lph = Affix(affix='lph',
		is_primary=True,
		desc='<span>+</span> Life per Hit',
		ancient='<span>+</span> Life per Hit')
	lph.save()

	lifePerWrath = Affix(affix='lifePerWrath',
		is_primary=True,
		desc='<span>+</span> Life per Wrath spent',
		ancient='<span>+</span> Life per Wrath spent')
	lifePerWrath.save()


	rcr = Affix(affix='rcr',
		is_primary=True,
		desc='<span>+%</span> Resource Cost Reduction')
	rcr.save()

	wrathRegen = Affix(affix='wrathRegen',
		is_primary=True,
		desc='<span>+1.85 - 2.00</span> Wrath Regeneration')
	wrathRegen.save()

	hatredRegen = Affix(affix='hatredRegen',
		is_primary=True,
		desc='<span>+1.35 - 1.50</span> Hatred Regeneration per Second')
	hatredRegen.save()

	apCrit = Affix(affix='apCrit',
		is_primary=True,
		desc='<span>+3 - 4</span> Arcane Power on Critical Hits')
	apCrit.save()

	manaRegen = Affix(affix='manaRegen',
		is_primary=True,
		desc='<span>+12.00 - 14.00</span> Mana Regeneratioin per Second')
	manaRegen.save()


	sockets = Affix(affix='sockets',
		is_primary=True,
		desc='Sockets (<span></span>)')
	sockets.save()


	skillDmg = Affix(affix='skillDmg',
		is_primary=True,
		desc='Increases {<span class="vary">Skill Damage</span>} by <span>10 - 15%</span>'
		notes='<br>')
	skillDmg.save()

#Crusader Skills
#==============================================================================
#==============================================================================
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

#Demon Hunter Skills
#==============================================================================
#==============================================================================
	bolas = Affix(affix='bolas',
		is_primary=True,
		desc='Increase Bola damage by <span>10 - 15%</span>')
	bolas.save()

	chakram = Affix(affix='chakram',
		is_primary=True,
		desc='Increase Chakram damage by <span>10 - 15%</span>')
	chakram.save()

	clusterArrow = Affix(affix='clusterArrow',
		is_primary=True,
		desc='Increase Cluster Arrow damage by <span>10 - 15%</span>')
	clusterArrow.save()

	companion = Affix(affix='companion',
		is_primary=True,
		desc='Increase Companion damage by <span>10 - 15%</span>')
	companion.save()

	elementalArrow = Affix(affix='elementalArrow',
		is_primary=True,
		desc='Increase Elemental Arrow damage by <span>10 - 15%</span>')
	elementalArrow.save()

	entanglingShot = Affix(affix='entanglingShot',
		is_primary=True,
		desc='Increase Entangling Shot damage by <span>10 - 15%</span>')
	entanglingShot.save()

	evasiveFire = Affix(affix='evasiveFire',
		is_primary=True,
		desc='Increase Evasive Fire damage by <span>10 - 15%</span>')
	evasiveFire.save()

	fanOfKnives = Affix(affix='fanOfKnives',
		is_primary=True,
		desc='Increase Fan of Knives damage by <span>10 - 15%</span>')
	fanOfKnives.save()

	grenade = Affix(affix='grenade',
		is_primary=True,
		desc='Increase Grenade damage by <span>10 - 15%</span>')
	grenade.save()

	hungeringArrow = Affix(affix='hungeringArrow',
		is_primary=True,
		desc='Increase Hungering Arrow damage by <span>10 - 15%</span>')
	hungeringArrow.save()

	impale = Affix(affix='impale',
		is_primary=True,
		desc='Increase Impale damage by <span>10 - 15%</span>')
	impale.save()

	multishot = Affix(affix='multishot',
		is_primary=True,
		desc='Increase Multishot damage by <span>10 - 15%</span>')
	multishot.save()

	rainOfVengeance = Affix(affix='rainOfVengeance',
		is_primary=True,
		desc='Increase Rain of Vengeance damage by <span>10 - 15%</span>')
	rainOfVengeance.save()

	rapidFire = Affix(affix='rapidFire',
		is_primary=True,
		desc='Increase Rapid Fire damage by <span>10 - 15%</span>')
	rapidFire.save()

	sentry = Affix(affix='sentry',
		is_primary=True,
		desc='Increase Sentry damage by <span>10 - 15%</span>')
	sentry.save()

	spikeTrap = Affix(affix='spikeTrap',
		is_primary=True,
		desc='Increase Spike Trap damage by <span>10 - 15%</span>')
	spikeTrap.save()

	strafe = Affix(affix='strafe',
		is_primary=True,
		desc='Increase Strafe damage by <span>10 - 15%</span>')
	strafe.save()

#Monk Skills
#==============================================================================
#==============================================================================
	explodingPalm = Affix(affix='explodingPalm',
		is_primary=True,
		desc='Increase Exploding Palm damage by <span>10 - 15%</span>')
	explodingPalm.save()

	lashingTailKick = Affix(affix='Lashing Tail Kick',
		is_primary=True,
		desc='Increase lashingTailKick damage by <span>10 - 15%</span>')
	lashingTailKick.save()

	tempestRush = Affix(affix='tempestRush',
		is_primary=True,
		desc='Increase Tempest Rush damage by <span>10 - 15%</span>')
	tempestRush.save()

	waveOfLight = Affix(affix='waveOfLight',
		is_primary=True,
		desc='Increase Wave of Light damage by <span>10 - 15%</span>')
	waveOfLight.save()

#Witch Doctor Skills
#==============================================================================
#==============================================================================
	acidCloud = Affix(affix='acidCloud',
		is_primary=True,
		desc='Increase Acid Cloud damage by <span>10 - 15%</span>')
	acidCloud.save()

	corpseSpiders = Affix(affix='corpseSpiders',
		is_primary=True,
		desc='Increase Corpse Spiders damage by <span>10 - 15%</span>')
	corpseSpiders.save()

	fetishArmy = Affix(affix='fetishArmy',
		is_primary=True,
		desc='Increase Fetish Army damage by <span>10 - 15%</span>')
	fetishArmy.save()

	firebats = Affix(affix='firebats',
		is_primary=True,
		desc='Increase Fire Bats damage by <span>10 - 15%</span>')
	firebats.save()

	firebomb = Affix(affix='firebomb',
		is_primary=True,
		desc='Increase Fire Bomb damage by <span>10 - 15%</span>')
	firebomb.save()

	gargantuan = Affix(affix='gargantuan',
		is_primary=True,
		desc='Increase Gargantuan damage by <span>10 - 15%</span>')
	gargantuan.save()

	graspOfTheDead = Affix(affix='graspOfTheDead',
		is_primary=True,
		desc='Increase Grasp of the Dead damage by <span>10 - 15%</span>')
	graspOfTheDead.save()

	haunt = Affix(affix='haunt',
		is_primary=True,
		desc='Increase Haunt damage by <span>10 - 15%</span>')
	haunt.save()

	locustSwarm = Affix(affix='locustSwarm',
		is_primary=True,
		desc='Increase Locust Swarm damage by <span>10 - 15%</span>')
	locustSwarm.save()

	piranhas = Affix(affix='piranhas',
		is_primary=True,
		desc='Increase Piranhas damage by <span>10 - 15%</span>')
	piranhas.save()

	plagueOfToads = Affix(affix='plagueOfToads',
		is_primary=True,
		desc='Increase Plague of Toads damage by <span>10 - 15%</span>')
	plagueOfToads.save()

	poisonDart = Affix(affix='poisonDart',
		is_primary=True,
		desc='Increase Poison Dart damage by <span>10 - 15%</span>')
	poisonDart.save()

	sacrifice = Affix(affix='sacrifice',
		is_primary=True,
		desc='Increase Sacrifice damage by <span>10 - 15%</span>')
	sacrifice.save()

	spiritBarrage = Affix(affix='spiritBarrage',
		is_primary=True,
		desc='Increase Spirit Barrage damage by <span>10 - 15%</span>')
	spiritBarrage.save()

	summonZombieDogs = Affix(affix='summonZombieDogs',
		is_primary=True,
		desc='Increase Summon Zombie Dogs damage by <span>10 - 15%</span>')
	summonZombieDogs.save()

	wallOfDeath = Affix(affix='wallOfDeath',
		is_primary=True,
		desc='Increase Wall of Death damage by <span>10 - 15%</span>')
	wallOfDeath.save()

	zombieCharger = Affix(affix='zombieCharger',
		is_primary=True,
		desc='Increase Zombie Charger damage by <span>10 - 15%</span>')
	zombieCharger.save()


#Wizard Skills
#==============================================================================
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
	eleRes = Affix(affix='eleRes',
		is_primary=False,
		desc='<span>+</span> Resistance to {<span class="vary">One Element</span>}',
		ancient='<span>+</span> Resistance to {<span class="vary">One Element</span>}',
		notes='Physical<br>Cold<br>Fire<br>Lightning<br>Poison<br>Arcane')
	eleRes.save()

	physRes = Affix(affix='physRes',
		is_primary=False,
		desc='<span>+</span> Physical Resistance',
		ancient='<span>+</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(affix='coldRes',
		is_primary=False,
		desc='<span>+</span> Cold Resistance',
		ancient='<span>+</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(affix='fireRes',
		is_primary=False,
		desc='<span>+</span> Fire Resistance',
		ancient='<span>+</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(affix='lightRes',
		is_primary=False,
		desc='<span>+</span> Lightning Resistance',
		ancient='<span>+</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(affix='poisRes',
		is_primary=False,
		desc='<span>+</span> Poison Resistance',
		ancient='<span>+</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(affix='arcaneRes',
		is_primary=False,
		desc='<span>+</span> Arcane Resistance',
		ancient='<span>+</span> Arcane Resistance')
	arcaneRes.save()

	maxResource = Affix(affix='maxResource',
		is_primary=False,
		desc='Increase Max {<span class="vary">Resource</span>}',
		notes='Fury<br>Wrath<br>Discipline<br>Spirit<br>Mana<br>Arcane Power')
	maxResource.save()

	maxWrath = Affix(affix='maxWrath',
		is_primary=False,
		desc='<span>+</span> Max Wrath')
	maxWrath.save()

	maxDisc = Affix(affix='maxDisc',
		is_primary=False,
		desc='<span>+</span> Max Discipline')
	maxDisc.save()

	maxAP = Affix(affix='maxAP',
		is_primary=False,
		desc='<span>+10 - 14</span> Max Arcane Power')
	maxAP.save()

	maxMana = Affix(affix='maxMana',
		is_primary=False,
		desc='<span>+</span> Max Mana')
	maxMana.save()


	reducedRangedDmg = Affix(affix='reducedRangedDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Ranged Damage Reduction')
	reducedRangedDmg.save()

	reducedMeleeDmg = Affix(affix='reducedMeleeDmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	reducedMeleeDmg.save()

	ccReduction = Affix(affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()


	lpk = Affix(affix='lpk',
		is_primary=False,
		desc='<span>+</span> Life per Kill',
		ancient='<span>+</span> Life per Kill')
	lpk.save()

	itemHealing = Affix(affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29,713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	itemPickup = Affix(affix='itemPickup',
		is_primary=False,
		desc='<span>+1 - 2</span> Yards to Gold and Globe Pickup')
	itemPickup.save()


	fearChance = Affix(affix='fearChance',
		is_primary=False,
		desc='<span>+%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(affix='stunChance',
		is_primary=False,
		desc='<span>+%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(affix='blindChance',
		is_primary=False,
		desc='<span>+%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(affix='freezeChance',
		is_primary=False,
		desc='<span>+%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(affix='chillChance',
		is_primary=False,
		desc='<span>+%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(affix='slowChance',
		is_primary=False,
		desc='<span>+%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(affix='immobilizeChance',
		is_primary=False,
		desc='<span>+%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(affix='knockbackChance',
		is_primary=False,
		desc='<span>+%</span> chance to Knockback on Hit')
	knockbackChance.save()


	extraGold = Affix(affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	thorns = Affix(affix='thorns',
		is_primary=False,
		desc='Attackers take <span></span> damage',
		ancient='Attackers take <span></span> damage')
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