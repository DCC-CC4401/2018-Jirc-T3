from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_manager:
            return redirect('manager:landing_manager')
        else:
            if request.user.is_person:
                return redirect('person:landing_person')

    return render(request, 'landingPage/home.html')
