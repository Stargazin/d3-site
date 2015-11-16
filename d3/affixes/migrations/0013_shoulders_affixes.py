# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_shoulders_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "ShouldersAffix")


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

	armor = Affix(affix='armor',
		is_primary=True,
		desc='<span>+373 - 397</span> Armor',
		ancient='<span>+436 - 516</span> Armor')
	armor.save()

	itemHealing = Affix(affix='itemHealing',
		is_primary=False,
		desc='<span>+20,001 - 29,713</span> Healing from Health Globes and Potions',
		ancient='<span>+32,684 - 38,625</span> Healing from Health Globes and Potions')
	itemHealing.save()

	extraGold = Affix(affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()

	profaneItemPickup = Affix(affix='profaneItemPickup',
		is_primary=False,
		desc='<span>+4 - 6</span> Yards to Gold and Globe Pickup')
	profaneItemPickup.save()




	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0012_wizard_hat_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_shoulders_affixes)
    ]
