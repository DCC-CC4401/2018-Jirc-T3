from django.contrib import admin
import django.contrib.auth.admin
from .models import User, Person, Manager

admin.site.register(User, django.contrib.auth.admin.UserAdmin)
admin.site.register(Person)
admin.site.register(Manager)
