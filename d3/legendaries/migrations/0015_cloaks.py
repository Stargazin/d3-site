# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_cloaks(apps, schema_editor):
	Cloak = apps.get_model("legendaries", "Cloak")
	Affix = apps.get_model("affixes", "CloakAffix")


	dext = Affix.objects.get(affix='dext')
	vita = Affix.objects.get(affix='vita')
	armor = Affix.objects.get(affix='armor')
	sockets = Affix.objects.get(affix='sockets')


	beckonSail = Cloak(name='Beckon Sail',
		pic='/assets/media/items/legendaries/armor/torso/cloaks/beckon_sail.png',
		unique='When receiving fatal damage, you instead automatically cast Smoke Screen and are healed to <span class="silver">25%</span> Life. This effect may occur once every <span class="silver">120</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	beckonSail.save()
	beckonSail.affixes.add(dext, sockets)

	blackfeather = Cloak(name='blackfeather',
		pic='/assets/media/items/legendaries/armor/torso/cloaks/blackfeather.png',
		unique='Dodging or getting hit by a ranged attack automatically shoots a homing rocket back at the attacker for <span>600 - 800%</span> weapon damage as Physical.',
		random_primaries='2',
		random_secondaries='1')
	blackfeather.save()
	blackfeather.affixes.add(dext, sockets)

	capeOfTheDarkNight = Cloak(name='Cape of the Dark Night',
		pic='/assets/media/items/legendaries/armor/torso/cloaks/cape_of_the_dark_night.png',
		unique='Automatically drop Caltrops when you are hit. This effect may only occur once every <span class="silver">6</span> seconds.',
		random_primaries='3',
		random_secondaries='1')
	capeOfTheDarkNight.save()
	capeOfTheDarkNight.affixes.add(dext)

	cloakOfDeception = Cloak(name='Cloak of Deception',
		pic='/assets/media/items/legendaries/armor/torso/cloaks/cloak_of_deception.png',
		random_primaries='1',
		random_secondaries='1')
	cloakOfDeception.save()
	cloakOfDeception.affixes.add(dext, vita, armor)

	theCloakOfTheGarwulf = Cloak(name='The Cloak of the Garwulf',
		pic='/assets/media/items/legendaries/armor/torso/cloaks/the_cloak_of_the_garwulf.png',
		unique='Companion - Wolf Companion now summons <span class="silver">3<span> wolves.',
		random_primaries='3',
		random_secondaries='1')
	theCloakOfTheGarwulf.save()
	theCloakOfTheGarwulf.affixes.add(dext)


	for cloak in Cloak.objects.all():
		cloak.slug = slugify(cloak.name)
		cloak.category = 'Cloak'
		cloak.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0014_chest_armor'),
    ]

    operations = [
    	migrations.RunPython(load_cloaks)
    ]
