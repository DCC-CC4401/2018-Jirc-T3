# Generated by Django 2.0.5 on 2018-07-09 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichaArticulo', '0003_auto_20180709_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_articulo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='is_espacio',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fechadereserva',
            name='id',
            field=models.CharField(default='1bc1c607e04749f381b1f90da786f9fc', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(default='e1dfa5b3ffe94e8e95660a398a82e515', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
    ]