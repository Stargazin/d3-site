# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_cloak_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "CloakAffix")


	dext = Affix(affix='dext',
		is_primary=True,
		desc='<span>+416 - 500</span> Dexterity',
		ancient='<span>+550 - 650</span> Dexterity')
	dext.save()

	vita = Affix(affix='vita',
		is_primary=True,
		desc='<span>+416 - 500</span> Vitality',
		ancient='<span>+550 - 650</span> Vitality')
	vita.save()

	armor = Affix(affix='armor',
		is_primary=True,
		desc='<span>+373 - 595</span> Armor',
		ancient='<span>+436 - 775</span> Armor')
	armor.save()

	sockets = Affix(affix='sockets',
		is_primary=True,
		desc='Sockets (<span>3</span>)')
	sockets.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0014_chest_armor_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_cloak_affixes)
    ]
