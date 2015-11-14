# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_quiver_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "QuiverAffix")

	dext = Affix(id=0,
		affix='dext',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000</span> Dexterity')
	dext.save()

	vita = Affix(id=1,
		affix='vita',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000</span> Vitality')
	vita.save()

	life = Affix(id=2,
		affix='life',
		is_primary=True,
		desc='<span>+10 - 15%</span> Life')
	life.save()

	lps = Affix(id=3,
		affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	ias = Affix(id=4,
		affix='ias',
		is_primary=True,
		desc='<span>+15.0 - 20.0%</span> Attack Speed')
	ias.save()

	chc = Affix(id=5,
		affix='chc',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	areaDmg = Affix(id=6,
		affix='areaDmg',
		is_primary=True,
		desc='<span>+10 - 20%</span> Area Damage')
	areaDmg.save()

	eliteDmg = Affix(id=7,
		affix='eliteDmg',
		is_primary=True,
		desc='Increases damage against elites by <span>5.0 - 8.0%</span>')
	eliteDmg.save()

	bleedChance = Affix(id=8,
		affix='bleedChance',
		is_primary=True,
		desc='<span>34.0 - 39.0%</span> chance to inflict Bleed for <span>400%</span> weapon damage over <span class="silver">5</span> seconds')
	bleedChance.save()

	cdr = Affix(id=9,
		affix='cdr',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	rcr = Affix(id=10,
		affix='rcr',
		is_primary=True,
		desc='<span>+5 - 8%<span> Resource Cost Reduction')
	rcr.save()

	sockets = Affix(id=11,
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	hatredRegen = Affix(id=12,
		affix='hatredRegen',
		is_primary=True,
		desc='<span>+1.35 - 1.50</span> Hatred Regeneration per Second')
	hatredRegen.save()

	bolas = Affix(id=13,
		affix='bolas',
		is_primary=True,
		desc='Increase Bola damage by <span>10 - 15%</span>')
	bolas.save()

	chakram = Affix(id=14,
		affix='chakram',
		is_primary=True,
		desc='Increase Chakram damage by <span>10 - 15%</span>')
	chakram.save()

	clusterArrow = Affix(id=15,
		affix='clusterArrow',
		is_primary=True,
		desc='Increase Cluster Arrow damage by <span>10 - 15%</span>')
	clusterArrow.save()

	companion = Affix(id=16,
		affix='companion',
		is_primary=True,
		desc='Increase Companion damage by <span>10 - 15%</span>')
	companion.save()

	elementalArrow = Affix(id=17,
		affix='elementalArrow',
		is_primary=True,
		desc='Increase Elemental Arrow damage by <span>10 - 15%</span>')
	elementalArrow.save()

	entanglingShot = Affix(id=18,
		affix='entanglingShot',
		is_primary=True,
		desc='Increase Entangling Shot damage by <span>10 - 15%</span>')
	entanglingShot.save()

	evasiveFire = Affix(id=19,
		affix='evasiveFire',
		is_primary=True,
		desc='Increase Evasive Fire damage by <span>10 - 15%</span>')
	evasiveFire.save()

	fanOfKnives = Affix(id=20,
		affix='fanOfKnives',
		is_primary=True,
		desc='Increase Fan of Knives damage by <span>10 - 15%</span>')
	fanOfKnives.save()

	grenade = Affix(id=21,
		affix='grenade',
		is_primary=True,
		desc='Increase Grenade damage by <span>10 - 15%</span>')
	grenade.save()

	hungeringArrow = Affix(id=22,
		affix='hungeringArrow',
		is_primary=True,
		desc='Increase Hungering Arrow damage by <span>10 - 15%</span>')
	hungeringArrow.save()

	impale = Affix(id=23,
		affix='impale',
		is_primary=True,
		desc='Increase Impale damage by <span>10 - 15%</span>')
	impale.save()

	multishot = Affix(id=24,
		affix='multishot',
		is_primary=True,
		desc='Increase Multishot damage by <span>10 - 15%</span>')
	multishot.save()

	rainOfVengeance = Affix(id=25,
		affix='rainOfVengeance',
		is_primary=True,
		desc='Increase Rain of Vengeance damage by <span>10 - 15%</span>')
	rainOfVengeance.save()

	rapidFire = Affix(id=26,
		affix='rapidFire',
		is_primary=True,
		desc='Increase Rapid Fire damage by <span>10 - 15%</span>')
	rapidFire.save()

	sentry = Affix(id=27,
		affix='sentry',
		is_primary=True,
		desc='Increase Sentry damage by <span>10 - 15%</span>')
	sentry.save()

	spikeTrap = Affix(id=28,
		affix='spikeTrap',
		is_primary=True,
		desc='Increase Spike Trap damage by <span>10 - 15%</span>')
	spikeTrap.save()

	strafe = Affix(id=29,
		affix='strafe',
		is_primary=True,
		desc='Increase Strafe damage by <span>10 - 15%</span>')
	strafe.save()


	maxDisc = Affix(id=30,
		affix='maxDisc',
		is_primary=False,
		desc='<span>+9 - 12</span> Max Discipline')
	maxDisc.save()

	fearChance = Affix(id=31,
		affix='fearChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Fear on Hit')
	fearChance.save()

	stunChance = Affix(id=32,
		affix='stunChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Stun on Hit')
	stunChance.save()

	blindChance = Affix(id=33,
		affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Blind on Hit')
	blindChance.save()

	freezeChance = Affix(id=34,
		affix='freezeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Freeze on Hit')
	freezeChance.save()

	chillChance = Affix(id=35,
		affix='chillChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Chill on Hit')
	chillChance.save()

	slowChance = Affix(id=36,
		affix='slowChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Slow on Hit')
	slowChance.save()

	immobilizeChance = Affix(id=37,
		affix='immobilizeChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Immobilize on Hit')
	immobilizeChance.save()

	knockbackChance = Affix(id=38,
		affix='knockbackChance',
		is_primary=False,
		desc='<span>+1.0 - 2.6%</span> chance to Knockback on Hit')
	knockbackChance.save()

	thorns = Affix(id=39,
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,200 - 2,600</span> damage')
	thorns.save()

	itemHealing = Affix(id=40,
		affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29,713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	killExp = Affix(id=41,
		affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

	extraGold = Affix(id=42,
		affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	durability = Affix(id=43,
		affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

	lvlReq = Affix(id=44,
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


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0004_source_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_quiver_affixes)
    ]
