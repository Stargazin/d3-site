# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_boots(apps, schema_editor):
	Boots = apps.get_model("legendaries", "Boots")
	Affix = apps.get_model("affixes", "BootsAffix")

	mainStat = Affix.objects.get(affix='mainStat')
	vita = Affix.objects.get(affix='vita')
	allRes = Affix.objects.get(affix='allRes')
	armor = Affix.objects.get(affix='armor')
	lps = Affix.objects.get(affix='lps')
	movementSpeed = Affix.objects.get(affix='movementSpeed')

	bojSkillDmg = Affix.objects.get(affix='bojSkillDmg')
	iceReducedColdDmg = Affix.objects.get(affix='iceReducedColdDmg')

	boardWalkers = Boots(name='Board Walkers',
		pic='/assets/media/items/legendaries/armor/feet/board_walkers.png',
		random_primaries='3',
		random_secondaries='2',
		notes='crafted')
	boardWalkers.save()
	boardWalkers.affixes.add(movementSpeed)

	bojAnglers = Boots(name='Boj Anglers',
		pic='/assets/media/items/legendaries/armor/feet/boj_anglers.png',
		unique='',
		random_primaries='2',
		random_secondaries='2')
	bojAnglers.save()
	bojAnglers.affixes.add(mainStat, bojSkillDmg)

	bootsOfDisregard = Boots(name='Boots of Disregard',
		pic='/assets/media/items/legendaries/armor/feet/boots_of_disregard.png',
		unique='Gain <span>10000</span> Life regeneration per Second for each second you stand still. This effect stacks up to <span>4</span> times.',
		random_primaries='1',
		random_secondaries='1')
	bootsOfDisregard.save()
	bootsOfDisregard.affixes.add(vita, armor, lps)

	fireWalkers = Boots(name='Fire Walkers',
		pic='/assets/media/items/legendaries/armor/feet/fire_walkers.png',
		unique='Burn the ground you walk on, dealing <span>300 - 400%</span> weapon damage each second.',
		random_primaries='2',
		random_secondaries='1')
	fireWalkers.save()
	fireWalkers.affixes.add(mainStat, movementSpeed)

	iceClimbers = Boots(name='iceClimbers',
		pic='/assets/media/items/legendaries/armor/feet/ice_climbers.png',
		unique='Gain immunity to Freeze and Immobilize effects.',
		random_primaries='2',
		random_secondaries='1')
	iceClimbers.save()
	iceClimbers.affixes.add(mainStat, allRes, iceReducedColdDmg)

	illusoryBoots = Boots(name='Illusory Boots',
		pic='/assets/media/items/legendaries/armor/feet/illusory_boots.png',
		unique='You may move unhindered through enemies.',
		random_primaries='1',
		random_secondaries='1')
	illusoryBoots.save()
	illusoryBoots.affixes.add(mainStat, allRes, movementSpeed)

	irontoeMudsputters = Boots(name='Irontoe Mudsputters',
		pic='/assets/media/items/legendaries/armor/feet/irontoe_mudsputters.png',
		unique='Gain up to <span>25 - 30%</span> increased movement speed based on amount of Life missing.',
		random_primaries='2',
		random_secondaries='1')
	irontoeMudsputters.save()
	irontoeMudsputters.affixes.add(mainStat, vita)

	lutSocks = Boots(name='Lut Socks',
		pic='/assets/media/items/legendaries/armor/feet/lut_socks.png',
		unique='Leap can be cast again within <span class="silver">2</span> seconds before the cooldown begins.',
		random_primaries='3',
		random_secondaries='1')
	lutSocks.save()
	lutSocks.affixes.add(mainStat)

	nilfursBoast = Boots(name='Nilfur\'s Boast',
		pic='/assets/media/items/legendaries/armor/feet/nilfurs_boast.png',
		unique='Increase the damage of Meteor by <span class="silver">100%</span>. When your Meteor hits <span class="silver">3</span> or fewer enemies, the damage is increased by <span>150 - 200%</span>.',
		random_primaries='2',
		random_secondaries='1')
	nilfursBoast.save()
	nilfursBoast.affixes.add(mainStat, allRes)

	theCrudestBoots = Boots(name='The Crudest Boots',
		pic='/assets/media/items/legendaries/armor/feet/the_crudest_boots.png',
		unique='Mystic Ally summons <span class="silver">2</span> extra Mystic Allies that fight by your side.',
		random_primaries='2',
		random_secondaries='1')
	theCrudestBoots.save()
	theCrudestBoots.affixes.add(mainStat, movementSpeed)


	for boots in Boots.objects.all():
		boots.slug = slugify(boots.name)
		boots.category = 'Boots'
		boots.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0020_pants'),
    ]

    operations = [
    	migrations.RunPython(load_boots)
    ]
