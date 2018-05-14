from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_person = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    rut = models.PositiveSmallIntegerField(default=1)
    """
    username, first_name, last_name, email, password, groups, is_active,
    is_staff, is_superuser, last_login, date_joined.
    """

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)