from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    HABILITADO = 1
    NO_HABILITADO = 2


    STATES = (
        (HABILITADO, 'Habilitado'),
        (NO_HABILITADO, 'No habilitado'),
    )
    is_person = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    rut = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=80, verbose_name='Email', unique=True)
    state = models.PositiveSmallIntegerField(choices=STATES, null=True, blank=True, default=1)
