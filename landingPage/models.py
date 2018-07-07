from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_person = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    rut = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=80, verbose_name='Email', unique=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
