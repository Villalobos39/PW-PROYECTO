# Generated by Django 3.1.7 on 2021-05-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210520_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_materias',
            name='horario',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='historial_materias',
            name='nombre_materia',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='materia_actual',
            name='horario',
            field=models.CharField(choices=[('8:00-9:00', '8:00-9:00'), ('9:00-10:00', '9:00-10:00'), ('10:00-11:00', '10:00-11:00'), ('11:30-12:30', '11:30-12:30'), ('12:30-13:30', '12:30-13:30'), ('13:30-14:30', '13:30-14:30'), ('13:30-14:00', '13:30-14:00'), ('14:00-15:00', '14:00-15:00'), ('15:00-16:00', '15:00-16:00'), ('16:30-17:00', '16:00-17:00'), ('17:00-18:30', '17:30-18:30'), ('18:30-19:30', '17:30-18:30'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=50),
        ),
        migrations.AlterField(
            model_name='materia_actual',
            name='nombre_materia',
            field=models.CharField(choices=[('Español 1', 'Español 1'), ('Matemáticas 1', 'Matemáticas 1'), ('Exploración de la Naturaleza y la Sociedad 1', 'Exploración de la Naturaleza y la Sociedad 1'), ('Formación Cívica y Ética 1', 'Formación Cívica y Ética 1'), ('Español 2', 'Español 2'), ('Matemáticas 2', 'Matemáticas 2'), ('Exploración de la Naturaleza y la Sociedad 2', 'Exploración de la Naturaleza y la Sociedad 2'), ('Formación Cívica y Ética 2', 'Formación Cívica y Ética 2'), ('Español 3', 'Español 3'), ('Matemáticas 3', 'Matemáticas 3'), ('Ciencias Naturales 1', 'Ciencias Naturales 1'), ('La Entidad donde vivo', 'La Entidad donde vivo'), ('Formación Cívica y Ética 3', 'Formación Cívica y Ética 3'), ('Español 4', 'Español 4'), ('Matemáticas 4', 'Matemáticas 4'), ('Ciencias Naturales 2', 'Ciencias Naturales 2'), ('Geografía 1', 'Geografía 1'), ('Historia 1', 'Historia 1'), ('Formación Cívica y Ética 4', 'Formación Cívica y Ética 4'), ('Español 5', 'Español 5'), ('Matemáticas 5', 'Matemáticas 5'), ('Ciencias Naturales 3', 'Ciencias Naturales 3'), ('Geografía 2', 'Geografía 2'), ('Historia 2', 'Historia 2'), ('Formación Cívica y Ética 5', 'Formación Cívica y Ética 5'), ('Español 6', 'Español 6'), ('Matemáticas 6', 'Matemáticas 6'), ('Ciencias Naturales 4', 'Ciencias Naturales 4'), ('Geografía 3', 'Geografía 3'), ('Historia 3', 'Historia 3'), ('Formación Cívica y Ética 6', 'Formación Cívica y Ética 6'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=50),
        ),
    ]