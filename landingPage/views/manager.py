from django.shortcuts import redirect, render
from fichaArticulo.models import Item
from landingPage.models import User


def manager_landing_page(request):

    return render(request, 'landingPage/manager/manager_landing_page.html')


def display_table(request):
    items = Item.objects.all()
    users = User.objects.all()
    # Spaces
    #Schedule =
    # return render(request, 'tablas/tablas.html', {'items, Users, Spaces, Schedule': items, Users, Spaces, Schedules})
    return render(request, 'landingPage/manager/tablas.html', {'items': items, 'users': users})
