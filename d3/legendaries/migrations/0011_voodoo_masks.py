# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_voodoo_masks(apps, schema_editor):
	VoodooMask = apps.get_model("legendaries", "VoodooMask")
	Affix = apps.get_model("affixes", "VoodooMaskAffix")

	inte = Affix.objects.get(affix='inte')
	chc = Affix.objects.get(affix='chc')
	sockets = Affix.objects.get(affix='sockets')

	maxMana = Affix.objects.get(affix='maxMana')
	killExp = Affix.objects.get(affix='killExp')


	carnevil = VoodooMask(name='carnevil',
		pic='/assets/media/items/legendaries/armor/head/voodoomasks/carnevil.png',
		unique='The <span class="silver">5</span> Fetishes closest to you will shoot a powerful Poison Dart every time you do.',
		random_primaries='2',
		random_secondaries='1')
	carnevil.save()
	carnevil.affixes.add(inte, chc)

	maskOfJeram = VoodooMask(name='Mask of Jeram',
		pic='/assets/media/items/legendaries/armor/head/voodoomasks/mask_of_jeram.png',
		unique='Pets deal <span>75 - 100%</span> more damage.',
		random_primaries='2',
		random_secondaries='1')
	maskOfJeram.save()
	maskOfJeram.affixes.add(inte, sockets)

	quetzalcoatl = VoodooMask(name='Quetzalcoatl',
		pic='/assets/media/items/legendaries/armor/head/voodoomasks/quetzalcoatl.png',
		unique='Locust Swarm and Haunt now deal their damage in half of the normal duration.',
		random_primaries='3',
		random_secondaries='1')
	quetzalcoatl.save()
	quetzalcoatl.affixes.add(inte)

	splitTusk = VoodooMask(name='Split Tusk',
		pic='/assets/media/items/legendaries/armor/head/voodoomasks/split_tusk.png',
		random_primaries='3')
	splitTusk.save()
	splitTusk.affixes.add(inte, maxMana, killExp)

	theGrinReaper = VoodooMask(name='The Grin Reaper',
		pic='/assets/media/items/legendaries/armor/head/voodoomasks/the_grin_reaper.png',
		unique='Chance when attacking to summon horrific Mimics that cast some of your equipped skills.',
		random_primaries='2',
		random_secondaries='1')
	theGrinReaper.save()
	theGrinReaper.affixes.add(inte, sockets)

	tiklandianVisage = VoodooMask(name='Tiklandian Visage',
		pic='/assets/media/items/legendaries/armor/head/voodoomasks/tiklandian_visage.png',
		unique='Horrify causes you to Fear and Root enemies around you for <span>6 - 8</span> seconds.',
		random_primaries='3',
		random_secondaries='1')
	tiklandianVisage.save()
	tiklandianVisage.affixes.add(inte)

	visageOfGiyua = VoodooMask(name='Visage Of Giyua',
		pic='/assets/media/items/legendaries/armor/head/voodoomasks/visage_of_giyua.png',
		unique='Summon a Fetish Army after you kill <span class="silver">2</span> Elites.',
		random_primaries='3',
		random_secondaries='1')
	visageOfGiyua.save()
	visageOfGiyua.affixes.add(inte)


	for voodooMask in VoodooMask.objects.all():
		voodooMask.slug = slugify(voodooMask.name)
		voodooMask.category = 'VoodooMask'
		voodooMask.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0010_spirit_stones'),
    ]

    operations = [
    	migrations.RunPython(load_voodoo_masks)
    ]
