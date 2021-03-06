# Generated by Django 2.0.3 on 2018-07-09 20:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichaArticulo', '0003_auto_20180709_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechadereserva',
            name='fTime',
            field=models.DateField(default='', max_length=150, validators=[django.core.validators.MinValueValidator('09:00'), django.core.validators.MaxValueValidator('18:00')]),
        ),
        migrations.AlterField(
            model_name='fechadereserva',
            name='iDate',
            field=models.DateField(default='', max_length=150, validators=[django.core.validators.MinValueValidator('09:00'), django.core.validators.MaxValueValidator('18:00')]),
        ),
        migrations.AlterField(
            model_name='fechadereserva',
            name='iTime',
            field=models.DateField(default='', max_length=150, validators=[django.core.validators.MinValueValidator('09:00'), django.core.validators.MaxValueValidator('18:00')]),
        ),
        migrations.AlterField(
            model_name='fechadereserva',
            name='id',
            field=models.CharField(default='1f0f9ae31e8f420e8e90b65ab4a8e235', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(default='f1737f2b7939481495ad54e02b97b846', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
    ]
