# Generated by Django 2.1a1 on 2018-07-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichaArticulo', '0012_auto_20180710_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechadereserva',
            name='id',
            field=models.CharField(default='5632e80d205d408d8834186017bf10d2', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(default='a520e8bff2ac4970ab21f0b35a97ac80', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
    ]
