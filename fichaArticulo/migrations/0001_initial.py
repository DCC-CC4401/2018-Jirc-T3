# Generated by Django 2.0.5 on 2018-07-09 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FechaDeReserva',
            fields=[
                ('id', models.CharField(default='2badd642b1a6445db143c5e6b619e404', editable=False, max_length=30, primary_key=True, serialize=False)),
                ('iTime', models.CharField(default='', max_length=150)),
                ('fTime', models.CharField(default='', max_length=150)),
                ('iDate', models.CharField(default='', max_length=150)),
                ('fDate', models.CharField(default='', max_length=150)),
                ('reservaDe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(default='771f9b72c5f748b5be5dd418678d86d0', editable=False, max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('img', models.ImageField(blank=True, null=True, upload_to='imagenes')),
                ('description', models.CharField(max_length=200)),
                ('state', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Disponible'), (2, 'En prestamo'), (3, 'Perdido')], default=1, null=True)),
                ('Reserva', models.ManyToManyField(blank=True, to='fichaArticulo.FechaDeReserva')),
            ],
        ),
    ]
