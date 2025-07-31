from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome da Nacionalidade')),
            ],
            options={
                'verbose_name': 'Nacionalidade',
                'verbose_name_plural': 'Nacionalidades',
                'ordering': ['name'],
            },
        ),

        migrations.AddField(
            model_name='actormodel',
            name='nationality_temp',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='actors.nationality',
                verbose_name='Nacionalidade'
            ),
        ),
    ]
