# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


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





	for crusaderShield in CrusaderShield.objects.all():
		crusaderShield.slug = slugify(CrusaderShield.name)
		crusaderShield.category = 'CrusaderShield'
		crusaderShield.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0006_mojos'),
    ]

    operations = [
    	migrations.RunPython(load_crusader_shields)
    ]
