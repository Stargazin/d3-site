# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_wizard_hats(apps, schema_editor):
	WizardHat = apps.get_model("legendaries", "WizardHat")
	Affix = apps.get_model("affixes", "WizardHatAffix")


	inte = Affix.objects.get(affix='inte')
	sockets = Affix.objects.get(affix='sockets')
	apCrit = Affix.objects.get(affix='apCrit')

	maxAP = Affix.objects.get(affix='maxAP')

	stormLightDmg = Affix.objects.get(affix='stormLightDmg')


	archmagesVicalyke = WizardHat(name='Archmage\'s Vicalyke',
		pic='/assets/media/items/legendaries/armor/head/wizardhats/archmages_vicalyke.png',
		unique='Your Mirror Images have a chance to multiply when killed by enemies.',
		random_primaries='3',
		random_secondaries='1')
	archmagesVicalyke.save()
	archmagesVicalyke.affixes.add(inte)

	crownOfThePrimus = WizardHat(name='Crown of The Primus',
		pic='/assets/media/items/legendaries/armor/head/wizardhats/crown_of_the_primus.png',
		unique='Slow Time gains the effect of every rune.',
		random_primaries='2',
		random_secondaries='1')
	crownOfThePrimus.save()
	crownOfThePrimus.affixes.add(inte, sockets)

	darkMagesShade = WizardHat(name='Dark Mage\'s Shade',
		pic='/assets/media/items/legendaries/armor/head/wizardhats/dark_mages_shade.png',
		unique='Automatically cast Diamond Skin when you fall below <span class="silver">35%</span> Life. This effect may occur once every <span>15 - 20</span> seconds.',
		random_primaries='3',
		random_secondaries='1')
	darkMagesShade.save()
	darkMagesShade.affixes.add(inte)

	stormCrow = WizardHat(name='Storm Crow',
		pic='/assets/media/items/legendaries/armor/head/wizardhats/storm_crow.png',
		unique='<span>20 - 40%</span> chance to cast a fiery ball when attacking.',
		random_primaries='2',
		random_secondaries='1')
	stormCrow.save()
	stormCrow.affixes.add(inte, stormLightDmg)

	theMagistrate = WizardHat(name='The Magistrate',
		pic='/assets/media/items/legendaries/armor/head/wizardhats/the_magistrate.png',
		unique='Frost Hydra now periodically casts Frost Nova.',
		random_primaries='2',
		random_secondaries='1')
	theMagistrate.save()
	theMagistrate.affixes.add(inte, sockets)

	theSwami = WizardHat(name='The Swami',
		pic='/assets/media/items/legendaries/armor/head/wizardhats/the_swami.png',
		unique='The bonuses from Archon stacks now last for <span>15 - 20</span> seconds after Archon expires.',
		random_primaries='1',
		random_secondaries='1')
	theSwami.save()
	theSwami.affixes.add(inte, apCrit, maxAP)

	velvetCamaral = WizardHat(name='velvetCamaral',
		pic='/assets/media/items/legendaries/armor/head/wizardhats/velvet_camaral.png',
		unique='Double the number of enemies your Electrocute jumps to.',
		random_primaries='2',
		random_secondaries='1')
	velvetCamaral.save()
	velvetCamaral.affixes.add(inte, sockets)


	for wizardHat in WizardHat.objects.all():
		wizardHat.slug = slugify(wizardHat.name)
		wizardHat.category = 'WizardHat'
		wizardHat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0011_voodoo_masks'),
    ]

    operations = [
    	migrations.RunPython(load_wizard_hats)
    ]
