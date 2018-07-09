from django.db import models
from landingPage.models import User
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class FechaDeReserva(models.Model):
    id = models.CharField(max_length=30, primary_key=True, default=str(uuid.uuid4()).replace("-", ""), editable=False)
    iTime = models.CharField(max_length=150, default="")
    fTime = models.CharField(max_length=150, default="")
    iDate = models.CharField(max_length=150, default="", validators=[MinValueValidator("09:00"), MaxValueValidator("18:00")])
    fDate = models.CharField(max_length=150, default="", validators=[MinValueValidator("09:00"), MaxValueValidator("18:00")])
    reservaDe = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

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
    img = models.ImageField(blank=True, upload_to='imagenes',null=True, default="/Users/juanpablosuazo/UChile/semestre7/ingDeSof/tareas/tarea3/2018-Jirc-T3/media/imagenes/noimage.png")
    description = models.CharField(max_length=200)
    state = models.PositiveSmallIntegerField(choices=STATES, null=True, blank=True, default=1)
