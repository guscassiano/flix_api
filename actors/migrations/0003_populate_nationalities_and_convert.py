from django.db import migrations


NATIONALITY_CHOICES = [
    'Brasil',
    'Estados Unidos',
    'Alemanha',
    'Inglaterra',
    'Japão',
    'China',
]


def populate_nationalities_and_convert(apps, schema_editor):
    Nationality = apps.get_model('actors', 'Nationality')
    ActorModel = apps.get_model('actors', 'ActorModel')

    nationality_objects = {}
    for name in NATIONALITY_CHOICES:
        nationality, created = Nationality.objects.get_or_create(name=name)
        nationality_objects[name] = nationality

    for actor in ActorModel.objects.all():
        if actor.nationality:
            nationality_obj = nationality_objects.get(actor.nationality)
            if nationality_obj:
                actor.nationality_temp = nationality_obj
                actor.save()

def reverse_populate_nationalities_and_convert(apps, schema_editor):
    ActorModel = apps.get_model('actors', 'ActorModel')

    for actor in ActorModel.objects.all():
        if actor.nationality_temp:
            actor.nationality = actor.nationality_temp.name
            actor.save()

class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_create_nationality_and_temp_field'),
    ]

    operations = [
        migrations.RunPython(
            populate_nationalities_and_convert,
            reverse_populate_nationalities_and_convert
        ),
    ]