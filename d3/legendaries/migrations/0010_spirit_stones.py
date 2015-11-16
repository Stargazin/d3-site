# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_spirit_stones(apps, schema_editor):
	SpiritStone = apps.get_model("legendaries", "SpiritStone")
	Affix = apps.get_model("affixes", "SpiritStoneAffix")

	dext = Affix.objects.get(affix='dext')
	chc = Affix.objects.get(affix='chc')
	sockets = Affix.objects.get(affix='sockets')
	skillDmg = Affix.objects.get(affix='skillDmg')

	ccReduction = Affix.objects.get(affix='ccReduction')
	killExp = Affix.objects.get(affix='killExp')

	eyeLightDmg = Affix.objects.get(affix='eyeLightDmg')
	tzoWaveOfLight = Affix.objects.get(affix='tzoWaveOfLight')


	bezoarStone = SpiritStone(name='Bezoar Stone',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/bezoar_stone.png',
		random_primaries='2',
		random_secondaries='2')
	bezoarStone.save()
	bezoarStone.affixes.add(dext, skillDmg)

	erlangShen = SpiritStone(name='Erlang Shen',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/erlang_shen.png',
		random_primaries='3',
		random_secondaries='1')
	erlangShen.save()
	erlangShen.affixes.add(dext, ccReduction)

	eyeOfPeshkov = SpiritStone(name='Eye Of Peshkov',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/eye_of_peshkov.png',
		unique='Reduce the cooldown of Breath of Heaven by <span>38 - 50%</span>.',
		random_primaries='2',
		random_secondaries='1')
	eyeOfPeshkov.save()
	eyeOfPeshkov.affixes.add(dext, sockets)

	gyanaNaKashu = SpiritStone(name='Gyana Na Kashu',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/gyana_na_kashu.png',
		unique='Lashing Tail Kick releases a piercing fireball that deals <span>525 - 700%</span> weapon damage as Fire to enemies within <span class="silver">10</span> yards on impact.',
		random_primaries='2',
		random_secondaries='1')
	gyanaNaKashu.save()
	gyanaNaKashu.affixes.add(dext, sockets)

	kekegisUnbreakableSpirit = SpiritStone(name='Kekegi\'s Unbreakable Spirit',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/kekegis_unbreakable_spirit.png',
		unique='Damaging enemies has a chance to grant you an effect that removes the Spirit cost of your abilities for <span>2 - 4</span> seconds.',
		random_primaries='2',
		random_secondaries='1')
	kekegisUnbreakableSpirit.save()
	kekegisUnbreakableSpirit.affixes.add(dext, chc)

	madstone = SpiritStone(name='Madstone',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/madstone.png',
		unique='Your Seven-Sided Strike applies Exploding Palm.',
		random_primaries='3',
		random_secondaries='1')
	madstone.save()
	madstone.affixes.add(dext)

	seeNoEvil = SpiritStone(name='See No Evil',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/see_no_evil.png',
		random_primaries='3',
		random_secondaries='1')
	seeNoEvil.save()
	seeNoEvil.affixes.add(dext, killExp)

	theEyeOfTheStorm = SpiritStone(name='The Eye of The Storm',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/the_eye_of_the_storm.png',
		random_primaries='2',
		random_secondaries='2')
	theEyeOfTheStorm.save()
	theEyeOfTheStorm.affixes.add(dext, eyeLightDmg)

	theLawsOfSeph = SpiritStone(name='The Laws of Seph',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/the_laws_of_seph.png',
		unique='Using Blinding Flash restores <span>125 - 165</span> Spirit.',
		random_primaries='2',
		random_secondaries='1')
	theLawsOfSeph.save()
	theLawsOfSeph.affixes.add(dext, sockets)

	theMindsEye = SpiritStone(name='The Mind\'s Eye',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/the_minds_eye.png',
		unique='Inner Sanctuary increases Spirit Regeneration per second by <span>10 - 15</span>.',
		random_primaries='2',
		random_secondaries='1')
	theMindsEye.save()
	theMindsEye.affixes.add(dext, sockets)

	tzoKrinsGaze = SpiritStone(name='Tzo Krin\'s Gaze',
		pic='/assets/media/items/legendaries/armor/head/spiritstones/tzo_krins_gaze.png',
		unique='Wave of Light is now cast at your enemy.',
		random_primaries='3',
		random_secondaries='1')
	tzoKrinsGaze.save()
	tzoKrinsGaze.affixes.add(dext, tzoWaveOfLight)


	for spiritStone in SpiritStone.objects.all():
		spiritStone.slug = slugify(spiritStone.name)
		spiritStone.category = 'SpiritStone'
		spiritStone.save()


class Migration(migrations.Migration):

	dependencies = [
		('legendaries', '0009_helmets'),
	]

	operations = [
		migrations.RunPython(load_spirit_stones)
	]
