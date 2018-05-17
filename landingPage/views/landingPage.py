from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_adminPerson:
            return redirect('adminPerson:landing_admin')
        else:
            return redirect('person:landing_person')

    return render(request, 'landingPage/home.html')
