# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_chest_armor_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "ChestArmorAffix")


	mainStat = Affix(affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	allRes = Affix(affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	durability = Affix(affix='durability',
		is_primary=False,
		desc='Item ignores Durability Loss')
	durability.save()

#CinderCoat
	cindercoatFireDmg = Affix(affix='cindercoatFireDmg',
		is_primary=True,
		desc='Fire skills do <span>15 - 20%</span> more damage')
	cindercoatFireDmg.save()

#Goldskin
	goldskinExtraGold = Affix(affix='goldskinExtraGold',
		is_primary=False,
		desc='<span>+100%</span> Extra Gold from Monsters')
	goldskinExtraGold.save()

#Tyrael's Might
	tyraelsDemonDmg = Affix(affix='tyraelsDemonDmg',
		is_primary=False,
		desc='Increases damage against Demons by <span>10 - 20%</span>')
	tyraelsDemonDmg.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0013_shoulders_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_chest_armor_affixes)
    ]
