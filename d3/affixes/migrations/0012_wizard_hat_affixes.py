# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def load_wizard_hat_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "WizardHatAffix")


	inte = Affix(affix='inte', 
		is_primary=True,
		desc='<span>+626 - 750</span> Intelligence',
		ancient='<span>+825 - 1,000</span> Intelligence')
	inte.save()

	apCrit = Affix(affix='apCrit',
		is_primary=True,
		desc='<span>+3 - 4</span> Arcane Power on Critical Hits')
	apCrit.save()

	sockets = Affix(affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()


	maxAP = Affix(affix='maxAP',
		is_primary=False,
		desc='<span>+10 - 14</span> Max Arcane Power')
	maxAP.save()


#Storm Crow
	stormLightDmg = Affix(affix='stormLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 20%</span> more damage')
	stormLightDmg.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0011_voodoo_mask_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_wizard_hat_affixes)
    ]
