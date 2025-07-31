from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0003_populate_nationalities_and_convert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actormodel',
            name='nationality',
        ),
        migrations.RenameField(
            model_name='actormodel',
            old_name='nationality_temp',
            new_name='nationality',
        ),
    ]