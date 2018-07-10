from django.shortcuts import redirect, render
from fichaArticulo.models import Item
from landingPage.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..decorators import manager_required
from ..models import User
from ..forms import ManagerSignUpForm


class ManagerSignUpView(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('manager:landing_manager')


@method_decorator([login_required, manager_required], name='dispatch')
class LandingManagerListView(ListView):
    template_name = 'landingPage/manager/tablas.html'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(LandingManagerListView, self).get_context_data()
        context['items_list'] = Item.objects.all()
        return context


def testing_horario(request):
    return render(request, 'landingPage/manager/testing_horario.html')