# Generated by Django 2.0.3 on 2018-07-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichaArticulo', '0007_auto_20180704_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(blank=True, upload_to='fichaArticulo/static'),
        ),
    ]
