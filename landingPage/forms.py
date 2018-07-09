from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from landingPage.models import User
from django import forms


class PersonSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=True)
    email = forms.EmailField(required=True)
    rut = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "rut", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_person = True
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.rut = self.cleaned_data["rut"]
        user.username = user.email
        if commit:
            user.save()
        return user


class ManagerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=True)
    email = forms.EmailField(required=True)
    rut = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "rut", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_manager = True
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.rut = self.cleaned_data["rut"]
        user.username = user.email
        if commit:
            user.save()
        return user

