# Generated by Django 2.0.5 on 2018-07-10 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichaArticulo', '0009_merge_20180710_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechadereserva',
            name='id',
            field=models.CharField(default='ba162731617c4f3a80d5f6ccbd496688', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(default='cdf789d989cd41c6967d06bcc8e90f27', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(blank=True, default='/Users/juanpablosuazo/UChile/semestre7/ingDeSof/tareas/tarea3/2018-Jirc-T3/media/imagenes/noimage.png', null=True, upload_to='imagenes'),
        ),
    ]