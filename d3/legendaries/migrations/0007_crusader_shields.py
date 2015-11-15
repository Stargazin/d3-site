# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_crusader_shields(apps, schema_editor):
	CrusaderShield = apps.get_model("legendaries", "CrusaderShield")
	Affix = apps.get_model("affixes", "CrusaderShieldAffix")

	sockets = Affix.objects.get(affix='sockets')
	stre = Affix.objects.get(affix='stre')
	vita = Affix.objects.get(affix='vita')

	armor = Affix.objects.get(affix='armor')
	allRes = Affix.objects.get(affix='allRes')
	blockChance = Affix.objects.get(affix='blockChance')
	reducedEliteDmg = Affix.objects.get(affix='reducedEliteDmg')
	life = Affix.objects.get(affix='life')
	lps = Affix.objects.get(affix='lps')
	lifePerWrath = Affix.objects.get(affix='lifePerWrath')

	chc = Affix.objects.get(affix='chc')
	cdr = Affix.objects.get(affix='cdr')
	eliteDmg = Affix.objects.get(affix='eliteDmg')
	areaDmg = Affix.objects.get(affix='areaDmg')
	bleedChance = Affix.objects.get(affix='bleedChance')

	rcr = Affix.objects.get(affix='rcr')
	wrathRegen = Affix.objects.get(affix='wrathRegen')

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


	eleRes = Affix.objects.get(affix='eleRes')
	physRes = Affix.objects.get(affix='physRes')
	coldRes = Affix.objects.get(affix='coldRes')
	fireRes = Affix.objects.get(affix='fireRes')
	lightRes = Affix.objects.get(affix='lightRes')
	poisRes = Affix.objects.get(affix='poisRes')
	arcaneRes = Affix.objects.get(affix='arcaneRes')

	maxWrath = Affix.objects.get(affix='maxWrath')

	reducedRangeDmg = Affix.objects.get(affix='reducedRangeDmg')
	reducedMeleeDmg = Affix.objects.get(affix='reducedMeleeDmg')
	ccReduction = Affix.objects.get(affix='ccReduction')

	itemHealing = Affix.objects.get(affix='itemHealing')

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

	akaratsAwakening = CrusaderShield(name='Akarat\'s Awakening',
		pic='/assets/media/items/legendaries/offhands/crusadershields/akarats_awakening.png',
		unique='Every successful block has a <span>20 - 25%</span> chance to reduce all cooldowns by <span class="silver">1</span> second.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='21.0 - 31.0%')
	akaratsAwakening.save()
	akaratsAwakening.affixes.add(stre, blockChance)

	frydehrsWrath = CrusaderShield(name='Frydehr\'s Wrath',
		pic='/assets/media/items/legendaries/offhands/crusadershields/frydehrs_wrath.png',
		unique='Condemn has no cooldown but instead costs <span class="silver">40</span> Wrath.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	frydehrsWrath.save()
	frydehrsWrath.affixes.add(stre)

	guardOfJohanna = CrusaderShield(name='Guard Of Johanna',
		pic='/assets/media/items/legendaries/offhands/crusadershields/guard_of_johanna.png',
		unique='Blessed Hammer damage is increased by <span>200 - 250%</span> for the first <span class="silver">3</span> enemies it hits.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	guardOfJohanna.save()
	guardOfJohanna.affixes.add(stre)

	hallowedBulwark = CrusaderShield(name='Hallowed Bulwark',
		pic='/assets/media/items/legendaries/offhands/crusadershields/hallowed_bulwark.png',
		unique='Iron Skin also increases your Block Amount by <span>45 - 60%</span>.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	hallowedBulwark.save()
	hallowedBulwark.affixes.add(stre)

	hellskull = CrusaderShield(name='hellskull',
		pic='/assets/media/items/legendaries/offhands/crusadershields/hellskull.png',
		unique='Gain <span class="silver">10%</span> increased damage while wielding a two-handed weapon.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	hellskull.save()
	hellskull.affixes.add(stre)

	jekangbord = CrusaderShield(name='jekangbord',
		pic='/assets/media/items/legendaries/offhands/crusadershields/jekangbord.png',
		unique='Blessed Shield ricochets to <span>4 - 6</span> additional enemies.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	jekangbord.save()
	jekangbord.affixes.add(stre)

	piroMarella = CrusaderShield(name='Piro Marella',
		pic='/assets/media/items/legendaries/offhands/crusadershields/piro_marella.png',
		unique='Reduces the Wrath cost of Shield Bash by <span>40 - 50%</span>.',
		random_primaries='4',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	piroMarella.save()
	piroMarella.affixes.add()

	salvation = CrusaderShield(name='salvation',
		pic='/assets/media/items/legendaries/offhands/crusadershields/salvation.png',
		unique='Blocked attacks heal you and your allies for <span>20 - 30%</span> of the amount blocked.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='21.0 - 31.0%')
	salvation.save()
	salvation.affixes.add(stre, blockChance)

	sublimeConviction = CrusaderShield(name='Sublime Conviction',
		pic='/assets/media/items/legendaries/offhands/crusadershields/sublime_conviction.png',
		unique='When you block, you have up to a <span>15 - 20%</span> chance to Stun the attacker for <span class="silver">1.5</span> seconds based on your current Wrath.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='21.0 - 31.0%')
	sublimeConviction.save()
	sublimeConviction.affixes.add(stre, blockChance)

	theFinalWitness = CrusaderShield(name='The Final Witness',
		pic='/assets/media/items/legendaries/offhands/crusadershields/the_final_witness.png',
		unique='Shield Glare now hits all enemies around you.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	theFinalWitness.save()
	theFinalWitness.affixes.add(stre)

	unrelentingPhalanx = CrusaderShield(name='Unrelenting Phalanx',
		pic='/assets/media/items/legendaries/offhands/crusadershields/unrelenting_phalanx.png',
		unique='Phalanx now casts twice.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	unrelentingPhalanx.save()
	unrelentingPhalanx.affixes.add(stre)


	for crusaderShield in CrusaderShield.objects.all():
		crusaderShield.slug = slugify(crusaderShield.name)
		crusaderShield.category = 'CrusaderShield'
		crusaderShield.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0006_mojos'),
    ]

    operations = [
    	migrations.RunPython(load_crusader_shields)
    ]
