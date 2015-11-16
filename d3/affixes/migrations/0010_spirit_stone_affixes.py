# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_spirit_stone_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "SpiritStoneAffix")


	dext = Affix(affix='dext',
		is_primary=True,
		desc='<span>+626 - 750</span> Dexterity',
		ancient='<span>+825 - 1,000</span> Dexterity')
	dext.save()

	chc = Affix(affix='chc',
		is_primary=True,
		desc='<span>+4.5 - 6.0%</span> Critical Hit Chance')
	chc.save()

	sockets = Affix(affix='sockets',
		is_primary=True,
		desc='Sockets (<span>1</span>)')
	sockets.save()

	skillDmg = Affix(affix='skillDmg',
		is_primary=True,
		desc='Increases {<span class="vary">Skill Damage</span>} by <span>10 - 15%</span>',
		notes='Tempest Rush<br>Exploding Palm<br>Wave of Light<br>Lashing Tail Kick')
	skillDmg.save()


	ccReduction = Affix(affix='ccReduction',
		is_primary=False,
		desc='<span>+20 - 40%</span> Crowd Control Duration Reduction')
	ccReduction.save()

	killExp = Affix(affix='killExp',
		is_primary=False,
		desc='<span>+140 - 200</span> Experience per Kill',
		ancient='<span>+220 - 260</span> Experience per Kill')
	killExp.save()

#The Eye of the Storm
	eyeLightDmg = Affix(affix='eyeLightDmg',
		is_primary=True,
		desc='Lightning skills do <span>15 - 30%</span> more damage')
	eyeLightDmg.save()

#Tzo Krin's Gaze
	tzoWaveOfLight = Affix(affix='tzoWaveOfLight',
		is_primary=True,
		desc='Increase Wave of Light damage by <span>20 - 25%</span>')
	tzoWaveOfLight.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

	dependencies = [
		('affixes', '0009_helmet_affixes'),
	]

	operations = [
		migrations.RunPython(load_spirit_stone_affixes)
	]
