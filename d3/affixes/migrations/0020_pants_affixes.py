# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_pants_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "PantsAffix")


	mainStat = Affix(affix='mainStat',
		is_primary=True,
		desc='<span>+416 - 500</span> {<span class="vary">Main Stat</span>}',
		ancient='<span>+550 - 650</span> {<span class="vary">Main Stat</span>}',
		notes='Dexterity<br>Intelligence<br>Strength')
	mainStat.save()

	lps = Affix(affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	allRes = Affix(affix='allRes',
		is_primary=True,
		desc='<span>+91 - 100</span> Resistance to All Elements',
		ancient='<span>+110 - 130</span> Resistance to All Elements')
	allRes.save()

	extraGold = Affix(affix='extraGold',
		is_primary=False,
		desc='<span>+32 - 35%</span> Extra Gold from Monsters')
	extraGold.save()


	hammerMovementSpeed = Affix(affix='hammerMovementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	hammerMovementSpeed.save()

	swampPoisDmg = Affix(affix='swampPoisDmg',
		is_primary=True,
		desc='Poison skills do <span>15 - 20%</span> more damage')
	swampPoisDmg.save()

	swampCCReduction = Affix(affix='swampCCReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	swampCCReduction.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0019_mighty_belt_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_pants_affixes)
    ]
