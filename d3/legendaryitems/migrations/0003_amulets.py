# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_amulets(apps, schema_editor):
	Amulet = apps.get_model("legendaryitems", "Amulet")

	ancestors = Amulet(id=0,
		category='Amulet',
		name='Ancestors\' Grace',
		pic='/assets/media/items/legendaries/accessories/amulets/ancestors_grace.png',
		unique='When receiving fatal damage, you are instead restored to 100% of maximum Life and resources. This item is destroyed in the process.',
		unique_is_primary=True,
		affixes=)
	ancestors.save()

	countess = Amulet(id=1,
		category='Amulet',
		name='Countess Julia\'s Cameo',
		pic='/assets/media/items/legendaries/accessories/amulets/countess_julias_cameo.png',
		unique='Prevent all Arcane damage taken and heal yourself for <span>20 - 25%</span> of the amount prevented.',
		unique_is_primary=False)
	countess.save()

	dovu = Amulet(id=2,
		category='Amulet',
		name='Dovu Energy Trap',
		pic='/assets/media/items/legendaries/accessories/amulets/dovu_energy_trap.png',
		unique='Increases duration of Stun effects by <span>20 - 25%</span>.',
		unique_is_primary=False)
	dovu.save()

	eye = Amulet(id=3,
		category='Amulet',
		name='Eye of Elitch',
		pic='/assets/media/items/legendaries/accessories/amulets/eye_of_elitch.png',
		unique='Reduces damage from ranged attacks by <span>27.7 - 32.9%</span>.',
		unique_is_primary=False)
	eye.save()

	gorget = Amulet(id=4,
		category='Amulet',
		name='Golden Gorget of Leoric',
		pic='/assets/media/items/legendaries/accessories/amulets/golden_gorget_of_leoric.png',
		unique='After earning a massacre bonus, <span>4 - 6</span> Skeletons are summoned to fight by your side for 10 seconds.',
		unique_is_primary=False)
	gorget.save()

	halcyon = Amulet(id=5,
		category='Amulet',
		name='Halcyon\'s Ascent',
		pic='/assets/media/items/legendaries/accessories/amulets/halcyons_ascent.png',
		unique='When you use <span><em>Class Skill</em></span>, you mesmerize nearby enemies with your skill, causing them to jump uncontrollably for <span>6 - 8</span> seconds.',
		unique_is_primary=False)
	halcyon.save()

	haunt = Amulet(id=6,
		category='Amulet',
		name='Haunt of Vaxo',
		pic='/assets/media/items/legendaries/accessories/amulets/haunt_of_vaxo.png',
		unique='Summons shadow clones to your aid when you Stun an enemy. This effect may occur once every 30 seconds.',
		unique_is_primary=False)
	haunt.save()

	hellfire = Amulet(id=7,
		category='Amulet',
		name='Hellfire Amulet',
		pic='/assets/media/items/legendaries/accessories/amulets/hellfire_amulet.png',
		unique='Gain a random <span><em>Class Specific</em></span> passive.',
		unique_is_primary=False)
	hellfire.save()

	holy = Amulet(id=8,
		category='Amulet',
		name='Holy Beacon',
		pic='/assets/media/items/legendaries/accessories/amulets/holy_beacon.png',
		unique='<span>+2.2 - 3.0</span> Spirit Regeneration per Second',
		unique_is_primary=True)
	holy.save()

	kymbos = Amulet(id=9,
		category='Amulet',
		name='Kymbo\'s Gold',
		pic='/assets/media/items/legendaries/accessories/amulets/kymbos_gold.png',
		unique='Picking up gold heals you for an amount equal to the gold that was picked up.',
		unique_is_primary=False)
	kymbos.save()

	maras = Amulet(id=10,
		category='Amulet',
		name='Mara\'s Kaleidoscope',
		pic='/assets/media/items/legendaries/accessories/amulets/maras_kaleidoscope.png',
		unique='Prevent all Poison damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		unique_is_primary=False)
	maras.save()

	moonlight = Amulet(id=11,
		category='Amulet',
		name='Moonlight Ward',
		pic='/assets/media/items/legendaries/accessories/amulets/moonlight_ward.png',
		unique='Hitting an enemy within 15 yards has a chance to ward you with Arcane shards that explode when enemies get close, dealing <span>240 - 320%</span> weapon damage as Arcane to enemies within 15 yards.',
		unique_is_primary=False)
	moonlight.save()

	ouroboros = Amulet(id=12,
		category='Amulet',
		name='Ouroboros',
		pic='/assets/media/items/legendaries/accessories/amulets/ouroboros.png')
	ouroboros.save()

	overwhelming = Amulet(id=13,
		category='Amulet',
		name='Overwhelming Desire',
		pic='/assets/media/items/legendaries/accessories/amulets/overwhelming_desire.png',
		unique='Chance on hit to charm the enemy. While charmed, the enemy takes 35% more damage.',
		unique_is_primary=False)
	overwhelming.save()

	rakoffs = Amulet(id=14,
		category='Amulet',
		name='Rakoff\'s Glass of Life',
		pic='/assets/media/items/legendaries/accessories/amulets/rakoffs_glass_of_life.png',
		unique='Enemies you kill have a <span>3 - 4%</span> additional chance to drop a health globe.',
		unique_is_primary=False)
	rakoffs.save()

	rondals = Amulet(id=15,
		category='Amulet',
		name='Rondal\'s Locket',
		pic='/assets/media/items/legendaries/accessories/amulets/rondals_locket.png')
	rondals.save()

	squirts = Amulet(id=16,
		category='Amulet',
		name='Squirt\'s Necklace',
		pic='/assets/media/items/legendaries/accessories/amulets/squirts_necklace.png')
	squirts.save()

	talisman = Amulet(id=17,
		category='Amulet',
		name='Talisman of Aranoch',
		pic='/assets/media/items/legendaries/accessories/amulets/talisman_of_aranoch.png',
		unique='Prevent all Cold damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		unique_is_primary=False)
	talisman.save()

	ess = Amulet(id=18,
		category='Amulet',
		name='The Ess of Johan',
		pic='/assets/media/items/legendaries/accessories/amulets/the_ess_of_johan.png',
		unique='Chance on hit to pull in enemies toward your target and Slow them by <span>60 - 80%</span>.',
		unique_is_primary=False)
	ess.save()

	flavor = Amulet(id=19,
		category='Amulet',
		name='The Flavor of Time',
		pic='/assets/media/items/legendaries/accessories/amulets/the_flavor_of_time.png')
	flavor.save()

	star = Amulet(id=20,
		category='Amulet',
		name='The Star of Azkaranth',
		pic='/assets/media/items/legendaries/accessories/amulets/the_star_of_azkaranth.png',
		unique='Prevent all Fire damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		unique_is_primary=False)
	star.save()

	xephirian = Amulet(id=22,
		category='Amulet',
		name='Xephirian Amulet',
		pic='/assets/media/items/legendaries/accessories/amulets/xephirian_amulet.png',
		unique='Prevent all Lightning damage taken and heal yourself for <span>10 - 15%</span> of the amount prevented.',
		unique_is_primary=False)
	xephirian.save()



class Migration(migrations.Migration):

    dependencies = [
        ('legendaryitems', '0002_amulet_affixes'),
    ]

    operations = [
    	migrations.RunPython(load_amulets),
    ]