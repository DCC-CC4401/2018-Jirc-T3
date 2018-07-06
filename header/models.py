from django.db import models


class Item(models.Model):

    DISPONIBLE = 1
    PRESTAMO = 2
    PERDIDO = 3

    STATES = (
        (DISPONIBLE, 'Disponible'),
        (PRESTAMO, 'En prestamo'),
        (PERDIDO, 'Perdido'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    img = models.ImageField(blank=True, upload_to='imagenes')
    iTime = models.CharField(max_length=150, default="")
    fTime = models.CharField(max_length=150, default="")
    description = models.CharField(max_length=200)
    state = models.PositiveSmallIntegerField(choices=STATES, null=True, blank=True)