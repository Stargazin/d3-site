# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_boots_affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "BootsAffix")


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

	armor = Affix(affix='armor',
		is_primary=True,
		desc='<span>+373 - 397</span> Armor',
		ancient='<span>+436 - 516</span> Armor')
	armor.save()

	lps = Affix(affix='lps',
		is_primary=True,
		desc='<span>+4,643 - 5,528</span> Life Regeneration per Second',
		ancient='<span>+6,080 - 7,185</span> Life Regeneration per Second')
	lps.save()

	movementSpeed = Affix(affix='movementSpeed',
		desc='<span>+10 - 12%</span> Movement Speed',
		is_primary=True)
	movementSpeed.save()


#Boj Anglers
	bojSkillDmg = Affix(affix='bojSkillDmg',
		is_primary=True,
		desc='Increases {<span class="vary">Skill Damage</span>} by <span>10 - 15%</span>',
		notes='<strong>Barbarian: </strong>Ancient Spear | Hammer of the Ancients | Seismic Slam | Whirlwind<br><strong>Crusader: </strong>Blessed Hammer | Blessed Shield | Fist of the Heavens | Phalanx | Shield Bash | Sweep Attack<br><strong>Demon Hunter: </strong>Chakram | Cluster Arrow | Elemental Arrow | Impale | Multishot | Rapid Fire | Strafe<br><strong>Monk: </strong>Exploding Palm | Lashing Tail Kick | Tempest Rush | Wave of Light<br><strong>Witch Doctor: </strong>Acid Cloud | Firebats | Sacrifice | Spirit Barrage | Zombie Charger<br><strong>Wizard: </strong>Arcane Orb | Arcane Torrent | Disintegrate | Energy Twister | Meteor | Ray of Frost | Wave of Force')
	bojSkillDmg.save()

#Ice Climbers
	iceReducedColdDmg = Affix(affix='iceReducedColdDmg',
		is_primary=True,
		desc='<span>+7 - 10%</span> Cold Damage Reduction')
	iceReducedColdDmg.save()


	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()


class Migration(migrations.Migration):

    dependencies = [
        ('affixes', '0020_pants_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_boots_affixes)
    ]
