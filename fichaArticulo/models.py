from django.db import models
import uuid


class FechaDeReserva(models.Model):
    id = models.AutoField(primary_key=True)
    iTime = models.CharField(max_length=150, default="")
    fTime = models.CharField(max_length=150, default="")
    iDate = models.CharField(max_length=150, default="")
    fDate = models.CharField(max_length=150, default="")


    def __str__(self):
        return self.iDate


class Item(models.Model):

    DISPONIBLE = 1
    PRESTAMO = 2
    PERDIDO = 3

    STATES = (
        (DISPONIBLE, 'Disponible'),
        (PRESTAMO, 'En prestamo'),
        (PERDIDO, 'Perdido'),
    )
    id = models.CharField(max_length=30, primary_key=True, default=str(uuid.uuid4()).replace("-", ""), editable=False)
    name = models.CharField(max_length=30)
    Reserva = models.ManyToManyField(FechaDeReserva, blank=True)
    img = models.ImageField(blank=True, upload_to='imagenes',null=True)
    description = models.CharField(max_length=200)
    state = models.PositiveSmallIntegerField(choices=STATES, null=True, blank=True, default=1)
