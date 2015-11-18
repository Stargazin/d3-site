# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify


def load_crusader_shields(apps, schema_editor):
	CrusaderShield = apps.get_model("legendaries", "CrusaderShield")
	Affix = apps.get_model("affixes", "CrusaderShieldAffix")

	stre = Affix.objects.get(affix='stre')
	blockChance = Affix.objects.get(affix='blockChance')

	akaratsAwakening = CrusaderShield(name='Akarat\'s Awakening',
		pic='/assets/media/items/legendaries/offhands/crusadershields/akarats_awakening.png',
		unique='Every successful block has a <span>20 - 25%</span> chance to reduce all cooldowns by <span class="silver">1</span> second.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='21.0 - 31.0%')
	akaratsAwakening.save()
	akaratsAwakening.affixes.add(stre, blockChance)

	frydehrsWrath = CrusaderShield(name='Frydehr\'s Wrath',
		pic='/assets/media/items/legendaries/offhands/crusadershields/frydehrs_wrath.png',
		unique='Condemn has no cooldown but instead costs <span class="silver">40</span> Wrath.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	frydehrsWrath.save()
	frydehrsWrath.affixes.add(stre)

	guardOfJohanna = CrusaderShield(name='Guard Of Johanna',
		pic='/assets/media/items/legendaries/offhands/crusadershields/guard_of_johanna.png',
		unique='Blessed Hammer damage is increased by <span>200 - 250%</span> for the first <span class="silver">3</span> enemies it hits.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	guardOfJohanna.save()
	guardOfJohanna.affixes.add(stre)

	hallowedBulwark = CrusaderShield(name='Hallowed Bulwark',
		pic='/assets/media/items/legendaries/offhands/crusadershields/hallowed_bulwark.png',
		unique='Iron Skin also increases your Block Amount by <span>45 - 60%</span>.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	hallowedBulwark.save()
	hallowedBulwark.affixes.add(stre)

	hellskull = CrusaderShield(name='hellskull',
		pic='/assets/media/items/legendaries/offhands/crusadershields/hellskull.png',
		unique='Gain <span class="silver">10%</span> increased damage while wielding a two-handed weapon.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	hellskull.save()
	hellskull.affixes.add(stre)

	jekangbord = CrusaderShield(name='jekangbord',
		pic='/assets/media/items/legendaries/offhands/crusadershields/jekangbord.png',
		unique='Blessed Shield ricochets to <span>4 - 6</span> additional enemies.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	jekangbord.save()
	jekangbord.affixes.add(stre)

	piroMarella = CrusaderShield(name='Piro Marella',
		pic='/assets/media/items/legendaries/offhands/crusadershields/piro_marella.png',
		unique='Reduces the Wrath cost of Shield Bash by <span>40 - 50%</span>.',
		random_primaries='4',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	piroMarella.save()
	piroMarella.affixes.add()

	salvation = CrusaderShield(name='salvation',
		pic='/assets/media/items/legendaries/offhands/crusadershields/salvation.png',
		unique='Blocked attacks heal you and your allies for <span>20 - 30%</span> of the amount blocked.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='21.0 - 31.0%')
	salvation.save()
	salvation.affixes.add(stre, blockChance)

	sublimeConviction = CrusaderShield(name='Sublime Conviction',
		pic='/assets/media/items/legendaries/offhands/crusadershields/sublime_conviction.png',
		unique='When you block, you have up to a <span>15 - 20%</span> chance to Stun the attacker for <span class="silver">1.5</span> seconds based on your current Wrath.',
		random_primaries='2',
		random_secondaries='1',
		block_chance='21.0 - 31.0%')
	sublimeConviction.save()
	sublimeConviction.affixes.add(stre, blockChance)

	theFinalWitness = CrusaderShield(name='The Final Witness',
		pic='/assets/media/items/legendaries/offhands/crusadershields/the_final_witness.png',
		unique='Shield Glare now hits all enemies around you.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	theFinalWitness.save()
	theFinalWitness.affixes.add(stre)

	unrelentingPhalanx = CrusaderShield(name='Unrelenting Phalanx',
		pic='/assets/media/items/legendaries/offhands/crusadershields/unrelenting_phalanx.png',
		unique='Phalanx now casts twice.',
		random_primaries='3',
		random_secondaries='1',
		block_chance='10.0 - 20.0%')
	unrelentingPhalanx.save()
	unrelentingPhalanx.affixes.add(stre)


	for crusaderShield in CrusaderShield.objects.all():
		crusaderShield.slug = slugify(crusaderShield.name)
		crusaderShield.category = 'CrusaderShield'
		crusaderShield.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legendaries', '0006_mojos'),
    ]

    operations = [
    	migrations.RunPython(load_crusader_shields)
    ]
