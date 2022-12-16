# Generated by Django 4.1.3 on 2022-11-27 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de carrera')),
                ('carrera_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Carrera')),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
                'db_table': 'carrera',
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, verbose_name='RUT')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('correo', models.CharField(max_length=100, verbose_name='Correo')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Alumnado.carrera')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
                'db_table': 'alumno',
                'ordering': ['rut', 'nombre', 'apellidos', 'correo'],
            },
        ),
    ]
