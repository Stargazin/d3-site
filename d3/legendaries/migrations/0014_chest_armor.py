# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_chest_armor(apps, schema_editor):
	ChestArmor = apps.get_model("legendaries", "ChestArmor")
	Affix = apps.get_model("affixes", "ChestArmorAffix")


	mainStat = Affix.objects.get(affix='mainStat')
	vita = Affix.objects.get(affix='vita')
	allRes = Affix.objects.get(affix='allRes')

	durability = Affix.objects.get(affix='durability')

	cindercoatFireDmg = Affix.objects.get(affix='cindercoatFireDmg')
	goldskinExtraGold = Affix.objects.get(affix='goldskinExtraGold')
	tyraelsDemonDmg = Affix.objects.get(affix='tyraelsDemonDmg')


	aquilaCuirass = ChestArmor(name='Aquila Cuirass',
		pic='/assets/media/items/legendaries/armor/torso/chestarmor/aquila_cuirass.png',
		random_primaries='2',
		random_secondaries='2')
	aquilaCuirass.save()
	aquilaCuirass.affixes.add(mainStat, vita)

	armorOfTheKindRegent = ChestArmor(name='Armor of the KindRegent',
		pic='/assets/media/items/legendaries/armor/torso/chestarmor/armor_of_the_kind_regent.png',
		unique='Smite will now also be cast at a second nearby enemy.',
		random_primaries='3',
		random_secondaries='1')
	armorOfTheKindRegent.save()
	armorOfTheKindRegent.affixes.add(mainStat)

	chaingmail = ChestArmor(name='chaingmail',
		pic='/assets/media/items/legendaries/armor/torso/chestarmor/chaingmail.png',
		unique='After earning a survival bonus, quickly heal to full Life.',
		random_primaries='2',
		random_secondaries='1')
	chaingmail.save()
	chaingmail.affixes.add(mainStat, allRes)

	cindercoat = ChestArmor(name='cindercoat',
		pic='/assets/media/items/legendaries/armor/torso/chestarmor/cindercoat.png',
		unique='Reduces the resource cost of Fire skills by <span>23 - 30%</span>.',
		random_primaries='2',
		random_secondaries='1')
	cindercoat.save()
	cindercoat.affixes.add(mainStat, cindercoatFireDmg)

	goldskin = ChestArmor(name='goldskin',
		pic='/assets/media/items/legendaries/armor/torso/chestarmor/goldskin.png',
		unique='Chance for enemies to drop gold when you hit them.',
		random_primaries='2')
	goldskin.save()
	goldskin.affixes.add(mainStat, allRes, goldskinExtraGold)

	heartOfIron = ChestArmor(name='Heart of Iron',
		pic='/assets/media/items/legendaries/armor/torso/chestarmor/heart_of_iron.png',
		random_primaries='2',
		random_secondaries='2')
	heartOfIron.save()
	heartOfIron.affixes.add(mainStat, allRes)

	mantleOfTheRydraelm = ChestArmor(name='Mantle of the Rydraelm',
		pic='/assets/media/items/legendaries/armor/torso/chestarmor/mantle_of_the_rydraelm.png',
		random_primaries='4',
		random_secondaries='6')
	mantleOfTheRydraelm.save()

	shiMizusHaori = ChestArmor(name='Shi Mizu\'s Haori',
		pic='/assets/media/items/legendaries/armor/torso/chestarmor/shi_mizus_haori.png',
		unique='While below <span>20 - 25%</span> Life, all attacks are guaranteed Critical Hits.',
		random_primaries='3',
		random_secondaries='1')
	shiMizusHaori.save()
	shiMizusHaori.affixes.add(mainStat)

	tyraelsMight = ChestArmor(name='Tyrael\'s Might',
		pic='/assets/media/items/legendaries/armor/torso/chestarmor/tyraels_might.png',
		random_primaries='2',
		random_secondaries='1')
	tyraelsMight.save()
	tyraelsMight.affixes.add(mainStat, allRes, tyraelsDemonDmg, durability)


	for chestArmor in ChestArmor.objects.all():
		chestArmor.slug = slugify(chestArmor.name)
		chestArmor.category = 'ChestArmor'
		chestArmor.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0013_shoulders'),
    ]

    operations = [
    	migrations.RunPython(load_chest_armor)
    ]
