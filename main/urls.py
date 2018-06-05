"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.urls

import landingPage.views

urlpatterns = [
    django.urls.path('', django.urls.include('landingPage.urls')),
    django.urls.path('accounts/', django.urls.include('django.contrib.auth.urls')),
    django.urls.path('accounts/signup/', landingPage.views.landingPage.SignUpView.as_view(), name='signup'),
    django.urls.path('accounts/signup/person/', landingPage.views.person.PersonSignUpView.as_view(), name='person_signup'),
    django.urls.path(r'fichaArticulo/', django.urls.include('fichaArticulo.urls')),
    django.urls.path(r'header/', django.urls.include('header.urls')),
    django.urls.path(r'header/', django.urls.include('header.urls'))

]


