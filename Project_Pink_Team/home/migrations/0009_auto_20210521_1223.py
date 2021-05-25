# Generated by Django 3.1.7 on 2021-05-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210521_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='curp',
            field=models.CharField(default='pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default='pendiente', max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='grado_alumno',
            field=models.CharField(choices=[('Primer grado', 'Primer grado'), ('Segundo grado', 'Segundo grado'), ('Tercer grado', 'Tercer grado'), ('Cuarto grado', 'Cuarto grado'), ('Quinto grado', 'Quinto grado'), ('Sexto grado', 'Sexto grado'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono_casa',
            field=models.CharField(default='pendiente', max_length=32),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono_cel',
            field=models.CharField(default='pendiente', max_length=32),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='titulo_docente',
            field=models.CharField(default='pendiente', max_length=50),
        ),
    ]
