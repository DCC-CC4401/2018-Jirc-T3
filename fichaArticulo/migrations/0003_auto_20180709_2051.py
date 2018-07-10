# Generated by Django 2.0.3 on 2018-07-09 20:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichaArticulo', '0002_auto_20180709_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechadereserva',
            name='fDate',
            field=models.DateField(default='', max_length=150, validators=[django.core.validators.MinValueValidator('09:00'), django.core.validators.MaxValueValidator('18:00')]),
        ),
        migrations.AlterField(
            model_name='fechadereserva',
            name='fTime',
            field=models.DateField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='fechadereserva',
            name='iDate',
            field=models.DateField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='fechadereserva',
            name='iTime',
            field=models.DateField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='fechadereserva',
            name='id',
            field=models.CharField(default='09723745268e4137a11d7a00c392be20', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(default='b67696bd031f440d92ad0118455bbfd2', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
    ]