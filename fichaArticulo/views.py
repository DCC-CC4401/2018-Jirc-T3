from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.


def fichaArticulo(request):
    context = {}
    return render(request, 'fichaArticulo.html', context)