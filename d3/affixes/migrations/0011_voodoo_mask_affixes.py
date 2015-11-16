# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_voodoo_mask_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "VoodooMaskAffix")


	inte = Affix(affix='inte', 
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	chc = Affix(affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()

	sockets = Affix(affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	maxMana = Affix(affix='maxMana',
		is_primary=False,
		desc='<span>+120 - 150</span> Max Mana')
	maxMana.save()

	killExp = Affix(affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0010_spirit_stone_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_voodoo_mask_affixes)
    ]
