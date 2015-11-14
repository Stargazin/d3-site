# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_quivers(apps, schema_editor):
	Quiver = apps.get_model("legendaries", "Quiver")
	Affix = apps.get_model("affixes", "QuiverAffix")

	sockets = Affix.objects.get(affix='sockets')

	dext = Affix.objects.get(affix='dext')
	vita = Affix.objects.get(affix='vita')

	life = Affix.objects.get(affix='life')
	lps = Affix.objects.get(affix='lps')

	ias = Affix.objects.get(affix='ias')
	chc = Affix.objects.get(affix='chc')
	cdr = Affix.objects.get(affix='cdr')
	eliteDmg = Affix.objects.get(affix='eliteDmg')
	areaDmg = Affix.objects.get(affix='areaDmg')
	bleedChance = Affix.objects.get(affix='bleedChance')

	rcr = Affix.objects.get(affix='rcr')
	hatredRegen = Affix.objects.get(affix='hatredRegen')

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


	maxDisc = Affix.objects.get(affix='maxDisc')

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


	for quiver in Quiver.objects.all():
		quiver.slug = slugify(Quiver.name)
		quiver.category = 'Quiver'
		quiver.save()

class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0004_sources'),
    ]

    operations = [
    	migrations.RunPython(load_quivers)
    ]
