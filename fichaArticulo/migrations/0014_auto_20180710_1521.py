# Generated by Django 2.1a1 on 2018-07-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichaArticulo', '0013_auto_20180710_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechadereserva',
            name='id',
            field=models.CharField(default='d2dd7a8fcf224887b3fcb714adeb3389', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(default='dbe6b850bd474643a2ba94eb6a04c917', editable=False, max_length=30, primary_key=True, serialize=False),
        ),
    ]
