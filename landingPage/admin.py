from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Person, AdminPerson
admin.site.register(User, UserAdmin)
admin.site.register(Person)
admin.site.register(AdminPerson)