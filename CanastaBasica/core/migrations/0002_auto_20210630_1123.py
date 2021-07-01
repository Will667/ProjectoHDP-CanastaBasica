# Generated by Django 3.2.4 on 2021-06-30 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.departaments')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='encuest',
            name='muni',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.municipio'),
            preserve_default=False,
        ),
    ]
