from django.db import models
from landingPage.models import User
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


class FechaDeReserva(models.Model):
    _0900 = 1
    _0930 = 2
    _1000 = 3
    _1030 = 4
    _1100 = 5
    _1130 = 6
    _1200 = 7
    _1230 = 8
    _1300 = 9
    _1330 = 10
    _1400 = 11
    _1430 = 12
    _1500 = 13
    _1530 = 14
    _1600 = 15
    _1630 = 16
    _1700 = 17
    _1730 = 18
    _1800 = 19

    TIME =(
        (_0900, '09:00'), (_0930,'09:30'), (_1000, '10:00'), (_1030, '10:30'), (_1100, '11:00'), (_1130, '11:30'),
        (_1200, '12:00'), (_1230, '12:30'), (_1300, '13:00'), (_1330, '13:30'), (_1400, '14:00'), (_1430, '14:30'),
        (_1500, '15:00'), (_1530, '15:30'), (_1600, '16:00'), (_1630, '16:30'), (_1700, '17:00'), (_1730, '17:30'),
        (_1800, '18:00'),
    )

    id = models.CharField(max_length=30, primary_key=True, default=str(uuid.uuid4()).replace("-", ""), editable=False)
    iTime = models.CharField(max_length=150, default="")
    fTime = models.CharField(max_length=150, default="")
    iDate = models.CharField(max_length=150, default="")  #validators=[MinValueValidator("09:00"), MaxValueValidator("18:00")]
    fDate = models.CharField(max_length=150, default="")
    reservaDe = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.iDate


class Item(models.Model):
    is_articulo = models.BooleanField(default=False)
    is_espacio = models.BooleanField(default=False)
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
