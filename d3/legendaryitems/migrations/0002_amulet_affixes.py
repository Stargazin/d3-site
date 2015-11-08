# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_amulet_affixes(apps, schema_editor):
	Affix = apps.get_model("legendaryitems", "AmuletAffix")

	damage = Affix(id=0,
		affix='Damage',
		is_primary=True,
		desc='<span>+[60 - 80]</span>-<span>[120 - 160]</span> Damage',
		ancient='<span>+[88 - 105]</span>-<span>[168 - 210]</span> Damage')
	damage.save()

	element_damage = Affix(id=1,
		affix='ele dmg',
		is_primary=True,
		desc='Skills of <span>[<em>One Element</em>]</span> do <span>[15 - 20]%</span> more damage',
		ancient='Skills of <span>[<em>One Element</em>]</span> do <span>[15 - 20]%</span> more damage')
	element_damage.save()

	physical_damage = Affix(id=2,
		affix='phys dmg',
		is_primary=True,
		desc='Physical skills do <span>[15 - 20]%</span> more damage',
		ancient='Physical skills do <span>[15 - 20]%</span> more damage')
	physical_damage.save()

	cold_damage = Affix(id=3,
		affix='cold dmg',
		is_primary=True,
		desc='Cold skills do <span>[15 - 20]%</span> more damage',
		ancient='Cold skills do <span>[15 - 20]%</span> more damage')
	cold_damage.save()

	fire_damage = Affix(id=4,
		affix='fire dmg',
		is_primary=True,
		desc='Fire skills do <span>[15 - 20]%</span> more damage',
		ancient='Fire skills do <span>[15 - 20]%</span> more damage')
	fire_damage.save()

	lightning_damage = Affix(id=5,
		affix='lightning dmg',
		is_primary=True,
		desc='Lightning skills do <span>[15 - 20]%</span> more damage',
		ancient='Lightning skills do <span>[15 - 20]%</span> more damage')
	lightning_damage.save()

	poison_damage = Affix(id=6,
		affix='posion dmg',
		is_primary=True,
		desc='Poison skills do <span>[15 - 20]%</span> more damage',
		ancient='Poison skills do <span>[15 - 20]%</span> more damage')
	poison_damage.save()

	arcane_damage = Affix(id=7,
		affix='arcane damage',
		is_primary=True,
		desc='Arcane skills do <span>[15 - 20]%</span> more damage',
		ancient='Arcane skills do <span>[15 - 20]%</span> more damage')
	arcane_damage.save()

	holy_damage = Affix(id=8,
		affix='holy damage',
		is_primary=True,
		desc='Holy skills do <span>[15 - 20]%</span> more damage',
		ancient='Holy skills do <span>[15 - 20]%</span> more damage')
	holy_damage.save()

	main_stat = Affix(id=9,
		affix='main stat',
		is_primary=True,
		desc='<span>+[626 - 750] <em>Main Stat</em></span>',
		ancient='<span>+[825 - 1,000] <em>Main Stat</em></span>')
	main_stat.save()

	dexterity = Affix(id=10,
		affix='dex',
		is_primary=True,
		desc='<span>+[626 - 750]</span> Dexterity',
		ancient='<span>+[825 - 1,000] Dexterity')
	dexterity.save()

	intelligence = Affix(id=11,
		affix='int',
		is_primary=True,
		desc='<span>+[626 - 750]</span> Intelligence',
		ancient='<span>+[825 - 1,000] Intelligence')
	intelligence.save()

	strength = Affix(id=12,
		affix='str',
		is_primary=True,
		desc='<span>+[626 - 750]</span> Strength',
		ancient='<span>+[825 - 1,000] Strength')
	strength.save()

	vitality = Affix(id=13,
		affix='vit',
		is_primary=True,
		desc='<span>+[626 - 750]</span> Vitality',
		ancient='<span>+[825 - 1,000] Vitality')
	vitality.save()

	life = Affix(id=14,
		affix='life',
		is_primary=True,
		desc='<span>+[14 - 18]%</span> Life',
		ancient='<span>+[14 - 18]%</span> Life')
	life.save()

	armor = Affix(id=15,
		affix='armor',
		is_primary=True,
		desc='<span>+[559 - 595]</span> Armor',
		ancient='<span>+[654 - 775]</span> Armor')
	armor.save()

	all_resist = Affix(id=16,
		affix='all res',
		is_primary=True,
		desc='<span>+[91 - 100]</span> Resistance to All Elements',
		ancient='<span>+[110 - 130]</span> Resistance to All Elements')
	all_resist.save()

	life_per_second = Affix(id=17,
		affix='lps',
		is_primary=True,
		desc='<span>+[6448 - 7678]</span> Life Regeneration per Second',
		ancient='<span>+[8,845 - 10,000]</span> Life Regeneration per Second')
	life_per_second.save()

	life_per_hit = Affix(id=18,
		affix='lph',
		is_primary=True,
		desc='<span>+[15,474 - 18,429]</span> Life per Hit',
		ancient='<span>+[20,271 - 23,950]</span> Life per Hit')
	life_per_hit.save()

	attack_speed = Affix(id=19,
		affix='ias',
		is_primary=True,
		desc='<span>+[5.0 - 7.0]%</span> Attack Speed',
		ancient='<span>+[5.0 - 7.0]%</span> Attack Speed')
	attack_speed.save()

	critical_hit_chance = Affix(id=20,
		affix='chc',
		is_primary=True,
		desc='<span>+[8.0 - 10.0]%</span> Critical Hit Chance',
		ancient='<span>+[8.0 - 10.0]%</span> Critical Hit Chance')
	critical_hit_chance.save()

	critical_hit_damage = Affix(id=21,
		affix='chd',
		is_primary=True,
		desc='<span>+[51.0 - 100.0]%</span> Critical Hit Damage',
		ancient='<span>+[51.0 - 100.0]%</span> Critical Hit Damage')
	critical_hit_damage.save()

	cooldown_reduction = Affix(id=22,
		affix='cdr',
		is_primary=True,
		desc='<span>+[5.0 - 8.0]%</span> Cooldown Reduction',
		ancient='<span>+[5.0 - 8.0]%</span> Cooldown Reduction')
	cooldown_reduction.save()

	resource_cost_reduction = Affix(id=23,
		affix='rcr',
		is_primary=True,
		desc='<span>+[5 - 8]%<span> Resource Cost Reduction',
		ancient='<span>+[5 - 8]%</span> Resource Cost Reduction')
	resource_cost_reduction.save()

	sockets = Affix(id=24,
		affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)',
		ancient='Sockets (<span>1</span>')
	sockets.save()



	element_res = Affix(id=25,
		affix='ele res',
		is_primary=False,
		desc='<span>+[141 - 160]</span> Resistance to <span>[<em>One Element</em>]</span>',
		ancient='<span>+[176 - 210]</span> Resistance to <span>[<em>One Element</em>]</span>')
	element_res.save()

	physical_res = Affix(id=26,
		affix='phys res',
		is_primary=False,
		desc='<span>+[141 - 160]</span> Physical Resistance',
		ancient='<span>+[176 - 210]</span> Physical Resistance')
	physical_res.save()

	cold_res = Affix(id=27,
		affix='cold res',
		is_primary=False,
		desc='<span>+[141 - 160]</span> Cold Resistance',
		ancient='<span>+[176 - 210]</span> Cold Resistance')
	cold_res.save()

	fire_res = Affix(id=28,
		affix='fire res',
		is_primary=False,
		desc='<span>+[141 - 160]</span> Fire Resistance',
		ancient='<span>+[176 - 210]</span> Fire Resistance')
	fire_res.save()

	lightning_res = Affix(id=29,
		affix='lightning res',
		is_primary=False,
		desc='<span>+[141 - 160]</span> Lightning Resistance',
		ancient='<span>+[176 - 210]</span> Lightning Resistance')
	lightning_res.save()

	poison_res = Affix(id=30,
		affix='poison res',
		is_primary=False,
		desc='<span>+[141 - 160]</span> Poison Resistance',
		ancient='<span>+[176 - 210]</span> Poison Resistance')
	poison_res.save()

	arcane_res = Affix(id=31,
		affix='arcane res',
		is_primary=False,
		desc='<span>+[141 - 160]</span> Arcane Resistance',
		ancient='<span>+[176 - 210]</span> Arcane Resistance')
	arcane_res.save()

	reduced_ranged_damage = Affix(id=32,
		affix='reduced range',
		is_primary=False,
		desc='<span>+[6.0 - 7.0]%</span> Ranged Damage Reduction',
		ancient='<span>+[6.0 - 7.0]%</span> Ranged Damage Reduction')
	reduced_ranged_damage.save()

	reduced_melee_damage = Affix(id=33,
		affix='reduced melee',
		is_primary=False,
		desc='<span>+[6.0 - 7.0]%</span> Melee Damage Reduction',
		ancient='<span>+[6.0 - 7.0]%</span> Melee Damage Reduction')
	reduced_melee_damage.save()

	life_per_kill = Affix(id=34,
		affix='lpk',
		is_primary=False,
		desc='<span>+[6,428 - 8,914] Life per Kill',
		ancient='<span>+[9,805 - 11,590] Life per Kill')
	life_per_kill.save()

	gold_drop = Affix(id=35,
		affix='gold drop',
		is_primary=False,
		desc='<span>+[71 - 80]%</span> Extra Gold from Monsters',
		ancient='<span>+[71 - 80]%</span> Extra Gold from Monsters')
	gold_drop.save()

	thorns = Affix(id=36,
		affix='thorns',
		is_primary=False,
		desc='Attackers take <span>[2,667 - 3,498]</span> damage',
		ancient='Attackers take <span>[3,847 - 4,550]</span> damage')
	thorns.save()

	exp_per_kill = Affix(id=37,
		affix='kill exp',
		is_primary=False,
		desc='<span>+[140 - 200]</span> Experience per Kill',
		ancient='<span>+[220 - 260]</span> Experience per Kill')
	exp_per_kill.save()

	crowd_control_reduction = Affix(id=38,
		affix='cc reduction',
		is_primary=False,
		desc='<span>+[20 - 40]%</span> Crowd Control Duration Reduction',
		ancient='<span>+[20 - 40]%</span> Crowd Control Duration Reduction')
	crowd_control_reduction.save()

	blind_chance = Affix(id=39,
		affix='blind',
		is_primary=False,
		desc='<span>+[1.0 - 5.1]%</span> Chance to Blind',
		ancient='<span>+[1.0 - 5.1]%</span> Chance to Blind')
	blind_chance.save()

	item_healing = Affix(id=40,
		affix='item healing',
		is_primary=False,
		desc='<span>+[20,001 - 29.713]</span> Healing from Health Globes and Potions',
		ancient='<span>+[32,684 - 38,625]</span> Healing from Health Globes and Potions')
	item_healing.save()



class Migration(migrations.Migration):

    dependencies = [
        ('legendaryitems', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(load_amulet_affixes),
    ]