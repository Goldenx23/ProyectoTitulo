# Generated by Django 4.1.3 on 2022-11-28 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alumnado', '0002_alter_carrera_carrera_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10, verbose_name='RUT Encargado')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Encargado')),
                ('sexo', models.CharField(max_length=10, verbose_name='Sexo Encargado')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha Nacimiento Encargado')),
            ],
            options={
                'verbose_name': 'Encargado',
                'verbose_name_plural': 'Encargados',
                'db_table': 'encargado',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100, verbose_name='Nombre Usuario Encargado')),
                ('contraseña', models.CharField(max_length=100, verbose_name='Contraseña Encargado')),
                ('correo', models.CharField(max_length=100, verbose_name='Correo Encargado')),
                ('encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumnado.encargado')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
    ]
