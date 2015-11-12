# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_ring_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "RingAffix")

	dmg = Affix(id=0,
		affix='Dmg',
		is_primary=True,
		desc='<span>+60 - 80</span>-<span>120 - 160</span> Damage',
		ancient='<span>+88 - 105</span>-<span>168 - 210</span> Damage')
	dmg.save()

	main_stat = Affix(id=1,
		affix='Main Stat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span>Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span>Main Stat</span>}')
	main_stat.save()

	dexterity = Affix(id=2,
		affix='Dex',
		is_primary=True,
		desc='<span>+416 - 500</span> Dexterity',
		ancient='<span>+550 - 650</span> Dexterity')
	dexterity.save()

	intelligence = Affix(id=3,
		affix='Int',
		is_primary=True,
		desc='<span>+416 - 500</span> Intelligence',
		ancient='<span>+550 - 650</span> Intelligence')
	intelligence.save()

	strength = Affix(id=4,
		affix='Str',
		is_primary=True,
		desc='<span>+416 - 500</span> Strength',
		ancient='<span>+550 - 650</span> Strength')
	strength.save()

	vitality = Affix(id=5,
		affix='Vit',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vitality.save()

	life = Affix(id=6,
		affix='Life',
		is_primary=True,
		desc='<span>+10 - 15%</span> Life',
		ancient='<span>+10 - 15%</span> Life')
	life.save()

	armor = Affix(id=7,
		affix='Armor',
		is_primary=True,
		desc='<span>+373 - 397</span> Armor',
		ancient='<span>+436 - 516</span> Armor')
	armor.save()

	all_res = Affix(id=8,
		affix='All Res',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	all_res.save()

	life_per_second = Affix(id=9,
		affix='LPS',
		is_primary=True,
		desc='<span>+6,448 - 7,678</span> Life Regeneration per Second',
		ancient='<span>+8,845 - 10,000</span> Life Regeneration per Second')
	life_per_second.save()

	life_per_hit = Affix(id=10,
		affix='LPH',
		is_primary=True,
		desc='<span>+7,737 - 9,214</span> Life per Hit',
		ancient='<span>+10,135 - 11,975</span> Life per Hit')
	life_per_hit.save()


	attack_speed = Affix(id=11,
		affix='AS',
		is_primary=True,
		desc='<span>+5.0 - 7.0%</span> Attack Speed',
		ancient='<span>+5.0 - 7.0%</span> Attack Speed')
	attack_speed.save()

	chc = Affix(id=12,
		affix='CHC',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance',
		ancient='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()

	chd = Affix(id=13,
		affix='CHD',
		is_primary=True,
		desc='<span>+26.0 - 50.0%</span> Critical Hit Damage',
		ancient='<span>+26.0 - 50.0%</span> Critical Hit Damage')
	chd.save()

	areadmg = Affix(id=14,
		affix='Area Damage',
		is_primary=True,
		desc='<span>+10 - 20%</span> Area Damage',
		ancient='<span>+10 - 20%</span> Area Damage')
	areadmg.save()

	cdr = Affix(id=15,
		affix='CDR',
		is_primary=True,
		desc='<span>+5.0 - 8.0%</span> Cooldown Reduction',
		ancient='<span>+5.0 - 8.0%</span> Cooldown Reduction')
	cdr.save()

	rcr = Affix(id=16,
		affix='RCR',
		is_primary=True,
		desc='<span>+5 - 8%<span> Resource Cost Reduction',
		ancient='<span>+5 - 8%</span> Resource Cost Reduction')
	rcr.save()

	sockets = Affix(id=17,
		affix='Sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)',
		ancient='Sockets (<span>1</span>')
	sockets.save()



	element_res = Affix(id=18,
		affix='Element Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Resistance to {<span>One Element</span>}',
		ancient='<span>+176 - 210</span> Resistance to {<span>One Element</span>}')
	element_res.save()

	physical_res = Affix(id=19,
		affix='Physical Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Physical Resistance',
		ancient='<span>+176 - 210</span> Physical Resistance')
	physical_res.save()

	cold_res = Affix(id=20,
		affix='Cold Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Cold Resistance',
		ancient='<span>+176 - 210</span> Cold Resistance')
	cold_res.save()

	fire_res = Affix(id=21,
		affix='Fire Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Fire Resistance',
		ancient='<span>+176 - 210</span> Fire Resistance')
	fire_res.save()

	lightning_res = Affix(id=22,
		affix='Lightning Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Lightning Resistance',
		ancient='<span>+176 - 210</span> Lightning Resistance')
	lightning_res.save()

	poison_res = Affix(id=23,
		affix='Poison Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Poison Resistance',
		ancient='<span>+176 - 210</span> Poison Resistance')
	poison_res.save()

	arcane_res = Affix(id=24,
		affix='Arcane Res',
		is_primary=False,
		desc='<span>+141 - 160</span> Arcane Resistance',
		ancient='<span>+176 - 210</span> Arcane Resistance')
	arcane_res.save()

	cc_reduction = Affix(id=25,
		affix='CC Reduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction',
		ancient='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	cc_reduction.save()

	thorns = Affix(id=26,
		affix='Thorns',
		is_primary=False,
		desc='Attackers take <span>1,525 - 2,000</span> damage',
		ancient='Attackers take <span>2,220 - 2,600</span> damage')
	thorns.save()

	item_healing = Affix(id=27,
		affix='Item Healing',
		is_primary=False,
		desc='<span>+20,001 - 29.713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	item_healing.save()

	life_per_kill = Affix(id=28,
		affix='LPK',
		is_primary=False,
		desc='<span>+6,428 - 8,914</span> Life per Kill',
		ancient='<span>+9,805 - 11,590</span> Life per Kill')
	life_per_kill.save()

	exp_per_kill = Affix(id=29,
		affix='Kill EXP',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	exp_per_kill.save()

	extra_gold = Affix(id=30,
		affix='Extra Gold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters',
		ancient='<span>+32 - 35%</span> Extra Gold from Monsters')
	extra_gold.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0002_amulet_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_ring_affixes)
    ]
