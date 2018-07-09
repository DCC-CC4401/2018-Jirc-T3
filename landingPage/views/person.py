from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..decorators import person_required
from ..models import User
from ..forms import PersonSignUpForm




class PersonSignUpView(CreateView):
    model = User
    form_class = PersonSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'person'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('person:landing_person')

@method_decorator([login_required, person_required], name='dispatch')
class LandingPersonListView(ListView):
    model = User
    template_name = 'landingPage/person/landing_person.html'


@method_decorator([login_required, person_required], name='dispatch')
class ProfilePersonView(ListView):
    model = User
    template_name = 'landingPage/person/profile_person.html'


@login_required
@person_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('person:profile_person_change_pass')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'landingPage/person/profile_person_change_pass.html', {
        'form': form
    })
