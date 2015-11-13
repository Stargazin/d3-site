# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_amulet_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "AmuletAffix")

	dmg = Affix(id=0,
		affix='Dmg',
		is_primary=True,
		desc='<span>+60 - 80</span>-<span>120 - 160</span> Damage',
		ancient='<span>+88 - 105</span>-<span>168 - 210</span> Damage')
	dmg.save()

	eleDmg = Affix(id=1,
		affix='Element Dmg',
		is_primary=True,
		desc='Skills of {<span>One Element</span>} do <span>15 - 20%</span> more damage')
	eleDmg.save()

	physDmg = Affix(id=2,
		affix='Physical Dmg',
		is_primary=True,
		desc='Physical skills do <span>15 - 20%</span> more damage')
	physDmg.save()

	coldDmg = Affix(id=3,
		affix='Cold Dmg',
		is_primary=True,
		desc='Cold skills do <span>15 - 20%</span> more damage')
	coldDmg.save()

	fireDmg = Affix(id=4,
		affix='Fire Dmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	fireDmg.save()

	lightDmg = Affix(id=5,
		affix='Lightning Dmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	lightDmg.save()

	poisDmg = Affix(id=6,
		affix='Poison Dmg',
		is_primary=True,
		desc='Poison skills do <span>15 - 20%</span> more damage')
	poisDmg.save()

	arcaneDmg = Affix(id=7,
		affix='Arcane Dmg',
		is_primary=True,
		desc='Arcane skills do <span>15 - 20%</span> more damage')
	arcaneDmg.save()

	holyDmg = Affix(id=8,
		affix='Holy Dmg',
		is_primary=True,
		desc='Holy skills do <span>15 - 20%</span> more damage')
	holyDmg.save()

	mainStat = Affix(id=9,
		affix='Main Stat',
		is_primary=True,
		desc='<span>+626 - 750</span> {<span>Main Stat</span>}',
		ancient='<span>+825 - 1,000</span> {<span>Main Stat</span>}')
	mainStat.save()

	dext = Affix(id=10,
		affix='Dex',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000 Dexterity')
	dext.save()

	inte = Affix(id=11,
		affix='Int',
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000 Intelligence')
	inte.save()

	stre = Affix(id=12,
		affix='Str',
		is_primary=True,
		desc='<span>+626 - 750</span> Strength',
		ancient='<span>+825 - 1,000 Strength')
	stre.save()

	vita = Affix(id=13,
		affix='Vit',
		is_primary=True,
		desc='<span>+626 - 750</span> Vitality',
		ancient='<span>+825 - 1,000 Vitality')
	vita.save()

	life = Affix(id=14,
		affix='Life',
		is_primary=True,
		desc='<span>+14 - 18%</span> Life')
	life.save()

	armor = Affix(id=15,
		affix='Armor',
		is_primary=True,
		desc='<span>+559 - 595</span> Armor',
		ancient='<span>+654 - 775</span> Armor')
	armor.save()

	allRes = Affix(id=16,
		affix='All Res',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	lps = Affix(id=17,
		affix='LPS',
		is_primary=True,
		desc='<span>+6,448 - 7,678</span> Life Regeneration per Second',
		ancient='<span>+8,845 - 10,000</span> Life Regeneration per Second')
	lps.save()

	lph = Affix(id=18,
		affix='LPH',
		is_primary=True,
		desc='<span>+15,474 - 18,429</span> Life per Hit',
		ancient='<span>+20,271 - 23,950</span> Life per Hit')
	lph.save()

	ias = Affix(id=19,
		affix='AS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed')
	ias.save()

	chc = Affix(id=20,
		affix='CHC',
		is_primary=True,
		desc='<span>+8.0 - 10.0%</span> Critical Hit Chance')
	chc.save()

	chd = Affix(id=21,
		affix='CHD',
		is_primary=True,
		desc='<span>+51.0 - 100.0%</span> Critical Hit Damage')
	chd.save()

	cdr = Affix(id=22,
		affix='CDR',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	rcr = Affix(id=23,
		affix='RCR',
		is_primary=True,
		desc='<span>+5 - 8%<span> Resource Cost Reduction')
	rcr.save()

	sockets = Affix(id=24,
		affix='Sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()



	eleRes = Affix(id=25,
		affix='Element Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Resistance to {<span>One Element</span>}',
		ancient='<span>+176 - 210</span> Resistance to {<span>One Element</span>}')
	eleRes.save()

	physRes = Affix(id=26,
		affix='Physical Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Physical Resistance',
		ancient='<span>+176 - 210</span> Physical Resistance')
	physRes.save()

	coldRes = Affix(id=27,
		affix='Cold Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Cold Resistance',
		ancient='<span>+176 - 210</span> Cold Resistance')
	coldRes.save()

	fireRes = Affix(id=28,
		affix='Fire Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Fire Resistance',
		ancient='<span>+176 - 210</span> Fire Resistance')
	fireRes.save()

	lightRes = Affix(id=29,
		affix='Lightning Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Lightning Resistance',
		ancient='<span>+176 - 210</span> Lightning Resistance')
	lightRes.save()

	poisRes = Affix(id=30,
		affix='Poison Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Poison Resistance',
		ancient='<span>+176 - 210</span> Poison Resistance')
	poisRes.save()

	arcaneRes = Affix(id=31,
		affix='Arcane Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Arcane Resistance',
		ancient='<span>+176 - 210</span> Arcane Resistance')
	arcaneRes.save()

	reducedRange = Affix(id=32,
		affix='Reduced Ranged Dmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Ranged Damage Reduction')
	reducedRange.save()

	reducedMelee = Affix(id=33,
		affix='Reduced Melee Dmg',
		is_primary=False,
		desc='<span>+6.0 - 7.0%</span> Melee Damage Reduction')
	reducedMelee.save()

	ccReduction = Affix(id=34,
		affix='CC Reduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	thorns = Affix(id=35,
		affix='Thorns',
		is_primary=False,
		desc='Attackers take <span>2,667 - 3,498</span> damage',
		ancient='Attackers take <span>3,847 - 4,550</span> damage')
	thorns.save()

	blindChance = Affix(id=36,
		affix='blindChance',
		is_primary=False,
		desc='<span>+1.0 - 5.1%</span> chance to Blind on Hit')
	blindChance.save()

	itemHealing = Affix(id=37,
		affix='Item Healing',
		is_primary=False,
		desc='<span>+20,001 - 29.713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	lpk = Affix(id=38,
		affix='LPK',
		is_primary=False,
		desc='<span>+6,428 - 8,914</span> Life per Kill',
		ancient='<span>+9,805 - 11,590</span> Life per Kill')
	lpk.save()

	exp = Affix(id=39,
		affix='Kill EXP',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	exp.save()

	extraGold = Affix(id=40,
		affix='Extra Gold',
		is_primary=False,
		desc='<span>+71 - 80%</span> Extra Gold from Monsters')
	extraGold.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()
		else:
			pass


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(load_amulet_affixes),
    ]