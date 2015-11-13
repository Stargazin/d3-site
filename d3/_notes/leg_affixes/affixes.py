def load__affixes(apps, schema_editor):
	Affix = apps.get_model("affixes", "Affix")















































	for affix in Affix.objects.all():
		if not affix.ancient:
			affix.ancient = affix.desc
			affix.save()
		else:
			pass