import django.contrib.auth.models
from django.db import models


class User(django.contrib.auth.models.AbstractUser):
    is_person = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    rut = models.PositiveSmallIntegerField(default=1)
    """
    username, first_name, last_name, email, password, groups, is_active,
    is_staff, is_superuser, last_login, date_joined.
    """


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    @property
    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    @property
    def __str__(self):
        return self.user.username
