from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..decorators import person_required, adminPerson_required
from ..models import User, Person
from ..forms import PersonSignUpForm


@method_decorator([login_required, adminPerson_required], name='dispatch')
class LandingAdminListView(ListView):
    model = User
    template_name = 'landingPage/adminPerson/landing_admin.html'

