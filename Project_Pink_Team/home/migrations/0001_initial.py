# Generated by Django 3.1.7 on 2021-05-25 20:42

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_institucion', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('nivel_educativo', models.CharField(max_length=20)),
                ('control', models.CharField(max_length=30)),
                ('turno', models.CharField(max_length=10)),
                ('clave', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grupo', models.CharField(max_length=50)),
                ('turno', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_periodo', models.CharField(max_length=40)),
                ('inicio_periodo', models.CharField(max_length=30)),
                ('fin_periodo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_usuario', models.CharField(choices=[('Alumno', 'Alumno'), ('Docente', 'Docente'), ('Administrador', 'Administrador'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=20)),
                ('is_docente', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_alumno', models.BooleanField(default=False)),
                ('telefono_casa', models.CharField(default='pendiente', max_length=32)),
                ('telefono_cel', models.CharField(default='pendiente', max_length=32)),
                ('titulo_docente', models.CharField(default='pendiente', max_length=50)),
                ('grado_alumno', models.CharField(choices=[('Primer grado', 'Primer grado'), ('Segundo grado', 'Segundo grado'), ('Tercer grado', 'Tercer grado'), ('Cuarto grado', 'Cuarto grado'), ('Quinto grado', 'Quinto grado'), ('Sexto grado', 'Sexto grado'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=20)),
                ('curp', models.CharField(default='pendiente', max_length=20)),
                ('direccion', models.CharField(default='pendiente', max_length=50)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('register_timestamp', models.DateTimeField(auto_now_add=True)),
                ('register_update', models.DateTimeField(auto_now=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.grupo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('is_teacher', 'Is Teacher'), ('is_student', 'Is Student'), ('is_admin', 'Is Admin')),
            },
        ),
        migrations.CreateModel(
            name='Materia_Actual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_materia', models.CharField(choices=[('Español 1', 'Español 1'), ('Matemáticas 1', 'Matemáticas 1'), ('Exploración de la Naturaleza y la Sociedad 1', 'Exploración de la Naturaleza y la Sociedad 1'), ('Formación Cívica y Ética 1', 'Formación Cívica y Ética 1'), ('Español 2', 'Español 2'), ('Matemáticas 2', 'Matemáticas 2'), ('Exploración de la Naturaleza y la Sociedad 2', 'Exploración de la Naturaleza y la Sociedad 2'), ('Formación Cívica y Ética 2', 'Formación Cívica y Ética 2'), ('Español 3', 'Español 3'), ('Matemáticas 3', 'Matemáticas 3'), ('Ciencias Naturales 1', 'Ciencias Naturales 1'), ('La Entidad donde vivo', 'La Entidad donde vivo'), ('Formación Cívica y Ética 3', 'Formación Cívica y Ética 3'), ('Español 4', 'Español 4'), ('Matemáticas 4', 'Matemáticas 4'), ('Ciencias Naturales 2', 'Ciencias Naturales 2'), ('Geografía 1', 'Geografía 1'), ('Historia 1', 'Historia 1'), ('Formación Cívica y Ética 4', 'Formación Cívica y Ética 4'), ('Español 5', 'Español 5'), ('Matemáticas 5', 'Matemáticas 5'), ('Ciencias Naturales 3', 'Ciencias Naturales 3'), ('Geografía 2', 'Geografía 2'), ('Historia 2', 'Historia 2'), ('Formación Cívica y Ética 5', 'Formación Cívica y Ética 5'), ('Español 6', 'Español 6'), ('Matemáticas 6', 'Matemáticas 6'), ('Ciencias Naturales 4', 'Ciencias Naturales 4'), ('Geografía 3', 'Geografía 3'), ('Historia 3', 'Historia 3'), ('Formación Cívica y Ética 6', 'Formación Cívica y Ética 6'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=50)),
                ('horario', models.CharField(choices=[('8:00-9:00', '8:00-9:00'), ('9:00-10:00', '9:00-10:00'), ('10:00-11:00', '10:00-11:00'), ('11:30-12:30', '11:30-12:30'), ('12:30-13:30', '12:30-13:30'), ('13:30-14:30', '13:30-14:30'), ('13:30-14:00', '13:30-14:00'), ('14:00-15:00', '14:00-15:00'), ('15:00-16:00', '15:00-16:00'), ('16:30-17:00', '16:00-17:00'), ('17:00-18:30', '17:30-18:30'), ('18:30-19:30', '17:30-18:30'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=50)),
                ('b1', models.FloatField(default=0.0)),
                ('b2', models.FloatField(default=0.0)),
                ('b3', models.FloatField(default=0.0)),
                ('b4', models.FloatField(default=0.0)),
                ('b5', models.FloatField(default=0.0)),
                ('promedio', models.FloatField(default=0.0)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Historial_Materias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_materia', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
                ('b1', models.FloatField(default=0.0)),
                ('b2', models.FloatField(default=0.0)),
                ('b3', models.FloatField(default=0.0)),
                ('b4', models.FloatField(default=0.0)),
                ('b5', models.FloatField(default=0.0)),
                ('promedio', models.FloatField(default=0.0)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.periodo')),
            ],
        ),
    ]